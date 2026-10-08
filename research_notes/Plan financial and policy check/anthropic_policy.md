# Anthropic policy & pricing check (researched 2026-10-08)

Setup: Max ($200, i.e. Max 20x) subscriber uses Claude Code (CLI, cloud sessions, routines) to build revenue projects (Metaculus forecasting bot; paid Apify actors). The bot itself calls Claude via OpenRouter from GitHub Actions.

Method: WebSearch (standard and extended) plus WebFetch. Anthropic pages fetched in full: anthropic.com/legal/{consumer-terms, aup, commercial-terms, credit-terms}, code.claude.com docs, platform.claude.com pricing, and several support.claude.com articles. openrouter.ai was **blocked** by the egress proxy, so everything about OpenRouter comes from search snippets. Items marked "(snippet)" are secondary or unverified.

---

## 1. Consumer Terms and subscription use for commercial projects

**Consumer Terms** (page shows "Effective October 8, 2025" as of 2026-10-08): https://www.anthropic.com/legal/consumer-terms
- Nothing in the terms restricts commercial use of a *paid* plan or of its outputs. The only "personal, non-commercial" clause covers use "for evaluation purposes".
- Outputs: "Subject to your compliance with our Terms, we assign to you all of our right, title, and interest—if any—in Outputs." So the subscriber owns the code and text, to whatever extent rights exist. Inputs stay theirs.
- Prohibited: "develop any products or services that compete with our Services, including to develop or train any AI/ML models … or resell the Services."
  - Selling products built *with* Claude, or selling outputs, is not reselling the Services.
  - Reselling *access* to Claude is prohibited.
- Prohibited: "Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through automated or non-human means, whether through a bot, script, or otherwise."
  - Routines, cloud sessions and `claude-code-action` with `CLAUDE_CODE_OAUTH_TOKEN` are first-party features that Anthropic documents and permits, so they fall under "explicitly permit".
- Prohibited: crawling or scraping the Services; sharing credentials or "mak[ing] your account available to anyone else".

**Claude Code Legal & compliance page** (current): https://code.claude.com/docs/en/legal-and-compliance
- Pro and Max users fall under the Consumer Terms. API users fall under the Commercial Terms.
- Quote: "Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK."
- OAuth (subscription) authentication "is designed to support ordinary use of Claude Code and other native Anthropic applications."
- Quote: "Developers building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication." Third parties may not offer Claude.ai login, may not route requests through Free, Pro or Max credentials on behalf of users, and may not collect or intermediate tokens. Anthropic "may [enforce] without prior notice."

