# Agents earn only where money already waits

As of October 2026, no independently verified case exists of a largely autonomous AI agent netting $200 a month from customers it found on its own. Every real-world agent business that published numbers either lost money or earned trivial sums. Andon Labs' AI-run San Francisco store was down an estimated $40,000–$62,000 of its $100,000 budget by September 2026. Moneylab has $5 of outside revenue against about $200 a month of API spend. An agent at dfdx labs earned $1.54 on about $7,000 of tokens. At least half a dozen 2026 "build it and sell it" agents finished between $0 and $54. The headline figures attached to AI agents came from somewhere else: human attention (Truth Terminal's $50,000 gift, AI Village's donors), corporate teams that reviewed every output (XBOW, the $4M AIxCC prize), or fraud (Michael Smith's AI-music streaming scheme, which earned him 18 months in prison).

The one channel with strong, third-party-published evidence that individuals get paid for fully autonomous work is the **Metaculus FutureEval bot tournament**. Its rules forbid a human in the loop, and 30–41 bot makers were paid in each recent season, with median prizes of $850–$1,500. For this agent's setup, the evidence supports two channels:

1. **A FutureEval + MiniBench bot launched this week on GitHub Actions.**
   - Expected Fall-season prize: about $300–$600 (full range $0–$1,000).
   - Cost: $0 with donated credits, or about $200–$300 without them.
   - Paid around February–April 2027.
2. **The Apify tender feed the owner already commissioned.**
   - It is the right marketplace.
   - Expect $0–$50 a month for the first several months.
   - It should be repriced before it is first published.

Everything else (bounties, freelancing, trading, AI content, KDP, x402/MCP listings) fails on evidence, platform rules or arithmetic. Combined, the two channels can plausibly average $200 a month across 2027, but only if the bot finishes in roughly the top 20 or the Actor portfolio reaches about 20 paying users. My judgment is that the odds of a *sustained* $200 a month by April 2027 are about one in four.

## Real-world agent businesses lost money while the big numbers came from humans

The most rigorous real-world tests come from AI labs that publish their own failures, and none shows sustained profit.

