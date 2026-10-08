# Codex on a ChatGPT subscription for recurring autonomous work (research notes)

Researched: 2026-10-08. Use case: an hourly Metaculus FutureEval forecasting bot (fetch questions, web research, post forecasts, no human in the loop) plus a weekly code-maintenance job on a GitHub repo, run with Codex while signed in with a ChatGPT Plus or Pro account (not an API key).

## How these notes were gathered

- The network egress proxy in this session blocked: developers.openai.com, learn.chatgpt.com (OpenAI's docs mirror), help.openai.com, openai.com, community.openai.com, forum.effectivealtruism.org, metaculus.com, archive.org and r.jina.ai.
- **VERIFIED** = I read the text myself in a primary source I could reach: the openai/codex repo (shallow clone at commit 14c8b77, 2026-10-08), the openai/codex-action README, the Metaculus/metac-bot-template README (commit da5de87), or GitHub issue pages fetched directly.
- **SNIPPET** = the text comes from a search-engine summary of the official page, or from a third-party page that quotes it. The wording is probably close but not guaranteed exact.
- **PRIOR-VERSION** = wording from an earlier OpenAI Terms of Use (Dec 2024 to 2025 versions). The 2026 version has not been checked word for word.

---

## 1. Authentication guidance: ChatGPT plan vs API key for CI and automation

### 1a. openai/codex README (VERIFIED, repo HEAD 2026-10-08)
https://github.com/openai/codex/blob/main/README.md
> "Run `codex` and select **Sign in with ChatGPT**. We recommend signing into your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise plan."
> "You can also use Codex with an API key, but this requires additional setup."

`docs/authentication.md` and `docs/exec.md` in the repo now contain only pointers to developers.openai.com/codex/auth and /codex/noninteractive.

### 1b. developers.openai.com/codex/auth (SNIPPET, from search summaries of the official page)
- "We recommend API key authentication for programmatic Codex CLI workflows (e.g., CI/CD jobs)." (Several search summaries agree on this wording.)
- "Don't expose Codex execution in untrusted or public environments."
- "Codex cloud requires signing in with ChatGPT."
- Enterprise "access tokens" exist for non-interactive local workflows ("trusted scripts, schedulers, and private CI runners"). They are **Business/Enterprise only**, not Plus or Pro.

### 1c. developers.openai.com/codex/auth/ci-cd-auth, "Maintain Codex account auth in CI/CD (advanced)" (SNIPPET)
These quotes come from GitHub issue sunholo-data/ailang#903 (opened 2026-08-26, quoting the page as checked on 2026-08-16) and from search summaries:
- "The right way to authenticate automation is with an API key."
- "Use this guide only if you specifically need to run the workflow as your Codex account."
- One condition is that "only one machine or serialized job stream will use a given auth.json copy".
- Paraphrased conditions:
  - API keys "remain the recommended option for most CI/CD jobs".
  - Use the guide only when ChatGPT-managed auth is needed, `codex login` can't run on the runner, and the runner is "trusted private infrastructure".
  - Treat auth.json like a password and never commit it.
  - "Don't use this workflow for public or open-source repositories."
  - Mechanics: run `codex login` on a trusted machine, copy `~/.codex/auth.json` to the runner, and persist the refreshed file after each run. Tokens refresh when the last refresh is about 8 days old, and again on a 401.
- **Significance:** OpenAI documents ChatGPT-plan auth in CI as a supported "advanced" path, not a forbidden one. It attaches conditions to it: trusted or private runner, a private repo, and one serialized job stream per auth.json.

### 1d. developers.openai.com/codex/noninteractive (SNIPPET)
- "Non-interactive mode lets you run Codex from scripts (for example, continuous integration (CI) jobs) without opening the interactive TUI."
- "codex exec reuses saved CLI authentication by default." In other words, a ChatGPT login works with `codex exec`.
- ChatGPT-account CI auth is described as advanced, for "enterprise teams using ChatGPT-managed Codex access on trusted runners or users who need ChatGPT/Codex rate limits instead of API key usage". Here OpenAI explicitly names "users who need ChatGPT/Codex rate limits instead of API key usage" as a legitimate reason.
- On key handling: scope `CODEX_API_KEY` inline to the single `codex exec` call, not as a job-level environment variable.

### 1e. openai/codex-action (GitHub Action) README (VERIFIED, main branch, 2026-10-08)
https://github.com/openai/codex-action
> "Users must provide an API key for their chosen provider (for example, `OPENAI_API_KEY` or `AZURE_OPENAI_API_KEY` …) as a GitHub Actions secret to use this action."
> "This action handles installing the Codex CLI and configuring it with a secure proxy to the Responses API."

- **The official Action has no ChatGPT-login input.** It is API-key only, and the key is billed at API rates.
- The README says `codex-args` such as `--search` "remain supported".

### 1f. Codex SDK (VERIFIED, sdk/python/README.md)
"Existing Codex authentication is reused automatically." The SDK provides `login_chatgpt()`, `login_chatgpt_device_code()` and `login_api_key()`.

### 1g. "Sign in with ChatGPT" for third-party tools (SNIPPET, secondary coverage)
- At DevDay (Sept 2026), OpenAI reportedly launched "Sign in with ChatGPT", which lets third-party developer tools such as OpenCode, Devin, Amp and Warp draw on a user's Plus or Pro allowance. Users set a weekly cap per app.
  - Sources: https://thenewstack.io/sign-in-with-chatgpt/ and https://www.mindstudio.ai/blog/anthropic-restricts-third-party-agents-openai-opens-codex-comparison
- OpenClaw's docs say Codex OAuth is "explicitly supported for use outside the Codex CLI": https://docs.openclaw.ai/concepts/oauth
- **Significance:** OpenAI's posture in 2026 is permissive about subscription allowance being used in agentic and harness contexts. This contrasts with Anthropic's early-2026 restrictions.

---

## 2. OpenAI Terms of Use and Usage Policies

### 2a. Terms of Use
- Effective date: January 1, 2026 (SNIPPET). The "Previous version" link on the page suggests there may be an even newer revision.
- URLs: https://openai.com/policies/terms-of-use/ and https://openai.com/policies/row-terms-of-use/

**"What you cannot do"** (PRIOR-VERSION wording. Search snippets confirm that the 2026 version still has the heading, the rate-limit clause and the extraction clause.)
> "Automatically or programmatically extract data or Output (defined below)."
> "Represent that Output was human-generated when it was not."
> "Interfere with or disrupt our Services, including circumvent any rate limits or restrictions or bypass any protective measures or safety mitigations we put on our Services."
> "Use Output to develop models that compete with OpenAI."

**Account section** (PRIOR-VERSION, corroborated by ConductAtlas provision records)
> "You may not share your account credentials or make your account available to anyone else and are responsible for all activities that occur under your account."

**Interpretation**
- The "programmatically extract" clause targets scraping the ChatGPT web UI. Codex CLI and `codex exec` are OpenAI's own official programmatic clients, and OpenAI documents using them from scripts and CI with ChatGPT auth (1c, 1d). Using the official client as documented is therefore not "extraction". It is the intended use.
- What would breach the Terms:
  - Reverse-engineering the ChatGPT OAuth tokens to call the backend from a custom client, or proxying them as a generic API.
  - Running multiple accounts to get around limits ("circumvent any rate limits").
  - Sharing one auth.json among other people.
- Copying your own auth.json to your own runner is not "sharing with anyone else". That is the documented ci-cd-auth workflow.
- Metaculus bot accounts are labelled as bots, so the "human-generated" clause is not triggered.

### 2b. Usage Policies
- Last substantive revision: 2025-10-29, "universal set of policies across OpenAI products" (SNIPPET).
- URL: https://openai.com/policies/usage-policies/
- Relevant prohibitions, quoted in snippets: "real money gambling"; "automation of high-stakes decisions in sensitive areas without human review". The sensitive areas listed are critical infrastructure, education, housing, employment, financial activities and credit, insurance, legal, medical, essential government services, product safety, national security, migration and law enforcement.
- **Assessment:**
  - A free-entry forecasting tournament with cash prizes is not real-money gambling. No stake is wagered.
  - Forecasts on public questions are not "high-stakes decisions about individuals" in those domains.
  - So the Metaculus use falls outside these prohibitions.
- One edge case: be careful if the bot forecasts on questions whose answers it could influence. That is not an OpenAI policy issue.

### 2c. Service Terms
- I could not retrieve the current text. No Codex-specific clause banning scheduled or automated use turned up in searches.
- The help center says the ChatGPT Terms of Use and Privacy Policy apply when you sign in to Codex with a ChatGPT account (SNIPPET).

---

## 3. Enforcement in 2025–2026 (all SNIPPET or anecdotal)

- **Account bans, June 2026.** Community forum threads report Pro and Codex account bans with generic "violation of Terms and Usage Policies" notices. None of these posts names automation as the cause.
  - https://community.openai.com/t/codex-chatgpt-pro-account-banned-with-no-warning-no-explanation-18-month-subscriber/1381906
  - https://community.openai.com/t/recent-false-suspensions-of-paid-users-may-be-connected-to-the-codex-quota-anomalies/1385096 (2026-06-28)
- **Rate-limit incident, June 2026.** OpenAI's status page reportedly attributed a rate-limit anomaly to "abuse and fraud prevention mechanisms incorrectly applying rate limits to specific accounts" and then reset usage caps.
- **Cyber Abuse warnings.** There are reports of automated "Cyber Abuse" warnings tied to Codex prompts: https://community.openai.com/t/improving-transparency-around-automated-cyber-abuse-enforcement/1388469
- **Conclusion:** I found **no OpenAI statement or documented enforcement wave aimed at scheduled `codex exec` use on Plus or Pro**. Automated abuse detection does exist and can misfire. The practical risk is false-positive flags, for example from running from many IPs or datacenter runners, not a rule against cron.

---

## 4. Official scheduled and automated features

### 4a. Codex app / ChatGPT desktop "Scheduled tasks" (formerly Codex "Automations")
Official pages: https://developers.openai.com/codex/app/automations and https://learn.chatgpt.com/docs/automations

From the official page (SNIPPET):
- "In the ChatGPT desktop app, scheduled tasks can work with local projects and run in the project directory or an isolated worktree."
- "Keep the computer on and the app running when a scheduled task needs local files."
- "Web tasks can use uploaded context and connected tools … but cannot read a local folder directly."
- The Codex CLI does not manage schedules. Create and manage them in ChatGPT web or the desktop app.

GitHub issue openai/codex#18472 (VERIFIED page, opened 2026-04-18):
> "cron automations appear limited to hourly or weekly RRULE shapes"

Minute-level schedules such as `FREQ=MINUTELY;INTERVAL=20` are not supported. The issue was still open as of Oct 2026.

GitHub issue openai/codex#47660 (VERIFIED page, opened 2026-09-23):
> "Scheduled tasks can run in the desktop app, but only while the computer is on. They can also run on the web, but there they can't target a repository environment."

In other words, there is no cloud-environment-bound scheduling yet.

### 4b. ChatGPT "Scheduled tasks" help article (SNIPPET)
https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- Active task limits: Free/Go 3, **Plus 5**, Business/Edu 10, **Pro 15**, Enterprise 15.
- Frequency: "Eligible paid plans support recurring tasks up to once per hour."
- Event-triggered tasks are capped at 30 per hour and 720 per day.
- Model availability and usage limits depend on plan.

### 4c. Codex cloud environments, labelled "Codex Cloud (Legacy)" in the docs (SNIPPET)
https://developers.openai.com/codex/cloud/internet-access and https://developers.openai.com/codex/cloud/environments
- Agent internet access is **off by default**. You can turn it on per environment, with a domain allowlist and an allowed-HTTP-methods restriction.
- Setup scripts always get internet access.
- "Secrets … are only available to setup scripts. For security reasons, they are removed before the agent phase starts."
  - So a Metaculus token stored as a secret is not visible to the agent. A plain environment variable would be visible, but less secure.

---

## 5. Usage limits on Plus and Pro, as of Oct 2026 (SNIPPET, third-party sources that conflict)

Official page: https://developers.openai.com/codex/pricing. You can check your own limits with `/status` or `/usage` in the CLI, or in Codex Settings > Usage.

**Plus ($20/month)**
- A five-hour rolling window plus a weekly cap.
- The five-hour window was suspended on 2026-07-12 and restored for Plus on 2026-08-25 (one source says 07-30).
- Estimated local messages per five hours: GPT-6.1-Sol about 15–160 (another source gives 15–150 for GPT-6-Sol), GPT-6-Astra about 5–45, GPT-6-Luna about 350–3,000.
- Cloud tasks consume more of the allowance. There is no published per-task figure for 2026. Older figures of 10–60 cloud tasks per five hours are outdated.

**Pro (reported as $100 "5x" and $200 "20x" tiers)**
- Pricing page: "Pro plans currently have no five-hour limit." A weekly cap still applies.
- New $200 sign-ups have reportedly been paused since 2026-09-10.

**General**
- No fixed weekly message count is published.
- Plus and Pro can buy extra credits.
- Sources: https://www.morphllm.com/codex-pricing, https://sessionwatcher.com/guides/codex-rate-limits-explained, https://www.eesel.ai/blog/gpt-remove-5-hour-limits

**Rough fit for this use case:** an hourly bot works out to about 24 runs a day, or about 170 a week, each making several tool-heavy turns. This should fit Pro comfortably. On Plus it could exhaust the weekly cap if each run spends many turns on Sol or Astra. Using Luna for triage and Sol only for final forecasts is the lever to pull.

### Models (VERIFIED, codex-rs/models-manager/models.json at HEAD 2026-10-08)
Listed models:

| Model | Bundled description |
|---|---|
| gpt-6-astra | "Frontier intelligence for the most demanding work." |
| gpt-6.1-sol | "Latest workhorse model for coding and everyday work." |
| gpt-6-sol | |
| gpt-6-luna | "Fast and affordable model." |
| gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna | |
| gpt-5.5 | "Legacy coding model." |

- GPT-6.1-Sol launched around 2026-09-29 (TechCrunch, SNIPPET). It is available on Plus, Pro, Business, Enterprise and Edu.
- The older "gpt-5.x-codex" names still appear in the code but are no longer in the listed presets.

### Web search (VERIFIED, source code)
- `codex-rs/protocol/src/config_types.rs`: `enum WebSearchMode { Disabled, #[default] Cached, Indexed, Live }`. So **the default is "cached"**: the `web_search` tool is available, but it runs against OpenAI's cached index.
- `codex-rs/tui/src/cli.rs`: "`--search` Enable live web search. When enabled, the native Responses `web_search` tool is available to the model (no per-call approval)."
- `--search` is defined on the interactive CLI. For `codex exec`, use `-c web_search="live"` or set `web_search = "live"` in `~/.codex/config.toml`. `codex-rs/config/src/config_toml.rs` documents it as: "Controls the web search tool mode: disabled, cached, indexed, or live."
- Network access for shell commands such as curl to the Metaculus API is a separate setting from the web_search tool. It is controlled by the sandbox or permission profile. The default `workspace-write` sandbox and the `:workspace` profile block network, so posting forecasts needs network enabled. Options:
  - `-c sandbox_workspace_write.network_access=true`
  - a permission profile that allows network
  - have the wrapper script post the forecasts instead of Codex

---

## 6. Output ownership and commercial use or prizes

Terms of Use, "Ownership of content" (SNIPPET. The same wording appears on several openai.com versions, including the 2024-10-23 revision.)
> "As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input and (b) own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output."
> "Output may not be unique and other users may receive similar output from our Services. Our assignment above does not extend to other users' output or any Third Party Output."

- Nothing in the Terms of Use or Usage Policies prohibits using Output for commercial gain or prize money.
- The only output-related restrictions are:
  - don't present Output as human-generated
  - don't use Output to build competing models
  - follow the Usage Policies
- Prize eligibility is governed by Metaculus's rules: no human in the loop, code inspectable, and a comment with each forecast.

---

## 7. OpenAI-sponsored model access for Metaculus bot makers

**Metaculus/metac-bot-template README** (VERIFIED, commit da5de87, Oct 2026)
> "`OPENROUTER_API_KEY` — get free credits via this form (https://forms.gle/aQdYMq9Pisrf1v7d8), or make your own key on OpenRouter."
> "…all participants are required to fill out the first section of our participation form … also to collect applications for LLM credits."
> "The `Forecast on new AI tournament questions` workflow … will run every 20 minutes"

**Metaculus announcements** (SNIPPET)
- Spring 2026: Metaculus "covers LLM and search costs for participants via donations from Anthropic and OpenAI, as well as a partnership with AskNews".
- Summer 2026 FutureEval: "via donations from Anthropic, Google, and OpenAI".
  - https://forum.effectivealtruism.org/posts/5EX9dz7nKthcxECTe/announcing-spring-2026-ai-forecasting-benchmark
  - https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament
- The Fall 2026 tournament reportedly started 2026-09-28: https://github.com/Bowen1314/metaculus-bot

**Conclusion:** there is no direct OpenAI program. **OpenAI-donated credits are distributed by Metaculus**, now through OpenRouter keys and applied for through the participation form. These are API credits, not Codex or ChatGPT plan access. They are the clean, terms-safe path for the hourly forecasting loop.

---

## 8. Verdicts per mode, for one individual on their own account and own repos

| Mode | Verdict | Notes |
|---|---|---|
| `codex exec` via cron on your own computer, ChatGPT login | **Allowed (low risk)** | Officially documented ("reuses saved CLI authentication"). Your own machine counts as trusted. Stay within plan limits, use one account, and never share auth.json. |
| `codex exec` in GitHub Actions, ChatGPT auth.json | **Grey (documented "advanced", discouraged)** | OpenAI: "The right way to authenticate automation is with an API key." Allowed only on trusted or private runners and **not for public or open-source repos**. You must persist the refreshed auth.json (refresh about every 8 days) and run a single serialized job stream (use a `concurrency:` group). GitHub-hosted runners on a public repo would violate the guide. |
| openai/codex-action | **Not possible with ChatGPT plan** | API key required (VERIFIED). |
| Codex cloud tasks | **Allowed, but not schedulable in the cloud yet** | Requires ChatGPT sign-in. Agent internet is off by default (allowlist possible). Secrets are stripped before the agent phase. |
| Codex app / ChatGPT Scheduled tasks | **Allowed (official)** | At most hourly. Plus 5 active tasks, Pro 15. Local tasks need the computer on and the app open. Web tasks can't target a repo environment. |
| Using outputs to win prize money | **Allowed** | You own the Output. No commercial restriction. |
| Sharing credentials, multiple accounts to evade limits, or custom clients reusing OAuth tokens | **Not allowed** | Terms of Use prohibit credential sharing and getting around rate limits. |
