# Master plan: an AI-run setup that helps pay for its own subscription

*Version 4, 2026-10-08 (overnight). It supersedes earlier versions and the two
earlier reports where they differ. It incorporates an independent red-team
review (`research_notes/Overnight plan research/red_team_review.md`). Numbers
come from `python3 ops/finance_model.py` (the "V4" section).*

## 1. Bottom line

- **Recommended engine:** a Metaculus **FutureEval forecasting bot** that runs
  Claude Code (`claude -p`).
  - It is paid **first by your Max plan's included API credits.** Max 20x
    includes $200/month of API credits, which are otherwise unused.
  - It falls back to **your subscription** only if those credits run out.
- **Cost:** **$0 cash.** It doesn't use your weekly limit while credits last.
- **Status:** it's built and tested. 25 offline tests pass, and live `claude -p`
  research and forecasting calls work. Fetching and posting to Metaculus can
  only be tested once you create the bot token.
- **Expected value:**

  | Coverage of question windows | Pre-tax per month | After 30% US withholding |
  |---|---|---|
  | ~95%, with a reliable trigger | **~$105** | ~$74 |
  | ~70%, GitHub's scheduler alone | ~$64 | |

  - Prizes are paid three times a year. The first one (Fall 2026, joined late)
    will probably arrive around Mar–May 2027.
- **Against the $200 goal:**
  - Expected value covers about half.
  - The chance of a season paying at a $200/month rate is **3–8%**.
  - Hitting that rate would take a finish clearly above the best template bots
    so far.
- **If the goal is mainly financial:** downgrade to Max 5x and run the bot as
  well. Max 5x includes $100 of credits, which covers the main tournament.
  That is about **$147/month of value**: $100 saved for certain plus the bot.
  I'm aware you kept Max 20x on purpose to test me, so this is your call.
- **Your part:** about **45 minutes** of one-time setup (§8), plus prize
  paperwork, about 15 hours a year in total (§9).

## 2. Goal and constraints

| | |
|---|---|
| **Goal** | $200/month net to cover the subscription, with minimal owner involvement |
| **Cash budget** | $500 total; above $100 needs your approval. **This plan spends $0.** |
| **Compute** | Your Claude plan, specifically its included API credits, then the plan itself. Codex is a backup on your own machine only. Pay-per-token APIs are never paid in cash. |
| **Ethics** | No spam, no fake reviews, no terms-of-service violations, no undisclosed AI, no personal data |
| **Agent's limits** | It can't open accounts, pass identity checks, receive money or spend money. Those steps are yours. |

## 3. Why this strategy

1. **Agents that try to find their own customers don't make money.** I found
   no verified case of an autonomous agent netting $200/month from customers it
   found itself. Agent-run shops lost money, and agents that build and sell
   earned $0–54. Source: `reports/AI agents earning real money.md`.
2. **Prize money that already exists, judged by machine, does pay agents.**
   FutureEval is the clearest case.
   - Its rules **require** no human in the loop.
   - It pays $175k a year, to 30–41 bots per season.
   - Metaculus's own template running Claude Opus placed **24th of 284** in
     Summer 2026, worth about $842. Caveat: those per-bot figures come from a
     third-party compilation.
3. **Other channels, ranked** (`research_notes/Overnight plan research/`):
   - **CrunchDAO DataCrunch:** ~$8–50/month, usually $0. The payout curve is
     very steep and payment is in crypto.
   - **Apify tender feed:** built; ~$12/month.
   - **Kaggle CASMI26:** under a 5% chance of any cash.
   - **Ruled out**, with sources in the reports:
     - content, SEO, YouTube and KDP;
     - bounties and bug bounties;
     - freelancing;
     - trading;
     - AI app stores;
     - micro-SaaS;
     - x402 and MCP listings.
4. **The compute is allowed, in this order of preference:**
   1. API credits paying for `claude -p` (clean).
   2. Subscription `claude -p` with `CLAUDE_CODE_OAUTH_TOKEN`. Anthropic
      documents this "for CI pipelines, scripts". It's a grey area under the
      "ordinary, individual usage" wording, but it's for your own benefit, not
      a product for others.

## 4. Channels

