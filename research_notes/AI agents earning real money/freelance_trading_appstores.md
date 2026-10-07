# Remaining money channels for an autonomous Claude Code agent: freelancing/labor marketplaces, prediction markets & trading bots, AI app stores (as of 2026-10-07)

Method note: Research used WebSearch (standard + extended). WebFetch was blocked by the egress proxy for metaculus.com, lesswrong.com, greaterwrong.com, metaculus.substack.com, arxiv.org, dev.to, and developers.openai.com, so most findings below come from search-result snippets/summaries of those pages, not full-text reads. The only full fetch that succeeded was the GitHub `bounty-census` README. Treat figures accordingly. "Self-reported" = number comes from the platform or person with a stake in it.

Agent profile assumed: Claude Code in a cloud container, GitHub access, scheduled sessions; owner does one-time KYC/payment setup; $0–$500 budget; strictly legal/ethical.

## Q1. Which channels have verified cases of >=$200/month to an individual operator with an AI doing most of the work?

### Takeaway
The single best-evidenced case is **Metaculus AI forecasting bot tournaments (FutureEval)**: official leaderboards show individual bot-makers winning $700–$7,700 per quarterly tournament from bots that must run with *no human in the loop*, i.e. roughly $230–$2,500/month equivalent for top-10 finishers. Every other channel (agent task boards, Poe, GPT Store, Apify, Claude skills marketplaces, Polymarket/Kalshi bots, "AI agencies") has either only aggregate/self-reported numbers or no verifiable individual numbers at all.

### Cited Findings

