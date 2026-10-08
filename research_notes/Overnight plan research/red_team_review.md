# Red-team review of PLAN.md v3 (2026-10-08)

Independent, skeptical review of `PLAN.md` v3, the finance model, the bot code, the workflows and the research notes. Repository files were not modified apart from this note.

**Method.**
- Read every file in scope.
- Ran `python3 ops/finance_model.py`.
- Inspected the pinned `forecasting-tools==0.2.92` wheel (the version locked in `poetry.lock`).
- Read this repo's Actions run history and job logs through the GitHub MCP.
- Re-read two Claude Code docs pages (`/docs/en/authentication`, `/docs/en/cli-reference`, `/docs/en/model-config`) on 2026-10-08.
- Read this session's own metadata (`get_session`) and the operator routine (`list_triggers`).
- Ran a small Monte Carlo of the prize outcome. Its script is in the scratchpad; the inputs are stated in C4.

Items are ordered by priority within each tier.

---

## Critical

### C1. GitHub cron reliability is the dominant risk, but the plan treats it as a week-1 contingency and the model ignores it

**Issue.** The plan relies on the `7,37 * * * *` schedule and adds an external trigger only "if week-1 coverage < 90%". Coverage is the strongest predictor of being paid. Bots with 50–90% coverage had a **median prize of $0** in all three recent seasons.

**Evidence.**
- *This repo's own history.* The tournament workflow ran on an hourly `13 * * * *` cron from commit d4b6aa7 (2026-10-07 23:21Z) until 4956e9c (06:27Z). Only **one** scheduled run fired in that ~7 h window (run 37735329099, created 06:01Z, roughly 48 min late). About 7 were expected. Skipped jobs still create run records, so the count is reliable.
- *robcam55 PR #3,* cited in `free_inference_and_metaculus_ops.md` §B1. A 20-minute cron fired about 5 times a day: median gap 5 h, never under 2.5 h. The author concluded the bot would miss "roughly half the main tournament". Metaculus temporarily widened windows to 3 h "while GitHub Actions is degraded", which is not permanent.
- *Prize data by coverage.* Bots at 50–90% coverage had median prizes of $0 in Fall 2025, Spring 2026 and Summer 2026 (`metaculus_bot_tournaments.md` §2).
- *Finance model.* `ops/finance_model.py` applies only the 12% late-start loss (`COVERAGE_LOSS`) and has no term for missed windows. `P_ZERO=0.30` is the only proxy.

**Fix.**
1. Make a reliable trigger part of the base setup, not a contingency. Options, in order of preference:
   - The owner's always-on machine, or a free-tier VM (Oracle Always Free or GCP e2-micro), running a systemd timer every 10 min. This needs about 30 min of owner time and avoids GitHub cron and minutes entirely.
   - cron-job.org or a Cloudflare Worker cron calling `workflow_dispatch` every 15 min. This needs a fine-grained PAT scoped to this repo with only Actions: write and a 1-year expiry. Add that PAT to the secrets inventory and expiry calendar.
   - Avoid a 24/7 self-chaining Actions job. It burns minutes in a private repo and is the "serverless" pattern the Actions terms call out.
2. Add a coverage factor to the finance model: base 0.9 with a reliable trigger, 0.5–0.95 without one.

### C2. The claim that a 30-minute cron fits in 2,000 private-repo minutes is unsupported and probably false; one failure mode burns the quota in about a week

**Issue.** `PLAN.md` §5 says a 30-minute cadence "stays within GitHub's free 2,000 private-repo minutes". No calculation supports this anywhere in the repo.