**2026 OAuth timeline:**
- **Jan 9, 2026**: server-side blocks stop subscription OAuth tokens working outside Claude Code and Claude.ai (snippet: gigazine, winbuzzer).
- **Feb 19, 2026**: the docs say explicitly that using subscription tokens in other tools, including the Agent SDK, violates the Consumer Terms (snippet: https://winbuzzer.com/2026/02/19/anthropic-bans-claude-subscription-oauth-in-third-party-apps-xcxwbn/).
- **Apr 4, 2026**: third-party harnesses such as OpenClaw are cut off from plan limits and moved to "extra usage" billing. A plan follows for a capped "Agent SDK credit" pool for programmatic use (snippet: VentureBeat, TheNextWeb).
- **Jun 15, 2026**: Anthropic support says: "We've paused the previously-announced changes to Claude Agent SDK usage". Agent SDK, `claude -p` and third-party apps "still draw from your subscription limits." (https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- **Oct 7, 2026**: monthly API credits are added for Max and Team plans (see section 4).

**Implications for this setup:**
- Using Max and Claude Code (including routines) to build the subscriber's own money-making software is permitted.
- Selling the bot's forecasts or the Apify actors' data is not "reselling the Services".
- Do **not** run the production bot's inference on a subscription OAuth token. Do not expose subscription-backed Claude to Apify customers.
- `claude-code-action` with `CLAUDE_CODE_OAUTH_TOKEN` is documented for repository and dev automation (https://code.claude.com/docs/en/github-actions). Using it as the bot's production LLM backend conflicts with the "ordinary, individual usage" and "use API keys for products" language.

## 2. Usage Policy (AUP)

Source: https://www.anthropic.com/legal/aup. The page says "Effective September 15, 2025". ConductAtlas (snippet) logs only formatting edits in Mar 2026.
- The words "gambling", "betting", "wager" and "prediction" do not appear in the AUP (checked against the fetched text). Forecasting tournaments and prediction markets are not restricted as such. The general fraud and financial-harm clauses still apply.
- Election content: the AUP bars voting misinformation, personalized campaign targeting, and "automated communications to public officials or voters at scale that conceal their artificial origin". Forecasting election outcomes is not covered.
- Data collection: the AUP bars collecting private information without permission and tracking people without consent. It also bars "model scraping" and "model distillation", meaning training other models on Claude outputs.
  - Public government APIs and non-personal data are fine.
  - Avoid using Claude outputs as training data for a competing model.
- Disclosure:
  - Consumer-facing chatbots and interactive agents must disclose that they are AI.
  - High-risk use cases (legal, health, insurance, **finance**, employment, housing, academic testing, journalism) need human-in-the-loop review **and** AI disclosure when outputs reach consumers.
  - A Metaculus bot posting forecasts is not a consumer chatbot. The AUP has no general disclosure duty for it. Metaculus's own rules require bots to be declared anyway.
  - If Apify products give finance advice to consumers, the high-risk rules could apply.

## 3. OpenRouter

- Anthropic's Commercial Terms (effective June 17, 2025; https://www.anthropic.com/legal/commercial-terms):
  - The customer may use the Services "to power products and services" for its own customers.
  - The customer "owns its Outputs".
  - Use restriction: "resell the Services except as expressly approved by Anthropic." The AUP is incorporated.
- OpenRouter lists "Anthropic" as a provider at https://openrouter.ai/provider/anthropic, and Claude is also served via Bedrock and Vertex (snippet). Anthropic has published no reseller list. That OpenRouter has Anthropic's approval is inferred from years of open, first-party listing, not documented.
- OpenRouter's terms (snippet only; the site was blocked) require users to review and comply with each model provider's terms ("AI Model Terms"). For Claude, that brings in Anthropic's AUP and use restrictions, and violations can lead to suspension.
- Conclusion: using Claude via OpenRouter, pay-as-you-go, to power one's own forecasting bot is a mainstream use that appears compliant. The obligations are the AUP plus no resale, distillation or competing model.

## 4. Subscription economics

**Plans** (https://claude.com/pricing):
- Pro: $20 a month, or $17 a month billed annually ($200 a year).
- Max 5x: $100 a month. Max 20x: $200 a month. Max is billed monthly only.
- Limits work on a rolling 5-hour window plus weekly limits. Web, desktop, mobile and Claude Code share one pool.
- Beyond the limits, "usage credits" are billed at standard API rates.
- Anthropic publishes no token or dollar caps.

**Limit history:**
- **Jul 28, 2025**: weekly caps announced, effective **Aug 28, 2025**. For Max 20x the guidance was about 240–480 h of Sonnet 4 and 24–40 h of Opus 4 per week. Anthropic cited a user consuming "tens of thousands in model usage on a $200 plan" (TechCrunch 2025-07-28, https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/).
- **Mar 26, 2026**: peak-hour faster drain (snippet).
- **May 6, 2026**: 5-hour limits doubled and peak-hour reduction removed for Pro and Max (snippet).
- **May 13, 2026**: weekly Claude Code limits +50% as a temporary promotion, extended through Aug 31 (snippet).
- **Sep 14, 2026**: weekly limits permanently +25% over the pre-promotion baseline, which Anthropic itself called a 17% cut from the promotional level (BleepingComputer, https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/; snippet).

**API-equivalent value of Max 20x** (third-party, from Claude Code logs priced at list rates):
- FinOps LLM: about **$1.86k a week** (range $1.74k–$2.2k) at current (125%) limits. https://finopsllm.com/research/claude-max-20x-vs-5x-weekly-limit
- GitHub issue anthropics/claude-code#99330: one week capped at about $1,827 (week starting 2026-09-30). The same issue found a 20x week is only about 1.6× a 5x week.
- Botfarm, with Feb–Mar 2026 data: about $1.1k a week.
- Older anecdotes: "$2k+/month" and "about $15k/yr" (snippets).
- Working estimate: **about $7–8k a month** of API-priced usage at full saturation. That puts $200 at roughly **2.5–3% of list price** when maxed out.
- Converting a task: share of subscription ≈ task API-$ / (weekly cap API-$ ≈ $1.86k), or ≈ $200 × API-$ / about $8,000. For real cost, divide by actual utilization; when usage is well below the cap, the effective cost per API-$ is higher.

**NEW (Oct 7, 2026): monthly API credits.**
- Max 5x gets **$100 a month** and Max 20x gets **$200 a month** in Claude Console API credits.
- Claim them via claude.ai Billing by linking one Console org, after 7 days on the plan.
- The credits cover the Messages and Batch API, Agent SDK and Managed Agents. They do not cover interactive Claude Code or extra usage. They do not roll over and are non-transferable.
- Sources: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans and https://www.anthropic.com/legal/credit-terms.
- **Relevance:** the bot could run on a first-party API key funded by these credits, under the Commercial Terms, instead of paying OpenRouter.

**API prices** (https://platform.claude.com/docs/en/about-claude/pricing, fetched 2026-10-08), per MTok:

| Model | Input | 5m cache write | 1h cache write | Cache read | Output |
|---|---|---|---|---|---|
| Opus 5.5 | $4 | $5 | $8 | $0.20 (0.05×) | $20 |
| Opus 5 | $5 | $6.25 | $10 | $0.50 | $25 |
| Sonnet 5.5 | $2 | $2.50 | $4 | $0.10 | $10 |
| Sonnet 5 | $2 | $2.50 | $4 | $0.20 | $10 |

- Batch API is 50% off (Opus 5.5 is $2/$10).
- Fast mode on Opus 5.5 is $8/$40.
- The full 1M context is at standard price.
- `inference_geo: "us"` costs 1.1×.

## 5. Cloud sessions and routines

- Cloud sessions: "share rate limits with all other Claude and Claude Code usage within your account … There is no separate compute charge for the cloud VM." https://code.claude.com/docs/en/claude-code-on-the-web
- Routines (research preview):
  - "Routines draw down subscription usage the same way interactive sessions do."
  - Hourly start caps: 100 scheduled runs per hour per account; 30 Run-now or API fires per hour per routine; 100 Run-now per hour and 100 API fires per hour per account. There is no overage on these caps.
  - Past the subscription limit, routines continue only if usage credits (metered, at API rates) are enabled. Otherwise runs are rejected until the reset.
  - Minimum interval is 1 hour.
  - Source: https://code.claude.com/docs/en/routines
- Third-party blogs cite daily run caps of Pro 5, Max 15 and Team/Enterprise 25 (snippet). These are **not** on the current official page, which lists only hourly caps.
- No official source mentions a separate "promotional" CCR charge or allowance.
