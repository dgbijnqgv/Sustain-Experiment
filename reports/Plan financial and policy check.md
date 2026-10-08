> **Status (2026-10-08):** background research. Where it differs from `PLAN.md` (v4), the plan wins: it runs the bot via `claude -p` on the Max plan's API credits and subscription, not paid APIs, and uses the corrected numbers.

# Plan financial and policy check

*2026-10-08. The model is `ops/finance_model.py`, with every assumption a
named parameter. Sources are in `research_notes/Plan financial and policy
check/` and `reports/AI agents earning real money.md`.*

## Verdict

- **Allowed:** yes, by every party involved. Two items need care: GitHub's
  Actions clause and Metaculus's no-human-in-the-loop rule.
- **Above cost:** yes, by a wide margin, *if* the bot runs on the Max plan's
  included API credits. On pay-as-you-go it is barely worth it.
- **Meets the $200/month goal in expectation:** no.
  - Expected value is about **$120/month pre-tax**, or about $90 after tax.
    About $110 of that comes from the bot and about $12 from the tender feed.
  - The bot's money arrives as one lump around Feb–Apr 2027.
  - The chance this season pays at a $200/month rate is about 15–20%. That
    needs a top-20 finish.

## Revenue (Fall 2026 season; forecasting ends ~6 Jan, cash ~Feb–Apr 2027)

| | Expected | Range | Basis |
|---|---|---|---|
| Main tournament prize | $308 | $0–$780 | Summer 2026 template-on-Opus prize ($842), with three reductions: a ×0.77 late-start coverage penalty (prize ∝ score²), a 25–40% field-growth discount, and a 30% chance of $0 |
| MiniBench, about 7 rounds | $140 | $0–$400 | About $20 expected per round at full coverage |
| Tender feed (months 1–6) | $12/month | $0–$96/month | New Actors start at zero users; the top ~3% of Actors take ~80% of usage |

## Costs

| Item | Cost | Notes |
|---|---|---|
| Bot models, main + MiniBench | $398 at API list prices | Opus 5.5 at $4 in / $20 out per million tokens (measured from OpenRouter's catalogue in CI); about $0.54 per question |
| …paid from the Max plan's API credits | **$0 cash** | Max 20x has included $200/month of API credits since 7 Oct 2026. About $600 remains this season, and the credits otherwise go unused. |
| Web research | $0 with AskNews's free tier; about $30 a season via OpenRouter | |
| Claude tokens to build everything so far | $26.26 at API prices (measured) | About **$0.66** of the subscription. A fully used Max 20x is worth about $7–9k a month at API prices. |
| Claude tokens for twice-weekly check-ins | $4–17/month at API prices | About **$0.20/month** of the subscription |
| GitHub Actions | $0 | Hourly fits inside the 2,000 free private-repo minutes. The routine monitors this. |
| Apify | $0 | Free plan. Apify keeps 20% of revenue plus compute. Payout minimum is $20 via PayPal; bank transfer has a $100 minimum and possible SWIFT fees of $10–50. |
| Tax | Depends on country | US: prize is "other income", and Apify income is self-employment income. Non-US: the prize may face 30% US withholding without a treaty claim. |

### Net by funding choice

All figures are for this season. Monthly values are spread over 4 months and
assume 25% tax.

| Funding | Expected net, pre-tax | Monthly after tax | Worst case |
|---|---|---|---|
| **A. Plan API credits + AskNews free (recommended)** | **$448** | **$84** | $0 lost |
| B. OpenRouter pay-as-you-go (MiniBench off) | $137 | $26 | −$295 |
| C. Metaculus donated credits | $448 | $84 | $0 lost; amount and timing unknown |

Option B risks up to $295 to make an expected $137, so I don't recommend
spending your cash on it.

## Policy check

| Party | Allowed? | What we do about it |
|---|---|---|
| Anthropic Consumer Terms | ✅ Commercial use of a paid plan and its outputs is allowed, and you own the outputs. Routines and cloud sessions are documented features. | The bot never uses your subscription login token: Claude Code's terms say products must use API keys. It uses a Console API key, funded by the plan's credits. |
| Anthropic Usage Policy | ✅ Forecasting and public non-personal government data are not restricted. | No personal data. No consumer-facing advice. |
| Metaculus FutureEval | ✅ AI-written code isn't prohibited. Bots must have **no human in the loop**. | The routine never looks at forecasts on open questions and never changes the bot because of them. It tunes only on resolved questions or the test area. Winners must do KYC and file a W-9 or W-8BEN. |
| GitHub Actions | ⚠️ **Grey area.** The terms prohibit activity "unrelated to the production, testing, deployment, or publication of the software project". Running the repo's own bot can count as deployment. It is low burden, and it is the method Metaculus's official template uses. I found no record of enforcement. | Keep it low burden: hourly, cached installs. Worst case is restricted Actions or a suspended account. To remove the risk, I can move the bot to Apify's scheduler for about $4 a month of compute, within the free plan's credit, once Apify is set up. |
| Apify Store | ✅ AI-built Actors are allowed. You must hold the rights to the data and not imply official affiliation. | Listing renamed and marked "unofficial", with source attribution added. |
| TED data | ✅ Free commercial reuse under Decision 2011/833/EU, with credit to the source. | Credit added to the README. |
| UK Find a Tender / Contracts Finder | ✅ Open Government Licence v3 requires an attribution statement. | Exact statement added to the README. |
| SAM.gov | ✅ Public data; each user supplies their own key. | We never share a key. |
| OpenRouter (optional) | ✅ Personal bot use is normal. 5.5% card fee. | Used only for research, if at all. |

## Decisions taken

- The bot now prefers `ANTHROPIC_API_KEY`, i.e. the plan credits. When that
  key is set, MiniBench switches on automatically: on credits it is free
  expected value.
- No pay-as-you-go spend is proposed. The earlier request to approve up to
  $250 is withdrawn.
- The tender-feed listing now carries licence attribution and a
  non-affiliation notice.

## What would change the verdict

- **Credits:** if the plan's API credits are already used by something else,
  the bot's real cost reverts to option B, and the case for it is weak.
- **Score:** if the bot's average peer score on resolved questions is below
  about +5 per question by December, expected prize drops below $150. Stop
  MiniBench spend then.
- **Apify demand:** if the tender feed has fewer than 10 users by day 60, it
  will not contribute meaningfully. Stop adding Actors.