**Evidence.**
- *Run count.* 48 runs a day is about 1,440 jobs a month. GitHub rounds each job up to a whole minute (`counterparty_policies.md` §1).
- *Idle-run duration.* The measured setup in test run 37737720223 (checkout, Python, Poetry, cache restore, `poetry install`) took about 25 s. The tournament job also runs `npm install -g @anthropic-ai/claude-code@2.1.293` and starts `run.py`, which imports `forecasting_tools`/litellm and calls the Metaculus API. An idle run is therefore about 45–75 s, which bills as **1 or 2 minutes**. That gives 1,440–2,880 idle minutes, plus about 300–600 minutes of real forecasting.
- *Retry storm.* When Metaculus returns 403, `forecasting_tools`' `retry_with_exponential_backoff` kept a single call alive for **about 4.5 minutes**: the "Live read-only check" step in the same run took 06:28:37 to 06:33:03, then raised `HTTPError 403`. If the token is revoked or Metaculus has an outage, every run costs about 5 min. That is about 7,000 min a month, so the quota is gone in about 6 days.
- *No payment method.* "If your account does not have a valid payment method on file, usage is blocked once you use up your quota." The bot then stops silently until the next billing cycle. `PLAN.md` §6 says "about $3/month of GitHub minutes", but that only works if the owner adds a card and a spending limit, which §8 never asks for.

**Fix.**
1. Move the bot to its own **public** repo. Standard runners are free and unmetered there. This also unlocks MiniBench, removes the private-repo dilemma in §8, and makes the Metaculus "allow inspection of code" rule easy to meet.
   - Keep the plan and research in this private repo.
   - Keep a monthly commit in the bot repo so the 60-day public-repo schedule shutoff never triggers.
2. If it stays private:
   - Add a first step that checks for unforecasted open questions with plain `curl` in about 3 s before installing anything, and exits early if there are none.
   - Make `run.py` fail fast on 401/403.
   - Measure real billed minutes for one week (Settings → Billing) before claiming they fit.

### C3. The bot runs Opus at *medium* effort with Claude Code's coding-agent system prompt, so the "template Opus-high" benchmark does not describe it

**Issue.** The plan's prize anchor is the Summer 2026 template result for "claude-opus-4-8-**high**". Winning bots used high-reasoning variants (p = 0.004, `metaculus_bot_tournaments.md` §5). The subscription path silently drops the effort setting.

**Evidence.**
- `run.py:115-118` passes `reasoning_effort` to `make_llm`. For CLI models, `make_llm` calls `CliLlm(model, web_tools=...)` and discards `**kwargs` (`run.py:108-111`). `cli_llm.py:306-315` builds `claude -p --model opus --tools "" --max-turns 1` with no `--effort` flag.
- The same path also discards `timeout=` and `allowed_tries=`. Every CLI call uses a 600 s timeout and 2 tries, so the researcher's `timeout=180` is ignored.
- Claude Code docs (`/docs/en/model-config`, read 2026-10-08): "Opus 5.5, Sonnet 5.5, and Haiku 5.5 default to `medium`". Effort is set with `--effort`, `CLAUDE_CODE_EFFORT_LEVEL` or `effortLevel`.
- Each call also gets Claude Code's default system prompt, which tells the model it is a coding assistant. It also gets cwd and git context from `forecast-bot/`, and any `CLAUDE.md` that might later be added to the repo.
- The CLI reference recommends `--system-prompt` (replace) for "a non-coding agent in a pipeline that no human watches".

**Fix.**
- Add `--effort high` (or `xhigh`), driven by `REASONING_EFFORT`.
- Add `--system-prompt "You are a careful, calibrated forecaster..."`. For research calls, keep minimal web-tool guidance.
- Add `--no-session-persistence`, and run each subprocess with `cwd=tempfile.mkdtemp()` so no repo context or `CLAUDE.md` leaks into the prompts.
- Pass the timeout through to the CLI.
- Record `total_cost_usd` and `modelUsage` from the JSON output as a counts-only log line. This turns the 1–6% capacity estimate into a measurement and confirms the alias resolved to Opus 5.5.
- Validate the changes on the bot-testing-area only.

### C4. The headline income figures do not match the recommended configuration or the model, and the 15–20% chance of $200/month is unsupported

**Issue 1: MiniBench is counted but recommended off.**
- `PLAN.md` §1 and §6 give "$75–110 a month after tax in steady state".
- The model's later-season figure is $429 per season = main $268.5 + **MiniBench $160** (`finance_model.py:158`: `fall_main * LATER_SEASON_FACTOR + 8 * MINIBENCH_EV`).
- §8 recommends keeping the repo private, and the workflow defaults `RUN_MINIBENCH` to false. So the recommended configuration earns about **$67/month pre-tax, about $50 after 25% tax, or about $47 after 30% withholding**.

