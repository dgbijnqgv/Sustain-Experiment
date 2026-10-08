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
from cli_llm import CliLlm, is_cli_model
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
# verifies the configured IDs exist.
#
# Three ways to pay for the models, in order of preference:
# - CLAUDE_CODE_OAUTH_TOKEN: Claude Code on the owner's Claude plan (`claude -p`),
#   documented by Anthropic for CI and scripts; no per-token cost.
# - ANTHROPIC_API_KEY: a Console key, e.g. funded by the plan's API credits.
# - OPENROUTER_API_KEY: pay as you go, or Metaculus's donated credits.
# With the API options, web research needs AskNews or OpenRouter.
def use_anthropic() -> bool:
    return bool(os.getenv("ANTHROPIC_API_KEY", "").strip())


def use_subscription_cli() -> bool:
    """Claude Code via `claude -p`, paid by the plan's API credits
    (ANTHROPIC_API_KEY) and/or the plan itself (CLAUDE_CODE_OAUTH_TOKEN)."""
    return bool(os.getenv("CLAUDE_CODE_OAUTH_TOKEN", "").strip()) or use_anthropic()


def defaults() -> dict[str, str]:
    if use_subscription_cli():
        # Preferred: Claude Code paid by the plan's included API credits first,
        # then the plan itself (see cli_llm.py). Research uses Claude Code's
        # own web search, so no separate search service is needed.
        return {
            **_shared_defaults(),
            "FORECAST_MODELS": "claude-code/opus",
            "RESEARCH_MODEL": "claude-code/sonnet",
            "PARSER_MODEL": "claude-code/haiku",
            "RUN_MINIBENCH": "true",
        }
    # OpenRouter (pay as you go, or Metaculus's donated credits).
    return {**_shared_defaults(), **{
        # Opus-only: in Summer 2026 the unmodified template ranked 24th on Claude
        # Opus vs 35th on GPT-5.5, and Opus is also cheaper than GPT-5.5.
        "FORECAST_MODELS": "openrouter/anthropic/claude-opus-5.5",
        "RESEARCH_MODEL": "openrouter/perplexity/sonar-reasoning-pro",
        "PARSER_MODEL": "openrouter/openai/gpt-5-mini",
        # MiniBench pays ~$20 per 60-question round in expectation, below its
        # pay-as-you-go cost.
        "RUN_MINIBENCH": "false",
    }}


def _shared_defaults() -> dict[str, str]:
    return {
        "REASONING_EFFORT": "high",
        "PREDICTIONS_PER_QUESTION": "5",
        "CLIP_MIN": "0.03",
        "CLIP_MAX": "0.97",
        "MAX_COST_PER_RUN_USD": "15",
        # Season tournament IDs change three times a year (next: Spring 2027,
        # starting ~January). Empty means forecasting-tools' built-in current IDs.
        "TOURNAMENT_ID": "",
        "MINIBENCH_ID": "",
    }


def setting(name: str) -> str:
    value = os.getenv(name, "").strip()
    return value or defaults()[name]


def has_web_research() -> bool:
    research = setting("RESEARCH_MODEL")
    if is_cli_model(research):
        return True  # the agent CLI searches the web itself
    return bool(os.getenv("OPENROUTER_API_KEY", "").strip()) and research.startswith("openrouter/")


def make_llm(model: str, *, web_tools: bool = False, **kwargs) -> GeneralLlm:
    if is_cli_model(model):
        return CliLlm(model, web_tools=web_tools)
    return GeneralLlm(model=model, **kwargs)


def forecaster_llms() -> list[GeneralLlm]:
    effort = setting("REASONING_EFFORT")
    kwargs = {} if effort.lower() == "none" else {"reasoning_effort": effort}
    return [
        make_llm(m.strip(), timeout=300, allowed_tries=3, **kwargs)
        for m in setting("FORECAST_MODELS").split(",")
        if m.strip()
    ]


# Which forecaster model the current prediction task should use. Each
# prediction runs in its own asyncio task, so a ContextVar set inside
# _make_prediction is visible only to that prediction.
_forecaster: contextvars.ContextVar[GeneralLlm | None] = contextvars.ContextVar("forecaster", default=None)