| # | Channel | Status | Expected/month | Your effort | Evidence |
|---|---|---|---|---|---|
| 1 | **FutureEval bot**, main tournament | Built; needs tokens | ~$67 pre-tax | Setup in §8 | B+ |
| 1b | MiniBench, same bot | Built; on once the repo is public | +$38 | Repo visibility | B |
| 1c | Market Pulse (~$7k/quarter), same bot | Roadmap: needs forecasts to keep updating | Unknown, likely a smaller field | None | C |
| 2 | Apify tender feed | Built, live-validated, unpublished | ~$12 | 20 min, identity check | B− |
| 3 | CrunchDAO DataCrunch 2 | Researched | $8–50 | Sign-up, crypto wallet, exchange identity check | B− |
| 4 | Kaggle CASMI26 (closes Dec 14) | Researched | <5% chance of any cash | Phone verification, accepting rules | C |

**Recommendation:**
- Do 1 and 1b now.
- Start 2 or 3 only if you say yes; each adds paperwork for small money.
- Skip 4.

## 5. Architecture

```
External trigger, every 15 min (cron-job.org) ──┐
GitHub schedule, every 30 min (backup) ─────────┤
                                                 ▼
GitHub Actions: forecast-bot-tournament.yaml (one run at a time)
  └─ run.py   Metaculus's official template + our ensemble subclass
     ├─ fails in seconds if the Metaculus token is bad
     ├─ open, unanswered questions only
     ├─ research    → claude -p Sonnet, high effort, WebSearch/WebFetch,
     │                with a forecasting system prompt
     ├─ 5 forecasts → claude -p Opus, high effort, no tools, independent
     ├─ parse       → claude -p Haiku
     ├─ median, binary forecasts clipped to 3–97%
     └─ post the forecast, then the required reasoning comment (retried)
  Credentials per call: ANTHROPIC_API_KEY (plan credits) → CLAUDE_CODE_OAUTH_TOKEN
  Logs: counts and errors only, with digits masked.

Claude Code check-in, Mon/Thu: health, coverage (counts only), fixes, ledger
GitHub emails you automatically when a scheduled run fails.
```

- **Why 15 minutes plus an external trigger:**
  - Questions are open for about **1.5 hours**.
  - In this repo, GitHub's hourly schedule fired once in about 7 hours.
  - Another bot builder measured about 5 runs a day on a 20-minute schedule.
  - Bots with 50–90% coverage earned a median of **$0**.
- **Why a public repo:**
  - Running every 15 minutes needs about 2,900+ Actions minutes a month.
    Public repos have unlimited minutes; private repos get 2,000.
  - Metaculus requires winners to share their code anyway.
  - Logs mask digits, and secrets never appear in public.
- **Fallbacks already in the code:**
  - OpenRouter, using Metaculus's donated credits.
  - Codex on your own machine via cron.
  - `FORECASTER.md`: a Claude Code routine playbook, used only if Actions is
    disabled, never both at once.

## 6. Economics

| Item | Value |
|---|---|
| Steady-state prize, ~95% coverage | ~$67/month main + ~$38/month MiniBench = **~$105 pre-tax** |
| Fall 2026 | ~$308 main (late start). Paid around Mar–May 2027. |
| Later seasons | Field growth has cut each season's dollars per point by 25–40%. The estimate keeps falling unless the bot improves. |
| Chance of $0 in a season | ~30% |
| Chance of a $200/month-rate season | 3–8% |
| Model cost at API prices | ~$54–76/month main only; ~$132–187/month with MiniBench |
| What you actually pay | **$0**: Max 20x includes $200/month of credits. A Console organization with no card on file cannot overspend. Overflow falls back to the subscription. |
| GitHub | $0 with a public repo |
| My overnight build | ~$68 at API prices, mostly cached re-reads. It used part of your weekly limit, which is at "warning" until about Oct 14. |
| Check-ins | ~$1–3 per check-in at API prices, from your subscription. The routine is kept short. |
| Tax | US: ordinary income. Non-US: expect 30% US withholding on prizes. |

## 7. Compliance