**Issue 2: the upper bound is not in the model.** "$110 after tax" is higher than the model's *pre-tax* $107. The model prints US about $80 and non-US about $75.

**Issue 3: the §4 channel-1 range is too high.** The table gives "$55–80 after tax" for the main tournament. The model gives $308/4 × 0.75 = $58 for Fall, and about $50 for later seasons.

**Issue 4: "steady state" is not steady.** `LATER_SEASON_FACTOR` applies one more season of the 25–40% $/point decline. The plan's own premise compounds: about $181 in Summer 2027 and about $122 in Fall 2027 for the main tournament.

**Issue 5: the 15–20% figure is not derived anywhere.**
- At Summer-2026 rates, prize ≈ 9.9 × (score per question × coverage)². The template table gives 5 → $248, 7 → $484, 10 → $979.
- With one season of decline (×0.675) and 0.84 effective coverage, $800 pre-tax needs about **13 peer points per question**. $1,067 (which is $200/month after 25% tax) needs about **15**.
- Claude template bots scored 6.3, 7.3 and 9.8 in the last three seasons, and no template bot exceeded about 10.
- A quick simulation (score N(7.8, 3.5), 10% disqualify/bug, coverage 0.9–0.98, 25–40% decline, $50 floor) gives **P(≥$800 in Fall) ≈ 6%** and **P(≥$1,067) ≈ 2%**. With the current cron (coverage 0.5–0.95) it gives ≈1% and ≈0%, with EV ≈ $180.

**Fix.**
- Restate the headline separately for the recommended configuration and for the MiniBench configuration.
- Show the season-by-season decay, or justify a plateau.
- Replace "15–20%" with a derived number of about 2–8%, or add a Monte Carlo to `finance_model.py` with the coverage scenarios from C1.

### C5. The bot shares the owner's weekly limit, which is already in its warning band, and the account-level downside is understated

**Issue.** The plan rates "bot competes with your own usage" as Low and frames the risk one way only. In practice the owner's own use can starve the bot, a Max 20x subscriber is likely a heavy user, and a policy problem lands on the owner's main Claude account.

**Evidence.**
- *Live limit state.* This session's metadata shows `rate_limit_info: {rateLimitType: "seven_day", status: "allowed_warning", resetsAt: 2026-10-14T19:00Z}`. The account is near its weekly cap six days before reset.
- *Limits block the bot.* A limit-reached error in `claude -p` makes every prediction fail. Questions then miss their 1.5–3 h windows until the reset.
- *Extra usage costs cash.* If "extra usage" (usage credits) is enabled, overflow is billed at API rates. That would break the "no spend above $100 without approval" rule, and §8 does not tell the owner to check it.
- *Who is affected by enforcement.* The 2025 weekly caps targeted "running Claude Code continuously in the background, 24/7". Bans for third-party-harness use in January 2026 included some erroneous ones (`claude_subscription_automation.md` §2). If something goes wrong, the owner's primary $200 account is the one affected, not just "the bot stops" (`PLAN.md` §10).

**Fix.** Make the plan's **included $200/month API credits** the primary credential, using `claude -p` with `ANTHROPIC_API_KEY` from the linked Console org.
- Support article 17154008: credits "cover `claude -p` ... when you run them yourself with an API key from your linked Claude Console organization".
- This runs under the Commercial Terms, uses zero subscription capacity and carries no consumer-account risk.
- At about $1–2 per question API-equivalent (`CLI_API_EQ_PER_QUESTION`), the main tournament needs $90–180 a month, which fits.
- Keep **no payment method** on that Console org, so it hard-stops instead of charging.
- Use the subscription token only as an automatic fallback when credits are exhausted, or the other way round. Either way, add automatic fallback on usage-limit errors.
- §8 should also tell the owner to confirm that extra usage is off or capped.

---

## Important

### I1. The coverage metric is wrong for its two jobs: week-1 diagnosis and season rollover

**Issue.**
- *Pre-start questions.* `mc.py cmd_coverage` counts **every** question in the tournament, including those that opened between Sep 28 and the bot's start date. Coverage is therefore capped at about 88% from day one. The week-1 rule (§9: "Coverage ≥ 90%? Below that: add an external trigger") will always fire, and it cannot tell cron misses from the late start.
- *Season rollover.* `poetry.lock` pins `forecasting-tools 0.2.92`, whose `CURRENT_AI_COMPETITION_ID` is Fall 2026 (33121, set 2026-09-08). When Spring 2027 opens (about Jan 7), both the bot and the coverage job keep pointing at Fall. The bot gets zero Spring questions while coverage still reports Fall's healthy numbers.

