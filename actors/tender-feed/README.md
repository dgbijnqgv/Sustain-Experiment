# Public Tender Feed — EU TED, UK Find a Tender, UK Contracts Finder & SAM.gov

**One clean feed of government contract opportunities from four official portals — filtered to your market, de-duplicated, and returning only what is *new or changed* since your last run.**

Bid teams, consultants and SMEs spend hours a week checking several procurement portals that all use different formats and codes. This Actor pulls them into **one consistent schema**, applies your keyword / CPV / NAICS / country / value filters, and remembers what it already sent you. Schedule it daily and you get a short list of fresh tenders — in a spreadsheet, via webhook, Slack, email, Zapier/Make, or straight into an AI agent via Apify's MCP server.

## What you get

| | |
|---|---|
| **Sources** | 🇪🇺 TED (all EU/EEA above-threshold tenders) · 🇬🇧 Find a Tender · 🇬🇧 Contracts Finder · 🇺🇸 SAM.gov (bring your free key) |
| **Change detection** | Each *watch* remembers delivered notices. Deadline moved, value changed, status updated? You get it again with `changeType: "updated"` and the exact `changedFields`. |
| **Unified schema** | Same fields for every portal: title, buyer, country, deadline, value + currency, CPV, NAICS, link. |
| **LLM-ready** | Every row has a one-line `summary` that drops neatly into prompts, RAG or alerts. |
| **Pay only for results** | Charged per notice delivered. Unchanged notices aren't returned and aren't charged. Set a max cost per run and the Actor stops cleanly at it. |

## Quick start

1. Pick sources, add a few keywords (e.g. `cybersecurity`, `penetration testing`) and/or code prefixes (CPV `72`, NAICS `5415`).
2. Give the watch a name, e.g. `it-security-eu`.
3. Run once to see the last few days, then **Schedule** it daily. Each run returns only new or changed tenders.

### Example input

```json
{
  "sources": ["ted", "uk-fts", "uk-cf"],
  "keywords": ["cybersecurity", "penetration test", "SOC"],
  "cpvPrefixes": ["72", "79417"],
  "countries": ["DE", "NL", "GB", "IE"],
  "minValue": 50000,
  "lookbackDays": 3,
  "watchName": "security-nw-europe"
}
```

### Example output

```json
{
  "id": "ted:612345-2026",
  "changeType": "new",
  "changedFields": [],
  "source": "ted",
  "title": "Germany – IT services – Managed SOC services",
  "buyerName": "Stadt München",
  "country": "DE",
  "deadlineAt": "2026-11-03T00:00:00.000Z",
  "value": { "amount": 480000, "currency": "EUR" },
  "cpv": ["72000000", "79417000"],
  "naics": [],
  "url": "https://ted.europa.eu/en/notice/-/detail/612345-2026",
  "summary": "Germany – IT services – Managed SOC services | Buyer: Stadt München (DE) | Value: 480,000 EUR | Deadline: 2026-11-03 | CPV: 72000000, 79417000"
}
```

## Filters

- **Keywords** — any match in title, description or buyer (case-insensitive). **Exclude keywords** drop matches.
- **CPV / NAICS prefixes** — `72` matches every CPV starting with 72. A notice passes if *either* a CPV or a NAICS prefix matches, so one watch can cover EU and US.
- **Countries** — ISO-2 buyer country (`DE`, `FR`, `GB`, `US` …).
- **Minimum value** — in the notice's currency. Notices that don't publish a value are kept, because most buyers never publish one.

## Pricing

Pay per event: **$0.01 per tender notice returned** (= $10 per 1,000). A typical daily niche watch returns 5–50 notices — roughly $1.50–$15 a month, far below the £350–£5,000 a year that tender-alert subscriptions charge. Apify's standard Actor start fee applies.

## SAM.gov key

SAM.gov requires a free personal API key: sign in at sam.gov → Account Details → API Key (or request one at api.data.gov). Paste it into **SAM.gov API key**; it is stored as a secret input. Daily limits on free keys are low, so SAM.gov results are fetched in a few large pages.

## FAQ

**Is this legal / allowed?** Yes. It only uses the official public APIs and open-data feeds of each portal (TED Search API, the UK OCDS APIs published under the Open Government Licence, SAM.gov's public Opportunities API). No logins are bypassed and no personal contact data is collected.

**How fresh is the data?** As fresh as the portals: TED publishes daily on working days; UK and SAM.gov continuously.

**Can an AI agent use it?** Yes — call it through Apify's MCP server or API and feed the `summary` field to your model.

**Something broken or a portal missing?** Open an issue on the Actor's Issues tab. Reports are triaged within a few days.
