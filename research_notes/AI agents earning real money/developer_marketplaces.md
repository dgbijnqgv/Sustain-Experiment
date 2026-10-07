# Developer Marketplaces & Agent-Payment Rails: What Independent (incl. AI-built) Offerings Actually Earn (as of 7 Oct 2026)

Method note: WebFetch was blocked (egress proxy) for apify.com, blog.apify.com, docs.apify.com, dev.to, danielmcglynn.com and decipherclub.com. Almost all findings below come from WebSearch result summaries/snippets, not full-page reads. The exception is the GitHub repo savecharlie/x402-census, which I read in full. "Snippet-only" means I saw only search excerpts. Dates are publication or snapshot dates where known. Labels used: **[OFFICIAL]** means a platform's own docs, blog or press; **[SELF-REPORTED]** means an individual developer's claim; **[VENDOR]** means a seller of tools, courses or payment rails, which has an interest in the numbers; **[3P-ANALYSIS]** means an independent analyst or on-chain study.

---

## Key Question 1: Which channels have documented, verifiable cases of small independent developers earning ≥$200/month, and how common is that? (Per-channel earnings distribution and evidence quality)

### Takeaway
Only **Apify Store** has platform-official evidence that a meaningful population of independent developers clears $200/month. The evidence is an aggregate payout of about $1.2–1.6M/month spread across about 3,000–4,500 paid developers, plus official claims that "many" earn over $1k/month. The distribution is power-law: an estimated ~3% of Actors get ~80% of usage, and new Actors usually start with zero users.
- **Shopify, JetBrains and WordPress** have real paid economies, but the median listing earns little and the indie cases are self-reported.
- **MCP marketplaces and x402/agent-payment rails** have almost no verified indie sellers at ≥$200/month. Filtered x402 data shows most sellers earn ~$0, and the top single endpoints gross roughly $1k–5k/month.
- **Raycast, Obsidian, Zapier, Make, Kaggle and Hugging Face** have no native payout mechanism for indie developers.

### Cited Findings

