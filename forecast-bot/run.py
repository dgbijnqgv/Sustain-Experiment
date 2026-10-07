"""
Entry point for our FutureEval bot.

`main.py` is Metaculus's official template, kept unmodified so upstream fixes
can be copied in. This file subclasses it with the changes that past winners
had in common (see reports/AI agents earning real money.md):

1. A flagship-model ensemble: the N predictions per question rotate across
   FORECAST_MODELS, and the template's median aggregation combines them.
2. Two research sources when available (AskNews + a web-search model), so one
   source's gaps or failures do not leave the forecasters blind.
3. Binary forecasts clipped to [CLIP_MIN, CLIP_MAX]; extremizing hurt past bots.
4. A per-run spending cap.

Tournament rule: no human in the loop. Nobody (person or agent) may look at
this bot's forecasts on open questions and then change code or rerun because
of them. Tune only on resolved questions or the bot-testing area.
"""
from __future__ import annotations

import argparse
import asyncio
import contextvars
import itertools
import logging
import os
from typing import Literal

from main import FallTemplateBot2026  # also loads .env and silences noisy deps
from bot_helpers import check_environment, print_run_summary_banner, print_startup_banner
from forecasting_tools import (
    AskNewsSearcher,
    BinaryQuestion,
    GeneralLlm,
    MetaculusClient,
    MetaculusQuestion,
    MonetaryCostManager,
)

logger = logging.getLogger(__name__)

# Defaults are overridden by GitHub repository variables of the same name, so
# models can be swapped without a code change. `scripts/check_models.py`
# verifies the IDs against OpenRouter's catalogue.
DEFAULTS = {
    # Opus-only: in Summer 2026 the unmodified template ranked 24th on Claude
    # Opus vs 35th on GPT-5.5, and Opus is the cheaper of the two on OpenRouter.
    "FORECAST_MODELS": "openrouter/anthropic/claude-opus-5.5",
    "RESEARCH_MODEL": "openrouter/perplexity/sonar-reasoning-pro",
    "PARSER_MODEL": "openrouter/openai/gpt-5-mini",
    "REASONING_EFFORT": "high",
    "PREDICTIONS_PER_QUESTION": "5",
    "CLIP_MIN": "0.03",
    "CLIP_MAX": "0.97",
    "MAX_COST_PER_RUN_USD": "15",
    # MiniBench pays ~$20 per 60-question round in expectation, below its API
    # cost at this configuration, so it is opt-in.
    "RUN_MINIBENCH": "false",
}


def setting(name: str) -> str:
    value = os.getenv(name, "").strip()
    return value or DEFAULTS[name]


def forecaster_llms() -> list[GeneralLlm]:
    effort = setting("REASONING_EFFORT")
    kwargs = {} if effort.lower() == "none" else {"reasoning_effort": effort}
    return [
        GeneralLlm(model=m.strip(), timeout=300, allowed_tries=3, **kwargs)
        for m in setting("FORECAST_MODELS").split(",")
        if m.strip()
    ]


# Which forecaster model the current prediction task should use. Each
# prediction runs in its own asyncio task, so a ContextVar set inside
# _make_prediction is visible only to that prediction.
_forecaster: contextvars.ContextVar[GeneralLlm | None] = contextvars.ContextVar("forecaster", default=None)


class EnsembleBot(FallTemplateBot2026):
    _max_concurrent_questions = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._forecasters = forecaster_llms()
        self._rotation = itertools.cycle(self._forecasters)
        self._clip = (float(setting("CLIP_MIN")), float(setting("CLIP_MAX")))

    def get_llm(self, purpose="default", guarantee_type=None):
        chosen = _forecaster.get()
        if purpose == "default" and chosen is not None:
            if guarantee_type == "string_name":
                return chosen.model
            return chosen
        return super().get_llm(purpose, guarantee_type)

    async def _make_prediction(self, question, research):
        _forecaster.set(next(self._rotation))
        return await super()._make_prediction(question, research)

    async def run_research(self, question: MetaculusQuestion) -> str:
        async with self._concurrency_limiter:
            tasks = {}
            if os.getenv("ASKNEWS_CLIENT_ID") and os.getenv("ASKNEWS_SECRET"):
                tasks["News (AskNews)"] = AskNewsSearcher().call_preconfigured_version(
                    "asknews/news-summaries", question.question_text
                )
            researcher = self.get_llm("researcher")
            tasks["Web research"] = self.get_llm("researcher", "llm").invoke(
                self._get_research_prompt(question, researcher)
            )
            results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        sections = []
        for name, result in zip(tasks, results):
            if isinstance(result, BaseException):
                logger.warning(f"{name} failed for {question.page_url}: {result}")
                continue
            sections.append(f"## {name}\n{result}")
        if not sections:
            # Forecasting without research beats skipping: a skipped question scores 0.
            logger.error(f"All research failed for {question.page_url}; forecasting without research.")
            return "No research available. Rely on base rates and the question background."
        return "\n\n".join(sections)

    async def _aggregate_predictions(self, predictions, question):
        aggregate = await super()._aggregate_predictions(predictions, question)
        if isinstance(question, BinaryQuestion):
            low, high = self._clip
            aggregate = min(high, max(low, float(aggregate)))
        return aggregate


def build_bot(publish: bool) -> EnsembleBot:
    n = int(setting("PREDICTIONS_PER_QUESTION"))
    return EnsembleBot(
        research_reports_per_question=1,
        predictions_per_research_report=n,
        use_research_summary_to_forecast=False,
        publish_reports_to_metaculus=publish,
        folder_to_save_reports_to=None,
        skip_previously_forecasted_questions=True,
        extra_metadata_in_explanation=True,
        llms={
            "default": forecaster_llms()[0],
            "summarizer": setting("PARSER_MODEL"),
            "researcher": GeneralLlm(model=setting("RESEARCH_MODEL"), timeout=180, allowed_tries=2),
            "parser": setting("PARSER_MODEL"),
        },
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    parser = argparse.ArgumentParser(description="Run the ensemble forecasting bot")
    parser.add_argument("--mode", choices=["tournament", "test_questions"], default="tournament")
    parser.add_argument("--dry-run", action="store_true", help="Forecast without publishing to Metaculus")
    args = parser.parse_args()
    mode: Literal["tournament", "test_questions"] = args.mode

    check_environment(strict=True)
    publish = not args.dry_run
    print_startup_banner(mode, will_publish=publish)
    bot = build_bot(publish)
    client = MetaculusClient()

    async def forecast_all():
        if mode == "test_questions":
            bot.skip_previously_forecasted_questions = False
            return await bot.forecast_on_tournament("bot-testing-area", return_exceptions=True)
        reports = await bot.forecast_on_tournament(client.CURRENT_AI_COMPETITION_ID, return_exceptions=True)
        if setting("RUN_MINIBENCH").lower() == "true":
            reports += await bot.forecast_on_tournament(client.CURRENT_MINIBENCH_ID, return_exceptions=True)
        return reports

    with MonetaryCostManager(float(setting("MAX_COST_PER_RUN_USD"))) as cost:
        reports = asyncio.run(forecast_all())
        logger.info(f"Run cost: ${cost.current_usage:.2f}")

    bot.log_report_summary(reports)
    print_run_summary_banner(
        reports,
        will_publish=publish,
        tournament_url={
            "tournament": "https://www.metaculus.com/tournament/fall-futureeval-2026/",
            "test_questions": "https://www.metaculus.com/tournament/bot-testing-area/",
        }[mode],
    )
