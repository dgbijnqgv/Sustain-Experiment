# Free inference + Metaculus FutureEval operations (research as of 2026-10-08)

Labels:
- **VERIFIED**: read directly in primary source code/docs (git clones of Metaculus repos, HEADs listed below) or a page fetched in full.
- **SNIPPET**: from web-search summaries or third-party pages (bot makers' GitHub READMEs/issues/PRs). Not confirmed against a Metaculus/vendor page.

Network note: metaculus.com, llm-proxy.metaculus.com, forum.effectivealtruism.org, lesswrong.com, greaterwrong.com, ai.google.dev, openrouter.ai and metaculus.substack.com were all **egress-blocked** from this sandbox (WebFetch and curl). That means no live API counts and no Metaculus notebook 38928 (the resources page). github.com was reachable.

Repos cloned (HEAD at time of research):
- Metaculus/forecasting-tools `aa32be3` (2026-10-04)
- Metaculus/metac-bot-template `da5de87` (2026-10-01)
- Metaculus/metaculus `c7df099` (2026-10-07)

---

## PART A: Free/sponsored inference

### A1. The `metaculus/` model prefix (Metaculus LLM proxy): VERIFIED, but it is legacy

How it works (forecasting-tools `forecasting_tools/ai_models/general_llm.py` ~L189-235, VERIFIED):
```python
metaculus_prefix = "metaculus/"
...
self._use_metaculus_proxy = model.startswith(metaculus_prefix)
...
if "claude" in self.model or "anthropic" in self.model:
    self.litellm_kwargs["base_url"] = ("https://llm-proxy.metaculus.com/proxy/anthropic")
else:
    self.litellm_kwargs["base_url"] = ("https://llm-proxy.metaculus.com/proxy/openai/v1")
METACULUS_TOKEN = os.getenv("METACULUS_TOKEN")
self.litellm_kwargs["extra_headers"] = {
    "Content-Type": "application/json",
    "Authorization": f"Token {METACULUS_TOKEN}",
}
if self.litellm_kwargs.get("api_key") is None:
    self.litellm_kwargs["api_key"] = METACULUS_TOKEN
```
- The client strips the prefix and sends an OpenAI-compatible call (or Anthropic-format for claude/anthropic names) to `llm-proxy.metaculus.com`, authenticated with `Token <METACULUS_TOKEN>`. The proxy decides which models and budgets apply; the client code has no model allow-list.
- `ForecastBot._llm_config_defaults` (forecast_bot.py ~L960-1022) falls back to `metaculus/gpt-4o`, `metaculus/gpt-4o-mini` and `metaculus/gpt-4o-search-preview` **only if** no OPENAI/ANTHROPIC/OPENROUTER key is set and METACULUS_TOKEN is set.
- README (current): "Additionally the Metaculus proxy doesn't support all models." Example: `GeneralLlm(model="metaculus/claude-3-5-sonnet-20241022")`.

Eligibility and quotas (VERIFIED from template git history, README before commit 319410d, 2025-07-29):
> "OpenAI and Anthropic have generously donated credits to bot builders in the tournament which we are providing through an llm proxy. To get credits assigned to your model choices ... please send an email to `ben [at] metaculus [.com]` with: the username of your bot; a couple paragraph description...; an estimate of how much budget/tokens you might productively use; your preferred Anthropic/OpenAI model(s) and how you want the budget distributed between them (**there is budget distributed to each individual model name rather than to your account on whole**)."
> "You will need METACULUS_TOKEN set ... and have already had credits assigned to your account and model choice."

So the proxy was free but **gated**. A token alone gives nothing until Metaculus assigns a per-model budget.

Status in 2026 (VERIFIED by git history; the conclusion is my inference):
- 2025-07-29: the template README dropped the whole "Accessing the Metaculus LLM Proxy" section and switched to "get an OPENROUTER_API_KEY with free credits by filling out this form" (commits 319410d/a08653e).
- 2025-08-05: template example changed from `metaculus/anthropic/claude-3-5-sonnet...` to `openrouter/...`.
- 2026-05-16 (ee8841d): forecasting-tools README examples changed `metaculus/gpt-4o` to `openrouter/openai/gpt-4o`.
- **2026-05-30 (b69ffbf): deleted `.github/workflows/basic-test-proxy.yaml` and `stress-test_proxy.yaml`.** The last proxy smoke test checked: `metaculus/gpt-4o`, `metaculus/claude-3-7-sonnet-latest`, `metaculus/o1`, `metaculus/o4-mini`, `metaculus/gpt-4.1`, `metaculus/gpt-4o-mini`, `metaculus/o3-mini`.
- No evidence was found of any 2026-era model (GPT-5, Claude 4.x/5, Sonnet 4.6) on the proxy. **The proxy should be treated as deprecated or legacy.** Current sponsored credits come as an OpenRouter key (A2). I could not test the endpoint because it is blocked from the sandbox.

### A2. Donated-credit program (OpenAI / Anthropic / Google via OpenRouter key)
- VERIFIED (template README, current): "`OPENROUTER_API_KEY` — get free credits via [this form](https://forms.gle/aQdYMq9Pisrf1v7d8)". The form is mandatory for all participants ("all participants are required to fill out the first section of our participation form ... also to collect applications for LLM credits"; added 2026-09-26, commit c16d91f).
- VERIFIED (metaculus front end, orbit-constants.ts): FutureEval chip "Complimentary AI credits provided".
- VERIFIED (forecasting-tools git): Metaculus's own MetacBots and the proxy are separate from participant credits.
- SNIPPET, amount: robcam55/metaculus-bot PR #1 (2026-09-27): "Metaculus funds the OpenRouter key in steps: about $100 to start, more only after above-average MiniBench results ... plus a possible open-source bonus later." Same PR: credits are for "FutureEval and MiniBench only" (not the Metaculus Cup). https://github.com/robcam55/metaculus-bot/pull/1
- SNIPPET: Bowen1314/metaculus-bot README (state 2026-10-04): "Amount and waiting time are not published"; the key had not arrived by 2026-10-04 (applied before then). Its estimate without credits: about $200/season plus about $15/MiniBench round at about $0.25-0.50/question. https://github.com/Bowen1314/metaculus-bot
- SNIPPET: Daatan/retro #616/#724 (Aug 2026): credits are "per season, by application"; "Summer LLM credit budget is largely exhausted" (citing admin comments on notebook 38928); advice is to apply before the season opens. https://github.com/Daatan/retro/issues/724
- Approval time: **unknown/unpublished**. Anecdotes suggest days to more than a week. Do not plan around having credits on day 1.
- Historical (SNIPPET): 2024-25 credits were requested by email with a token estimate. In Q2 2025 Metaculus said it was giving credits "fairly generously".

### A3. Other free inference/search
**AskNews (Metaculus partnership)**
- VERIFIED, historical (template README before 2025-07-29): "Each registered bot builder gets 3k calls per month, 9k calls total for the tournament (latest news requests (48 hours back) are 1 call and archive news requests are 5 calls), and 5M tokens. Bots have access to the /news and /deepnews endpoints." Sign-up was via the AskNews Discord #api-support, giving bot name and email. "only one account allowed per participant."
- SNIPPET, 2026: Daatan #616 (citing notebook 38928, Aug 2026): "AskNews access (1k calls/month, 4k per tournament, /news and /deepnews)", requiring per-season application. Bowen1314 (Oct 2026) also says 1,000 calls/month and one account per person. **So in 2026 the figure is about 1,000 calls/month, not 3k.**
- The template still supports `ASKNEWS_CLIENT_ID`/`ASKNEWS_SECRET` (VERIFIED, .env.template). Metaculus's own MetacBots "usually use AskNews" (VERIFIED, futureeval-methodology-sections.tsx).

**Google AI Studio / Gemini API free tier**: SNIPPET only (ai.google.dev blocked)
- Terms (search snippets of ai.google.dev/terms): for Unpaid Services "Google uses the content you submit ... and any generated responses to provide, improve, and develop Google products and services and machine learning technologies"; "human reviewers may read, annotate, and process your API input and output"; "Do not submit sensitive, confidential, or personal information to the Unpaid Services."
- **EEA/Switzerland/UK**: "If you're in the European Economic Area, Switzerland, or the United Kingdom, the terms under 'How Google uses Your Data' in 'Paid Services' apply to all Services, including Google AI Studio and unpaid quota", so free-tier data is NOT used for training there. Also: "You may use only Paid Services when making API Clients available to users in the EEA, Switzerland, or the UK". A bot that only you run is arguably not "making API clients available to users".
- Commercial use: no explicit ban in the snippets. Free-tier output used in a prize contest is not obviously restricted. UNVERIFIED.
- Limits (conflicting third-party blogs): Dec 2025 cut Flash free quota sharply (reports say 20-50 RPD on some accounts); **Pro models removed from the free tier on 2026-04-01**. Flash/Flash-Lite remain free, with figures quoted from about 20 to 1,500 RPD at about 10-15 RPM. Treat as roughly "a few hundred calls/day of Flash-class at best, no Pro". News on 2026-10-09 consumer-app changes concerns the Gemini app, not the API.
- Gemini Flash with search grounding may be useful for cheap research. Check quotas in AI Studio before relying on it.

**OpenRouter free models**: SNIPPET
- `:free` model IDs: 20 req/min; **50 req/day if lifetime credit purchases < $10; 1,000 req/day after buying >= $10** (the threshold is lifetime). The quota is probably shared across free models. Free models get throttled at peak and rotate without notice. A negative balance gives 402 even on free models.
- Free models are typically open-weight (DeepSeek/Qwen/Llama/gpt-oss-class) and are not frontier closed models.

**Exa**: SNIPPET. Around 2026-07-17..24 the free tier (up to 20k req/month) was replaced by **$10 credits/month plus $20 on sign-up** (about 1,400 basic searches/month; $7 per 1k searches).
**Perplexity Sonar API**: SNIPPET. No standing free tier. Perplexity Pro subscribers get $5/month API credit. Sonar is about $5/1k searches plus tokens.

---

## PART B: Metaculus operations

### B1. Question windows and cadence
- VERIFIED, design history (forecasting-tools `util/launch_utils.py`, deleted 2026-01-28; 2025 launch tooling): questions were scheduled in non-overlapping slots, `proposed_open_time += timedelta(hours=2); proposed_closed_time = proposed_open_time + timedelta(hours=2)`, with a validator: "If bots, The open time must be 2hr before scheduled close time ... If pros it must be 2 days [+14h]". Random slot skipping added unpredictability.
- VERIFIED: the template cron is `"7,27,47 * * * *"` ("every 20 min, offset off the hour"), changed from */30 to */20 on 2025-08-05 when the windows shortened. Metaculus's own MetacBot runner uses `"13,43 * * * *"` (every 30 min).
- VERIFIED (scores FAQ in repo): "For a spot score, only the prediction at a specified time is considered ... spot scores are evaluated at the same time the Community Prediction is revealed. Coverage is 100% if there is an active prediction at the time, and 0% if there is not." So you must have a forecast standing at CP-reveal (≈close).
- SNIPPET (2026): base window **1.5 h**, "temporarily raised to 3h while GitHub Actions reliability is degraded", per pinned admin comments on notebook 38928 (Daatan #616, 2026-08-23; robcam55 PR #3, 2026-10-02: "open at random hours, up to five at a time, and each stays open for 1.5 hours ... 3 for now, per Metaculus, while GitHub Actions is degraded"). Example: Summer post 45182 open 2026-08-19T15:00Z, close 18:00Z (3 h). Bowen1314 (2026-10-04): "question windows are about 3 hours."
- **The ~3 h claim is correct for now but temporary. Design for 1.5 h windows.** Launch times are random UTC hours, 7 days a week, sometimes up to 5 at once.
- Cadence needed: **every 2 hours is NOT enough.** With 1.5 h windows, polling must be at most about every 30-60 min minus run time; with 3 h windows, 2 h is marginal. Run every 15-20 min.
- **Important (SNIPPET, measured):** robcam55 PR #3 found that GitHub Actions fired the 20-min cron only about 5x/day (45 runs Sep 23-Oct 2, median gap 5 h, never under 2.5 h), so the bot would miss "roughly half the main tournament". Workarounds: an external cron (Cloudflare Worker calling workflow_dispatch), an always-on box/systemd timer, or a scheduled routine.
- Volume: VERIFIED "300–500 questions" per ~4-month season (participate tab). That works out to about 3-5/day on average. MiniBench: "~60 auto-generated questions" per 2-week round.

### B2. Fall 2026 progress and late joining
- VERIFIED: forecasting-tools `FE_FALL_2026_ID = 33121 # fall-futureeval-2026`, `CURRENT_MINIBENCH_ID = "minibench"`, set 2026-09-08. Template targets fall-futureeval-2026 plus MiniBench.
- SNIPPET: Fall started **2026-09-28**, ends **2027-01-06** (BySergiMM PR #10, 2026-10-01). "the fall tournament had opened 9 questions and closed at least 4 of them" after about 3 days. Rough extrapolation (UNVERIFIED): about 25-40 opened by 2026-10-08, leaving about 270-470 remaining.
- Late joining, VERIFIED (scores FAQ): "Your rank in the tournament is determined by the sum of your Peer scores ... (**you get 0 for any question you didn't forecast**)"; prize share ∝ max(sum,0)². **There is no penalty beyond the zeros**, though missed questions do reduce attainable total and squared take. SNIPPET (Summer announcement): "always open to new entrants ... start at the middle of the leaderboard with 0 points."

### B3. Seasons and prize totals
- VERIFIED (metaculus front end): "Seasonal Bot Tournament — ~$50k · 3x/year — ~4-month seasons starting every January, May, and September, each with 300–500 questions"; "MiniBench ~$1k · bi-weekly"; "Market Pulse ~$7k · bot-eligible"; "Metaculus Cup — practice — bots aren't prize-eligible". Methodology: "compete for a share of $175k in prizes yearly. Our primary $50k seasonal bot tournament repeats every 4 months and is always open to new entrants."
- VERIFIED: tournament cards show Fall 2026, Summer 2026, Spring 2026 and Fall 2025 at **$58,000** each ($50k seasonal plus MiniBench, per PR #5205 of 2026-09-24). Earlier quarterly seasons Q3 2024-Q2 2025 were $30,000 each. The program has run continuously since July 2024 with prizes growing.
- No Spring 2027 announcement found (SNIPPET search). On the established pattern, the next season would start around January 2027. Continuation is likely but not guaranteed (funding not public).

### B4. Rules
VERIFIED (metaculus en.json FAB strings):
- "No human in the loop"
- "Bots must post a comment explaining reasoning alongside each forecast"
- "One prize-eligible bot per user"
- "Bot makers must be willing to share code or a description of how their bot works, and allow a member of Metaculus to inspect their code."

VERIFIED (backend): `DEFAULT_MAX_BOTS = 5` bot accounts per human; the first is `is_primary_bot`; "The primary bot is eligible for prizes, counts toward peer scores, and appears on leaderboards"; scoring: "all non-primary bots are unconditionally excluded". Bot accounts are created from the human account (Settings → My Forecasting Bots). Human accounts have API forecasting disabled by default (`ApiForecastingAccess.DISABLED`).

VERIFIED (old AIB contest-rules page, Q3 2024 text still served at /aib/contest-rules):
- "No individual may enter more than one bot ... Entering more than one will void all entries."
- "must be 18 years of age or older"
- "In order to be eligible for the prize, the participating bot needs to have written a comment response under every single question that it is forecasting. To be eligible for a prize, Bot makers must provide a description of how their bot works or the actual code. Bots may not have a human in the loop when forecasting. This includes running a bot on questions that are open or upcoming in the competition, seeing the bot's output, and then modifying the bot to improve its output."
- Excluded: "Crimea, Cuba, Iran, Syria, North Korea, Sudan, Russia". "Taxes and fees are paid by recipients."

VERIFIED (general /tournament-rules, last modified Jun 13 2025):
- No cash "to individuals located in countries subject to U.S. sanctions or export restrictions, including ... Russia, Cuba, North Korea".
- Winners must provide "(b) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident ...); (c) payment delivery information, such as bank account information, provided to Metaculus or via a third-party service".
- "Monetary payouts may be paid in the form of cash or a cash equivalent, which may include ... prepaid virtual cards, gift cards ... at the discretion of Metaculus."
- Forfeit if no response within "the sooner of (i) the required time period(s) or (ii) 180 days".

**Ramp**: not mentioned in any Metaculus source found. A third-party README claims bank transfer via Ramp (UNVERIFIED). The countries supported are unknown, so ask Metaculus.

SNIPPET (Daatan #616 quoting notebook 38928):
- Secondary bots are allowed but must be labelled "v2" in username/email.
- Comments should be private; Metaculus makes them public after close.
- No previewing/tuning on open questions; testing only on closed questions or the main site.
- "Using publicly available forecasts on questions found on other platforms or on Metaculus itself" is allowed; creating questions elsewhere to feed the bot is not.

Community prediction: no explicit ban found. In practice the CP is hidden until reveal (≈close), so it cannot be copied. Pro forecasts are hidden from bots.

LLM/tool restrictions: none found beyond the above. Any model and search tool is allowed.

Agent-driven bot implications: a Claude Code/Codex-CLI agent that forecasts autonomously is allowed. **A human (or a supervising agent session acting on a human's instruction) iterating on prompts after viewing outputs on open tournament questions is prohibited.** Keep dev/testing on closed questions and the bot-testing-area tournament.

### B5. Claude Code / Codex CLI–driven entrants: SNIPPET
- Many 2026 entrants were *built* with Claude Code (EskemoMan, XtremeSavage; rowanmck-asi/mm-forecast-bot is "maintained by an AI agent" that reviews resolved questions and tests one change at a time). The runtime is still a Python pipeline.
- The template ships a Claude Code skill `.claude/skills/review-bot/SKILL.md` for post-hoc review (VERIFIED, integrations/README.md).
- No public results were found for a bot whose *runtime* is a CLI agent (`claude -p`/`codex exec`).
- FutureSearch (ReAct-style research agents) reportedly ranked #1 of 166 in Summer 2026 (interim, crypto-news source).
- napzter13 fork: 15th of 277 in Summer 2026 (ensemble median).
- Metaculus's survey says agentic/iterative search beats one-shot retrieval.

### B6. Other cash contests open to bots, late 2026
- VERIFIED: Market Pulse "~$7k · bot-eligible — Bots compete for prizes by continuously updating forecasts on numeric group questions throughout each question's lifetime". forecasting-tools `CURRENT_MARKET_PULSE_ID = "market-pulse-26q4"` (added 2026-09-08). It requires *continuous updating* (not one-shot), so runs are needed over the question lifetime.
- VERIFIED: MiniBench, about $1k per 2-week round with about 60 questions. Included in template "tournament" mode.
- VERIFIED: Metaculus Cup Fall 2026 (id 33108) is practice only; "bots aren't prize-eligible". SNIPPET: 4-5 questions/week, 2026-08-28 to 2027-01-01.

---

## Key URLs
- https://github.com/Metaculus/forecasting-tools (general_llm.py, forecast_bot.py, run_bots.py, helpers/metaculus_client.py)
- https://github.com/Metaculus/metac-bot-template (README, .env.template, .github/workflows/run_bot_on_tournament.yaml)
- https://github.com/Metaculus/metaculus (front_end/src/app/(futureeval)/..., (main)/aib/contest-rules, (main)/tournament-rules, (main)/help/scores-faq, users/services/bots_management.py, scoring/utils.py)
- https://github.com/Metaculus/metaculus/pull/5205 ($58k card, 2026-09-24)
- https://github.com/robcam55/metaculus-bot/pull/1 (~$100 credit steps) and /pull/3 (GH Actions cron unreliability; 1.5h→3h windows)
- https://github.com/Daatan/retro/issues/616 , /724 , /740 (rules digest, AskNews 1k/mo, credits exhausted)
- https://github.com/BySergiMM/metac-bot-template/pull/10 , /11 (Fall start 9/28, 9 questions in 3 days; Cup cadence)
- https://github.com/Bowen1314/metaculus-bot (3h windows, credits unpublished)
- https://github.com/jaa92-lab/trigpoint (90-min windows)
- Participation/credits form: https://forms.gle/aQdYMq9Pisrf1v7d8
- Resources notebook (blocked here, check manually incl. pinned comments): https://www.metaculus.com/notebooks/38928/
