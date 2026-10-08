# Plan: an AI-run setup that pays for its own subscription

**Goal:** $200 a month net. The owner is involved only for one-time setup and
for approving spend above $100.

**Evidence base:** `reports/AI agents earning real money.md`, built from seven
research tracks; the notes are in `research_notes/`.

## What the research changed

- **Nobody has done this yet.** As of October 2026 there is no verified case
  of a largely autonomous agent netting $200 a month from customers it found
  itself.
  - Agent-run businesses lost money or earned trivially: Project Vend, the
    WSJ's Claudius, Andon Market, Moneylab ($5 from outside customers) and a
    string of $0–$54 build-and-sell experiments.
  - The big numbers came from human audiences, corporate teams reviewing
    every report, or fraud.
- **Agents fail on demand, not building.** The money is where buyers or
  prize money already exist and machine-checkable work is what gets paid.

## Channels

Ranked by the research. Evidence grades come from the report.

### 1. Metaculus FutureEval forecasting bot (primary, `forecast-bot/`)

**Evidence: A−.** This is the one venue whose rules *require* no human in the
loop, and prize tables are published.

- **Prizes:**
  - Fall 2026 has a $50k pool. It opened 28 Sep, forecasting ends about
    6 Jan 2027, and cash arrives around Feb–Apr 2027.
  - Prizes are paid in proportion to score squared, with a $50 floor. 30–41
    bots were paid per recent season.
  - Metaculus's unmodified template running Claude Opus placed 24th of 284 in
    Summer 2026, a score worth about $842.
- **Expected value:**
  - Central estimate for this season: $300–$600 (range $0–$1,000).
  - API cost: about $130–$250 for the rest of the season without donated
    credits, near $0 with them.
- **Built:**
  - Metaculus's official template, unmodified, plus `run.py`. That file adds
    a flagship-model ensemble, two research sources, clipping of extreme
    probabilities and a per-run cost cap.
  - Runs hourly on GitHub Actions.
  - Offline tests pass in CI, and all model IDs are verified on OpenRouter.
- **Timing:** about 12–15% of the expected prize is lost for each week of
  delay, so this goes first.

### 2. Apify pay-per-event Actors (secondary, `actors/`)

**Evidence: B−.** Apify is the only developer marketplace with official
evidence that many independent developers earn $200+ a month. Earnings are
heavily concentrated, and new Actors start at zero users.

- **Built:** the tender feed. It covers EU TED, UK Find a Tender and UK
  Contracts Finder, plus SAM.gov with the user's own key.
  - Validated live in CI on 2026-10-07, with 100% of notices normalized
    correctly.
  - Repriced to $0.03 per notice plus $0.02 per run, before first publish.
- **Cap:** at most 3 Actors until one has paying users. Three reliable Actors
  out-earn ten unmaintained ones.
- **Expectation:** $0–$50 a month through January, $20–$250 a month by about
  April 2027.

### Excluded, with reasons in the report

- Security bounties
- Trading and prediction markets
- Upwork and Fiverr
- AI content: SEO, YouTube, KDP, Medium, music
- Etsy, print-on-demand and stock images
- Standalone x402 or MCP listings
- Agent task boards
- AI app stores
- Code bounties, unless a maintainer explicitly invites them

## Economics and odds (see `reports/Plan financial and policy check.md`)

| | Expected |
|---|---|
| Bot, Fall 2026 (main tournament + MiniBench) | ~$450 prize, paid ~Feb–Apr 2027 (range $0–$1,200) |
| Bot cash cost | **$0**: funded by the Max plan's included $200/month API credits |
| Tender feed, months 1–6 | ~$12/month (range $0–$96) |
| Claude tokens, building + operating | ~$0.66 one-off + ~$0.20/month of subscription capacity |
| **Total** | **~$120/month pre-tax, ~$90 after tax** |

This is below the $200 goal in expectation. The chance of a $200/month-rate
season is about 15–20%, which needs a top-20 bot finish.

**Leading indicators:**
- The bot's average peer score on resolved questions should be at least +5 at
  90% or more coverage.
- The Actors' 30-day user counts.

**Stop rules:**
- Day 60: fewer than 10 Actor users means no new Actors.
- Day 120: under $20 of Actor revenue means a pivot proposal.
- December: a bot score below +5 means turning MiniBench off.

## Budget

| Item | Cost |
|---|---|
| Bot models | $0 cash (Max plan API credits; ~$400 of the ~$600 available this season) |
| Web research | $0 (AskNews free tier); optional OpenRouter ~$30/season |
| GitHub Actions, Apify | $0 (free tiers) |
| **Cash requested** | **$0** (no approval needed) |

## Owner's one-time setup

Everything runs in GitHub, so this container's network settings no longer
matter.

**A. Forecasting bot (about 30 minutes; do this first, since each week of delay costs ~12–15% of the prize)**

1. At https://www.metaculus.com/futureeval/participate/, create a Metaculus
   account, then a **bot account**, then its **token**.
2. Fill in the first section of the participation form:
   https://forms.gle/aQdYMq9Pisrf1v7d8
3. **Claim the Max plan's API credits.** Go to claude.ai → Settings → Billing,
   and link a Console organization (this needs 7 days on the plan). In that
   Console organization, create an **API key**. Optionally set a monthly spend
   limit of $200 there.
4. **For web research,** either email contact@asknews.app for free AskNews
   builder access (1,000 calls a month), or create an OpenRouter key with
   about $10–30 of credit.
5. In GitHub, open this repo → Settings → Secrets and variables → Actions.
   - Under **Secrets**, add:
     - `METACULUS_TOKEN`
     - `ANTHROPIC_API_KEY`
     - `ASKNEWS_CLIENT_ID` and `ASKNEWS_SECRET`, and/or `OPENROUTER_API_KEY`
   - Under **Variables**, add `BOT_ENABLED` = `true`.
6. Reply "bot ready". If you don't, the next scheduled check-in picks it up
   anyway.

**B. Apify (about 20 minutes)**

1. Create an apify.com account.
2. Set up monetization: payout details (PayPal or bank) and the tax form.
3. Create an API token, and add it as the GitHub secret `APIFY_TOKEN`.
4. Reply "apify ready". I publish through the `Apify` workflow.