#### Apify Store (pay-per-event Actors)
- **Aggregate payouts [OFFICIAL, snippet-only; snapshots conflict]:** I found three figures that don't agree, so the current number is uncertain.
  - The Apify developer-partner page currently advertises **$1.6M monthly payout and 4,500 community developers**. — [Apify partners page](https://apify.com/partners/actor-developers)
  - Earlier 2026 snapshots of the same page, as quoted by third parties, said **$1.4M/month across ~3,000 developers**. — [AgentByline](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr); [reinventing.ai](https://www.reinventing.ai/blog/apify-actor-passive-income). These two pages appear to be the same syndicated article, written by a developer who builds with Claude Code.
  - An Apify-sponsored talk on daily.dev (~mid-Sept 2026) cited **$1.2M paid to developers "last month"**, 28,000+ Actors and a 20% platform fee. — [daily.dev (sponsored by Apify)](https://daily.dev/posts/build-deploy-monetize-the-future-of-the-developer-economy-sponsor-apify--ybjmxtuy3)
- **Mean vs. median:** $1.4M ÷ 3,000 gives a **mean of about $470 per developer per month**. That is third-party arithmetic, and the source notes it is "heavily skewed, with a few top Actors earning five figures and many earning nothing." — [AgentByline](https://agentbyline.com/articles/apify-actor-passive-income-what-really-earns-in-2026-67lcfr)
- **Top tail [OFFICIAL, help-center article ~late 2025]:** "the most successful independent creators make over **$10,000 MRR**, and many others make more than **$1,000** every month." Apify says it cannot share names or numbers. — [Apify Help Center](https://help.apify.com/en/articles/8684010-make-money-publishing-your-actors-on-apify-store). An older version from summer 2023 said the top creator made over $4,000 MRR. — [DEV/Apify](https://dev.to/apify/programmer-passive-income-how-to-get-new-customers-for-your-web-scrapers-3id)
- **Concentration [SELF-REPORTED analysis, snippet-only]:** One developer's analysis of the top 3,253 Actors found that **the top 100 (~3%) get ~80% of all usage**, and that "a new actor usually starts with zero users." I believe this comes from a dev.to post titled "Why 99% of Scrapers Get Zero Users," but I couldn't confirm that attribution. — [DEV "Apify Actor Survival Guide"](https://dev.to/agenthustler/the-apify-actor-survival-guide-why-99-of-scrapers-get-zero-users-and-how-to-fix-it-5eoh)
- **Competition per target [SELF-REPORTED]:** There are typically **5–15 competing Actors per major site**, several of them maintained by Apify itself. — reported via search summary of [Apify blog "98 Actors"](https://blog.apify.com/building-98-actors-on-apify-store/) / developer accounts (snippet-only)
- **Case studies with numbers:**
  - **Olivier Reynaud (Apify blog, ~July 2026) [SELF-REPORTED on official blog]:** 98 public Actors in 6 months, 2,500 total users, 855 monthly active users and a 98.8% run-success rate. He says PPE variants began outperforming standard ones in early 2026 and that revenue was "meaningful but inconsistent." The excerpts I saw gave no dollar figure. His lesson: "three reliable Actors out-earn ten unmaintained ones." — [Apify blog](https://blog.apify.com/building-98-actors-on-apify-store/)
  - **CTO quoted in an Apify blog post [SELF-REPORTED, partner-facing]:** "Apify is bringing in more than **$2,000** from Apify Store," compared with about $500/month from earlier side projects. — [Apify blog: How to monetize your API](https://blog.apify.com/how-to-monetize-api/)
  - **Partner-page testimonials:** One developer shows a 15-month payout trend across 37 Actors, and another calls September "the first profitable month." The excerpts contained no amounts. — [Apify partners page](https://apify.com/partners/actor-developers)
  - **AI-built case (Indie Hackers) [SELF-REPORTED]:** A developer built 4 Apify scrapers in one day with Claude. By day 3: "no real users yet (the few runs are my own tests)," $0 revenue, and a self-estimate of "$0–20/month, maybe a few hundred if one takes off." — [Indie Hackers](https://indiehackers.com/post/i-built-4-apify-scrapers-in-a-day-with-claude-day-3-no-real-users-yet-heres-what-i-m-doing-about-it-3af12de827)
  - **Hypothetical model [not a case]:** "At 1,000 runs per month per actor, that's $14 to $21 per month per actor." — [DEV: 7 Apify Actors](https://dev.to/weeknds/how-i-built-7-apify-actors-and-started-earning-passive-income-from-web-scraping-5b9e)
- **Store size (conflicting):**
  - "15,000+ Actors" on an older Apify page.
  - "20,000+ Actors" made x402-payable on 30 June 2026. — [Apify blog x402](https://blog.apify.com/introducing-x402-agentic-payments/); [FF News](https://ffnews.com/news/ai-agents-gain-financial-independence-apify-adds-20000-tools-to-coinbases-x402-standard)
  - 28,000+ Actors in the Sept 2026 sponsored talk. — [daily.dev](https://daily.dev/posts/build-deploy-monetize-the-future-of-the-developer-economy-sponsor-apify--ybjmxtuy3)
  - A secondhand "53,954 tools" figure, unverified.

#### MCP server marketplaces
- **Share monetized [SECONDARY blogs, unverified]:** An estimated **<5% of MCP servers are monetized** at all. — [chatforest](https://chatforest.com/guides/mcp-marketplace-monetization/); [DEV "State of MCP Monetization 2026"](https://dev.to/kirothebot/the-state-of-mcp-monetization-in-2026-where-builders-actually-get-paid-34k9)
- **Most-cited success:** 21st.dev reportedly reached **$10k MRR in 6 weeks**. This is a founder claim repeated across vendor blogs, and it is a funded/team product, not an indie MCP-marketplace listing. — [getchatads](https://www.getchatads.com/blog/tools-for-monetizing-mcp-servers/); [mcp-marketplace.io](https://mcp-marketplace.io/blog/state-of-mcp-monetization-2026)
- **MCPize's own guidance [VENDOR]:** It presents a "realistic first-year" target of $500–5,000/month for a well-positioned server. A third-party review called MCPize's payout figures "ecosystem-wide marketing rather than audited totals." — [MCPize blog](https://mcpize.com/blog/make-money-with-mcp)
- **Counter-evidence [SELF-REPORTED, ~early Oct 2026]:** A developer deployed **35 MCP servers on MCPize in 10 days**. Result: "Revenue so far: $0," zero active users, and zero external API calls in the last 24 hours. — [DEV](https://dev.to/alexcodebytes/i-deployed-35-mcp-servers-in-10-days-heres-what-nobody-tells-you-about-ai-monetization-4j8h)
- **Another MCPize write-up:** One developer posted "tier structure, Stripe Connect, real numbers." I could not read it because dev.to was blocked, and the snippet gave no figures. — [DEV](https://dev.to/sai_93caeceb4f6a4d9969910/i-monetized-my-mcp-server-on-mcpize-tier-structure-stripe-connect-real-numbers-4jhf)
- **Unverified mid-tier claim:** "mid-tier servers make $3K–10K/month, most make $0." I couldn't verify it. — [DEV/godberrystudios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)
- **Apify as an MCP channel:** Apify markets "build and monetize MCP servers" with the same 80% PPE split, and Apify Actors are callable through the Apify MCP server. — [Apify MCP developers](https://apify.com/mcp/developers)

#### x402 (Coinbase) and agent-payment rails
- **Headline vs. filtered volume:** The headline numbers overstate real activity by a wide margin.
  - x402.org's "last 30 days" counter (75.41M transactions, $24.24M, 22K sellers) **has shown the same numbers since March 2026**, through Sept 2026. CoinDesk re-reported it in July. — [Daniel McGlynn, 2026](https://www.danielmcglynn.com/the-x402-counter-has-shown-the-same-four-numbers-since-march/) (snippet-only)
  - **Chainalysis (Base only) [3P-ANALYSIS]:** 100M cumulative transactions through Q1 2026, and **3.1M transactions / $1.2M value in the 30 days to 29 May 2026**. Transactions of $1 or more were 95% of volume. — [Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/)
  - **Artemis/Visa:** 178.3M raw transactions and $135.7M raw volume filter down to ~109.6M transactions and **$15.0M** (as of 21 Apr 2026). Artemis classified **~50% of transactions as artificial**, meaning self-dealing or seller-funded buyers. An Artemis analyst's filter puts 30-day adjusted volume at ~$1.6M. Allium puts it at ~$3M. — summarized in [McGlynn](https://www.danielmcglynn.com/the-x402-counter-has-shown-the-same-four-numbers-since-march/); [startuphub.ai](https://www.startuphub.ai/ai-news/startup-news/2026/x402-payments-the-real-numbers)
  - Coinbase's head of AI product (23 Aug) said **25–30% of transactions "may have been generated by users trying to climb public leaderboards."** — via [McGlynn](https://www.danielmcglynn.com/the-x402-counter-has-shown-the-same-four-numbers-since-march/) (snippet-only)
  - Adjusted volume reportedly fell ~77%, from a $5.15M peak (Nov 2025) to $1.19M (May 2026). — [startuphub.ai](https://www.startuphub.ai/ai-news/startup-news/2026/x402-payments-the-real-numbers)
  - **TRM Labs [3P-ANALYSIS]:** ~$52.7M across 198.9M settlements on Base, Solana and Polygon. After excluding self-payments, flows dominated by one or two payers, and sellers with fewer than 10 distinct buyers, about $25.6M remains. TRM notes the excluded activity has not all been proven fraudulent. — via search summary (snippet-only; primary TRM URL not retrieved)
- **Seller concentration:**
  - **Decipher Club [3P-ANALYSIS, 2026]:** Across 2,252 merchants from CDP Bazaar, x402scan and AgentCash, **total 30-day settled revenue was $76,279.84**. One merchant held 38%, the top 3 held 59.5%, and the **top 1% (22 merchants) held 78.6%**. — [Decipher Club](https://www.decipherclub.com/why-x402-merchants-are-poor/) (snippet-only)
  - **x402-list.com directory:** Of 575 services, **only 26 earned anything in 30 days**. The whole directory settled **$516.96**, and one service took 78.6%. — via search summary (snippet-only)
  - **x402scan snapshot (Japanese analysis, note.com):** 3.69M transactions, $1.11M volume, 189,900 buyers and 43,000 "sellers." Even the top seller, StableEnrich, had only **$3.12K over 30 days**. The author's verdict: "everyone is thin." — [note.com/x402inc](https://note.com/x402inc/n/nfd6227f13b55?hl=en-US)
  - **x402-census (read in full) [3P-ANALYSIS, on-chain sample of Base, 23 Aug–25 Sep 2026, 0.35% block sample]:**
    - The busiest seller by call count grosses ~**$1,078/month** at $0.00229 per call.
    - The #2 seller grosses ~**$5,365/month** at $0.02 per call.
    - Recurring payees: 15 of them account for **63.9% of payments but only 1.0% of dollars**.
    - Mean payment is $1.70, but the median of daily medians is **$0.003**.
    - Sellers persist, buyers don't: heavy payees recur ~58% of days, heavy payers ~6%.
    - Caveat: the EIP-3009 selector isn't unique to x402, so dollar totals are contaminated.
    - Source: [GitHub savecharlie/x402-census](https://github.com/savecharlie/x402-census)
  - **Self-reported x402 sellers:**
    - "x402 Week in Production: 689 Probes, **$0.11 Revenue**." — [DEV](https://dev.to/nathanielc85523/x402-week-in-production-689-probes-011-revenue-and-what-fridays-402-minute-event-reveals-24n4)
    - "I fixed the payment rail. **Still $0.** So I measured what every x402 service actually earns." — [DEV](https://dev.to/ofirbaranesadagent/i-fixed-the-payment-rail-still-0-so-i-measured-what-every-x402-service-actually-earns-14j2) (title/snippet only; the author handle suggests an agent-run account)
- **Apify on x402:** Since **30 June 2026**, 20,000+ Apify Actors can be paid via x402, settled in USDC on Base, through the Apify API and MCP server. Developers have to meet eligibility criteria. Apify earlier integrated Skyfire (Dec 2025). — [Apify blog](https://blog.apify.com/introducing-x402-agentic-payments/); [Apify changelog](https://apify.com/change-log/pay-for-apify-actors-with-x402); [Apify on X](https://x.com/apify/status/2001633659921502508). No data on what developers earn via this path.
- **Stripe ACP, Skyfire, Nevermined and Google AP2:**
  - No seller volume figures found.
  - AP2 launched Sept 2025 with 60+ partners.
  - Stripe's Agentic Commerce Suite (Dec 2025) lists big-brand merchants such as Coach, Kate Spade, URBN and Etsy, not indie developers.
  - Skyfire: "thousands of transactions daily," unsourced.
  - Most comparison content comes from Nevermined, a competitor. — [rye.com](https://rye.com/blog/agentic-commerce-startups); [Nevermined blog](https://nevermined.ai/blog/stripe-vs-skyfire-vs-nevermined)
  - A Nevermined roundup cites "$600M annualized" agent-to-agent volume (via BlockEden). That figure is irreconcilable with the filtered data. — [Nevermined](https://nevermined.ai/blog/stablecoin-payments-ai-agents-statistics)

#### API/data marketplaces
- **RapidAPI (Rapid API Hub) [OFFICIAL docs]:**
  - Still operating. Nokia acquired its tech and R&D team in Nov 2024. — [Yahoo Finance](https://finance.yahoo.com/news/nokia-acquires-rapid-api-company-150922026.html)
  - **Marketplace fee rose from 20% to 25% from 15 Nov 2025.** Payouts go through PayPal only, PayPal fees (up to $20) are extra, and providers are paid only after Rapid receives final payment. — [Rapid docs](https://docs.rapidapi.com/docs/payouts-and-finance)
  - Anecdotal reports describe delayed or missing payouts after the acquisition (Jan 2025 forum thread) and payment lag of about 6–8 weeks. — [Latenode community](https://community.latenode.com/t/rapid-api-payments-to-vendors-have-ceased-following-nokias-acquisition-important-update/2888); [archtools (competitor)](https://archtools.dev/blog-rapidapi-alternative)
  - No indie earnings data found.
- **Zyla API Hub:** 80/20 split by default, but the ToS scales the developer share down with uptime: 70/60/50/40%, and 0% below 95% uptime. There is also a 2% processing fee. No earnings data found. — [Zyla monetize](https://zylalabs.com/monetize-your-api); [Zyla ToS](https://zylalabs.com/terms)
- **AWS Data Exchange [OFFICIAL]:** 3% listing fee on public offers plus data-grant hourly charges. Sellers are enterprise-oriented and must register as AWS Marketplace sellers. No indie earnings data found. — [AWS docs](https://docs.aws.amazon.com/marketplace/latest/userguide/listing-fees.html); [AWS pricing](https://aws.amazon.com/data-exchange/pricing/)
- **Datarade:** Quote-based provider subscriptions plus ~30% commission. This comes from a competitor's page. — [ZoomInfo pipeline](https://pipeline.zoominfo.com/sales/datarade-pricing)
- **Kaggle and Hugging Face:** Neither has a seller revenue-share program. HF creators who sell weights do it off-platform via Gumroad or Patreon (forum anecdote). — [HF forum](https://discuss.huggingface.co/t/are-you-monetizing-your-ai-models-and-how/168783)

#### Browser and IDE extensions
- **Chrome Web Store via ExtensionPay [VENDOR]:**
  - ExtensionPay claims developers have made over $500k total through it. It charges a 5% fee on top of Stripe. Its showcase cases, such as GMass at $130k/month in 2019, are old and self-reported. — [ExtensionPay](https://extensionpay.com/); [ExtensionPay article](https://extensionpay.com/articles/browser-extensions-make-money)
  - Vendor benchmark: freemium extensions with 2k–10k users earn **$50–500/month**. The vendor itself says the median is the honest guide because outliers skew the average. — [chromegoldmine](https://chromegoldmine.com/blog/chrome-extension-monetization/chrome-extension-revenue-benchmarks/)
  - **Measured counterpoint [SELF-REPORTED, end of July 2026]:** A portfolio of **38 live extensions** had **MRR of $31.03** and lifetime net revenue of $165.47. — [DEV ktg0215](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga) (snippet-only)
- **VS Code:** No native paid tier; developers sell licenses externally. A widely surfaced "$6,800/month from 3 niche VS Code extensions" post is by the same dev.to author who also wrote an MCP-monetization post (hopkins_jesse). Treat it as **low-credibility, possibly content-farm**. — [DEV](https://dev.to/hopkins_jesse_cdb68cfa22c/how-i-make-6800month-selling-niche-vs-code-extensions-eji). An SEO guide's "$300–2,100/month" benchmark is unverified. — [markaicode](https://markaicode.com/sell-vs-code-extensions-2025/)
- **JetBrains Marketplace [OFFICIAL]:** 15% commission (capped at 25%), with built-in licensing and billing. Perpetual licenses were added in Jan 2025. No indie revenue figures found. — [JetBrains revenue sharing](https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html); [JetBrains blog](https://blog.jetbrains.com/platform/2025/01/introducing-perpetual-licenses-on-jetbrains-marketplace/)
- **Raycast:** There is no paid-extension mechanism. Extensions must be MIT open source and are published via PR to a public monorepo. The store had ~2,000 extensions by April 2026. — [platformappstores](https://www.platformappstores.com/categories/browser-os-extension-stores/raycast-store); [tech-insider](https://tech-insider.org/raycast-vs-alfred-2026/)
- **Obsidian [OFFICIAL]:** "Not a store, does not offer any built-in payment solutions." Plugins must be labeled Free, Optional payments or Paid, and developers handle payments externally. — [Obsidian blog: future of plugins](https://obsidian.md/blog/future-of-plugins/). The one big case is Brevilabs (Copilot for Obsidian): reportedly **$19,541 MRR**, 1,459 subscriptions and $864k lifetime as of 1 Sept 2026. The source labels it "verified," but this is a funded startup, not a typical indie. — [sofarbot](https://www.sofarbot.com/stories/brevilabs-logan-yang-19463-mrr-verified)
- **WordPress:**
  - Barn2's 2025 survey of 33 plugin companies found new-plugin sales **down 17.8%**, with renewals at 61% of revenue. Respondents said people now lean on AI instead of paying for support, which hurts free-to-paid conversion. — [WP Product Talk](https://wpproducttalk.com/blog/wordpress-plugin-sales-survey-2025/); [The Repository](https://www.therepository.email/are-declining-plugin-sales-the-canary-in-wordpress-coalmine)
  - Old Freemius/CodeCanyon data put the average plugin at $3,838/year (~9 years old). — [ChargePanda](https://www.chargepanda.com/blog/post/best-platform-to-sell-wordpress-plugins)

#### Zapier, Make and Shopify
- **Zapier:** Pays app builders nothing; there is "no compensation for app usage" (community team, ~2023). — [Zapier community](https://community.zapier.com/how-do-i-3/do-i-get-any-revenue-as-my-app-is-used-23345). **Make:** no developer payout program found.
- **Shopify App Store [OFFICIAL fees]:**
  - 0% revenue share on the first $1M, 15% above that. There is a $19 one-time registration fee. — [shopify.dev](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
  - The sources disagree on whether the $1M is annual or lifetime from 1 Jan 2025. — [BetaKit](https://betakit.com/shopify-app-developers-will-no-longer-be-exempt-from-sharing-their-first-1-million-usd-in-revenue-every-year/)
  - Third-party estimates (inferred, not audited) put the **median paying app under $1k MRR**, with the top 10% above $100k ARR. — [Weekone Labs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/); [GapQuery](https://www.gapquery.com/blog/how-much-do-shopify-apps-make)

#### Autonomous-agent experiment (cross-channel)
- **Automaton Agency [SELF-REPORTED]:** Gave an autonomous agent a month, a budget and a product, targeting $700/month net. It made **$0**. The agent did the work (funnel, reports, a 25-firm cold-email sequence); "the constraint was never execution, it was demand." — [automatonagency.com](https://automatonagency.com/insights/autonomous-agent-revenue-experiment-teardown)

### Inferences
- **Ranking by verified ≥$200/month indie evidence:**
  1. **Apify:** official aggregate data plus "many over $1k."
  2. **Shopify and JetBrains:** real paid economies, but mostly established teams and few verifiable indie numbers.
  3. **WordPress, Chrome and VS Code:** possible but self-reported, with medians near zero.
  4. **MCP marketplaces, x402 and agent rails:** essentially no verified indie sellers at ≥$200/month apart from a handful of top x402 endpoints that gross ~$1k–5k/month.
  5. **Raycast, Obsidian, Zapier, Make, Kaggle and HF:** no native payout.
- **How many Apify developers clear $200/month (my estimate):**
  - If ~80% of usage goes to ~3% of Actors, and roughly 3,000–4,500 developers receive payouts (the official count may include anyone with any payout), then probably only a few hundred to ~1,000 developers clear $200/month.
  - That is a small fraction of all publishers. Many publishers never earn, and Store size is 20k–28k+ Actors.
  - This is an inference from snippet-level figures, not a published statistic.
- **Time to first revenue:**
  - On Apify, a new Actor typically starts at zero users. The AI-built cases (4 Actors in 1 day; 98 Actors in 6 months) show that usage takes weeks to months, and earnings come mainly from reliability and maintenance, not volume.
  - On x402 and MCP marketplaces, the documented time-to-first-revenue for new sellers is effectively "not yet" ($0, $0.11).
- **x402 economics:** For the few real x402 sellers, price per call matters more than call volume. Micro-priced endpoints at $0.001–0.003 cannot reach $200/month without huge organic agent demand, and that demand largely doesn't exist yet.

### Gaps
- No official Apify distribution data (median payout, number of developers above $X). The partner page, help center and blog could not be fetched directly, so the $1.6M vs $1.4M vs $1.2M figures are unreconciled snapshot quotes.
- No Apify developer revenue screenshots with dollar amounts found for 2025–2026.
- No published payout data from Smithery, Glama, MCP.so, Composio, Cloudflare or MCPize. Smithery reportedly charges creators (~$30/month per one blog), and I found no revenue share, but I didn't verify this.
- I could not retrieve primary TRM Labs or Artemis/Visa reports, or the x402-list.com data.
- Usage of Stripe ACP, Skyfire, Nevermined and AP2 by independent sellers is undocumented.
- No JetBrains or Zyla indie earnings data.

---

## Key Question 2: Where are marketplaces already flooded with AI-generated (or low-effort) listings, and what does that do to new entrants?

### Takeaway
I found no source that directly measures an "AI-generated flood" on any of these marketplaces. The indirect signals are strong, though:
- Apify's Store grew from ~15k to 20k–28k+ Actors, with heavy usage concentration and 5–15 competitors per popular site.
- MCP directories hold thousands of mostly free, low-traffic servers.
- x402 "sellers" are 22k–43k nominal, but only a few dozen earn.
- Google cut new Chrome Web Store publishers to two extension slots in Aug 2026, citing "rising submissions."
- AI-themed Chrome extensions are a documented malware and copycat vector.

For new entrants, especially volume-publishing agents, the result is near-zero discovery. Platforms now rank or limit by quality and usage.

### Cited Findings
- **Apify:**
  - Store growth: 15,000+, then 20,000+ (June 2026), then 28,000+ Actors (Sept 2026), alongside an Apify push to "develop AI agents on Apify" with templates and PPE. — [Apify docs: develop AI agents](https://docs.apify.com/actors/development/quick-start/develop-ai-agents); [daily.dev](https://daily.dev/posts/build-deploy-monetize-the-future-of-the-developer-economy-sponsor-apify--ybjmxtuy3)
  - The top ~3% of Actors get ~80% of usage, and new Actors start at zero users. — [DEV survival guide](https://dev.to/agenthustler/the-apify-actor-survival-guide-why-99-of-scrapers-get-zero-users-and-how-to-fix-it-5eoh) (snippet-only)
  - **Apify launched an Actor Quality score in Nov 2025.** It runs 0–100 and covers reliability, docs, user satisfaction, pricing strategy and maintenance, and it affects Store ranking and Apify MCP `search-actors` ranking. — [Apify changelog: Actor quality](https://apify.com/change-log/actor-quality-is-here); [Apify docs: quality score](https://docs.apify.com/actors/publishing/quality-score)
  - Daily automated tests run each Actor with default input within 5 minutes. Three days of failures puts an Actor "under maintenance," and 28 more days of failures deprecates it. — [How Apify Store works](https://docs.apify.com/academy/actor-marketing-playbook/store-basics/how-store-works)
- **MCP:**
  - Fewer than 5% of servers are monetized. — [chatforest](https://chatforest.com/guides/mcp-marketplace-monetization/)
  - The 35-servers-in-10-days experiment got zero users. — [DEV](https://dev.to/alexcodebytes/i-deployed-35-mcp-servers-in-10-days-heres-what-nobody-tells-you-about-ai-monetization-4j8h)
  - Glama's index includes repo files such as an AI-written "MONETIZATION_STRATEGY.md" for an SSH MCP server, which illustrates speculative listings. — [Glama](https://glama.ai/mcp/servers/@KinoThe-Kafkaesque/ssh-mcp-server/blob/d20d458270b00b0836a56a0408de5fb2b935fbdc/MONETIZATION_STRATEGY.md)
- **x402:**
  - 43,000 "sellers" on x402scan, yet the top seller made only $3.12k/30 days. — [note.com](https://note.com/x402inc/n/nfd6227f13b55?hl=en-US)
  - Only 26 of 575 directory services earned anything. — via search summary
  - About 50% of transactions are artificial (Artemis), and 25–30% are leaderboard-farming per Coinbase. — [McGlynn](https://www.danielmcglynn.com/the-x402-counter-has-shown-the-same-four-numbers-since-march/)
  - Token speculation ("x402 token boom") also inflated activity. — [Yahoo Finance](https://finance.yahoo.com/news/inside-x402-token-boom-payment-081559379.html)
- **Chrome Web Store:**
  - **New per-publisher publication limits took effect 20 Aug 2026, "to keep quality high and account for rising submissions."** The default is **2 extension slots** for new publishers, based on the quality and usage of existing extensions. Developers can request an increase from the dashboard. — [Chrome for Developers blog](https://developer.chrome.com/blog/cws-review-updates-2026)
  - Third-party reporting says approval considers tenure and activity. — [TechStoriesIndia](https://techstoriesindia.com/?p=10591)
- **AI-themed malicious and copycat extensions:**
  - Palo Alto analyzed 5,551 AI-themed extensions released over 9 months and found 341 malicious. — [arXiv 2512.10029](https://arxiv.org/pdf/2512.10029)
  - LayerX found 30+ near-identical "AI assistant" extensions (260k+ users), which Google then removed. — [The Register, Feb 2026](https://www.theregister.com/2026/02/12/30_chrome_extensions_ai/); [Dark Reading](https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions)
  - Two extensions with 900k installs were stealing chats. — [The Hacker News, Jan 2026](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html)
- **WordPress:** AI substitutes for paid support, which reduces free-to-paid conversions (Barn2 survey 2025). — [WP Product Talk](https://wpproducttalk.com/blog/wordpress-plugin-sales-survey-2025/)

### Inferences
- **Mass-publishing is now actively counterproductive.**
  - Chrome caps slots by quality and usage.
  - Apify ranks by quality score and deprecates failing Actors.
  - MCP and x402 directories are already saturated with zero-revenue listings.
- An autonomous agent's edge has to be maintenance discipline and reliability (Reynaud's "3 reliable > 10 unmaintained"), plus niche targets not already covered by 5–15 competitors or Apify's own Actors.
- The AI-themed malware wave likely raises review friction and user distrust for any new AI-branded extension.

### Gaps
- No platform publishes counts of AI-generated listings or removal rates, including Apify, Smithery, MCP.so, Chrome and RapidAPI.
- I found no Reddit or HN thread quantifying an "agent-generated Actor flood" on Apify.

---

## Key Question 3: Platform rules, fees, payout/KYC requirements, and fit for an autonomous Claude Code agent (owner does one-time KYC; $0–$500 budget; no spam)

### Takeaway
No platform found explicitly bans AI-generated code or listings. The rules target duplicate or repetitive experiences, deception, fake reviews and non-functioning listings, and newer controls rate-limit by quality.
- **Apify** is the best fit structurally: GitHub-driven, PPE billing handled by the platform, 80% of revenue minus compute, low payout minimums, monthly payouts, x402 and MCP distribution built in, and quality-score ranking that rewards maintenance an agent can automate.
- **x402** needs only a wallet (no KYC for crypto receipt), but organic demand is negligible.
- **MCP marketplaces** have unclear economics.
- **Chrome and JetBrains** require more human-facing work and review.
- **RapidAPI** now takes 25% and has payout-reliability complaints.

### Cited Findings
- **Apify rules and economics:**
  - **Revenue share:** PPE and pay-per-result developers receive **80% of revenue minus platform (compute) costs**. If an Actor's price doesn't cover usage costs in a month, its profit is set to $0. — [Apify Help](https://help.apify.com/en/articles/12800725-ship-your-actor-and-get-paid); [Apify Academy: how monetization works](https://docs.apify.com/academy/actor-marketing-playbook/store-basics/how-actor-monetization-works)
  - **Rental model retired:** Rental pricing is gone, with Sept 30 / Oct 1 2026 as the hard deadline. Unmigrated Actors move to pay-per-usage. Apify standardized on PPE "following customer feedback and the rise of AI agents." — [Apify blog: standardizing pricing](https://blog.apify.com/standardizing-actor-pricing); [Apify blog: migrate](https://blog.apify.com/migrating-to-pay-per-event-pricing/)
  - **Payouts:** Monthly; the help center says the 11th, while the sponsored talk says the first week. Minimums are **$20 via PayPal and $100 via other methods**, and unmet balances roll over. — [Apify Help](https://help.apify.com/en/articles/12800725-ship-your-actor-and-get-paid); [use-apify.com (unofficial)](https://use-apify.com/docs/apify-for-developers/monetize-actors)
  - **Store terms:** Community Actors are not vetted by Apify. The Acceptable Use Policy (updated 20 Feb 2026) bans "fake accounts or deceptive content" and review manipulation (paid reviews, coordinated accounts), and Apify can remove Actors without notice. — [Apify AUP](https://docs.apify.com/legal/acceptable-use-policy); [Store publishing terms](https://docs.apify.com/legal/store-publishing-terms-and-conditions); [Actor T&C](https://docs.apify.com/legal/actor-terms-and-conditions)
  - **AI-built Actors:** No specific rule on AI-generated Actors was found. Apify actively encourages AI-agent Actors. — [Apify docs](https://docs.apify.com/actors/development/quick-start/develop-ai-agents)
- **Chrome Web Store:**
  - The spam policy bans multiple extensions offering "the same user experience," even with different code or metadata. That covers template extensions, converter clones and localization-only duplicates. — [Chrome spam FAQ](https://developer.chrome.com/docs/webstore/program-policies/spam-faq)
  - The two-slot default limit applies from Aug 2026. — [Chrome blog](https://developer.chrome.com/blog/cws-review-updates-2026)
  - ExtensionPay takes a 5% fee plus Stripe. — [ExtensionPay](https://extensionpay.com/)
- **JetBrains:** 15% commission (max 25%). — [JetBrains docs](https://plugins.jetbrains.com/docs/marketplace/revenue-sharing-and-fees.html)
- **Shopify:** 0% on the first $1M, then 15%, plus a $19 registration fee. — [shopify.dev](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- **RapidAPI:** 25% fee from 15 Nov 2025, PayPal-only payouts, and payment only after Rapid collects. — [Rapid docs](https://docs.rapidapi.com/docs/payouts-and-finance)
- **Zyla:** 80/20 with uptime-based reductions. — [Zyla ToS](https://zylalabs.com/terms)
- **AWS Data Exchange:** 3% fee plus grant charges. — [AWS docs](https://docs.aws.amazon.com/marketplace/latest/userguide/listing-fees.html)
- **MCPize [VENDOR]:**
  - Splits: 80/20 standard. 85/15 was a "Founding Member" rate for servers that activated monetization before 10 June 2026. Payouts go through Stripe Connect. — [MCPize](https://mcpize.com/developers/monetize-mcp-servers)
  - MCP Marketplace: 85/15, per a single vendor post. — [mcp-marketplace.io](https://mcp-marketplace.io/blog/state-of-mcp-monetization-2026)
  - Apify MCP: 80% of charged events. — [godberrystudios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)
- **x402 [OFFICIAL]:**
  - Sellers set the price per request: fixed, "upto" (authorize a maximum, settle usage) or deferred batch settlement. — [Coinbase CDP docs](https://docs.cdp.coinbase.com/x402/how-it-works)
  - Most facilitators charge no fee beyond gas (calculator assumption). — [apicostcalc](https://apicostcalc.com/x402-micropayment-fee-calculator.html)
  - Revenue accrues in a USDC wallet, e.g. a Circle Gateway balance. — [Circle](https://www.circle.com/blog/turn-your-api-into-a-storefront-for-agents)
- **Raycast and Obsidian:** Raycast requires MIT-licensed, PR-reviewed extensions with no payments. Obsidian has no payments and requires labeling. — [platformappstores](https://www.platformappstores.com/categories/browser-os-extension-stores/raycast-store); [Obsidian](https://obsidian.md/blog/future-of-plugins/)

### Inferences
- **Fit for an autonomous Claude Code agent (cloud container + GitHub, owner KYC once, $0–500 budget, no spam). This ranking is my judgment from the evidence above:**
  1. **Apify Store (PPE): best fit.**
     - The whole pipeline is code: build from a GitHub repo, PPE billing, platform-side payments, low payout thresholds, monthly payouts.
     - It comes with distribution via Store search, the Apify MCP server and 20k+-Actor x402 exposure.
     - The quality score rewards things an agent can automate: tests, docs, issue responses, uptime.
     - Realistic outcome: the median new Actor earns ~$0. A small, well-maintained portfolio aimed at underserved niches has a plausible but unproven path to ≥$200/month over months.
     - Compute costs come out of the 80%, so pricing must cover proxy and compute costs.
  2. **MCP via Apify or MCPize: secondary.** It costs little to list alongside Apify, but there is no verified indie revenue, and the 35-server test earned $0.
  3. **x402 endpoints: experimental only.** The setup is easy (wallet, no marketplace KYC), but filtered market-wide revenue is tens of thousands of dollars per month, concentrated in a handful of sellers, and the median seller earns ~$0. It's worth exposing an existing paid service via x402 for marginal reach, not as a primary channel.
  4. **Chrome extensions (ExtensionPay) and JetBrains plugins: poor fit.** They need human-facing UX, support, review cycles and marketing, and Chrome now has a two-slot limit. The measured indie outcome for a 38-extension portfolio was $31/month MRR.
  5. **RapidAPI and Zyla: poor fit.** Fees are high (25% at RapidAPI; Zyla cuts the share with uptime), RapidAPI has payout-reliability complaints, and there is no evidence of indie earnings.
  6. **AWS Data Exchange and Datarade: no fit at this budget.** They are enterprise-oriented and Datarade's provider plans are quote-based.
  7. **Raycast, Obsidian, Zapier, Make, Kaggle and HF: no fit.** None has a payout mechanism.
- **Spam constraints:** The "no spam" constraint lines up with platform rules. Duplicate-experience clones (Chrome), fake reviews and coordinated accounts (Apify AUP) and wash-trading to climb x402 leaderboards would all violate rules or ethics and could get the account removed.

### Gaps
- I could not read the exact Apify payout KYC requirements (tax forms, identity verification) or the x402 Actor eligibility criteria, because the pages were blocked.
- No explicit statements on AI-generated listings from Apify, Smithery, RapidAPI, JetBrains or Shopify.
- No data on how Apify's quality score treats brand-new Actors (cold-start) or whether high-volume publishers are penalized.
