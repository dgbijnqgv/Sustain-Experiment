# Ledger

Append-only log kept by the operator sessions, newest first.

## Status

| Item | State |
|---|---|
| Cash spent | $0 of $500 (owner approval needed above $100) |
| Forecast bot: code | ✅ Built; offline tests and model-ID check pass in CI |
| Forecast bot: Metaculus bot account, token, participation form | ⏳ Owner |
| Forecast bot: OpenRouter key (donated credits or own, ≤$100 limit) | ⏳ Owner |
| Forecast bot: GitHub secrets + `BOT_ENABLED=true` | ⏳ Owner |
| Tender feed Actor: code | ✅ Live-validated in CI against TED, FTS and CF |
| Apify account, payout, `APIFY_TOKEN` secret | ⏳ Owner |
| Actors live | 0 |
| Revenue to date | $0 |

## Blocked

- Waiting on the owner's one-time setup (see `PLAN.md`).

## Proposals

- **Forecast bot model budget:** up to $250 for the Fall 2026 season if
  Metaculus's donated credits don't arrive. The estimate is $0.40–$0.75 per
  question for about 320 remaining main-tournament questions, against a
  central prize estimate of $300–$600. Awaiting owner approval; $0 spent.

## Log

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
