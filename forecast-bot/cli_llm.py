"""
Run the template's LLM calls through a subscription-backed agent CLI instead of
a pay-per-token API:

    claude-code/<model>   ->  `claude -p` (Claude Code, logged in with the
                              owner's Claude plan, e.g. via CLAUDE_CODE_OAUTH_TOKEN)
    codex/<model>         ->  `codex exec` (Codex CLI, logged in with the
                              owner's ChatGPT plan)

Everything else in forecasting-tools (prompts, parsing, CDF construction,
publishing) is unchanged: this class only replaces the transport.

Research calls can let the agent search the web (CLI_WEB_TOOLS=true), which
replaces paid search APIs.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import shlex
import tempfile

from forecasting_tools import GeneralLlm
from forecasting_tools.ai_models.ai_utils.response_types import TextTokenCostResponse

logger = logging.getLogger(__name__)

CLI_PREFIXES = ("claude-code/", "codex/")
# One CLI process per call; keep a ceiling so a burst of questions cannot
# exhaust the plan's short-term rate limit.
_cli_slots = asyncio.Semaphore(int(os.getenv("CLI_MAX_PARALLEL", "3")))


def is_cli_model(model: str) -> bool:
    return model.startswith(CLI_PREFIXES)


class CliLlm(GeneralLlm):
    def __init__(self, model: str, *, web_tools: bool = False, timeout: int = 600, allowed_tries: int = 2):
        if not is_cli_model(model):
            raise ValueError(f"CliLlm needs a model starting with {CLI_PREFIXES}, got {model}")
        super().__init__(model=model, timeout=timeout, allowed_tries=allowed_tries)
        self.backend, self.cli_model = model.split("/", 1)
        self.web_tools = web_tools
        self.cli_timeout = timeout

    def command(self, output_file: str) -> list[str]:
        if self.backend == "claude-code":
            cmd = [os.getenv("CLAUDE_BIN", "claude"), "-p", "--output-format", "json", "--model", self.cli_model]
            if self.web_tools:
                cmd += ["--allowedTools", "WebSearch,WebFetch", "--max-turns", os.getenv("CLI_RESEARCH_MAX_TURNS", "12")]
            else:
                # Pure reasoning call: no tools, one turn.
                cmd += ["--disallowedTools", "Bash,Edit,Write,Read,WebSearch,WebFetch", "--max-turns", "1"]
            return cmd
        cmd = [os.getenv("CODEX_BIN", "codex"), "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--model", self.cli_model, "--output-last-message", output_file]
        cmd += shlex.split(os.getenv("CODEX_WEB_ARGS", '-c web_search="live"') if self.web_tools else "")
        cmd.append("-")  # read the prompt from stdin
        return cmd

    async def _mockable_direct_call_to_model(self, prompt) -> TextTokenCostResponse:
        text_prompt = prompt if isinstance(prompt, str) else json.dumps(prompt)
        with tempfile.NamedTemporaryFile("r", suffix=".txt", delete=False) as out:
            output_file = out.name
        try:
            async with _cli_slots:
                proc = await asyncio.create_subprocess_exec(
                    *self.command(output_file),
                    stdin=asyncio.subprocess.PIPE,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                )
                try:
                    stdout, stderr = await asyncio.wait_for(proc.communicate(text_prompt.encode()), self.cli_timeout)
                except asyncio.TimeoutError:
                    proc.kill()
                    raise TimeoutError(f"{self.model} timed out after {self.cli_timeout}s")
            if proc.returncode != 0:
                raise RuntimeError(f"{self.model} exited {proc.returncode}: {stderr.decode()[-800:]}")
            text = self._parse_output(stdout.decode(), output_file)
        finally:
            os.unlink(output_file)
        if not text.strip():
            raise RuntimeError(f"{self.model} returned an empty answer")
        # Subscription usage has no per-call price; cost stays 0 so the
        # template's cost caps never trip on it.
        return TextTokenCostResponse(data=text, prompt_tokens_used=0, completion_tokens_used=0, total_tokens_used=0, model=self.model, cost=0.0)

    def _parse_output(self, stdout: str, output_file: str) -> str:
        if self.backend == "claude-code":
            result = json.loads(stdout)
            if result.get("is_error"):
                raise RuntimeError(f"{self.model} reported an error: {str(result.get('result'))[:500]}")
            return result.get("result", "")
        with open(output_file) as f:
            return f.read()
