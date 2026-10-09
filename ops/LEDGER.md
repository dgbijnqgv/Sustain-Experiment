# Ledger

Append-only log kept by the operator sessions, newest first.

## Status

| Item | State |
|---|---|
| Cash spent | $0 of $500 |
| Forecast bot code | ✅ 28 offline tests; practice-area test posted 9/9 forecasts (2026-10-08) |
| Metaculus bot account, token and participation form | ✅ Done by owner 2026-10-08 |
| `ANTHROPIC_API_KEY` and `CLAUDE_CODE_OAUTH_TOKEN` | ✅ Set |
| Repository public, secrets, `BOT_ENABLED` / `RUN_MINIBENCH` | ✅ Set (`BOT_ENABLED=true`, `RUN_MINIBENCH=true`) |
| External 15-minute trigger (cron-job.org) | ✅ Working; dispatched runs seen 2026-10-08 19:51 UTC |
| Tournament target | `fall-futureeval-2026` via `mc.SEASON_TOURNAMENT`; **change for Spring 2027 (~Jan)** |
| Tender feed (optional) | ✅ Built; not published; awaiting the owner's yes |
| Revenue to date | $0 |

## Blocked

- Nothing. Waiting on the owner only for: yes/no to CrunchDAO (recommended: no)
  and the tender feed; and how much weekly time they can give to a
  human-in-the-loop channel, if any.

## Proposals

- ~~Pay-as-you-go model budget of up to $250~~: withdrawn. Plan credits and the
  subscription cover it.
- ~~Downgrade to Max 5x and run the bot~~: declined by owner 2026-10-08 (stays on Max 20x).

## Log

- **2026-10-09, shiteven listings.** Owner submitted to iogames.fun (with the reciprocal footer link live),
  iogame.io (/contact) and r/playmygame. The sitemap was fixed by the owner's server-side agent.
  r/iogames is still optional.

- **2026-10-09, priority change.** For shiteven, visits come before money; the owner has no immediate need
  for income. Listed on iogames.fun. Its free "boost" is a reciprocal text link; the owner adds it to the
  `public/index.html` footer.

- **2026-10-09, shiteven visibility.** The session's search tool found nothing, but the owner confirms Google already lists it. Sent 5 live pages to IndexNow
  (Bing, DuckDuckGo, Yandex) using the site's existing key; it accepted them (HTTP 200). The sitemap lists
  /arena, /community and /garden, which return 404; the fix needs a deploy. No Search Console step
  is needed.

- **2026-10-09, owner decisions.** Shiteven is parked: no owner time, keep the name, no portals, and don't
  make the AI-play API the focus. The owner is a director with little attention to spare, so messages to
  them must be short: outcome first, at most one decision. The Metaculus bot stays the only active channel.

- **2026-10-08, owner answers.** Tax residence: California, so US person. W-9, no withholding; prizes are
  ordinary income for federal and CA tax, with a 1099 likely at $600+. Rough after-tax value of the bot is
  ~$70–80/month. No downgrade. Owner flagged the opportunity cost of plan API credits and doubts the
  approach matches successful examples. Answered in session; MiniBench can be switched off
  (`RUN_MINIBENCH=false`) as soon as credits have a better use.

- **2026-10-08 ~20:00 UTC, setup session.** Owner finished setup with ops/setup.sh. Fixed three bugs found
  live: out-of-range numeric answers (now retried with the range), the test workflow always running dry,
  and forecasting-tools 0.2.92 targeting Summer 2026 (now `fall-futureeval-2026`). Coverage baseline:
  Fall main 14 questions and MiniBench 59 so far, all closed before launch (missed). Bot is live.

- 2026-10-08 08:58 UTC check-in: tournament runs #1 and #2 both `skipped` (`BOT_ENABLED` unset); setup still pending, stopped per ROUTINE step 1.

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
