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

- **Bot stopped by owner 2026-10-26.** Optional cleanup for the owner: delete the cron-job.org job and set
  `BOT_ENABLED=false`. Until then, the external trigger keeps starting runs that are skipped at no cost.
- Nothing. Waiting on the owner only for: yes/no to CrunchDAO (recommended: no)
  and the tender feed; and how much weekly time they can give to a
  human-in-the-loop channel, if any.

## Proposals

- ~~Pay-as-you-go model budget of up to $250~~: withdrawn. Plan credits and the
  subscription cover it.
- ~~Downgrade to Max 5x and run the bot~~: declined by owner 2026-10-08 (stays on Max 20x).

## Log

- **2026-10-26, owner: turn off check-ins.** Disabled the "Sustain operator check-in" scheduled task (Mon/Thu).

- **2026-10-26, owner: stop the bot.** At API prices the bot loses money: ~240 questions/month x $0.60-0.85
  = ~$145-205/month of tokens against ~$105/month of expected prize. Main alone is ~$79 of tokens against ~$67 of
  prize. The tournament job is now hard-disabled (`if: false`) in `forecast-bot-tournament.yaml`. The forecasts
  already submitted stay in the Fall tournament and can still score.

- **2026-10-26 09:00 UTC, check-in.** Bot healthy: the last 100 tournament runs (Oct 25 09:30 to Oct 26 08:45)
  all succeeded. Coverage: main 63/63 (62 closed, 1 resolved; was 48/48); MiniBench 60/60 closed (was 58/58). The
  newest MiniBench question opened today. Target `fall-futureeval-2026` is still current. 1 question has resolved;
  the learning step waits for 20. No changes made.

- **2026-10-22, owner: drop Reddit for now.** Emptied the Ox inbox so a backlog can't post when the phone comes on;
  the two video tasks are parked in `ops/ox-parked.json`. Three clips stay in `ops/clips/` for later use. Owner
  paused the Ox-scheduled posts and the Codex clipping agent the same day.

- **2026-10-22, owner checked Reddit and Ox: nothing has been published.** None of the Ox-scheduled posts
  (r/WebGames Oct 13, r/iogames Oct 20) or the inbox video tasks went out. The Reddit channel has produced zero
  in two weeks. Likely cause: Ox only runs while the phone is on, and it usually isn't. Not yet confirmed that Ox
  can post at all. Lesson: I logged the scheduled posts as if they would happen and never checked that one had
  actually gone out.

- **2026-10-22 09:00 UTC, check-in.** Bot healthy: the last 100 tournament runs (Oct 21 09:15 to Oct 22 08:45)
  all succeeded. Coverage: main 48/48 (47 closed, 1 resolved; was 40/40); MiniBench 58/58 closed (was 13/13).
  The newest MiniBench question opened today. Target `fall-futureeval-2026` is still current. 1 question has
  resolved, so the learning step waits for 20. No changes made.

- **2026-10-21, owner chose 1a:** the r/IndieDev task now posts the tighter `shiteven-mutant-boss-20261008` cut
  instead of the comeback clip (same fight). If the task already ran, the edit does nothing. The owner doesn't
  read Ox notifications, and Reddit is blocked from these sessions, so what has been posted is unknown.

- **2026-10-21, owner: the phone with Ox is usually off.** Ox runs only while the phone is on, so Reddit tasks
  wait and then run together. Added `max_tasks_per_run: 1` to the inbox so Ox posts one per run. Owner decided
  to keep the repo public: no secrets or personal email in its history, and the Ox raw links and free Actions
  minutes need it public.

- **2026-10-19 09:00 UTC, check-in.** Bot healthy: the last 100 tournament runs (Oct 18 09:45 to Oct 19 08:45)
  all succeeded. Coverage, counted since the bot's first answer: main 40/40 (39 closed, 1 open; was 26/26), MiniBench
  13/13 (9 closed, 4 open; was 1/1). MiniBench is active again: three questions opened today. Target
  `fall-futureeval-2026` is still current. No changes made.

- **2026-10-15 09:00 UTC, check-in.** Bot healthy: the last 100 tournament runs (Oct 14 09:30 to Oct 15 08:45)
  all succeeded. Coverage, counted since the bot's first answer: main 26/26 closed questions answered (100%; was
  10/10). MiniBench 1/1 (100%). MiniBench has resumed: question 45950 opened 2026-10-12 16:16 UTC and was answered.
  The earlier 59 pre-launch misses are no longer counted. Target `fall-futureeval-2026` is still current.
  No changes made.

- **2026-10-14, owner: "Anthropic rejected the form".** The owner clarified it was the Anthropic startup
  program application. The program favours funded companies, so a solo project doesn't qualify. No impact: the
  bot runs on plan credits. Verified: tournament run 38611458633
  (18:00 UTC) submitted 1 forecast with 0 failures on the plan-credits API key, with no fallback warning. The last
  100 runs all succeeded.

- **2026-10-12 09:00 UTC, check-in.** Bot healthy: the last 100 tournament runs (Oct 11 09:00 to Oct 12 08:45)
  all succeeded, every 15 minutes. Coverage: main 10/10 closed questions answered (100%; was 3/3); MiniBench 59
  closed, all missed before launch (unchanged). Target `fall-futureeval-2026` is current (runs to 2027-03-05). MiniBench:
  no question has opened since 2026-10-07 20:38 UTC (over 4 days). forecasting-tools 0.3.4, the latest, still points
  at `minibench`, so no new location is known. Runs find nothing to answer there, so it costs no model spend;
  `RUN_MINIBENCH` left on, and the next check-in looks again.

- **2026-10-10, waste check.** The bot ran every 15 minutes with no errors. Main tournament: 3 of 3 new questions
  answered since launch. MiniBench: no question has opened since 2026-10-07 20:38 UTC (before launch), so it may
  have paused or moved to a new project. The check-in routine now verifies both targets (ROUTINE step 4, using
  `metaculus-meta.yaml`). The Fall season runs to 2027-03-05. Disabled the clip-queue routine
  `trig_01KdBYTqvJhy1kFbnLnSAMB7` because its sessions can't push; clips are queued by hand. Ox has two video
  posts queued: r/indiegames on Oct 10 and r/IndieDev on Oct 15.

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
