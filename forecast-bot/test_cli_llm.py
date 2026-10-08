"""Offline end-to-end test of the subscription-CLI backend with a fake `claude`."""
import asyncio
import json
import os
import pathlib
import unittest
from unittest import mock

FAKE = pathlib.Path(__file__).parent / "tests_fake" / "claude"
os.environ.setdefault("METACULUS_TOKEN", "test-token")
ENV = {
    "CLAUDE_BIN": str(FAKE),
    "FORECAST_MODELS": "claude-code/opus",
    "RESEARCH_MODEL": "claude-code/sonnet",
    "PARSER_MODEL": "claude-code/haiku",
    "PREDICTIONS_PER_QUESTION": "3",
    "ANTHROPIC_API_KEY": "",
    "OPENROUTER_API_KEY": "",
    "ASKNEWS_CLIENT_ID": "",
    "CLAUDE_CODE_OAUTH_TOKEN": "",
}

import run  # noqa: E402
from cli_llm import CliLlm  # noqa: E402
from forecasting_tools import BinaryQuestion  # noqa: E402

QUESTION = BinaryQuestion(question_text="Will X happen?", page_url="https://example.org/q/2",
                          resolution_criteria="Resolves Yes if X.", background_info="Background.")
CALLS = pathlib.Path(str(FAKE) + ".calls")


class CliBackendTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, ENV)
        patcher.start()
        self.addCleanup(patcher.stop)
        CALLS.unlink(missing_ok=True)
        self.bot = run.build_bot(publish=False)

    def calls(self):
        return [json.loads(line) for line in CALLS.read_text().splitlines()]

    def test_research_uses_web_tools_and_is_labelled(self):
        text = asyncio.run(self.bot.run_research(QUESTION))
        self.assertIn("## Web research", text)
        self.assertTrue(any(c[c.index("--tools") + 1] == "WebSearch,WebFetch" for c in self.calls()))

    def test_full_binary_forecast_through_cli(self):
        report = asyncio.run(self.bot.forecast_question(QUESTION))
        self.assertAlmostEqual(report.prediction, 0.37)
        models = [c[c.index("--model") + 1] for c in self.calls()]
        self.assertIn("opus", models)      # forecasters
        self.assertIn("haiku", models)     # parser
        reasoning_calls = [c for c in self.calls() if "opus" in c]
        self.assertTrue(all("--max-turns" in c and c[c.index("--max-turns") + 1] == "1" for c in reasoning_calls))

    def test_cli_error_is_raised(self):
        llm = CliLlm("claude-code/opus")
        os.environ["CLAUDE_BIN"] = "/bin/false"
        try:
            with self.assertRaises(Exception):
                asyncio.run(llm.invoke("hi"))
        finally:
            os.environ["CLAUDE_BIN"] = str(FAKE)


if __name__ == "__main__":
    unittest.main()