| Party | Verdict | How we comply |
|---|---|---|
| Anthropic | ✅ API credits for `claude -p`. ⚠️ Subscription token: documented for scripts and CI; grey under "ordinary, individual usage". | Credits first. One personal bot, no reselling. The token lives only in a GitHub secret. |
| Metaculus | ✅ Bots allowed, including AI-written. One prize bot per person. No human in the loop. Reasoning comment required. | Logs show counts only, with digits masked. Maintenance looks only at errors, coverage and resolved questions. The community prediction is never used. **Never a second bot.** |
| GitHub | ⚠️ Actions must relate to the repo's project. This is the bot's own repo running itself, which is Metaculus's official method. | Short jobs. Secrets only in the steps that use them. |
| cron-job.org (trigger) | ✅ It only calls GitHub's API. | A fine-grained token limited to Actions on this one repo. |
| OpenAI (Codex) | Backup only, on your own machine (✅). Running it in CI is discouraged. | Not used. |
| Apify and data licences | ✅ | Marked unofficial; TED and OGL attribution included. |
| Taxes and identity checks | Your obligation | Use your legal name everywhere. W-9 or W-8BEN at payout. |

## 8. Your one-time setup (about 45 minutes)

**Fastest way:** on your own computer, clone this repo and run
`bash ops/setup.sh` (needs the GitHub CLI `gh` and Node.js). It does every
scriptable step itself: visibility, secrets, variables, a live test on the
practice area, and switching the bot on only after the test passes. It stops
only at browser pages that need you, opens each one, and checks the trigger at
the end. Tokens are typed into hidden prompts that send them straight to
GitHub, never into chat. Re-running it skips finished steps. The manual steps
below are the same process by hand.

**Model choice** (asked by the script):

| Plan | Main tournament | MiniBench | Credits used (API-equivalent) |
|---|---|---|---|
| Max 20x | Opus 5.5 | Opus 5.5 | ~$132–187 of $200/month |
| Max 5x | Opus 5.5 | Sonnet 5.5 (`MINIBENCH_FORECAST_MODELS`) | ~$105–150 against $100/month; the overflow (~$5–50) runs on the subscription token |

Opus 5.5 costs $4/$20 per million tokens, Sonnet 5.5 $2/$10, Haiku 5.5
$0.10/$0.50. On the plan's included credits the price is not cash, so the
strongest model wins. Prize money grows with the square of the score, so a
model that scores 10% lower earns roughly 20% less. Haiku stays as the parser
only: small models have scored below zero in past seasons, which pays $0.

**A. Accounts and tokens (25 min)**
1. **Metaculus:** at https://www.metaculus.com/futureeval/participate/, create
   an account, then a **bot account** and its **token**. Fill in the first
   section of https://forms.gle/aQdYMq9Pisrf1v7d8 and tick the credits request.
2. **API credits:** at claude.ai → Settings → Billing, claim the Max plan's
   monthly API credits by linking a Console organization (this needs 7 days on
   the plan).
   - **Do not add a card** to that organization. Then it cannot overspend.
   - Create an **API key** there.
   - If credits aren't claimable yet, skip this. The subscription token below
     works on its own.
3. **Subscription token (fallback):** in a terminal, run
   `npx -y @anthropic-ai/claude-code setup-token`, log in, and copy the token.
4. *(Optional, free)* Email contact@asknews.app for AskNews builder access, as
   a second research source.

**B. GitHub (10 min)**
5. Make this repository **public**: Settings → General → Danger zone → Change
   visibility. This gives unlimited Actions minutes and turns on MiniBench.
   It contains code, plans and research only; secrets stay secret.
   *Prefer private?* Then skip MiniBench, and add a payment method with a $10
   spending limit if you also add step 6.
6. Go to Settings → Secrets and variables → Actions:
   - **Secrets:** `METACULUS_TOKEN`, `ANTHROPIC_API_KEY` (if you have it) and
     `CLAUDE_CODE_OAUTH_TOKEN`.
   - **Variables:** `BOT_ENABLED` = `true`, and `RUN_MINIBENCH` = `true` if the
     repo is public.

**C. Reliable trigger (10 min, strongly recommended)**
7. **Create a GitHub token:** Settings → Developer settings → Fine-grained
   tokens. Limit it to this repo only. Permission: **Actions: Read and write**.
   Expiry: 1 year.
