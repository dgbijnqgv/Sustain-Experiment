# Plan: an AI-run business that pays for its own subscription

**Goal:** $200/month net, with the owner involved only for one-time setup and
for approving spend above $100.

## What an agent can and can't do here

- **Can:** write, test and maintain code, research, and run on a schedule (Claude Code routines).
- **Can't:** open accounts that need identity checks, receive money, solve
  CAPTCHAs, or spend money. Those tie to the owner's identity, so they are the
  owner's one-time steps.
- **The real bottleneck is distribution, not building.** Public experiments
  where agents ran their own businesses show the same thing: the agent can
  build the product, but nobody finds it. Publishing 100+ articles brought
  near-zero traffic, and automated outreach gets flagged as spam.

## Options considered

| Option | Verdict |
|---|---|
| SEO/content site, ads, affiliate | ✗ Months to traffic, and Google penalizes scaled AI content |
| Gumroad or Stripe digital products | ✗ No built-in buyers, so it needs marketing an agent can't do without spamming |
| Open-source bounties (Algora etc.) | ✗ Saturated by agents (30+ attempts on $50 issues) and a burden on maintainers |
| Freelance platforms | ✗ Their terms forbid bots, and the work needs a human |
| Trading | ✗ Speculation, not income |
| **Apify Store pay-per-event Actors** | ✓ **Chosen.** Details below. |

### Why Apify

- **The marketplace brings the buyers.** Apify Store has its own search and SEO, and AI agents call Actors through Apify's MCP server.
- **Revenue depends on code, not marketing.** Developers keep 80% of revenue minus compute.
- **It's built for an agent.** The product is pure code, and the ongoing work is fixing breakage, which an agent does well.
- **No upfront cost.** The free plan covers development, and PayPal payouts start at $20.

### Choosing what to sell

Single-API scrapers are oversupplied. EDGAR, SAM.gov, openFDA and
ClinicalTrials.gov already have 5 to 10+ near-identical Actors, often
agent-made, with 2 to 36 users each. The opening is in **cross-source joins
plus change detection**, sold to buyers who already pay real money:

- Tender alerts cost £350 to £5,000 a year.
- GovCon intelligence costs $500 to $100,000+ a year.

## Product line

1. **Public Tender Feed** (built in session 1) covers EU TED, UK Find a Tender,
   UK Contracts Finder and SAM.gov in one schema. It returns only new or changed
   notices for $0.01 each.
   - No existing Actor covers all four portals.
   - Buyers are bid consultants and SMEs.

The backlog below is built in order, at most one per week:

2. **Pharma/MedTech Signal Monitor** gives field-level diffs from ClinicalTrials.gov, openFDA 510(k)/PMA and recalls, and FDA notices in the Federal Register. Buyers are biotech investors and competitive-intelligence teams.
3. **Rulemaking Docket Tracker** links Federal Register rules to Regulations.gov dockets, with comment-count deltas and deadline alerts.
4. **GovCon Vendor Dossier** is keyed by UEI and combines SAM registration status and exclusions, USAspending award history and SBIR history.
5. **Entity ID Crosswalk** maps LEI to SEC CIK to UEI, using GLEIF plus SEC data.

Avoid these sources:

- **OpenCorporates:** its free data is share-alike.
- **FRED:** third-party series carry copyright restrictions.
- **Any personal-data sources.**

## Economics (honest)

Net income is 80% of revenue minus compute, so **$200 net needs about $260
gross a month**. At $0.01 per notice, that is about 26,000 notices a month.

A typical paying user runs one daily watch and receives 300 to 1,500 notices a
month, so the target needs **about 20 to 80 active paying users across the
portfolio**. For comparison, the best SAM.gov Actor found had 36 users in total.

| Horizon | Realistic range | Odds of covering $200/mo |
|---|---|---|
| Month 1 | $0 (listing, validation, first users) | ~0% |
| Months 2–3 | $0–$50/mo | ~5% |
| Month 6, 4–5 Actors | $20–$250/mo | ~20–30% |

These odds are a judgement, not a forecast; Apify does not publish earnings
distributions. If the numbers aren't there by day 120, the routine stops and
proposes a pivot rather than burning more usage (see `ops/ROUTINE.md`).

## Budget

- **Planned cash spend now: $0.**
- **Possible later ask:** Apify's paid plan, if canary and test runs outgrow
  the free credits. I'll bring numbers before asking.

## How it runs on its own

A scheduled routine starts a fresh Claude Code session twice a week. Each
session follows `ops/ROUTINE.md`:

1. Validate and fix the live Actors.
2. Record metrics.
3. Improve the listings.
4. Build the next backlog item.
5. Commit the ledger.

Progress is visible in `ops/LEDGER.md` on this branch.

## Owner's one-time setup (about 20 minutes)

1. **Create an Apify account** at apify.com. Then open Settings → Integrations
   → API tokens, and create a token.
2. **Set up monetization.** In Apify Console → Development → Publication /
   Monetization, add your payout details (PayPal or bank) and the tax form. Only
   you can do this, because it is tied to your identity.
3. **Add the token to this cloud environment.** Open the environment menu in
   the session title bar → Edit, and add the environment variable `APIFY_TOKEN`.
   Don't paste the token into chat.
4. **Allow network access** in the same Edit screen. Either choose full network
   access, or add these allowed domains:
   - `api.apify.com`, `apify.com`, `console.apify.com`
   - `api.ted.europa.eu`, `ted.europa.eu`
   - `www.find-tender.service.gov.uk`, `www.contractsfinder.service.gov.uk`
   - `api.sam.gov`
   - Later Actors also need `clinicaltrials.gov`, `api.fda.gov`, `www.federalregister.gov`, `api.regulations.gov`, `api.usaspending.gov`, `api.gleif.org`, `data.sec.gov`, `www.sec.gov`
5. *(Optional)* Get a free SAM.gov API key and add it as `SAM_API_KEY`. It is
   only used to test the SAM.gov source; customers supply their own key.
6. Reply **"done"**. I'll then:
   - validate against live data,
   - publish the first Actor,
   - create the twice-weekly routine.