**Fix.**
- Add `--since <BOT_START>` and per-week buckets. Exclude pre-start questions.
- Print the tournament slug and the newest question's open time. The routine alarms if no question has opened in the last 48 h.
- Add a December routine task: bump `forecasting-tools`/template (watch the upstream `metac-bot-template` commits) and switch the tournament ID on Spring day 1.

### I2. The Spring 2027 decision point falls after Spring has already started

**Issue.** §9 re-plans Spring "Feb–Apr 2027 … using the real numbers". Spring starts about Jan 7, before any Fall prize is paid, and every day late costs about 1% of the season.

**Fix.** Add a late-December checklist:
- update the season ID (I1);
- re-submit the participation form and credit request if Metaculus requires it each season (the 2026 template made the form mandatory);
- re-apply for AskNews (Daatan #616 says per season);
- review the score on resolved Fall questions only.

### I3. An `ANTHROPIC_API_KEY` secret silently overrides the subscription, and the "API fallback" has no web research

**Issue.**
- *Silent override.* Claude Code docs (authentication precedence, read 2026-10-08): "In non-interactive mode (`-p`), the key is always used when present", ranking above `CLAUDE_CODE_OAUTH_TOKEN`. The workflow exports `ANTHROPIC_API_KEY` to every step. If the owner adds it as the "fallback" (§5 and §7), every `claude -p` call bills the Console org while `run.py` still assumes subscription defaults. With a card on file, that is real cash.
- *No research in the fallback.* With `ANTHROPIC_API_KEY` alone, `defaults()` sets `RESEARCH_MODEL=openrouter/perplexity/...`. `has_web_research()` then returns False without an OpenRouter key, so the bot forecasts with no web research unless AskNews is set. Research-less bots ranked last.

**Fix.**
- Decide one credential policy (see C5).
- Pass credentials to the CLI explicitly per subprocess, for example strip `ANTHROPIC_API_KEY` from the environment when the subscription is intended.
- Document that the API fallback keeps the `claude-code/*` models (so WebSearch still works) and only swaps the credential.

### I4. Research is single-source, serialized, and fails silently

**Evidence.**
- *One source.* Winners used 1.75 vs 1.00 research sources (r = 0.42). AskNews is free (about 1,000 calls/month) but needs an email from the owner, and §8 omits it.
- *Serialized.* `EnsembleBot._max_concurrent_questions = 2` is dead code. The parent `FallTemplateBot2026` creates `_concurrency_limiter = asyncio.Semaphore(1)` at class definition (`main.py:123-126`), and the subclass inherits that object. Research therefore runs one question at a time. With a 600 s × 2-try CLI timeout, one hung research call can hold the whole run for about 20 min of the 28-min job.
- *Silent failure.* `--max-turns 12` "exits with an error when the limit is reached" (CLI reference). The research then becomes "No research available", and the counts-only log still reports "submitted".

**Fix.**
- Add AskNews to owner setup (one email to contact@asknews.app).
- Override `_concurrency_limiter` in the subclass.
- Set the research timeout to about 240 s with 1 retry, and fall back to a short no-tool Sonnet summary.
- Add counts for "research failed" and "forecast without research" to the tournament log.

### I5. "Live end-to-end tested" is overclaimed

**Issue.** §1 and §5 say the bot is "tested, including a live end-to-end run". In CI, every OAuth-dependent step was **skipped**: no `CLAUDE_CODE_OAUTH_TOKEN` exists, so the Install CLI and smoke-test steps were skipped in run 37737720223. The Metaculus API returned **403** (no token). The live `claude -p` run happened in the dev container on the session's own credentials against non-Metaculus inputs.

Never exercised:
- `npm`-installed CLI 2.1.293 with a setup-token in Actions;
- fetching tournament questions with a bot token;
- posting a forecast and its comment;
- `already_forecasted` detection.

**Fix.** Reword this in §1. Make the first owner-enabled run a watched `forecast-bot-test.yaml publish=true` on bot-testing-area (ROUTINE.md already does this), followed by a dispatch of the tournament workflow with MiniBench off.

### I6. Logs can still leak forecast content to the maintenance agent

**Issue.** Tournament mode sets logging to WARNING. However:
- `forecasting_tools` logs `Encountered errors while predicting: {errors}` at WARNING (`forecast_bot.py:483`);
- reraised errors embed "Errors encountered: {all_errors}" (`:440-443`);
- `print_counts_only` prints `str(err)[:300]`.

Parse and validation errors often quote the LLM's text, which can include "Probability: NN%". ROUTINE step 2 tells the agent to read failure output. Metaculus's rule bans "seeing the bot's output, and then modifying the bot".

**Fix.**
- Set `logging.getLogger("forecasting_tools").setLevel(logging.ERROR)` in tournament mode.
- Print only the exception class, the question ID and a fixed error category.
- Add a unit test that asserts no digit-percent pattern appears in tournament-mode output.

### I7. A failed comment post can permanently void a question's eligibility

**Issue.** `binary_report.py`, `multiple_choice_report.py` and the other report types post the **forecast first, then the comment**. If the comment call fails, or the 28-min timeout kills the job between the two calls, the question becomes `already_forecasted` and is skipped forever. That leaves a forecast with no comment. The old AIB rules require "a comment response under every single question" to be prize-eligible.

**Fix.** In the coverage job, count answered questions that lack a bot comment (counts only). Add a `repair-comments` path that re-posts the stored explanation, regenerating it if necessary.

### I8. Secret handling and token lifecycle

**Issues.**
- *Exposure to third-party actions.* Job-level `env:` exposes `CLAUDE_CODE_OAUTH_TOKEN`, `METACULUS_TOKEN` and others to every step, including `snok/install-poetry@v1`, a third-party action on a mutable tag. The tj-actions/changed-files compromise (March 2025) exfiltrated exactly this kind of env.
- *Revocation path unverified.* §10 says "revoke it in claude.ai settings". The authentication docs describe `/logout` for local logins but no revocation for `setup-token` tokens. This is unverified.
- *Expiry not tracked.* The token lasts one year (docs: "one-year OAuth token"), so it expires about Oct 2027. Neither the plan nor the ledger records this.
- *Impact understated.* "Others use your plan" is too mild. A thief's misuse would happen on the owner's account and could trigger abuse enforcement there.

**Fix.**
- Pin actions to commit SHAs.
- Move secrets to step-level `env:` on the single step that needs them.
- Verify and document the revocation path before go-live.
- Add a ledger "credential calendar": Claude token issued and expiring dates, external-trigger PAT expiry, Apify token.
- Have the routine warn 30 days before each expiry.

### I9. Owner involvement is understated, and there is no alert channel

**Issue.** §1 says "about 25 minutes … after that, everything runs and is maintained autonomously". Recurring owner tasks include:
- per-prize identity/residency KYC;
- a W-9 or W-8BEN form;
- Ramp bank details;
- the mandatory bot-maker survey;
- code or description disclosure;
- per-season form and AskNews re-applications;
- annual tax filing;
- token renewal.

The owner-side note estimates about 15 h a year. The **30-day claim window** ("prizes unclaimed after 30 days may be forfeited", 180 days in the general rules) is not mentioned anywhere in `PLAN.md`.

On alerting: the operator routine (`trig_01MEsBL3pVp6XkbEasquHNa2`) fires into this persistent session. Push and email notifications are available only to fresh-session routines. "Only message the owner if something needs their action" therefore has no delivery channel, and the owner must open the session or ledger to learn anything.

**Fix.**
- Add an "Owner calendar" section listing each recurring task and its deadline.
- Switch the routine to `create_new_session_on_fire` with a standalone prompt and `notifications: {email: true}`. This also cuts its cost; see M2.
- Note that changing country or tax residence requires a new W-8BEN, a Ramp support check and a Metaculus eligibility re-check.
- Note that sanctioned or excluded regions void prizes.

### I10. The downgrade is complementary to the bot, not an alternative

**Issue.** §1 frames downgrading to Max 5x as a benchmark "so the experiment is judged fairly". But the bot needs only 1–6% of Max 20x, and `anthropic_policy.md` §4 cites GitHub issue #99330 finding that a 20x week is only about 1.6× a 5x week. The bot would fit on Max 5x, and Max 5x also includes $100 of monthly API credits. "Downgrade + bot" plausibly reaches the $200 goal (a certain $100 plus about $50–80 EV) far more often than the bot alone.

**Fix.** Present this as option A in §1. Ask the owner to check claude.ai/settings/usage. Note that this week's `allowed_warning` (C5) suggests their own usage is heavy, so this depends on their own workload.

### I11. Market Pulse is dismissed without data, though it may be the best $/bot

**Issue.** §4 lists Market Pulse as "+$0–100, later". It is bot-eligible, pays about $7–7.5k per round, and the current round (`market-pulse-26q4`) is live now. Its continuous-updating requirement deters casual entrants. That suggests a much smaller field than the main tournament, where about $50k is shared across about 190 eligible bots. No field size or payout table was gathered.

**Fix.**
- This week, pull the Market Pulse participant count and past payouts, the way Bowen1314 compiled the main table.
- If fewer than about 30 bots are active, a daily re-forecast job (`skip_previously_forecasted=False`, one run a day) could be the highest-EV addition. It runs at about the same plan cost as MiniBench.

### I12. Evidence grading and the prize anchor are overconfident

**Issue.** "Strong (A−)" rests mainly on one third-party compilation (Bowen1314 RESEARCH.md, tier C) of **non-finalized** Summer standings, and on a single template data point ($842). The other recent Claude template results were $602 (Fall 2025) and $700 (Spring 2026). The bot is also not the template: different research stack, effort level and system prompt (C3). `P_ZERO = 0.30` is not reconciled with the coverage data in C1.

**Fix.** Grade it B or B+. Use the mean of the Claude template results with a spread, not the best season. Tie `P_ZERO` to the coverage scenario.

### I13. The Anthropic compliance row is marked ✅ while the repo's own notes say "grey"

**Issue.**
- `owner_side_risks_tax_payouts.md` row B4 rates headless `claude -p` from cron on a subscription a **grey zone**. GitHub issue #36324, which asked the docs to warn about bans, was closed as not planned.
- `reports/Plan financial and policy check.md` (same day) says "The bot never uses your subscription login token: Claude Code's terms say products must use API keys".
- `anthropic_policy.md` called the GitHub Action used as a "production LLM backend" a conflict.
- v3 reverses all three without reconciling them in `PLAN.md`.
- Claude calls will come from GitHub's datacenter IPs, possibly in a different country from the owner's account. Region or payment mismatch is a commonly cited ban trigger (snippet-level).

**Fix.** Mark the row ⚠️. Cite the explicit permissions (support article 15036540, the setup-token docs) and the residual grey. Prefer the API-credit route from C5, which needs no interpretation.

---

## Minor

### M1. Stale or contradictory documents

- **`ops/LEDGER.md`:**
  - the Status table still asks for an "Anthropic Console API key (Max plan credits) + AskNews or OpenRouter";
  - the log says "Bot: now prefers ANTHROPIC_API_KEY";
  - it gives "~$120/month pre-tax";
  - there is no v3 entry.
- **`reports/Plan financial and policy check.md`:**
  - "never uses your subscription login token";
  - "Hourly fits inside the 2,000 free private-repo minutes";
  - it is not marked as superseded.
- **`reports/AI agents earning real money.md`:** "+5 … tracking to roughly $250–$1,000 per season". Summer data gives +5 → $248, and the figure falls each season.
- **`forecast-bot/FORECASTER.md`:** describes a Claude Code *routine* forecaster (3 subagents, `mc.py submit`) that `PLAN.md` never mentions. If it were ever scheduled, it would post under the same bot account in parallel with Actions, producing double or overwriting forecasts.
- **`ops/ROUTINE.md`:**
  - its stop rules refer to "model spend", which no longer exists;
  - its Day-60 and Day-120 Apify rules apply to a channel that is now optional and off.

**Fix:** add a v3 ledger entry, banner-mark superseded files, and either label FORECASTER.md "dormant, never schedule" or delete it.

### M2. Operator-token figures are stale and check-in cost is understated

**Issue.**
- §6 says the build cost about $26 (about $0.70 of capacity). This session now reports **$67.06** API-equivalent.
- Check-ins resume a session holding **about 567k tokens** of context. With a 1 h subscription cache TTL and 3–4 days between check-ins, each one rewrites about 0.5M tokens of cache before its 15 or so reads. That is about $3–6 per check-in, or about $30–50 a month API-equivalent, versus the model's $4–17. This is still under 1% of the plan.

**Fix:** use a fresh-session routine (see I9), and update the parameters.

### M3. Payout timing is optimistic

**Issue.** Fall forecasting ends 2027-01-06, but the tournament *closes* 2027-03-05. Payment follows all surveys and KYC, and Spring 2026 paid about 2–3 months after it ended.

**Fix:** say "about Mar–May 2027".

### M4. The tax treatment is simplistic

**Issue.**
- Non-US owners: 30% withholding plus possible home-country tax (foreign tax credit uncertain), plus SWIFT and FX costs of about $10–30 and 1–3%. On a $300 prize that is another 5–10%.
- US owners: state tax is ignored.

**Fix:** model fees as a separate line.

### M5. CLI pinning has no update plan

**Issue.** CLI 2.1.293 is pinned (good), and the `opus` alias needs v2.1.280 or later to reach Opus 5.5. But there is no `DISABLE_AUTOUPDATER=1`, no plan to bump the version for new models, and the resolved model is never logged.

**Fix:** set `DISABLE_AUTOUPDATER=1`, schedule a monthly version review, and log the resolved model (see C3).

### M6. Prize options in the notes are missing from the plan

**Issue.**
- AIcrowd ARC White-Box closes 2026-10-17 and explicitly welcomes AI; `other_prize_competitions.md` ranks it third.
- Kaggle "Build Coding Agents with Gemma 4" (Dec 2) has an EV of about $100–300 in `crunchdao_kaggle_deep_dive.md`.
- `PLAN.md` lists only CASMI26 (under 5% chance of any cash).

**Fix:** add both to §4, or state why they were dropped.

### M7. MiniBench EV in later seasons is undiscounted

**Issue.** MiniBench is valued at a flat $20 per round with no field-growth discount and no `P_ZERO`, while the main tournament gets both.

### M8. Branch and schedule fragility

**Issue.**
- Schedules run only from the default branch. `claude/ai-revenue-generation-ume6vn` is currently the only and default branch, so this works now. If the owner creates `main` or changes the default branch, the bot silently stops.
- Actions v4/v5 emit Node-20 deprecation warnings.

**Fix:** document the default-branch dependency in §8, and bump the actions when convenient.

### M9. Test coverage is narrow

**Issue.** Offline tests cover only binary questions through the CLI. Multiple-choice, date, conditional and group questions are untested on the CLI path.

**Fix:** add cases using the fake `claude`.

### M10. Wasted calls

**Issue.** The template still calls `summarize_research` even though `use_research_summary_to_forecast=False`, which wastes one Haiku call per question.

### M11. Refusals and model fallback on sensitive questions

**Issue.** On sensitive questions such as wars or weapons, Claude Code can refuse or apply content-based model fallback (model-config docs). The result is parse failures or a different model.

**Fix:** count both in the log.

---

## What to do tonight (highest expected-value actions)

**Agent, no owner needed:**
1. Fix C3: add `--effort high`, a forecasting `--system-prompt`, a temp-dir cwd, and log `total_cost_usd` and model.
2. Fix I4 (research concurrency and timeouts) and I6 (log sanitising).
3. Add the early-exit pre-check (C2) and measure an idle job.
4. Add coverage-since-start (I1).
5. Correct the §1, §4 and §6 numbers (C4).
6. Reconcile the stale documents (M1).

**Owner (about 45 minutes instead of 25):**
1. Do the §8 setup.
2. Email AskNews.
3. Link the Console org for API credits, with no card on that org (C5).
4. Confirm extra usage is off.
5. Pick the hosting:
   - preferred: a dedicated public bot repo plus an external 15-minute trigger;
   - or: an always-on machine.
6. Read the usage page to decide on the Max 5x downgrade (I10).

**Research, this week:** Market Pulse field size and payouts (I11).
