# Master plan: an AI-run setup that helps pay for its own subscription

*Version 3, 2026-10-08. Supersedes earlier versions. Evidence is in
`reports/` (three reports) and `research_notes/` (17 notes). Numbers come from
`ops/finance_model.py`.*

## 1. Bottom line

- **What to run:** a Metaculus **FutureEval forecasting bot**, running on **your
  Claude subscription** through `claude -p`. It runs every 30 minutes on GitHub
  Actions.
  - Cash cost: **$0**.
  - Plan capacity used: about **1–6%** of your Max 20x plan, roughly $2–13 of
    the $200.
  - It is built and tested, including a live end-to-end run. It is waiting
    only on your two tokens.
- **Expected income:** about **$75–110 a month after tax** in steady state (range
  $0 to ~$800 a month). Prizes are paid **3 times a year**; the first one
  arrives around Feb–Apr 2027.
- **Compared with your $200 goal:** expected value covers about half.
  - The chance of reaching $200 a month in a season is **~15–20%**, which needs
    a top-20 finish.
  - For comparison, downgrading to Max 5x saves $100 a month for certain. I
    say this plainly so the experiment is judged fairly.
- **Optional extras, low priority:** the Apify tender feed (built, ~$12 a month)
  and CrunchDAO DataCrunch (~$8–50 a month, paid in crypto). Each adds
  owner setup time for a small return, so neither is started without your
  yes.
- **Your part:** about **25 minutes** of setup (§8). After that, everything runs
  and is maintained autonomously.

## 2. Goal and constraints

| | |
|---|---|
| **Goal** | $200 a month net to cover the AI subscription, with minimal owner involvement |
| **Cash budget** | $500 total; anything above $100 needs your approval. **Current plan spends $0.** |
| **Compute** | Your Claude plan (Max, $200) is the engine. A ChatGPT/Codex plan is available as a backup. Pay-per-token APIs are avoided: they cost far more than the plan for the same work. |
| **Ethics** | No spam, no fake reviews, no terms-of-service violations, no undisclosed AI where disclosure is required, no personal data |
| **Agent's limits** | It can't open accounts, pass identity checks, receive money or spend money. Those steps are yours, one time each. |

## 3. Why this strategy (evidence summary)

1. **No verified case of an autonomous agent netting $200 a month from customers
   it found itself.**
   - Agent-run shops lost money: Project Vend, the WSJ's Claudius, and Andon
     Market, which is $40–62k down.
   - Agents that build and sell earned $0–54.
   - The big numbers came from human audiences or fraud.
   - Source: `reports/AI agents earning real money.md`.
2. **The money is where prize money already sits and the work is checked by
   machine.** Metaculus FutureEval is the clearest case.
   - Its rules **require** no human in the loop.
   - Prizes are published: $175k a year, with 30–41 bots paid per season.
   - Metaculus's own template running Claude Opus placed **24th of 284** last
     season, a would-be prize of about $842.
3. **Channels ruled out**, with sources in the reports:
   - Content/SEO/YouTube/KDP: platforms now punish AI volume.
   - Bounties and bug bounties: saturated, and banned or restricted in many
     places.
   - Freelancing: the terms forbid bots.
   - Trading: negative base rates.
   - AI app stores: no real revenue share.
   - Micro-SaaS: distribution is the bottleneck.
   - x402/MCP listings: inflated volumes.
4. **Running on the subscription is allowed.**
   - Anthropic documents `claude -p` and the `CLAUDE_CODE_OAUTH_TOKEN` "for CI
     pipelines, scripts".
   - Its support article (updated 2026-10-07) confirms `claude -p` uses
     subscription limits.
   - A bot that serves only you is not a "product offered to others".
   - Source: `research_notes/Overnight plan research/claude_subscription_automation.md`.

## 4. Channels

| # | Channel | Status | Expected net/month | Your effort | Evidence |
|---|---|---|---|---|---|
| 1 | **Metaculus FutureEval bot** (main tournament) | Built and tested; needs tokens | $55–80 after tax | 25 min once, plus prize KYC | Strong (A−) |
| 1b | MiniBench (same bot) | Built; off by default | +$25–35 | One decision (repo visibility) | Moderate |
| 1c | Market Pulse (~$7k/quarter, same bot) | Later: needs continuous updating | +$0–100 | None | Moderate |
| 2 | Apify tender feed | Built, live-validated; unpublished | ~$12 (range $0–96) | 20 min, Apify identity check | Moderate (B−) |
| 3 | CrunchDAO DataCrunch 2 | Researched; not built | $8–50, usually $0 | Sign-up, crypto wallet, exchange identity check to cash out | Moderate |
| 4 | Kaggle CASMI26 (closes Dec 14) | Researched | Under 5% chance of any cash | Phone verification, accept rules | Weak |

