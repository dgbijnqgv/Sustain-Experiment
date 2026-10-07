# Autonomous operator routine

This file is the standing instruction for every scheduled session that runs
the business. Read it fully, plus `PLAN.md` and `ops/LEDGER.md`, before acting.

## Hard rules (never break these)

1. **No spending.** Never buy, upgrade, or enter payment details. If a paid
   upgrade would pay for itself, write a proposal under *Proposals* in
   `ops/LEDGER.md`. The owner approves anything above $100 in total.
2. **Legal data only.** Use only official public APIs or open-data feeds whose
   terms allow commercial reuse. Never bypass logins, CAPTCHAs or rate limits.
   Never collect personal data such as named contacts, emails or phone numbers.
3. **No fake signals.** No fake reviews or ratings, and no runs from the owner's
   account to inflate stats. Never post spam or promotional messages anywhere.
4. **Quality over count.** Ship at most one new Actor per week. Only ship it
   when it passes tests and a successful live run.
5. **Leave a trail.** Every session ends by updating `ops/LEDGER.md`, then
   committing and pushing to `claude/ai-revenue-generation-ume6vn`.

## Each session, in order

1. **Preflight.** Check that `APIFY_TOKEN` is set and that
   `curl -s https://api.apify.com/v2/users/me -H "Authorization: Bearer $APIFY_TOKEN"`
   returns 200. If either check fails, record it in the ledger under *Blocked*,
   push, and stop. Do not try to route around the network policy.
2. **Live-validate each Actor locally** with a small input (`lookbackDays: 1`,
   one source at a time). The first time this runs, replace the fixtures in
   `test/` with trimmed real responses and fix every normalizer mismatch,
   especially TED field names, UK notice URLs and Contracts Finder paging.
3. **Health check in production.** For each Actor, `GET /v2/acts/{id}` (stats)
   and `GET /v2/acts/{id}/runs?desc=1&limit=50`. Read the failed runs' logs.
   Fix the root cause, run `npm test`, then `node ops/publish.mjs <dir>`.
4. **Record metrics** in the ledger: total users, 30-day users, 30-day runs,
   failure rate, and any earnings figure the API exposes. Compare them with the
   last entry.
5. **Improve the listing** when users are flat for 2+ weeks. Adjust the README
   title, keywords and example input to match what buyers search for. Do not
   change prices more than once a month, because Apify enforces a notice
   period on price changes.
6. **Build next**, but only if every live Actor is healthy. Take the top
   unbuilt item from *Backlog* in `PLAN.md`. Copy the structure of
   `actors/tender-feed` (normalizer, `ChangeTracker`, pay-per-event `pushData`,
   tests, README listing). Publish it with `--public` once the live run is clean.
7. **Ledger, commit, push.**

## Pivot and stop criteria (evaluate monthly)

- **Day 60:** if total Store users across all Actors are under 10, stop adding
  new Actors. Spend the next month on improving listings and on the backlog
  item with the strongest buyer evidence.
- **Day 120:** if 30-day revenue is under $20, write a *Pivot* proposal in the
  ledger and tell the owner. Do not keep spending their usage on a channel
  that isn't working.
