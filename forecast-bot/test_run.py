"""Offline tests for run.py's additions to the template (no network, no keys)."""
import asyncio
import os
import unittest
from unittest import mock

ENV = {
    "METACULUS_TOKEN": "test-token",
    "FORECAST_MODELS": "openrouter/vendor/model-a, openrouter/vendor/model-b",
    "RESEARCH_MODEL": "",
    "PARSER_MODEL": "",
    "PREDICTIONS_PER_QUESTION": "5",
    "ASKNEWS_CLIENT_ID": "",
    "ANTHROPIC_API_KEY": "",
    "OPENROUTER_API_KEY": "test-key",
    "CLAUDE_CODE_OAUTH_TOKEN": "",
}
os.environ.setdefault("METACULUS_TOKEN", "test-token")

import run  # noqa: E402
from forecasting_tools import BinaryQuestion  # noqa: E402

QUESTION = BinaryQuestion(question_text="Will X happen?", page_url="https://example.org/q/1")


class EnsembleBotTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, ENV)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.bot = run.build_bot(publish=False)

    def test_predictions_rotate_across_models(self):
        async def fake_parent_prediction(bot, question, research):
            await asyncio.sleep(0)  # let other prediction tasks interleave
            return bot.get_llm("default", "llm").model

        async def go():
            with mock.patch.object(run.FallTemplateBot2026, "_make_prediction", fake_parent_prediction):
                return await asyncio.gather(*[self.bot._make_prediction(QUESTION, "") for _ in range(5)])

        used = asyncio.run(go())
        self.assertEqual(used.count("openrouter/vendor/model-a"), 3)
        self.assertEqual(used.count("openrouter/vendor/model-b"), 2)

    def test_subscription_token_selects_cli_backend(self):
        with mock.patch.dict(os.environ, {"CLAUDE_CODE_OAUTH_TOKEN": "tok", "FORECAST_MODELS": "", "PARSER_MODEL": ""}):
            self.assertEqual(run.setting("FORECAST_MODELS"), "claude-code/opus")
            self.assertEqual(run.setting("RESEARCH_MODEL"), "claude-code/sonnet")
            self.assertEqual(run.setting("RUN_MINIBENCH"), "true")
            self.assertTrue(run.has_web_research())

    def test_tournament_summary_hides_forecasts(self):
        import io
        from contextlib import redirect_stdout
        with redirect_stdout(io.StringIO()) as out:
            run.print_counts_only([object(), ValueError("boom")])
        self.assertIn("1 forecast(s) submitted, 1 failed", out.getvalue())

    def test_non_default_purposes_unaffected(self):
        self.assertEqual(self.bot.get_llm("parser", "string_name"), run.setting("PARSER_MODEL"))

    def test_binary_median_is_clipped(self):
        low = asyncio.run(self.bot._aggregate_predictions([0.001, 0.01, 0.02], QUESTION))
        high = asyncio.run(self.bot._aggregate_predictions([0.995, 0.999, 0.99], QUESTION))
        mid = asyncio.run(self.bot._aggregate_predictions([0.2, 0.4, 0.9], QUESTION))
        self.assertAlmostEqual(low, 0.03)
        self.assertAlmostEqual(high, 0.97)
        self.assertAlmostEqual(mid, 0.4)

    def test_research_failure_falls_back_instead_of_skipping(self):
        researcher = self.bot.get_llm("researcher", "llm")
        with mock.patch.object(type(researcher), "invoke", side_effect=RuntimeError("search down")):
            text = asyncio.run(self.bot.run_research(QUESTION))
        self.assertIn("No research available", text)

    def test_no_research_source_still_forecasts(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}):
            text = asyncio.run(self.bot.run_research(QUESTION))
        self.assertIn("No research available", text)

    def test_research_success_is_labelled(self):
        researcher = self.bot.get_llm("researcher", "llm")
        with mock.patch.object(type(researcher), "invoke", mock.AsyncMock(return_value="Recent news: ...")):
            text = asyncio.run(self.bot.run_research(QUESTION))
        self.assertTrue(text.startswith("## Web research\nRecent news"))


if __name__ == "__main__":
    unittest.main()