**Recommendation:**
- Start channel 1 now.
- Turn on 1b once you decide repo visibility (see §8).
- Add 2 or 3 only if you want more income streams in exchange for about 20
  minutes of identity checks each.
- Skip 4 unless there is spare time.

## 5. How it works

```
GitHub Actions, every 30 min (7 and 37 past each hour)
  └─ forecast-bot/run.py   Metaculus's official template, unmodified,
     │                     plus our ensemble subclass
     ├─ fetch open, not-yet-answered questions (Metaculus API, bot token)
     ├─ research    → claude -p (Sonnet) with WebSearch/WebFetch
     ├─ 5 forecasts → claude -p (Opus), no tools, independent
     ├─ parse       → claude -p (Haiku)
     ├─ median ensemble, clip binary to 3–97%
     └─ post forecast + required private reasoning comment
  Logs show counts and errors only, never forecasts.

Claude Code check-in (Mon/Thu 08:58 UTC, this session)
  └─ ops/ROUTINE.md: health, coverage (counts only), fixes, ledger
```

- **Why every 30 minutes:** questions are normally open for only **~1.5
  hours**, and GitHub sometimes delays scheduled runs. That rules out routines,
  which run at most hourly. Running every 30 minutes stays within GitHub's free
  2,000 private-repo minutes for the main tournament.
- **Fallbacks, already supported by the code:**
  - `ANTHROPIC_API_KEY`: your plan's included $200/month API credits.
  - `OPENROUTER_API_KEY`: Metaculus's donated credits.
  - Codex on a cron on your own computer, if Anthropic's policy changes.
- **Tested:** 23 offline tests; a live `claude -p` research and forecasting run
  on a binary and a numeric question; and CI on every change.

## 6. Economics

| Item | Value |
|---|---|
| Fall 2026 prize (late start, ~12% of questions missed) | ~$308 expected for the main tournament; +$140 with MiniBench |
| Later seasons (on time, larger field) | ~$430 per season expected → ~$107/month pre-tax |
| Upside | A top-15 finish paid $1.9–3.4k in Summer 2026 |
| Chance of $0 in a season | ~30% (bugs, missed windows, bad luck) |
| Cash cost | $0. About $3/month of GitHub minutes only if MiniBench runs in a private repo. |
| Plan capacity used | Main only: 1–3% of Max 20x. With MiniBench: 2–6%. |
| Claude tokens to build all this | About $26 API-equivalent, or about $0.70 of plan capacity |
| Check-in sessions | About $0.20/month of plan capacity |
| Tax | US: ordinary income. Non-US: expect 30% US withholding on prizes. |
| **Steady-state net** | **~$75–110/month after tax**; ~$90–150 with the optional extras |

Payout timing: the first Fall prize arrives around Feb–Apr 2027. Spring 2027
(Jan–Apr) pays around mid-2027. Prizes are lumpy: three times a year, not
monthly.

## 7. Compliance

| Party | Verdict | How we comply |
|---|---|---|
| Anthropic | ✅ `claude -p` with `CLAUDE_CODE_OAUTH_TOKEN` is documented for CI and scripts. The use is for your own benefit, not a product for others. | One personal bot. No reselling. The token is kept only in GitHub secrets. If policy changes, switch to the plan's API credits. |
| Metaculus | ✅ Bots are allowed, including AI-written ones. One prize bot per person. No human in the loop. A reasoning comment on every forecast. | Logs show counts only. Maintenance looks only at errors, coverage counts and resolved questions. We never use the community prediction. **Never run a second bot from Codex.** |
| GitHub | ⚠️ Grey area: Actions use must relate to the repo's software project. Running the repo's own bot can count as deployment, it is low burden, and it is Metaculus's official method. | Light jobs. If you prefer zero risk: a dedicated bot repo, or your own always-on machine. |
| OpenAI (Codex, backup only) | ✅ `codex exec` on your own computer's cron. ⚠️ Running it in CI on your ChatGPT login is discouraged. | Not used unless needed. |
| Apify and data licences (optional channel 2) | ✅ | Listing marked unofficial. TED and OGL v3 attribution added. |
| Taxes and identity checks | Your obligation | Use your legal name everywhere. W-9 or W-8BEN at payout. Keep a simple income log; the ledger helps. |