class EnsembleBot(FallTemplateBot2026):
    _max_concurrent_questions = 2
    # The parent builds its semaphore from its own class attribute, so it must
    # be rebuilt here for the higher limit to take effect.
    _concurrency_limiter = asyncio.Semaphore(_max_concurrent_questions)

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
            if has_web_research():
                researcher = self.get_llm("researcher")
                tasks["Web research"] = self.get_llm("researcher", "llm").invoke(
                    self._get_research_prompt(question, researcher)
                )
            results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        if not tasks:
            logger.error("No research source configured (set ASKNEWS_* or OPENROUTER_API_KEY).")
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
            "summarizer": make_llm(setting("PARSER_MODEL")),
            "researcher": make_llm(setting("RESEARCH_MODEL"), web_tools=True, timeout=180, allowed_tries=2),
            "parser": make_llm(setting("PARSER_MODEL")),
        },
    )


def _retry_comment_posts() -> None:
    """The template posts the forecast first and the required reasoning comment
    second. A forecast without its comment is still marked answered and never
    revisited, so retry the comment hard rather than lose eligibility."""
    import time

    original = MetaculusClient.post_question_comment
    if getattr(original, "_retrying", False):
        return

    def post_with_retry(self, *args, **kwargs):
        for attempt in range(4):
            try:
                return original(self, *args, **kwargs)
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(5 * 2 ** attempt)

    post_with_retry._retrying = True
    MetaculusClient.post_question_comment = post_with_retry


class _MaskNumbers(logging.Filter):
    """Tournament logs must not reveal forecasts. Errors from the forecasting
    library can quote model output, so mask every digit in log messages."""

    def filter(self, record: logging.LogRecord) -> bool:
        import re

        record.msg = re.sub(r"\d", "#", record.getMessage())
        record.args = ()
        return True


def check_metaculus_access(client) -> None:
    """Fail in seconds, not minutes of retries, when the token is missing or bad."""
    import requests

    # A single direct request: the client's own helpers retry for minutes.
    try:
        response = requests.get(f"{client.base_url}/users/me", timeout=20, **client._get_auth_headers())
    except requests.RequestException as e:
        raise SystemExit(f"Metaculus API unreachable ({type(e).__name__}); stopping.")
    if response.status_code != 200:
        raise SystemExit(f"Metaculus API rejected METACULUS_TOKEN (HTTP {response.status_code}); stopping.")


def print_counts_only(reports) -> None:
    """Tournament logs must not show forecasts on open questions (no human, and
    no maintenance agent, may react to them), so report counts and errors only."""
    failed = [r for r in reports if isinstance(r, BaseException)]
    print(f"Run finished: {len(reports) - len(failed)} forecast(s) submitted, {len(failed)} failed.")
    for err in failed:
        import re

        print(f"  error: {type(err).__name__}: {re.sub(r'[0-9]', '#', str(err))[:300]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ensemble forecasting bot")
    parser.add_argument("--mode", choices=["tournament", "test_questions"], default="tournament")
    parser.add_argument("--dry-run", action="store_true", help="Forecast without publishing to Metaculus")
    args = parser.parse_args()
    mode: Literal["tournament", "test_questions"] = args.mode
    # In the tournament, keep forecasts and reasoning out of the logs.
    logging.basicConfig(
        level=logging.INFO if mode == "test_questions" else logging.WARNING,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    if mode == "tournament":
        for handler in logging.getLogger().handlers:
            handler.addFilter(_MaskNumbers())
    _retry_comment_posts()

    check_environment(strict=True)
    publish = not args.dry_run
    print_startup_banner(mode, will_publish=publish)
    bot = build_bot(publish)
    client = MetaculusClient()
    check_metaculus_access(client)
    main_id = setting("TOURNAMENT_ID") or client.CURRENT_AI_COMPETITION_ID
    mini_id = setting("MINIBENCH_ID") or client.CURRENT_MINIBENCH_ID

    async def forecast_all():
        if mode == "test_questions":
            bot.skip_previously_forecasted_questions = False
            return await bot.forecast_on_tournament("bot-testing-area", return_exceptions=True)
        reports = await bot.forecast_on_tournament(main_id, return_exceptions=True)
        if setting("RUN_MINIBENCH").lower() == "true":
            reports += await bot.forecast_on_tournament(mini_id, return_exceptions=True)
        return reports

    with MonetaryCostManager(float(setting("MAX_COST_PER_RUN_USD"))) as cost:
        reports = asyncio.run(forecast_all())
        logger.warning(f"Run cost (API-billed models only): ${cost.current_usage:.2f}")

    if mode == "tournament":
        print_counts_only(reports)
        raise SystemExit(0)
    bot.log_report_summary(reports)
    print_run_summary_banner(
        reports,
        will_publish=publish,
        tournament_url={
            "tournament": "https://www.metaculus.com/tournament/fall-futureeval-2026/",
            "test_questions": "https://www.metaculus.com/tournament/bot-testing-area/",
        }[mode],
    )