**Forecasting tournaments (strongest evidence, platform-published payouts)**
- Metaculus Q1 2025 AI Forecasting Benchmark: $30,000 pool, 424 questions, 34 bot makers. Prize-winning bots per the official results page: manticAI (3rd) ~$7,685; acm_bot (5th) ~$5,498; GreeneiBot2 (7th) ~$4,065; twsummerbot (8th) ~$3,826; cookics_bot_TEST (9th) ~$2,380; pgodzinai (10th) ~$2,228; CumulativeBot (11th) ~$1,788; SynapseSeer (12th) ~$1,700; jkraybill_bot (14th) ~$712; MWG (17th) ~$117. Metaculus's own template bot (metac-o1) placed 1st but was not prize-eligible. (Seen via search summary of the results page; not fetched directly.) — [Metaculus Q1 2025 results](https://www.metaculus.com/aib/2025/q1/); [LessWrong: Q1 AI Benchmark Results](https://www.lesswrong.com/posts/rDy5z8ZEtMrEGnfBd/q1-ai-benchmark-results-pro-forecasters-crush-bots)
- Metaculus's template bot (metac-o1) placed 25th of 617 humans in the Q1 2025 Quarterly Cup (top 5%). — [Metaculus Q1 2025 results / LessWrong summary](https://www.lesswrong.com/posts/rDy5z8ZEtMrEGnfBd/q1-ai-benchmark-results-pro-forecasters-crush-bots)
- Spring 2026 FutureEval (5th tournament in series, Jan–May 2026): 173 bots (111 non-Metaculus) on 297 scored questions; $50,000 pool for non-Metaculus bot makers; **30 participants won prize money**. Top-10 bot builders all used GPT-5.2+ in final ensembles (9 of them GPT-5.4); best non-agentic baseline (GPT-5.1) placed 18th of 173; top 10 not statistically distinguishable from each other. — [EA Forum: Pros beat bots but the gap is nearly gone](https://forum.effectivealtruism.org/posts/iJ3qBDwpWCfNy9ZGd/pros-beat-bots-but-the-gap-is-nearly-gone); [EA Forum: What AI forecasting strategy works best (Spring 2026 survey)](https://forum.effectivealtruism.org/posts/tJoxFWkRev5wrEBar/what-ai-forecasting-strategy-works-best-spring-2026-survey)
- Spring 2026: 10 Metaculus Pros beat the top-10 bot team by 1.25 head-to-head points/question on 99 shared questions — not statistically significant. — [EA Forum Spring results](https://forum.effectivealtruism.org/posts/iJ3qBDwpWCfNy9ZGd/pros-beat-bots-but-the-gap-is-nearly-gone); [Metaculus GitHub PR #5205](https://github.com/Metaculus/metaculus/pull/5205)
- Named individual Spring 2026 prize amounts were NOT found (results posts summarized only aggregates).

**Agent task marketplaces (self-reported only)**
- Bounty (trybounty.ai, reportedly a16z-backed): homepage claims "2K+ tasks completed, 200+ active agents, $60K+ verified earnings"; founder claims some agents earn "up to $500 a month for their owners." Self-reported, unaudited. — [Bounty](https://trybounty.ai/); [Arab Founders](https://arabfounders.net/en/lebanese-founder-bounty-ai-agent-marketplace/)
- An autonomous-agent-authored GitHub repo claims agent labour marketplaces had paid **$96.87 total to all agents** (figure in a linked repo; unverified, but suggests very low real flow). — [bounty-census (GitHub)](https://github.com/AsherKasper/bounty-census)
- dealwork.ai (per a May 2026 roundup written by an agent persona): 15% fee, task values $1–$200, most $8–$35; one first gig cited at $2.50. Anecdotal, self-reported. — [DEV: 12 platforms where AI agents earn money (May 2026)](https://dev.to/kirothebot/the-agent-economy-is-real-12-platforms-where-ai-agents-actually-earn-money-may-2026-5bm2)

**App stores (aggregate only)**
- Apify Store: Apify says it has paid >$4M to Actor developers; $563K in Sept 2025 alone (6x YoY). No individual earnings figures found. — [Apify $1M Challenge page](https://apify.com/challenge); [everydev.ai profile](https://www.everydev.ai/developers/apify)
- Poe: no cumulative payout figure from Quora/Poe found; one unverified review claims ">$100,000 paid to bot makers by mid-2026"; another review says "most bots earn very little." — [Perplexity AI Magazine Poe review 2026](https://perplexityaimagazine.com/ai-tools/poe-ai-review-2026/)
- GPT Store: no evidence of meaningful payouts (see Q4). ChatGPT Apps SDK: no reported developer revenue figures found.

**Trading**
- Polymarket: only 2% of traders ever made >$1,000 lifetime (Sergeenkov, Apr 2026); only 0.51% of wallets >$1,000 profit (95M-tx analysis, Apr 2024–Dec 2025). — [Cointelegraph](https://cointelegraph.com/news/gambling-on-polymarket-profitability-data-revealed); [The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-profitability-report-april-2026); [1023jack syndicated analysis](https://1023jack.com/market/are-polymarket-trading-bots-actually-profitable-the-math-behind-2026-s-predictio/)

**AI agency / productized services**
- No verified, founder-attributed AI-agency revenue found. Commonly cited cases (unnamed Austin agency $42K MRR with 2 staff; podcast-clip agency $18K/mo; "restaurant AI host" 35 × $399/mo) come from vendor blogs (Taskade, ALM Corp) without verifiable attribution. — [Taskade](https://www.taskade.com/blog/one-person-companies); [ALM Corp](https://almcorp.com/blog/make-money-ai-digital-agencies-2026/)
- Fiverr seller claim "AI-agent setup for SMBs averages $3,800/month take-home" (June 2026 blog) — no data source named. — [memvers](https://memvers.com/blog/upwork-fiverr-ai-agents-marketplace-shift-2026)

### Inferences
- Metaculus FutureEval is the only channel where (a) the AI legally must do 100% of the work, (b) payouts are published by a neutral third party, and (c) top individual payouts clearly exceed $200/month averaged over a season. But winners in 2026 used frontier-model ensembles (GPT-5.4) with agentic research — competitive entry likely requires API spend, and prize ranking is tightly bunched (luck matters).
- A Claude Code agent with scheduled sessions is structurally well-suited (scheduled forecasting runs, GitHub-hosted bot code), though an "always-on" cron inside a GitHub Action is the more natural fit than ad-hoc sessions given questions can open at random times with 1–2 hour windows.
- Everything else at ">=$200/month verified" fails on verification, not necessarily on possibility.

### Gaps
- Named Spring 2026 and Summer 2026 FutureEval prize winners and amounts (Metaculus pages blocked; only aggregates seen).
- Whether any Claude-based bot placed in prize positions in 2026 (survey said top-10 mostly GPT-5.x).
- Any independently verified individual earnings on Apify, Poe, Bounty, or any agent task board.

## Q2. Freelancing/labor marketplaces: platform rules on bots/AI agents, Upwork/Fiverr agent initiatives, agent-task marketplaces

### Takeaway
Upwork and Fiverr both allow AI-*assisted* work but are built around an identified human account holder: Upwork prohibits unauthorized bots/automation (auto-submitting proposals, scraping) and requires "you and you alone" to use the account; Fiverr requires AI output be "meaningfully refined" and bans fake accounts. Upwork's Uma is a *client-side* hiring agent, not a program for agents to take paid work. Agent-native task boards exist (Bounty, dealwork.ai, Algora/GitHub bounties) but are crypto-heavy, tiny-ticket, saturated, and mostly self-reported.

### Cited Findings

**Upwork rules (official help center, seen via snippets)**
- Bots defined as "any script, program, browser extension, or third-party service that automatically sends requests to Upwork, collects data, or performs actions faster or more frequently than a human could"; unauthorized use can lead to warnings or bans; automation only via an approved API key; spamming proposals/invites and scraping remain off-limits even with a key. — [Upwork: Use bots and other automation properly](https://support.upwork.com/hc/en-us/articles/43342677368467-Use-bots-and-other-automation-properly)
- "You - and you alone - are to use your account and submit work on your behalf"; name should be the one you use in everyday life; freelancer profile needs a real head-and-shoulders photo; unverifiable info can lead to permanent suspension. — [Upwork: Represent yourself authentically](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)
- One main account per person; creating multiple accounts can lead to suspension; if blocked you can't create a new one. — [Upwork support](https://support.upwork.com/hc/en-us/articles/25205969832083)
- Secondary (vendor) sources: AI-drafted proposals are tolerated, but auto-submission without a human click is banned; detection uses behavioral fingerprints (submission speed, session patterns). Vendors (GigRadar, GetMany, Convertix) sell automation tools — biased. — [GetMany: Upwork AI Policy 2026](https://getmany.com/blog/upwork-ai-policy); [GigRadar](https://gigradar.io/blog/upwork-ai-automation)
- Upwork reportedly uses proposal/communication data for AI training by default from Jan 5, 2026 unless opted out (secondary). — [GetMany](https://getmany.com/blog/upwork-ai-policy)

**Upwork AI agent initiatives**
- Uma = "Upwork's AI work agent" to help SMBs find, hire, and work with talent; Spring 2026 update released May 5, 2026; Uma Recruiter shortlists/invites freelancers; vendor-reported "30% more hires" with shortlist. No evidence Uma bids/works on a freelancer's behalf. — [Upwork Spring 2026 updates](https://www.upwork.com/blog/updates-spring-2026); [Appalach.AI](https://appalach.ai/blog/upwork-uma-ai-work-agent-spring-2026-smb-impact/)
- Upwork CEO Hayden Brown (Apr 2026): "We actually see agents hitting our website and trying to hire humans to get work done" — volume small, agents "not very good at it." I.e., agents appear as *clients*, not sanctioned workers. — [CDO Magazine](https://www.cdomagazine.tech/aiml/ai-agents-are-posting-job-ads-on-upwork-and-theyre-not-very-good-at-it)
- Upwork launched a hiring app inside ChatGPT. — [CDO Magazine](https://www.cdomagazine.tech/aiml/upwork-launches-hiring-app-inside-chatgpt)
- Upwork data: AI-related GSV +60% YoY (2024); AI-enabled freelancers command 36% hourly premium (2025, Upwork data). — [agentmarketcap.ai](https://agentmarketcap.ai/blog/2026/04/06/ai-agents-gig-economy-upwork-freelance-job-displacement)
- I found NO Upwork program in which AI agents themselves legally hold accounts and take paid tasks.

**Fiverr rules (official help center)**
- Restrictions apply "regardless of whether a service is created, delivered, or facilitated by a person, through automation, or with the use of AI tools"; bans services automating actions on platforms that prohibit automation. — [Fiverr: Prohibited services](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr)
- Fiverr permits AI in all categories, but output "must be meaningfully refined and tailored"; no "generic, unmodified, or reused AI-generated output"; misrepresentation of AI use can lead to cancellation/refund; AI can't be used for fake accounts. — [Fiverr: Using AI on Fiverr](https://help.fiverr.com/hc/en-us/articles/34998793899665-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients); [Fiverr Community Standards](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards)
- Empty/placeholder deliveries violate ToS. — [Fiverr Policy Violations Explained](https://help.fiverr.com/hc/en-us/articles/48022851354385-Policy-Violations-Explained)
- Fiverr 2026 Business Trends Index (searches Nov 2025–Apr 2026): "Claude Code specialists" +938%; AI voice agents +49% (secondary). — [memvers](https://memvers.com/blog/ai-services-fiverr-2026)

**Agent-task marketplaces (2025–2026)**
- Bounty (NY, reportedly a16z): agents compete for paid tasks; ~1,300 bounties posted by early July 2026; vendor claims above. — [leb.business](https://leb.business/en/article/lebanese-co-founder-is-turning-ai-agents-into-freelancers); [trybounty.ai](https://trybounty.ai/)
- Others: TaskBounty (crypto bounties USDC/ETH/SOL), BountyBook (on-chain oracle escrow, Show HN), Claw Earn (USDC escrow on Base), dealwork.ai, opentask.ai, ugig.net; Circle launched an agent services marketplace May 11, 2026. — [DEV roundup](https://dev.to/kirothebot/the-agent-economy-is-real-12-platforms-where-ai-agents-actually-earn-money-may-2026-5bm2); [Show HN: BountyBook](https://news.ycombinator.com/item?id=47155088)
- RentAHuman (YC): the inverse — agents hire humans; claims "$500K+ paid to humans" (self-reported). — [rentahuman.ai](https://rentahuman.ai/); [YC](https://www.ycombinator.com/companies/rentahuman)
- Payman: payment rails letting agents pay humans under human-set policy limits; product descriptions inconsistent across directories. — [aiagentstore.ai](https://aiagentstore.ai/ai-agent/paymanai)
- Replit Bounties: Replit docs say the program is deprecated and no longer accepting Bounty Hunter applications. — [Replit docs](https://docs.replit.com/additional-resources/bounties/bounty-hunting)

**GitHub/Algora bounties (closest fit to a GitHub-equipped agent)**
- Census as of 2026-08-10 (fetched README; written by an autonomous Claude Code agent per its own claim): 561 open Algora-labeled issues across 74 repos advertise $1,142,625, but ~99% ($1,134,578) sits in 3 repos; the largest (ClankerNation/OpenAgents, $1,091,100 across 201 issues) has 12 stars and zero PRs (likely not real money); the other 71 repos total ~$8,047. After filtering, only 5 claimable bounties worth $60 remained; 9 of 14 initially recommended were already paid (Algora pays by comment, so issues stay open). — [bounty-census](https://github.com/AsherKasper/bounty-census)
- Fresh bounties reportedly attract 8–158 competing agent PRs within hours (blog-style source). — [AgentUpdate.ai](https://agentupdate.ai/news/open-source-monetization-map-2026); a Claude-authored PR in another project says boards are "crowded with competing agent PRs, so expect low yield." — [strikersam PR #1664](https://github.com/strikersam/autonomous-ai-agency/pull/1664)

### Inferences
- Running an AI-operated Upwork/Fiverr freelancer account would conflict with Upwork's "you alone" rule and its bot policy unless the owner personally reviews/submits everything; the legitimate version is "human-in-the-loop productized service" where the owner is the seller and the agent drafts/produces deliverables the owner reviews. That makes it not autonomous and capacity-limited by owner time.
- Agent-native boards are legal and open but economically thin (tasks $2.50–$35 typical, crypto payouts, heavy agent competition). Expected value for a single agent is likely well under $200/month.
- GitHub bounties look attractive on paper but the real claimable pool is tiny after removing phantom/already-paid bounties; spamming PRs also harms maintainers (ethical concern).

### Gaps
- No primary-source quote of Upwork's User Agreement on AI agents specifically; no official Fiverr "AI agent seller" category rules.
- No independently verified earnings for any agent on Bounty/dealwork/etc.
- Outcome of the "I tried to make Claude make me money on open-source bounties" experiment (excerpt cut off).

## Q3. Prediction markets & trading: bot earnings evidence, rules, legality, AI trading competitions, retail base rates

### Takeaway
Bots do extract money from prediction markets (~$40M arbitrage on Polymarket Apr 2024–Apr 2025 per a preprint), but profits are extremely concentrated among fast, well-capitalized market makers; 70–84% of Polymarket accounts lose money and Kalshi takers lose ~32% on average. A $0–$500 Claude Code agent running on scheduled sessions (not sub-100ms) would be on the losing side of arbitrage races. Kalshi's API legally permits automated trading on your own account; Polymarket US is CFTC-regulated and open to US users since ~May 2026; but sports contracts face an active federal circuit split. LLM trading competitions (Alpha Arena) show mostly losses and are statistically meaningless.

### Cited Findings

**Bot P&L / on-chain studies**
- arXiv 2508.03474 (Aug 2025 preprint, seen only via secondary summary): ~$40M extracted via arbitrage on Polymarket Apr 2024–Apr 2025; 86M bids across 17,218 markets; only ~1% of detectable opportunities captured. — [secondary: 1023jack](https://1023jack.com/market/are-polymarket-trading-bots-actually-profitable-the-math-behind-2026-s-predictio/) (arXiv blocked)
- arXiv 2606.16852 ("Ghosts of Polymarket"): documents cancellation attacks that exploit arbitrage bots; one wallet won 286 of 287 settled positions (99.7%), with >$1.49M attributable — i.e., naive arb bots get preyed on. — [arXiv 2606.16852](https://arxiv.org/pdf/2606.16852)
- Arbitrage window reportedly shrank from 12.3s (2024) to 2.7s, mostly captured by sub-100ms bots (secondhand vendor blog). — [Turbine](https://www.turbinefi.com/blog/prediction-market-arbitrage-latency-speed-2026)
- Polymarket profitability: 84.1% of traders in the red (Sergeenkov, Apr 2026, 2.5M wallets, realized P&L only); academic study (U Toronto/HEC Montréal/ESSEC, 2.4M users, $67B volume, Nov 2022–Mar 2026) finds 69% lost money and top 1% captured 76.5% of gains, with profitability tied to liquidity provision (makers). Solidus Labs: 0.55% of profitable maker wallets took 50% of profit. Only 172 of 6,600 wallets averaging >$5k/month profit stayed active >1 year. — [Cointelegraph](https://cointelegraph.com/news/gambling-on-polymarket-profitability-data-revealed); [The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-profitability-report-april-2026); [Coin360](https://coin360.com/news/polymarket-traders-losses-profit-concentration-2026-predictions)
- Kalshi (Bürgi, Deng & Whelan, "Makers and Takers," UCD/CEPR DP20631, 300K+ contracts): takers lose ~32% on average, makers ~10%; contracts <10c lose >60%; average pre-fee return about −20%; contracts >50c earn small positive returns; bias possibly diminishing over time. — [CEPR VoxEU](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market); [UCD WP2025_19](https://www.ucd.ie/economics/t4media/WP2025_19.pdf)
- Marketing claims to disregard: "$313 → $414,000 in a month" bot (Yahoo/Bitget, attributed to an analyst's account, no data); PolyCue Medium post (promotional). — [Yahoo Finance](https://finance.yahoo.com/news/arbitrage-bots-dominate-polymarket-millions-100000888.html); [Medium](https://medium.com/illumination/beyond-simple-arbitrage-4-polymarket-strategies-bots-actually-profit-from-in-2026-ddacc92c5b4f)

**Kalshi API rules & US legality**
- Kalshi offers an official API; Developer Agreement (v1.1, per secondary quotes) limits API use to trading your own account; prohibits redistributing market data, facilitating trades for other members, benchmarking; spoofing/wash trading/MNPI prohibited; limit orders only. Not verified against Kalshi's own docs (secondary). — [Traadence](https://www.traadence.com/blog/kalshi-automated-trading-bot-rules); [Turbine](https://www.turbinefi.com/blog/why-kalshi-built-for-automated-trading-2026)
- Sports contracts circuit split: 3rd Cir. (Apr 2026) sided with Kalshi vs NJ; 9th Cir. (Aug 28, 2026, Nevada) and 6th Cir. (Sept 25, 2026, Ohio/Tennessee) sided with states; NJ petitioned SCOTUS. Michigan preliminary injunction Sept 1, 2026 requires geoblocking ($500K/day penalty); Connecticut denied Kalshi injunction (Aug 2026). — [FinanceMagnates](https://financemagnates.com/fintech/federal-courts-now-disagree-on-kalshis-sports-contracts-new-jersey-wants-the-supreme-court-to-settle-the-fight); [WSN](https://www.wsn.com/betting/nj-asks-us-supreme-court-to-rule-on-sports-contracts/); [MLex](https://www.mlex.com/tax-authority/state-local/articles/2530376/kalshi-sports-contracts-aren-t-financial-swaps-6th-circ-says)
- CFTC ANPRM on event contracts published Mar 12, 2026; CFTC sued (May 19, 2026) to block Minnesota's prediction-market ban (effective Aug 1); one site says a federal court enjoined it July 27, 2026 (single source). — [JD Supra](https://www.jdsupra.com/legalnews/cftc-issues-advance-notice-of-proposed-5243563/); [tech-insider](https://tech-insider.org/prediction-markets/is-polymarket-legal-in-the-usa/)

**Polymarket US availability**
- Polymarket US (QCX LLC) launched Dec 2–3, 2025 as a CFTC-regulated DCM after a Nov 2025 amended designation order; invite-only waitlist removed ~May 2026; requires 18+, US address, KYC. International site still blocks new US trades; Polymarket sought CFTC approval (Apr 2026) to reopen main exchange to US users (no vote found). CNBC (June 26, 2026): CFTC investigating Polymarket (source-based). — [CoinDesk](https://www.coindesk.com/policy/2026/04/28/polymarket-seeks-cftc-approval-to-reopen-main-exchange-to-u-s-traders); [CNBC](https://www.cnbc.com/2026/06/26/cftc-is-conducting-an-investigation-into-polymarket-source-says.html); [Sportico](https://www.sportico.com/business/sports-betting/2026/polymarket-united-states-launch-invite-waitlist-delay-1234879944/)

**LLM trading competitions**
- Alpha Arena Season 1 (nof1, crypto perps, $10K/model, Oct 17–~Nov 3/5, 2025): Qwen3-Max +22.3% ($12,231), DeepSeek $10,489, Claude Sonnet 4.5 $5,799 (−42%), Gemini 2.5 Pro $5,445, Grok 4 $4,208, GPT-5 $4,126; >half ended in the red. — [ForkLog](https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/)
- Season 1.5 (US stocks, ~$320K deployed, Nov–Dec 2025): "Mystery model" Grok 4.20 won, +12% avg; as of Dec 8 only Grok 4.2 remained profitable. Season 2 funded by $15M raise; no final S2 results found. Outlets note short duration, no statistical controls. — [ForkLog](https://forklog.com/en/news/ai-model-grok-4-2-triumphs-in-trading-tournament); [AI Weekly](https://aiweekly.co/alerts/nof1-raises-15m-to-run-ai-models-in-live-trading)

**Retail trading base rates**
- Brazil (Chague, De-Losso, Giovannetti; mini-index futures): of traders persisting >300 days, 97% (1,504/1,551) lost money; ~1.1% earned above minimum wage. Taiwan (Barber, Lee, Liu, Odean; 1992–2006): <1% of day traders predictably profitable net of fees. (Secondary summaries.) — [Faisal Haroon Substack review](https://faisalharoon.substack.com/p/day-trading-failure-rate-analysis); [CNBC 2020](https://www.cnbc.com/2020/11/20/attention-robinhood-power-users-most-day-traders-lose-money.html)

**LLM forecasting benchmarks**
- ForecastBench (FRI): several models now statistically indistinguishable from superforecasters on the tournament leaderboard; top system from Cassi AI; 17 submissions rank above superforecasters on dataset questions (preliminary); an AI system outranks superforecasters on market questions. Earlier (Oct 2025) superforecasters led by 0.017 Brier. FRI projected overall parity ~Nov 2026. — [FRI: AI models have likely reached parity](https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity); [FRI: LLMs closing the gap](https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human)
- Summer 2026 Metaculus Cup: third-party blog reports a bot won outright (Sept 5, 2026), bots 1st/2nd/5th — unverified against Metaculus. — [explainx.ai](https://explainx.ai/blog/ai-beats-forecasters-metaculus-cup-coverage-2026)

### Inferences
- Forecasting skill parity does not translate into trading profit: markets embed fees, the favorite-longshot bias, and adversarial bots; the documented edge goes to makers with capital and latency. With $≤500, even a 5–10% monthly edge (optimistic) yields <$50/month — far below the $200 bar — while variance and loss risk are high.
- Legally, a US owner could KYC on Kalshi or Polymarket US and let the agent trade via API on the owner's own account; this is permitted but the agent must not manipulate (spoof/wash) or offer trading advice to others. Sports contracts carry state-law risk depending on owner's state.
- The better use of forecasting ability is tournaments (cash prizes, zero capital at risk) rather than markets.

### Gaps
- Could not read arXiv 2508.03474 directly; ~$40M figure is secondhand.
- Alpha Arena Season 2/3 results not found.
- No primary Kalshi Developer Agreement text retrieved.

## Q4. AI app stores with revenue sharing: did any pay meaningfully?

### Takeaway
No major AI app store has documented meaningful payouts to small individual builders. The GPT Store revenue program stalled at a closed pilot; the ChatGPT Apps SDK leaves monetization to developers (external checkout; in-app checkout limited); Anthropic's Claude Marketplace (launched late Sept 2026) has no stated developer revenue share; Character.AI has no creator payout program; Hugging Face Spaces has none; Poe pays but publishes no totals. The best-documented store is Apify (>$4M paid to developers, $563K in Sept 2025), which suits a code-shipping agent but lacks individual earnings data.

### Cited Findings
- **GPT Store**: builder revenue program promised for Q1 2024 (US builders, engagement-based); later OpenAI FAQ said it was "partnering with a small group of builders to test GPT earnings based on usage" and "not accepting additional builders." No payout totals ever found. — [VentureBeat](https://venturebeat.com/ai/openai-launches-gpt-store-but-revenue-sharing-is-still-to-come); [OpenAI community thread](https://community.openai.com/t/what-is-the-status-with-gpt-store-revenue-share/839172)
- **ChatGPT Apps SDK**: OpenAI docs describe an in-app checkout via ChatGPT payment sheet; one analysis says it's limited to select partners in private beta and external checkout is the general path. Jan 2026 OpenAI staff advised own-platform signup or external checkout; a user reply said digital-goods monetization/subscriptions weren't allowed in submissions yet. No usage-based revenue share from OpenAI found. No developer revenue figures found. (Docs page blocked; seen via search.) — [OpenAI Apps SDK Monetization](https://developers.openai.com/apps-sdk/build/monetization); [OpenAI forum thread](https://community.openai.com/t/chatgpt-app-monetization-apps-sdk/1372343); [arsum analysis](https://arsum.com/blog/posts/chatgpt-apps-sdk-business-opportunity/)
- **Claude Marketplace (Anthropic)**: launched ~Sept 2026 with 2,000+ connectors/plugins (MCP + Agent Skills); developer submission portal for paid Claude plan holders; paid partner products can be covered by an org's committed Anthropic spend; no developer revenue-share/payout terms found. — [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors/); [gHacks](https://www.ghacks.net/2026/09/27/anthropic-launches-claude-marketplace-with-more-than-2000-connectors-and-plugins/); [Xenospectrum](https://xenospectrum.com/en/claude-marketplace-connectors-enterprise-procurement/)
- **Third-party Claude skill marketplaces**: Agensi paid listings $5–$19 one-time with creator payouts; Agent37 hosted skills with Stripe, creators keep 80% (vendor claim); no revenue totals published. — [Agensi](https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026); [Agent37](https://www.agent37.com/blog/monetize-claude-code-skills)
- **Poe**: Creator Monetization Program — subscription-referral share (originally up to $20 per subscriber, US-only, Oct 2023) plus creator-set price-per-message paid in USD; must open payment-agent account within 90 days or forfeit earnings; Quora said (Jan 2024) the majority of a $75M a16z raise would go to paying creators. No cumulative payout figure found. — [Poe Earnings ToS](https://poe.com/pages/earnings-tos); [Poe blog: price per message](https://poe.com/blog/new-on-poe-creator-monetization-via-price-per-message); [TechCrunch Oct 2023](https://techcrunch.com/2023/10/31/quoras-poe-introduces-an-ai-chatbot-creator-economy/); [TechCrunch Jan 2024](https://techcrunch.com/2024/01/09/quora-75m-funding-a16z-poe-ai-chat)
- **Character.AI**: no creator payment program found as of Oct 2026; June 2026 "creator tools" announcement mentions no payments; monetization aimed at users (c.ai+ $9.99/mo, ads from Apr 15, 2026). Alternatives: Charms.ai ($1.5M pre-seed, May 2026), DreamRP (YC S24). — [eesel](https://www.eesel.ai/es/blog/precios-character-ai); [Decrypt](https://decrypt.co/367543/charms-raises-1-5m-pre-seed-to-bring-the-ai-character-economy-onchain)
- **Hugging Face Spaces**: no built-in creator payout/revenue share found; ad use in Spaces unclear (forum, no staff answer). — [HF forum](https://discuss.huggingface.co/t/policy-clarification-monetizing-spaces-with-google-adsense-third-party-ads/170191)
- **Microsoft**: secondary reports say a Windows Agent Store announced at Build 2026 lets developers keep 85% of revenue; no primary Microsoft doc found. — [FourWeekMBA](https://fourweekmba.com/ai-microsoft-windows-agent-store-framework-build-2026/); [byteiota](https://byteiota.com/windows-agent-store-publish-ai-agents/)
- **Apify Store**: >$4M paid to Actor developers; $563K in Sept 2025; standard 20% commission (developer keeps ~80%) on pay-per-result/pay-per-event; rental model retired Oct 1, 2026; $1M Challenge (ended Jan 31, 2026) paid $2/MAU, $100–$2,000 per Actor. — [Apify challenge](https://apify.com/challenge); [Apify docs: monetize](https://docs.apify.com/platform/actors/publishing/monetize)

### Inferences
- For a GitHub-equipped coding agent, Apify (publish scrapers/automation Actors, pay-per-event) is the most plausible app-store channel: it has a real payout pipeline and the agent can build/maintain code autonomously; owner handles payout KYC once. But individual earnings distribution is unknown and likely power-law; Apify's ToS on scraping targets must be respected (legal risk of scraping sites that prohibit it).
- GPT Store/Apps SDK and Claude Marketplace function as distribution channels for a business that bills elsewhere (Stripe), not as revenue-share programs.

### Gaps
- No individual Apify, Poe, or Agensi creator earnings with verification.
- Microsoft 85% revenue-share terms unconfirmed from primary source.

## Q5. What's prohibited vs legitimately open?

### Takeaway
Prohibited: AI-run or multiple/fake freelancer accounts and unauthorized auto-bidding/scraping on Upwork; generic unmodified AI deliverables or misrepresented AI use on Fiverr; market manipulation (spoofing, wash trading), trading for others or redistributing data via Kalshi API; using the international Polymarket site from the US; offering trading advice/signals to others (investment-advice regulation — not researched in depth). Open: owner-reviewed AI-assisted freelancing; API trading on the owner's own Kalshi/Polymarket US account; autonomous forecasting bots in Metaculus FutureEval; publishing Actors/skills/apps to stores; agent-native task boards.

### Cited Findings
- Upwork bot/automation and "you alone" rules — [Upwork bots policy](https://support.upwork.com/hc/en-us/articles/43342677368467-Use-bots-and-other-automation-properly); [Upwork authenticity](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)
- Fiverr AI/automation rules — [Fiverr AI guidelines](https://help.fiverr.com/hc/en-us/articles/34998793899665-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients); [Fiverr prohibited services](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr)
- Kalshi Developer Agreement restrictions (secondary) — [Traadence](https://www.traadence.com/blog/kalshi-automated-trading-bot-rules)
- Polymarket international site blocks new US trades; Polymarket US requires KYC — [startpolymarket](https://startpolymarket.com/countries/united-states/); [CoinDesk](https://www.coindesk.com/policy/2026/04/28/polymarket-seeks-cftc-approval-to-reopen-main-exchange-to-u-s-traders)
- Metaculus FutureEval explicitly requires no human in the loop; one prize-eligible bot per user; reasoning comment per forecast; makers must share code or description — [Metaculus Spring 2026 page](https://www.metaculus.com/aib/2026/spring/); [LessWrong original series rules](https://www.lesswrong.com/posts/hmnB9zpY5wB7dKMQ3/announcing-the-ai-forecasting-benchmark-series-or-july-8)

### Inferences
- The most "autonomy-friendly" legal channel is the one that *requires* autonomy (Metaculus). Freelance marketplaces structurally require a human principal.

### Gaps
- Did not research US investment-adviser rules for selling AI trading signals.

## Q6. Recurring competitions/tournaments with cash prizes an autonomous agent can legitimately enter

### Takeaway
Metaculus FutureEval is the standout: ~$175K/year in bot-only prizes ($50K Fall 2026 seasonal tournament, now open, plus $1K bi-weekly MiniBench), with ~30 of ~110 outside bot makers winning money in Spring 2026 — roughly 1-in-4 odds of *some* prize, but top prizes (~$5–8K) go to frontier-ensemble bots. ARC Prize 2026 (Kaggle) has big prizes but blocks internet/API access during evaluation (so Claude API-based agents can't compete directly) and is research-hard. Other options (Kaggle generally, hackathons) are per-competition and weren't verified for autonomous-agent eligibility.

### Cited Findings
- FutureEval: "developers compete for a share of $175k in prizes a year"; seasonal tournament every 4 months, always open. — [Metaculus Substack](https://metaculus.substack.com/p/metaculus-futureeval-ai-forecasting-benchmark); [GlobeNewswire launch, Feb 18, 2026](https://www.globenewswire.com/de/news-release/2026/02/18/3239902/0/en/Metaculus-Launches-FutureEval-to-Track-AI-Forecasting-Accuracy.html)
- Fall 2026: $50K tournament (FutureEval page reportedly shows $58K — conflict); Summer 2026 closed Sept 6; prizes paid after questions resolve and winner verification (incl. survey). — [EA Forum: Announcing Fall 2026 FutureEval](https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament); [Metaculus tournaments](https://www.metaculus.com/tournaments/); [GitHub PR #5205](https://github.com/Metaculus/metaculus/pull/5205)
- MiniBench: back-to-back two-week $1K tournaments of ~60 questions, fully AI-generated/resolved questions; prizes paid with main tournament. — [EA Forum Fall 2026](https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament); [Metaculus methodology](https://www.metaculus.com/futureeval/methodology/)
- Historical pools: Q4 2024 $30K (part of $120K series); Q1 2025 $30K; Spring 2026 $50K for outside makers ($58K listed). API credits historically provided courtesy of OpenAI and Anthropic. — [Metaculus AIB Q4](https://metaculus.com/tournament/aibq4); [Metaculus Q1 2025](https://www.metaculus.com/aib/2025/q1/)
- Spring 2026 odds: 30 prize winners among ~111 outside bots (48 survey respondents: 30 won, 18 didn't). — [EA Forum survey](https://forum.effectivealtruism.org/posts/tJoxFWkRev5wrEBar/what-ai-forecasting-strategy-works-best-spring-2026-survey)
- ARC Prize 2026 (Kaggle): ARC-AGI-3 track $850K total incl. $700K grand prize for 100%; solutions must be open-sourced (CC0/MIT-0); no internet during evaluation (rules out hosted LLM APIs); submissions due Nov 2, 2026; results Dec 4, 2026. — [ARC Prize 2026](https://arcprize.org/competitions/2026); [ARC-AGI-3](https://arcprize.org/competitions/2026/arc-agi-3)

### Inferences
- Expected value for a new, competent Claude-based FutureEval bot: plausibly in the hundreds to low thousands of dollars per season if it lands in the paid ranks; zero capital at risk; API cost is the main expense (likely tens to low hundreds of dollars per season depending on research depth — not verified). This is the best risk-adjusted, rules-compliant fit for the agent profile, though it's lumpy (paid after resolution, months later) not monthly income.
- One prize-eligible bot per user caps scaling; the owner's account is the eligible entity.

### Gaps
- Exact Fall 2026 prize distribution curve, start/end dates, and whether API credits are still offered to participants.
- Kaggle-wide rules on autonomous agent submissions; recurring hackathons/AIxCC-style competitions with agent eligibility were not researched in depth (AIxCC ended in 2025 per prior knowledge — not re-verified here).
