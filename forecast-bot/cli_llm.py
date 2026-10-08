"""
Run the template's LLM calls through an agent CLI instead of litellm:

    claude-code/<model>   ->  `claude -p` (Claude Code)
    codex/<model>         ->  `codex exec` (Codex CLI on the owner's ChatGPT
                              plan; only for running on the owner's own machine)

Everything else in forecasting-tools (prompts, parsing, CDF construction,
publishing) is unchanged: this class only replaces the transport.

Claude Code credentials, in order:
1. ANTHROPIC_API_KEY: a Console key funded by the Max plan's included monthly
   API credits (otherwise unused). This keeps the bot off the plan's weekly
   limits; with no card on the Console organization it cannot overspend.
2. CLAUDE_CODE_OAUTH_TOKEN (`claude setup-token`): the plan itself. Used when
   no API key is set, and as an automatic fallback when the credits run out.
Each subprocess receives exactly one credential, so which one pays is explicit.
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
# One CLI process per call; a ceiling keeps bursts of questions within the
# plan's short-term rate limits.
_cli_slots = asyncio.Semaphore(int(os.getenv("CLI_MAX_PARALLEL", "3")))
# Errors that mean "this credential cannot pay right now", so the other one
# should be tried.
_CREDENTIAL_ERRORS = ("credit balance", "billing", "insufficient", "usage limit", "rate limit", "quota", "401", "authentication")

SYSTEM_PROMPT = (
    "You are a careful, calibrated forecasting assistant working for an automated "
    "forecasting bot. Answer the user's request directly and completely in plain text. "
    "Do not ask questions, do not refuse, and do not mention being a coding assistant."
)
RESEARCH_SYSTEM_PROMPT = SYSTEM_PROMPT + (
    " Use the WebSearch and WebFetch tools to find current, dated, primary-source "
    "information before answering. Cite sources with dates."
)


def is_cli_model(model: str) -> bool:
    return model.startswith(CLI_PREFIXES)


def credential_order() -> list[str]:
    order = []
    if os.getenv("ANTHROPIC_API_KEY", "").strip():
        order.append("api")
    if os.getenv("CLAUDE_CODE_OAUTH_TOKEN", "").strip():
        order.append("subscription")
    return order or ["ambient"]  # e.g. a local machine already logged in


class CliLlm(GeneralLlm):
    def __init__(self, model: str, *, web_tools: bool = False, timeout: int | None = None, allowed_tries: int = 2):
        if not is_cli_model(model):
            raise ValueError(f"CliLlm needs a model starting with {CLI_PREFIXES}, got {model}")
        timeout = timeout or (420 if web_tools else 300)
        super().__init__(model=model, timeout=timeout, allowed_tries=allowed_tries)
        self.backend, self.cli_model = model.split("/", 1)
        self.web_tools = web_tools
        self.cli_timeout = timeout

    def command(self, output_file: str) -> list[str]:
        if self.backend == "claude-code":
            cmd = [os.getenv("CLAUDE_BIN", "claude"), "-p", "--output-format", "json", "--model", self.cli_model,
                   "--effort", os.getenv("CLI_EFFORT", "high"), "--no-session-persistence",
                   "--setting-sources", "", "--strict-mcp-config"]
            if self.web_tools:
                tools = "WebSearch,WebFetch"
                cmd += ["--system-prompt", RESEARCH_SYSTEM_PROMPT, "--tools", tools, "--allowedTools", tools,
                        "--max-turns", os.getenv("CLI_RESEARCH_MAX_TURNS", "20")]
            else:
                # Pure reasoning call: no tools at all, one turn.
                cmd += ["--system-prompt", SYSTEM_PROMPT, "--tools", "", "--max-turns", "1"]
            return cmd
        cmd = [os.getenv("CODEX_BIN", "codex"), "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--model", self.cli_model, "--output-last-message", output_file]
        cmd += shlex.split(os.getenv("CODEX_WEB_ARGS", '-c web_search="live"') if self.web_tools else "")
        cmd.append("-")  # read the prompt from stdin
        return cmd

    @staticmethod
    def _env_for(credential: str) -> dict[str, str]:
        env = dict(os.environ)
        if credential == "api":
            env.pop("CLAUDE_CODE_OAUTH_TOKEN", None)
        elif credential == "subscription":
            env.pop("ANTHROPIC_API_KEY", None)
        return env

    async def _mockable_direct_call_to_model(self, prompt) -> TextTokenCostResponse:
        text_prompt = prompt if isinstance(prompt, str) else json.dumps(prompt)
        credentials = credential_order() if self.backend == "claude-code" else ["ambient"]
        last_error: Exception | None = None
        for credential in credentials:
            try:
                text, cost = await self._run_once(text_prompt, credential)
                return TextTokenCostResponse(data=text, prompt_tokens_used=0, completion_tokens_used=0,
                                             total_tokens_used=0, model=self.model, cost=cost)
            except RuntimeError as e:
                last_error = e
                if not any(k in str(e).lower() for k in _CREDENTIAL_ERRORS):
                    raise
                logger.warning(f"{self.model} via {credential} credential failed; trying the next credential")
        raise last_error or RuntimeError("no credential available")

    async def _run_once(self, text_prompt: str, credential: str) -> tuple[str, float]:
        # An empty working directory keeps any repository files, CLAUDE.md or
        # settings out of the model's context.
        with tempfile.TemporaryDirectory() as workdir:
            output_file = os.path.join(workdir, "last_message.txt")
            async with _cli_slots:
                proc = await asyncio.create_subprocess_exec(
                    *self.command(output_file),
                    stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
                    cwd=workdir, env=self._env_for(credential),
                )
                try:
                    stdout, stderr = await asyncio.wait_for(proc.communicate(text_prompt.encode()), self.cli_timeout)
                except asyncio.TimeoutError:
                    proc.kill()
                    raise TimeoutError(f"{self.model} timed out after {self.cli_timeout}s")
            if proc.returncode != 0 and self.backend != "claude-code":
                raise RuntimeError(f"{self.model} exited {proc.returncode}: {stderr.decode()[-800:]}")
            return self._parse_output(stdout.decode(), stderr.decode(), output_file, credential)

    def _parse_output(self, stdout: str, stderr: str, output_file: str, credential: str) -> tuple[str, float]:
        if self.backend == "claude-code":
            try:
                result = json.loads(stdout)
            except json.JSONDecodeError:
                raise RuntimeError(f"{self.model} gave no JSON: {(stdout + stderr)[-800:]}")
            if result.get("is_error") or result.get("subtype", "success") != "success":
                raise RuntimeError(f"{self.model} error ({result.get('subtype')}): {str(result.get('result'))[:500]}")
            text = result.get("result", "")
            # Only API-key calls cost money; subscription calls are covered by the plan.
            cost = float(result.get("total_cost_usd") or 0) if credential == "api" else 0.0
        else:
            with open(output_file) as f:
                text, cost = f.read(), 0.0
        if not text.strip():
            raise RuntimeError(f"{self.model} returned an empty answer")
        return text, cost