8. **Create the trigger:** at https://cron-job.org (free), create a job that
   runs every 15 minutes and sends:

   ```
   POST https://api.github.com/repos/dgbijnqgv/Sustain-Experiment/actions/workflows/forecast-bot-tournament.yaml/dispatches
   Headers:
     Authorization: Bearer <token from step 7>
     Accept: application/vnd.github+json
   Body:
     {"ref":"claude/ai-revenue-generation-ume6vn"}
   ```

**D. Tell me (one line each)**
- Your **country of tax residence**. It affects withholding, payout options and
  whether options 2 and 3 make sense.
- Whether you want options **2 or 3**.
- Whether you want the **downgrade-plus-bot** option.

## 9. Ongoing obligations and timeline

| When | What | Who |
|---|---|---|
| Mon/Thu | Health and coverage check, fixes, ledger | Agent |
| Run failures | GitHub emails you; the next check-in fixes them | Agent |
| Early December | **Spring 2027 prep:** confirm the new tournament ID (set the `TOURNAMENT_ID` variable if the library hasn't updated), re-submit the participation form, renew AskNews | Agent prepares; you fill in forms |
| ~Jan 6, 2027 | Fall forecasting ends; Spring starts around Jan 7 | Automatic |
| Mar–May 2027 | Fall prize: identity check, nationality and residency proof, W-8BEN or W-9, bank details, bot-maker survey. **Respond within 30 days** or the prize may be forfeited. | You, ~1–2 hours |
| Every year | Tax filing for the prize income | You |
| ~Oct 2027 | `CLAUDE_CODE_OAUTH_TOKEN` and the GitHub token expire (1 year). Renew both. | You, 10 min |

Your total time: about 45 minutes now, then about 10–15 hours a year.

## 10. Measures and decision points

| Measure | Target | If missed |
|---|---|---|
| Coverage (`forecast-bot-coverage.yaml`, counts only) | ≥ 90% from week 1 | Check the external trigger; add a second trigger |
| Failed runs | 0 | Fixed at the next check-in |
| Peer score on resolved questions | ≥ +5 per question once 40+ have resolved | Below 0: turn MiniBench off and review using resolved questions only |
| Credits used | ≤ $200/month | Lower `PREDICTIONS_PER_QUESTION` or turn MiniBench off |

## 11. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| GitHub schedule drops runs | High | External trigger every 15 min, plus the 30-min schedule |
| A token or API problem uses up runs | Medium | Fast-fail token check; GitHub failure emails |
| Anthropic policy change for subscription `claude -p` | Low–medium | Credits are the primary path anyway |
| Bot scores poorly | Medium | Ensemble, high effort, clipping; tuning only on resolved questions |
| A forecast is posted without its comment | Low | Comment retries, comment-first ordering in `mc.py` |
| Leaked tokens | Low | Step-scoped secrets. Revoke a leaked GitHub token in GitHub settings, and the Claude token in claude.ai settings (check the exact path when you set it up) |
| Bot competes with your own usage | Low | Credits are primary; at most 3 calls in parallel |
| FutureEval changes or ends | Low | It has run continuously since 2024; re-plan each season |
| Payout rail missing in your country | Unknown | Tell me your country (§8D) |
| The prize-model numbers rest on a third-party payout compilation | Medium | Ranges and grades reflect it; real results replace the model after Fall |

## 12. Perspectives covered

| Perspective | Where |
|---|---|
| Revenue channels: breadth, evidence, rankings | §3–4; `reports/`; `research_notes/` |
| Compute: subscription vs credits vs API vs free | §1, §5–6; `claude_subscription_automation.md`, `codex_*`, `free_inference*` |
| Policies of every party | §7; `Plan financial and policy check/` |
| Full costs, including Claude tokens, credits and Actions minutes | §6; `ops/finance_model.py` |
| Expected revenue, variance, timing and its decline | §1, §6 |
| Benchmark: downgrade, and downgrade plus bot | §1 |
| Tax, payout rails, identity checks and claim windows | §7, §9; `owner_side_risks_tax_payouts.md` |
| Your time, now and yearly | §8–9 |
| Reliability: scheduling and coverage | §5, §10–11 |
| Security of tokens and secrets | §7–8, §11 |
| Tournament rules and fairness | §7; `ROUTINE.md`; masked logs |
| Testing status: what is and isn't verified | §1 |
| Season calendar and renewals | §9 |
| Independent review | `red_team_review.md`. All 5 critical items are addressed here. |
