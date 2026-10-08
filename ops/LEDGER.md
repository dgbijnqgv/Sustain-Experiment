# Ledger

Append-only log kept by the operator sessions, newest first.

## Status

| Item | State |
|---|---|
| Cash spent | $0 of $500 (owner approval needed above $100) |
| Forecast bot: code | ✅ Built; offline tests and model-ID check pass in CI |
| Forecast bot: Metaculus bot account, token, participation form | ⏳ Owner |
| Forecast bot: Anthropic Console API key (Max plan credits) + AskNews or OpenRouter for research | ⏳ Owner |
| Forecast bot: GitHub secrets + `BOT_ENABLED=true` | ⏳ Owner |
| Tender feed Actor: code | ✅ Live-validated in CI against TED, FTS and CF |
| Apify account, payout, `APIFY_TOKEN` secret | ⏳ Owner |
| Actors live | 0 |
| Revenue to date | $0 |

## Blocked

- Waiting on the owner's one-time setup (see `PLAN.md`).

## Proposals

- ~~Forecast bot pay-as-you-go budget of up to $250~~: withdrawn 2026-10-08.
  The Max plan's included API credits cover the bot. Pay-as-you-go would risk
  $295 for an expected net of $137.

## Log

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
