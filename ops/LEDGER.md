# Ledger

Append-only log kept by the operator sessions, newest first.

## Status

| Item | State |
|---|---|
| Cash spent | $0 of $500 |
| Forecast bot code | ✅ 25 offline tests; live `claude -p` research and forecast calls verified; Metaculus fetch and post untested until a token exists |
| Metaculus bot account, token and participation form | ⏳ Owner (PLAN.md §8A) |
| `ANTHROPIC_API_KEY` (plan credits) and/or `CLAUDE_CODE_OAUTH_TOKEN` | ⏳ Owner |
| Repository public, secrets, `BOT_ENABLED` / `RUN_MINIBENCH` | ⏳ Owner (§8B) |
| External 15-minute trigger (cron-job.org) | ⏳ Owner (§8C) |
| Tender feed (optional) | ✅ Built; not published; awaiting the owner's yes |
| Revenue to date | $0 |

## Blocked

- Waiting on the owner's one-time setup (PLAN.md §8).

## Proposals

- ~~Pay-as-you-go model budget of up to $250~~: withdrawn. Plan credits and the
  subscription cover it.
- **Owner decision:** downgrade to Max 5x *and* run the bot, worth ~$147/month
  (PLAN.md §1).

## Log

### 2026-10-08 (overnight): plan v4
- **Research:** six overnight tracks plus an independent red-team review:
  - Claude and Codex subscription automation policy
  - free inference and Metaculus operations
  - other prize competitions
  - CrunchDAO and Kaggle
  - owner-side tax, payouts and risks
- **Key findings:**
  - Questions are open for only ~1.5 hours.
  - GitHub's schedule is unreliable.
  - The Metaculus free model proxy has been retired.
  - Plan API credits are the cleanest way to pay for compute.
- **Built:**
  - a `claude -p` backend: high effort, forecasting system prompt, API credits
    with subscription fallback;
  - `mc.py` (pending, aggregate, submit, coverage);
  - digit-masked tournament logs, comment retries, fast-fail token check;
  - step-scoped secrets and tournament-ID overrides.
- **Economics:** ~$105/month pre-tax at ~95% coverage; 3–8% chance of a
  $200/month season.

### 2026-10-08: financial and policy check
- Report: `reports/Plan financial and policy check.md`. Model: `ops/finance_model.py`.
- **Expected value:** ~$120/month pre-tax, below the $200 goal. The bot's
  cash cost is $0 on plan API credits.
- **Claude tokens:**
  - Building so far: $26.26 at API prices, about $0.66 of the subscription.
  - Check-ins: about $0.20/month of the subscription.
- **Policy:** all parties allow the setup. The one grey area is GitHub's
  Actions "unrelated activity" clause; it is low burden and the
  Metaculus-endorsed method.
- **Bot:** now prefers ANTHROPIC_API_KEY, and MiniBench switches on with it.
- **Tender feed:** listing marked unofficial, with TED and OGL v3 attribution
  added.

### 2026-10-07: session 1 (continued)

**Research.** Ran deep research over 7 tracks; the report is in `reports/`.
Its conclusion: no verified autonomous agent nets $200 a month. The best
venues are Metaculus FutureEval (A−) and Apify (B−). The plan was rewritten
around those two.

**Forecasting bot.** Built `forecast-bot/`: Metaculus template da5de87 plus an
ensemble subclass.
- The CI test run passed.
- OpenRouter prices: Opus 5.5 at $4 in / $20 out per million tokens, and
  GPT-5.5 at $5 / $30.
- The default ensemble is Opus-only. In Summer 2026 the template ranked better
  on Opus than on GPT-5.5, and Opus is cheaper.
- MiniBench is opt-in. Its expected value of about $20 per round is below its
  API cost.

**Tender feed.**
- The live check passed. Normalized notices with title, link and date: TED
  200/200, FTS 12/12, CF 31/31. Change detection works across runs.
- FTS descriptions now include lot text.
- Repriced to $0.03 per notice plus $0.02 per run.

**Moved off the container's network.** Apify publishing and stats now run in
GitHub Actions, so the container's network allowlist and its `APIFY_TOKEN`
variable are no longer needed.

### 2026-10-07: session 1

- Chose Apify Store pay-per-event Actors and built `actors/tender-feed`, with
  7 unit tests.
- Wrote `ops/publish.mjs` and `ops/ROUTINE.md`.