## 8. Your one-time setup (about 25 minutes)

1. **Metaculus (10 min).** At https://www.metaculus.com/futureeval/participate/:
   - create an account, then a bot account and its **token**;
   - fill in the first section of the participation form at
     https://forms.gle/aQdYMq9Pisrf1v7d8 (tick the credits request as a backup).
2. **Claude token (5 min).** On your computer, in any terminal with Node
   installed, run:
   `npx -y @anthropic-ai/claude-code setup-token`
   Log in with your Claude account and copy the token it prints.
3. **GitHub (5 min).** In this repo, go to Settings → Secrets and variables →
   Actions.
   - Secrets: `METACULUS_TOKEN` and `CLAUDE_CODE_OAUTH_TOKEN`.
   - Variable: `BOT_ENABLED` = `true`.
4. **Two answers for me:**
   - **Country of tax residence.** This affects payout options, withholding
     and whether CrunchDAO or Apify make sense.
   - **Make this repo public?** Public means MiniBench runs free (about +$25–35
     a month). Private means main tournament only.
     *My recommendation: keep it private for now.* The repo holds the plan and
     research. If you want MiniBench, I can move the bot to its own public repo
     instead.

Nothing else is needed. The next check-in detects the secrets, runs the
end-to-end test against Metaculus's unscored test area, and confirms the
tournament runs.

## 9. Operations, measures and decision points

- **Autonomy:** `ops/ROUTINE.md` runs twice a week. The bot itself needs no
  sessions.
- **What I track:**
  - coverage of 90% or more (`mc.py coverage`);
  - zero failed runs;
  - average peer score on resolved questions of at least +5 per question;
  - plan capacity below 10%.

| When | Check | Action |
|---|---|---|
| Week 1 | Coverage ≥ 90%? | Below that: add an external trigger (cron-job.org calling workflow_dispatch), or a second schedule |
| December | Score ≥ +5 on 40+ resolved questions? | Below 0: stop MiniBench and review the approach using resolved questions only |
| Feb–Apr 2027 | Fall prize paid? | Re-plan Spring 2027 using the real numbers |
| Any time | Anthropic policy change on `claude -p` | Switch to plan API credits with `ANTHROPIC_API_KEY` |

## 10. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Missed question windows from GitHub cron delays | Medium | Lower score | 30-minute cadence, coverage tracking, external trigger as backup |
| Anthropic changes subscription use of `claude -p` | Low–medium | Bot stops | API-credit fallback already coded |
| GitHub flags the Actions use | Low | Actions restricted | Light jobs; can move to a dedicated repo or your own machine |
| Bot scores poorly | Medium | $0 season | Ensemble, clipping and research; tune on resolved questions only |
| Metaculus ends or changes FutureEval | Low | Channel ends | Continuous since 2024; watch for the Spring 2027 announcement |
| Payout rail not available in your country | Unknown | Can't collect | Answer the country question in §8 |
| Leaked `CLAUDE_CODE_OAUTH_TOKEN` | Low | Others use your plan | GitHub secret, private repo, no fork-PR triggers. Revoke it in claude.ai settings if exposed. |
| Bot competes with your own usage | Low | Hitting limits sooner | 1–6% of capacity, at most 3 parallel calls |

## 11. Perspectives covered

| Perspective | Section or source |
|---|---|
| Revenue channels: breadth and evidence | §3–4; reports |
| Compute model: subscription vs API vs free credits | §5–6; `Overnight plan research/*automation*`, `free_inference*` |
| Policies of every party (Anthropic, OpenAI, Metaculus, GitHub, Apify, data licences) | §7; `Plan financial and policy check` |
| Full costs, including Claude tokens and plan capacity | §6; `ops/finance_model.py` |
| Revenue expectation, variance and timing | §1, §6 |
| Benchmark against doing nothing or downgrading | §1, §6 |
| Taxes, payout rails and identity checks | §7; `owner_side_risks_tax_payouts.md` |
| Your time and effort | §8; owner-side notes |
| Account and security risks | §10 |
| Tournament rules and ethics | §7; `FORECASTER.md`; `ROUTINE.md` |
| Operations, monitoring, measures and stop rules | §9 |
| Technical feasibility (live-tested) | §5 |
| Long-term sustainability across seasons | §6, §9 |
