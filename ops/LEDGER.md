# Ledger

Append-only log kept by the operator sessions (newest first).

## Status

| Item | State |
|---|---|
| Cash spent | $0 of $500 (owner approval needed above $100) |
| Apify account + payout | ⏳ waiting on owner |
| Container network allowlist | ⏳ waiting on owner |
| `APIFY_TOKEN` in environment | ⏳ waiting on owner |
| Actors live | 0 |
| Revenue to date | $0 |

## Blocked

- 2026-10-07: The container can reach only GitHub and package registries.
  Apify and every data-source host are blocked, so the code is unit-tested
  against documented API shapes only, not yet against live responses.

## Proposals

_(none)_

## Log

### 2026-10-07 — session 1
- Researched channels and chose Apify Store pay-per-event Actors over public data. Reasoning is in `PLAN.md`.
- Built `actors/tender-feed`: TED, UK FTS, UK Contracts Finder and SAM.gov, with change detection and pay-per-event charging at $0.01 per notice. Wrote 7 unit tests, all passing. A local smoke run confirmed the Actor degrades cleanly when sources fail.
- Wrote `ops/publish.mjs` (push, pricing, Store metadata) and `ops/ROUTINE.md`.