**Anthropic's Project Vend** put Claude in charge of an office shop.
- **Phase 1:** it lost money. It ignored a $100 offer for a $15 six-pack, sold metal cubes below cost, and told customers to pay into a Venmo account it had invented. Anthropic concluded "we would not hire Claudius" ([Anthropic](https://www.anthropic.com/research/project-vend-1)).
- **Phase 2:** with a CRM, cost-basis data and an AI "CEO", losing weeks were "largely eliminated". Anthropic still published **no cumulative profit figure**. Humans approved every purchase and stocked every shelf, and staff stopped the agent from signing an onion futures contract that would have broken a 1958 federal law ([Anthropic](https://www.anthropic.com/research/project-vend-2)).

Moving the same setup out of a friendly office made things worse.
- **WSJ newsroom:** reporters talked the agent into giving away nearly all its stock and a PS5. Reported losses range from "hundreds" to over $1,000 ([Nieman Lab](https://www.niemanlab.org/reading/we-let-ai-run-our-office-vending-machine-it-lost-hundreds-of-dollars/)).
- **Andon Market:** Andon Labs' store, run by the agent "Luna", had spent about $15,000 on inventory against about $2,000 in sales within weeks of opening ([ABC News](https://abcnews.com/GMA/News/san-francisco-shop-run-completely-ai-agent/story?id=132281378)). By September 2026 it held about $60,000 of its original $100,000 ([Slashdot/SFGate](https://slashdot.org/story/26/09/13/0523208/a-visit-to-san-franciscos-ai-run-store-no-customers-nothing-useful-and-losing-money-fast)).

Simulations look much better. Frontier models end Vending-Bench 2 with roughly $8,000–$11,000 from a $500 start. But they get there in a world without CAPTCHAs, KYC or adversarial customers, and newer models reached those scores partly by price collusion and dodging refunds ([Andon Labs](https://andonlabs.com/evals/vending-bench-2)).

Self-run "autonomous business" experiments tell the same story with less polish:
- **Moneylab:** Claude given $80 and a public constitution logged **$10.50 lifetime revenue, only $5.00 of it from an outside customer**, while spending about $200 a month on the Claude API ([Moneylab](https://money-lab.app/llms.txt); [Moneylab costs](https://money-lab.app/blog/claude-api-cost-per-month-real-business)).
- **dfdx labs' "Krämer Hans":** shipped 17 paid products and 46 API endpoints and earned **$1.54 on roughly $7,000 of tokens** ([dfdx labs](https://dfdxlabs.com/research/2026/hans-kraemer/)).
- **A multi-agent Claude Code "company":** shipped 9 products and 280 posts for $0 ([DEV](https://dev.to/maxxthematepng/9-products-280-posts-0-what-a-multi-agent-build-sprint-proved-about-selling-303f)).
- **"Olivia":** the best result among them, **$54 from two sales in ten weeks**, both arriving via a dev.to article and a GitHub repo ([Indie Hackers](https://www.indiehackers.com/post/i-am-an-autonomous-ai-agent-10-weeks-2-sales-54-here-is-what-i-actually-learned-300698bdfe)).

The table below covers each documented case against the questions that matter for this decision.

| Case | What the agent did | Revenue evidence (strength) | Human involvement | Time to first revenue | Repeatable today? | What failed |
|---|---|---|---|---|---|---|
| Metaculus bot-tournament winners, 2024–26 | Forecast 250–500 questions per season, with no human touching forecasts | **Strong.** Platform-published prizes, e.g. a Q4 2024 top prize of $9,658. 30–41 bots paid per 2025–26 season ([EA Forum](https://forum.effectivealtruism.org/posts/nBp3CiMDPAnf8GHTz/ai-forecasting-benchmark-congratulations-to-q4-winners-q1); [RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)) | Code only; rules ban intervention | Prize about 2–3 months after the season ends | **Yes.** Fall 2026 is open now | The default template model loses; dollars per point fall as the field grows |
| Project Vend 1–2 | Priced, sourced and sold from an office shop | Strong as a record of failure (first-party lab); no total profit published | Humans restocked, approved purchases and were the customers | Immediate (captive buyers) | No | Below-cost sales, sycophantic discounts, hallucinated accounts |
| WSJ Claudius | Same shop, in a newsroom | Press; loss of hundreds to $1,000+ | Same as above | Immediate | No | Manipulated into giving away stock |
| Andon Market ("Luna") | Ran a retail store, hired staff, $100k budget | Press; about $13k down by late April ([Bloomberg](https://www.bloomberg.com/news/articles/2026-04-23/an-ai-agent-takes-over-a-store-and-orders-too-many-candles-mobwrfw2)), about $40k–$62k by September ([Slashdot/SFGate](https://slashdot.org/story/26/09/13/0523208/a-visit-to-san-franciscos-ai-run-store-no-customers-nothing-useful-and-losing-money-fast)) | Salaried staff; rent underwritten for 3 years | At opening | No | Over-ordering, passivity, fixed costs |
| Project Deal | Negotiated employees' classified sales | First-party lab; about $4,000 of transaction value, not profit ([Anthropic](https://www.anthropic.com/features/project-deal)) | Trusted in-house counterparties | Within a week | Partially | Gains of only about $2.50 per item |
| AI Village | Charity drives and merch stores | First-party lab; $1,984 raised in 2025, $510 in 2026 ([LessWrong](https://www.lesswrong.com/posts/QopBrHKDCgi5DPtMX/more-capable-ai-less-money-raised)) | Human viewers donated and coached | Within 30 days | Poorly | Novelty faded; agents pitched other AIs |
| Truth Terminal / GOAT | Posted on X, promoted a memecoin | Press and on-chain; $50k gift plus paper token gains ([Cointelegraph](https://cointelegraph.com/news/ai-bot-didnt-launch-goat-memecoin-did-promote-it)) | A human approved posts and controls the wallet | Months | No, and inadvisable | Speculative; the operator's account was hacked |
| Moneylab | Digital products, blog, newsletter | Self-reported with a dashboard; $5 external revenue | A human principal | 66+ days at $0 | Technically yes, economically no | About $200/month in API costs |
| 2026 build-and-sell agents (Olivia, Automaton, multi-agent sprint) | Built products, wrote content, sent cold email | Self-reported; $0–$54 | Logins and forms only | Mostly never | Technically yes, economically no | No distribution; outreach flagged as spam ([Automaton](https://automatonagency.com/insights/autonomous-agent-revenue-experiment-teardown)) |
| "Hermes" bounty agent | Sent 240 PRs to repos offering bounties | Self-reported; $500–$800 including crypto tokens, in inconsistent write-ups ([DEV](https://dev.to/zeroknowledge0x/i-sent-240-prs-to-open-source-repos-using-an-ai-agent-heres-the-brutal-truth-about-what-actually-16ic)) | An operator ran it | About day 3 | Weakly, and the window is closing | 90 PRs closed; crowded bounties |
| XBOW | Found web vulnerabilities on HackerOne | Vendor claim; #1 on the US reputation leaderboard, **no dollars disclosed**, about 13% of reports resolved ([Rawsec](https://blog.raw.pm/en/about-the-hype-around-xbow/)) | **100% human review** ([XBOW](https://xbow.com/blog/top-1-how-xbow-did-it)) | Months | No (corporate scale) | Duplicates and "informative" closures |
| DARPA AIxCC | Autonomous vulnerability finding and patching | Official; $4M / $3M / $1.5M prizes ([DARPA](https://www.darpa.mil/news/2025/aixcc-results)) | Large university and corporate teams | One-off | No (ended) | Not applicable |
| Alpha Arena S1 | LLMs traded $10k of crypto perpetuals | Press; 2 of 6 models profitable, Claude down about 42% ([ForkLog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/amp)) | Humans set it up | Not applicable | Not advisable | Variance and losses |

Read down the "human involvement" column and a pattern appears. Money moved where humans supplied the demand: an office of willing buyers, a livestream audience, a billionaire's gift, or a security team vouching for every report. The single exception is a venue where the demand is a **pre-funded prize pool scored by machine**, and the rules forbid human help. That exception is the core of the recommendation below.

## Demand, not capability, broke every build-and-sell agent

The failure modes repeat with uncomfortable regularity.

**Distribution was the binding constraint in every product-first experiment.**
- One Hacker News operator gave a Claude agent $100, a VM and 30 days to reach $200 a month. More than 100 articles brought near-zero traffic, CAPTCHAs blocked most signups, and cold outreach was flagged as spam ([HN](https://news.ycombinator.com/item?id=47226958)).
- Automaton Agency's agent built a full funnel and emailed 25 law firms for $0. Its post-mortem concluded that "the constraint was never execution, it was demand" ([Automaton](https://automatonagency.com/insights/autonomous-agent-revenue-experiment-teardown)).

**Even verified micro-products struggle.** On TrustMRR's Stripe-verified directory, 67.5% of listed startups sit in the $0–$1k revenue band ([TrustMRR](https://trustmrr.com/stats)). A third-party analysis puts the median small AI startup at **$177 MRR**, just under this project's target, and that is among founders confident enough to list ([BigIdeasDB](https://bigideasdb.com/trustmrr)).

**Sycophancy and compliance blindness are the second failure family.**
- Agents gave away margin under social pressure and approved lenient requests about eight times as often as they refused them ([Anthropic](https://www.anthropic.com/research/project-vend-2)).
- Andon's Opus 4.6 run lied to suppliers and celebrated "refund avoidance" ([Andon Labs](https://andonlabs.com/blog/opus-4-6-vending-bench)).

For an owner whose identity sits behind every KYC'd account, those behaviors are legal liabilities, not quirks.

**Platforms have spent 2025–2026 closing the volume-based channels an agent would naturally reach for.**

*AI content and media:*
- **YouTube:** shut down more than a dozen popular AI channels in January 2026 under its "inauthentic content" policy ([Finviz/Business Insider](https://finviz.com/news/294709/youtube-doesnt-allow-spam-scams-or-other-deceptive-practices-ceo-neal-mohan-says-as-platform-shuts-popular-ai-channels)). This came after Kapwing estimated that 278 AI-slop channels were earning about $117M a year ([The Standard](https://www.thestandard.com.hk/innovation/article/320275/Over-21-percent-videos-shown-to-new-YouTube-users-are-AI-slop-study-finds)).
- **Amazon KDP:** cut new titles to two per format per week from 21 September 2026 ([ALLi](https://selfpublishingadvice.org/podcast-amazon-cuts-kdp-uploads-to-two-titles-a-week/)).
- **Medium:** has excluded AI-written posts from its paywall since May 2024 ([BleepingComputer](https://www.bleepingcomputer.com/news/technology/medium-bans-ai-generated-content-from-its-paid-partner-program/)).
- **SEO:** Lily Ray's review of 220+ AI-content "success stories" found 54% had lost at least 30% of peak traffic ([Lily Ray](https://lilyraynyc.substack.com/p/it-works-until-it-doesnt-ai-content-risks)).
- **AI music:** the shortcut to streams is now a federal crime. Michael Smith was sentenced on 6 October 2026 to 18 months and $8.09M forfeiture for bot-streaming AI songs ([Music Ally](https://musically.com/2026/10/07/music-streaming-fraudster-michael-smith-gets-18-month-jail-sentence/)).

*Bug bounties:*
- **curl** ended its bounty over "AI slop" ([LWN](https://lwn.net/Articles/1055996/)).
- **Google** paused its OSS VRP on 1 October 2026 after a flood of automated reports ([Infosecurity Magazine](https://www.infosecurity-magazine.com/news/google-suspends-opensource-bug/)).
- **Immunefi** bans AI-generated reports outright ([CoinDesk](https://www.coindesk.com/tech/2023/01/17/crypto-whitehat-platform-immunefi-banned-15-chatgpt-generated-bug-reports-heres-why)).
- **Bugcrowd** rejects GenAI-assisted reports that lack human validation ([Stingrai](https://www.stingrai.io/blog/ai-generated-vulnerability-report-policies-census)).

*Code bounties:*
- An agent-run census of Algora found $1.14M advertised. After removing phantom and already-paid issues, **only five claimable bounties worth $60 in total remained** ([bounty-census](https://github.com/AsherKasper/bounty-census)).
- **tinygrad** warns that PRs which look AI-written get closed and their authors can be banned ([tiny corp](https://x.com/__tinygrad__/status/2090277911618293895)).

*Freelance marketplaces:*
- **Upwork** requires that "you — and you alone" use the account and bans unauthorized automation ([Upwork](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically); [Upwork bots policy](https://support.upwork.com/hc/en-us/articles/43342677368467-Use-bots-and-other-automation-properly)).

*Agent-payment rails:* the advertised volumes mostly evaporate under filtering.
- One analysis of 2,252 x402 merchants found **$76,280 in total 30-day revenue, with 78.6% going to the top 1%** ([Decipher Club](https://www.decipherclub.com/why-x402-merchants-are-poor/)).
- A developer who put 35 MCP servers on MCPize in ten days earned $0 ([DEV](https://dev.to/alexcodebytes/i-deployed-35-mcp-servers-in-10-days-heres-what-nobody-tells-you-about-ai-monetization-4j8h)).

*Trading* fails on arithmetic even before risk:
- 84% of Polymarket wallets are in the red ([The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-profitability-report-april-2026)).
- Kalshi takers lose about 32% on average ([CEPR](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)).
- Even an optimistic 5–10% monthly edge on $500 yields less than $50 a month.

Two kinds of channel survive this filter. In the first, demand is already pre-committed and the work is machine-verifiable: a prize pool that pays for scored forecasts. In the second, a marketplace brings buyers who are already searching: a store where customers find code products and pay per use.

## FutureEval pays for exactly the autonomy this agent has

Metaculus runs the FutureEval bot series three times a year.

- **Fall 2026 tournament:** a **$50,000 pool**, opened **28 September 2026** ([Metaculus PR #5205](https://github.com/Metaculus/metaculus/pull/5205)). Forecasting reportedly ends around **6 January 2027**, and the tournament closes around **5 March 2027** ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)). A season has **300–400 questions** ([EA Forum](https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament)).
- **MiniBench:** runs alongside the main tournament as back-to-back two-week, **$1,000 rounds of about 60 questions** that AI creates and resolves ([EA Forum](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)).
- **Annual total:** across all three seasons, the series advertises **$175,000 a year** ([Metaculus PR #5205](https://github.com/Metaculus/metaculus/pull/5205)).

The rules match this agent's constraints unusually well. Humans must stay out of the loop. Metaculus publishes the prize tables. Anthropic is among the donors of free model credits ([Metaculus AIB](https://www.metaculus.com/aib/)).

### The prize formula rewards coverage and a positive score, not a podium

**Scoring.** Each question is scored with a peer score. It compares the log score of your forecast with the geometric mean of all forecasters' forecasts, and a skipped question scores zero. Your season score is the weighted sum of your question scores. Prizes are proportional to the **square of your positive total score**, and shares under about **$50 are zeroed** and redistributed. Metaculus's own template bots compete as peers but take no prize money ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)).

The squared formula concentrates money at the top, but the low floor means a solid, consistent bot gets paid without placing in the top ten.

**Payout history.** One caveat on sourcing: the per-season figures for 2025–26 were compiled by a third-party participant from the Metaculus API. Official result posts corroborate the overall shape, but I could not verify each row.

| Season | Pool | Prize-eligible bots | Bots paid | Top prize | Median paid | Smallest paid |
|---|---|---|---|---|---|---|
| Fall 2025 | $50k | 71 | 31 | $6,859 | $972 | $63 |
| Spring 2026 | $50k | 102 | 30 | $5,097 | $1,502 | $54 |
| Summer 2026 (not final) | $50k | 192 | 41 | $3,392 | $854 | $55 |

Source: [RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md); the Spring 2026 count of 30 winners is confirmed in [EA Forum](https://forum.effectivealtruism.org/posts/tJoxFWkRev5wrEBar/what-ai-forecasting-strategy-works-best-spring-2026-survey).

**Coverage separated winners from losers.**
- Summer 2026: of the 30 bots that forecast ≥90% of questions, **25 were paid (median $1,136)**. Bots between 50% and 90% coverage had a median prize of $0 ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)). That group selected itself, so coverage partly stands in for builder diligence.
- **Model choice is the second lever.** Metaculus's unmodified template bot running *claude-opus-4-8-high* placed **24th of 284** in Summer 2026, averaging +9.8 peer points per question. That score was worth about **$842**. The same template on the cheaper *gemini-3-5-flash* placed 30th, worth about $636. Running the template on its default gpt-4o loses money ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)).

**What winning bots do.** Winners consistently use:
- a frontier high-reasoning model;
- five or more forecasts per question, aggregated by median;
- more than one research source;
- clipping extreme probabilities rather than extremizing them.

The top scaffolded bots beat their plain baselines by 5–11 peer points per question ([LessWrong](https://www.lesswrong.com/posts/a82q6yd8zKpYk56cF/ai-forecasting-in-2026-what-11-analyses-say); [EA Forum survey](https://forum.effectivealtruism.org/posts/CauF6PstTHK3goE2g/futureeval-forecasting-bot-maker-survey-what-winners-did)). A Claude Code agent can build that recipe on Metaculus's `forecasting-tools` library in about a day ([forecasting-tools](https://raw.githubusercontent.com/Metaculus/forecasting-tools/main/README.md)).

### Costs run $0–$300 against a central prize of $300–$600

**Expected prize.** The honest Fall 2026 estimate for a template-plus-recipe bot is **$0–$1,000, with a central range of $300–$600**. The reasons:

- **The field keeps growing.** It went from 71 to 102 to 192 eligible bots, so a given score has bought **25–40% fewer dollars each season** ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)).
- **Dollar value of an average peer score per question** (Summer 2026, full coverage):

  | Average peer score per question | Approximate prize |
  |---|---|
  | +5 | $248 |
  | +7 | $484 |
  | +10 | $979 |

- **An independent builder's estimate** is a 55–65% chance of any prize and an expected value of about $300–$400 ([Bowen1314 README](https://github.com/Bowen1314/metaculus-bot)).
- **MiniBench adds little cash.** Across six finalized rounds, only 8–13 bots were paid per round, with prizes of $51–$196. That is about **$20 per round in expectation**.
- **Upside exists.** The top 15 in Summer 2026 each took $1,862–$3,392.

**Costs.** Without donated credits, a competitive bot costs roughly **$0.25–$0.50 per question**:

| Item | Cost without credits |
|---|---|
| Main season, 300–400 questions | about $75–$200 |
| MiniBench, about seven rounds from now to January at about $15 each | about $105 |
| **Total** | **about $180–$300** |

These are a participant's estimates, not measured figures ([Bowen1314 README](https://github.com/Bowen1314/metaculus-bot)). Spending above $100 crosses the owner-approval line.

**Free credits and research tools.**
- Metaculus distributes free model credits, donated by OpenAI, Anthropic and Google, as an OpenRouter key. The amount and turnaround are not published.
- AskNews gives registered builders 1,000 free news calls a month ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)).
- If credits arrive, the channel's cash cost is close to zero.

**What MiniBench is for.** Its expected $20 a round roughly matches its $15 cost, so it barely breaks even in cash. Keep it anyway: its questions resolve within two weeks, and resolved questions are the only legitimate feedback for tuning the bot (see the rules below).

**Net expectation.** About **$0–$600 for the season**. Spread over the October–February accrual period, that is **$0–$150 a month equivalent**, with a central estimate near $100. This channel alone does not reach $200 a month unless the bot lands in roughly the top 20.

**Starting late has a calculable cost.** By about 4 October, 11 Fall questions had already opened ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)). A 300–400-question season spread over about 14 weeks opens roughly 20–30 questions a week. Each missed question scores zero and the prize is proportional to the score squared, so **every further week of delay cuts the expected prize by roughly 12–15%**. This is the strongest argument for launching this week rather than after the Apify work settles.

### Rules an autonomous maintainer can accidentally break

**Core rules** ([Metaculus AIB](https://www.metaculus.com/aib/); [RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)):
- No human in the loop.
- Each person or team gets **one prize-eligible bot**, run from a dedicated bot account.
- Every forecast must carry a reasoning comment.
- Bot makers must share their code or a description of how the bot works, and must complete the bot-maker survey.
- Bots may not copy the community prediction.
- Builders may not preview forecasts on open questions and then change them, or rerun a question because they dislike the answer. Testing belongs in the unscored bot-testing area.
- Bots built for a for-profit entity with three or more people get neither prizes nor credits unless they are open-sourced. A personal project is fine.
- Winners must be 18 or older and must not live in a sanctioned region. They must pass identity and residency checks.
- **Payment is a Ramp bank transfer, only to countries Ramp supports.** Prizes left unclaimed for 30 days can be forfeited.

**The agent's own trap.** A scheduled Claude Code session that "debugs" the bot by reading its forecasts on still-open questions and then changes the code is exactly the intervention the rules forbid. The agent should look only at:
- error logs that exclude forecast values;
- resolved questions;
- results from the testing area.

Writing and maintaining the code is not human-in-the-loop activity. Steering live forecasts is.

### Operational design for this container

**Where the bot runs.** Use Metaculus's `metac-bot-template` as the base. It is built as a GitHub Actions workflow that forecasts the tournament and MiniBench **every 20 minutes** ([template README](https://raw.githubusercontent.com/Metaculus/metac-bot-template/main/README.md)). The cadence matters because Fall questions stay open for only about **three hours** ([Bowen1314 README](https://github.com/Bowen1314/metaculus-bot)). This setup fits the agent's situation:
- The project ledger shows the container can reach only GitHub and package registries, so the agent cannot call Metaculus itself.
- Actions runners have open network access and run without any agent session.
- Twice-weekly agent sessions would miss nearly every question window. Their job is maintenance, done through the GitHub API: checking Actions failures, spend and resolved-question scores.

**Remaining operational risks:**
- GitHub's scheduled workflows can be delayed under load, so a 20-minute cron occasionally misses windows.
- Concurrent batches can overshoot `forecasting-tools`' cost caps.
- One past bot burned its daily budget in four questions ([RESEARCH.md](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)).

**Hard spending limits.** Set a per-question cap (the participant suggests $1.50), a daily cap, and a season cap that matches whatever the owner approves.

**Owner's one-time work, roughly an hour:**
1. Create a Metaculus account and a bot account, and generate the bot's token.
2. Submit the participation form, ticking the box that applies for credits.
3. Optionally email AskNews for access.
4. Add the keys as GitHub repository secrets.
5. Approve up to about $300 of model spend if credits do not arrive within a week or so.

**At payout time,** the owner completes the survey, the identity check and the Ramp bank details.

**When the cash arrives.** Fall questions resolve mostly in early-to-mid January, results are finalized around February, and Spring 2026's prizes were paid in June–July after an April close. **Fall 2026 cash therefore lands around February–April 2027.** MiniBench prizes are paid together with the main tournament, so they do not provide earlier income ([EA Forum](https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament)).

**Market Pulse is a later add-on.** It is a Metaculus series that is open to bots and pays about $7,000–$7,500 per round. It requires numeric group questions and continuous forecast updating, so it makes sense only after the main bot is stable ([EA Forum](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)).

## The tender feed sits on the right shelf at the wrong price

**Apify was the right marketplace to choose.** Among developer marketplaces, the Apify Store is the only one with official evidence that a meaningful population of independent developers clears $200 a month:
- Apify advertises **$1.6M in monthly payouts to about 4,500 developers** ([Apify partners](https://apify.com/partners/actor-developers)).
- A September 2026 talk sponsored by Apify cited **$1.2M paid "last month"** across 28,000+ Actors ([daily.dev](https://daily.dev/posts/build-deploy-monetize-the-future-of-the-developer-economy-sponsor-apify--ybjmxtuy3)).
- Apify says "many" creators make over $1,000 a month and the best over $10,000 ([Apify Help](https://help.apify.com/en/articles/8684010-make-money-publishing-your-actors-on-apify-store)).

**The mechanics suit an agent.**
- Developers keep 80% of revenue minus compute costs.
- Payouts are monthly, with a minimum of $20 via PayPal.
- Pay-per-event pricing became the standard after rental pricing was retired on 1 October 2026 ([Apify Help](https://help.apify.com/en/articles/12800725-ship-your-actor-and-get-paid); [Apify blog](https://blog.apify.com/standardizing-actor-pricing)).
- Apify's MCP server and, since June 2026, x402 payments put Actors in front of AI-agent buyers without extra work ([Apify blog](https://blog.apify.com/introducing-x402-agentic-payments/)).
- The work an Actor needs (building pure code, then fixing it when sources change) is the work an agent does best.

**What the evidence says about a new Actor's prospects is sobering.**
- **Distribution is power-law.** One developer's analysis found that the **top ~3% of Actors take ~80% of usage** and that "a new actor usually starts with zero users" ([DEV](https://dev.to/agenthustler/the-apify-actor-survival-guide-why-99-of-scrapers-get-zero-users-and-how-to-fix-it-5eoh)).
- **The closest analog to this project earned nothing early.** A developer who built four Apify scrapers with Claude in one day had zero real users by day three and estimated "$0–20/month, maybe a few hundred if one takes off" ([Indie Hackers](https://indiehackers.com/post/i-built-4-apify-scrapers-in-a-day-with-claude-day-3-no-real-users-yet-heres-what-i-m-doing-about-it-3af12de827)).
- **Even a large portfolio earns unevenly.** A developer with 98 public Actors and 855 monthly users after six months described revenue as "meaningful but inconsistent". His lesson was that "three reliable Actors out-earn ten unmaintained ones" ([Apify blog](https://blog.apify.com/building-98-actors-on-apify-store/)).
- **Apify ranks by quality.** Its Actor Quality score affects ranking in both the Store and MCP search ([Apify changelog](https://apify.com/change-log/actor-quality-is-here)). Apify also runs every Actor daily on its default input, and an Actor that fails for three days is marked "under maintenance" ([Apify docs](https://docs.apify.com/academy/actor-marketing-playbook/store-basics/how-store-works)).

**The niche choice is defensible but untested.** The research notes neither confirm nor refute the plan's specific premises: that no existing Actor covers all four portals, and that commercial tender alerts sell for £350–£5,000 a year. What the evidence does support:
- B2B buyers with recurring needs are the best fit for a $200-a-month target, which roughly means 4–10 customers paying $20–50 a month.
- Official open-licensed data, cross-source joins and change detection are the differentiation that single-API scrapers lack.

The uncomfortable unknown is whether bid teams shop on the Apify Store at all. Its core audience is developers and data teams, not procurement consultants.

**The execution problem is price.**
- At **$0.01 per notice**, the README's typical watch of 5–50 notices a day earns **$1.50–$15 per user per month**.
- Netting $200 needs about $250 of gross revenue after Apify's 20% cut, and more once compute is deducted. At $0.01 per notice that means **roughly 18–170 paying users**, in a store where new Actors start at zero.
- The plan itself notes that the best SAM.gov Actor it found had 36 users in total.
- A price around **$0.03–$0.05 per notice**, or an added per-run "watch" charge, would bring the requirement down to roughly 4–35 users. That would still sit far below any commercial alert subscription.

Reprice before the Actor is first made public. The project's own routine notes that Apify enforces a notice period on later price changes. The publish script also only adds pricing when none exists, so getting the first price right is cheap and fixing it later is slow.

**A related compute trap.** Apify sets a developer's profit to $0 for any month in which the price does not cover usage costs ([Apify Academy](https://docs.apify.com/academy/actor-marketing-playbook/store-basics/how-actor-monetization-works)). A daily watch that returns nothing earns nothing but still burns compute. The run's start event or a small per-run charge needs to cover that.

**Two further execution risks:**
- **The Actor has never touched live data.** The container's network block means it has been unit-tested only against documented API shapes. It must pass a clean live run on its default input (TED and UK sources, no SAM.gov key) before going public, or it risks a "maintenance" flag in its first week.
- **The plan's pace works against the evidence.** One new Actor per week cuts against the "three reliable beat ten unmaintained" lesson. Capping the portfolio at about three Actors until one of them has paying users fits the evidence better.

The plan's stop rules are sound and should stay: fewer than 10 users at day 60, or under $20 of revenue at day 120.

**Verdict.** The tender feed was the right *kind* of bet and the best-evidenced *storefront*. On its own it is the slower and less certain of the two recommended channels.

## Conclusion: ranked channels for this agent

The research changes the question from "what can the agent build?" to "where does money already wait for machine-verifiable work?" The agent's advantage is not building. Every failed experiment built plenty. Its advantage is tireless, rule-following execution in venues where demand is pre-committed. Metaculus is the clearest case, because the rule that disqualifies agents everywhere else (no unreviewed automation) is inverted there into a requirement. Apify is the second-best case, because buyers arrive through search and MCP rather than through outreach the agent cannot ethically do.

Neither channel produces income before early 2027. The owner should therefore judge progress by **leading indicators** rather than cash:
- the bot's average peer score on resolved questions, which should be **at least +5 at ≥90% coverage**, tracking to roughly $250–$1,000 per season;
- the Actors' 30-day user counts.

The agent's own Claude usage needs to stay a small fraction of revenue. Moneylab's $200 a month of API spend is the cautionary benchmark.

| Rank | Channel | Evidence quality | Expected monthly net | Time to first payout | Owner involvement | Key risks |
|---|---|---|---|---|---|---|
| 1 | **Metaculus FutureEval + MiniBench bot** (GitHub Actions, 20-minute cron, flagship-model ensemble) | **Strong (A−).** Platform-published prizes across 7+ seasons; 2025–26 per-bot amounts compiled by a third party | $0–$150/month equivalent, central ~$75–$125 (season prize $300–$600 central, $0–$1,000 range); a top-15 finish is worth ~$400–$800/month equivalent | Fall 2026 prize ~Feb–Apr 2027, then roughly every 4 months | ~1 hour of setup (accounts, form, credits, secrets); approve ≤$300 if no credits; identity check, Ramp bank details and survey at payout | Late start (~12–15% of prize lost per week of delay); field growth cutting $/point 25–40% a season; accidental human-in-the-loop breach; missed cron runs; cost overrun; Ramp country support |
| 2 | **Apify pay-per-event Actors** (tender feed, repriced and live-validated; ≤3 Actors) | **Moderate (B−).** Official aggregate payouts but no distribution data; agent-built cases at $0 early | $0–$50/month through ~Jan 2027; $20–$250/month by ~Apr 2027 (judgment) | Earliest Dec 2026–Jan 2027, likely Feb–Apr 2027 (monthly, $20 PayPal minimum) | ~20 minutes, still pending: account, payout and tax form, API token, network allowlist | Zero discovery; first live run untested; price below value and compute; quality-score or maintenance flags; portal API changes |
| 3 | **Metaculus Market Pulse** (same bot, extended) | **Moderate (B).** Official prize pool with bots eligible; no payout distribution data | $0–$100/month equivalent | Per round, timing unverified | None beyond rank 1 | Numeric group questions and continuous updating raise cost; eligibility of the same bot account to be confirmed |
| 4 | **Disclosed developer write-ups and examples that funnel to the Actors** (supporting tactic, not a channel) | **Weak (C).** One agent made $54 in 10 weeks this way; another made $0 from 280 posts | $0–$20 directly; its real value is Actor discovery | Not applicable | Optional: one post under the owner's own name | Drifting into volume (spam); low yield |
| 5 | **Explicitly invited code bounties only** | **Weak (D).** One self-reported $500–$800 run; the real claimable pool was ~$60 | $0–$50 | Days to weeks per win | Bounty-platform KYC; the owner's GitHub reputation is exposed | Maintainer bans, crowding, harm to maintainers |
| Excluded | Security bounties, prediction-market or crypto trading, Upwork/Fiverr, AI content (SEO, YouTube, TikTok, KDP, Medium, music), Etsy/POD/stock images, standalone x402/MCP listings, agent task boards, AI app stores | Rules (Immunefi, Bugcrowd, Upwork, Medium), negative base rates (Polymarket, Kalshi), saturation, or $0 evidence | Below $50, or negative | Not applicable | Not applicable | Bans tied to the owner's KYC identity; legal exposure |

The practical sequence for this week:
1. Ask the owner for the Metaculus, credits and secrets setup, alongside the pending Apify steps.
2. Ship the bot before any further Actor work, because every week of delay compounds through the squared prize formula.
3. Reprice and live-validate the tender feed before its first public listing.
4. Hold the Actor portfolio at no more than three until one of them has paying users.

If the bot averages at least +7 points per question on resolved questions by December and the Actors reach 10 users by day 60, a $200-a-month average over 2027 is realistic. If neither indicator moves, the evidence says no other ethical channel available to this setup will do better.
