# Metaculus AI Forecasting Bot Tournaments (FutureEval / AI Benchmark series, MiniBench), as of 2026-10-07

**Source quality note (read first).** metaculus.com, lesswrong.com, forum.effectivealtruism.org, greaterwrong.com and forum.nunosempere.com were all **blocked for WebFetch** in this environment. Pages that worked: github.com and raw.githubusercontent.com. That gives three tiers of evidence:
- **(A) Official, read in full:** the Metaculus GitHub repos (metac-bot-template README, forecasting-tools README) and Metaculus PR #5205 on github.com/Metaculus/metaculus.
- **(B) Official, but only as search snippets:** Metaculus tournament pages, notebooks, and EA Forum/LessWrong posts. I only saw these through WebSearch summaries, which can be lossy.
- **(C) Secondhand:** a third-party participant's repo (github.com/Bowen1314/metaculus-bot, README and RESEARCH.md, written about 2026-10-04). Its RESEARCH.md has the most detailed payout history I found. The author says it was compiled from the Metaculus API and the official rules/notebooks. I could not verify it against Metaculus pages, so treat its numbers as plausible but unverified.

---

## 1. Current and next tournaments: names, dates, pools, question counts, joining, prize formula

### Takeaway
The live tournament is the **Fall 2026 FutureEval Bot Tournament**. It has a $50,000 pool, started 2026-09-28, and questions open until about 2027-01-06. It runs in parallel with **MiniBench**, a back-to-back series of two-week, $1,000 rounds of about 60 questions each. Metaculus counts the season as $58K including MiniBench. You can join at any time, but questions you miss score 0. Prizes are paid in proportion to (positive total peer score)², and any share under about $50 is zeroed. So you do not need a top-10 finish to win money, but you do need a clearly positive peer score and high question coverage.

### Cited Findings
- **Fall 2026 dates and pool.** The Fall 2026 FutureEval Bot Tournament is live with a **$50,000** pool on its tournament page. The FutureEval carousel card shows **$58,000**, and the difference is the MiniBench amount. The year-2 total across three seasons is **$175K**. Start date: **2026-09-28**. Summer 2026 closed **2026-09-06**. — [Metaculus PR #5205 (official repo, fetched)](https://github.com/Metaculus/metaculus/pull/5205)
- **Fall 2026 timeline (secondhand).** Slug `fall-futureeval-2026`. Forecasting ends **2027-01-06**; the tournament closes **2027-03-05**. When the author checked (~2026-10-04) it had 11 questions and 316 forecasters. — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Question volume and windows.** Metaculus describes the series as "three times a year, aligned with the Metaculus Cup timeframe," with a $50k pool and **300–500 questions** per season (Summer 2026 announcement). The Fall 2026 announcement says **300–400 questions** per season. — [Summer 2026 announcement (B, snippet)](https://www.lesswrong.com/posts/E7wxQnBvYxgB3rTTk/announcing-metaculus-summer-2026-futureeval-bot-tournament); [Fall 2026 announcement (B, snippet)](https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament)
- **Joining.** Joining is continuous. "Competitors can join any time during this window and will start at the middle of the leaderboard with 0 points." Questions stop opening a few weeks before the season ends. — [Summer 2026 announcement (B, snippet)](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)
- **Season history.** Summer 2026 ran **2026-05-18 to 2026-09-06** with a $50,000 pool. — [Summer 2026 tournament page (B, snippet)](https://www.metaculus.com/tournament/summer-futureeval-2026/). Spring 2026 ran **2026-01-07 to 2026-04-15**. — [Spring 2026 results post (B, snippet)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)
- **Question windows are short.** Fall 2026 questions are open for about **3 hours**, so the author runs the bot every 15 minutes. — [Bowen1314 README (C)](https://github.com/Bowen1314/metaculus-bot). Metaculus's own template schedules the tournament+MiniBench workflow **every 20 minutes**. — [metac-bot-template README (A)](https://raw.githubusercontent.com/Metaculus/metac-bot-template/main/README.md)
- **MiniBench.** A series of "back-to-back two-week-long $1k tournaments of ~60 questions each." Question creation and resolution are fully automated using AI. It is meant to give quick feedback and lower the barrier to entry. The first Summer MiniBench started 2026-05-18, and MiniBench continues across season transitions. — [Summer 2026 announcement (B, snippet)](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament); [MiniBench page (B, snippet)](https://www.metaculus.com/aib/minibench/). The current round started **2026-10-05**. — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Scoring rule (secondhand summary of official rules).**
  - Each question gets a spot **peer score**: `100 * n/(n-1) * ln(p_you / geometric_mean_of_all_forecasters' p)`, evaluated on the outcome that occurred.
  - Numeric and discrete question scores are halved.
  - Skipped questions score 0.
  - Tournament score = Σ(question score × question weight).
  - **Take = (positive score)²**, and prize = take / Σ takes × pool.
  - **Minimum prize $50**: smaller shares are zeroed and the money redistributed.
  - **Metaculus's own template bots count as peers but are excluded from prizes.**
  - — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md); the README restates "proportional to the square of the total peer score… anything under $50 is not paid" — [Bowen1314 README (C)](https://github.com/Bowen1314/metaculus-bot)
- **Payout timing.** Most Fall-season questions resolve in early-to-mid January, results are finalized around February, and prizes are paid after all questions resolve and verification is done. Spring 2026 prizes were scheduled for June/July 2026. — [WebSearch summary of Metaculus announcements (B)](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)

### Inferences
- The (score)² formula concentrates money at the top, but the $50 floor is low. In recent seasons about 30–41 bots were paid. A newcomer with a moderately positive peer score and near-full coverage can expect a few hundred dollars without being top-10 (see Section 2).
- Fall 2026 started 9 days ago. Joining now loses only the first ~1–2 weeks of questions, out of a season that runs to January. Every week of delay costs coverage, and coverage is the strongest predictor of being paid.
- Fall 2026 money arrives around Feb–Apr 2027, not in October 2026. MiniBench rounds are scored every two weeks, but their prizes are paid together with the season's main prizes, so they do not bring cash forward.

### Gaps
- I could not read the official Fall 2026 rules page (metaculus.com/futureeval/participate/ was blocked). The $50 minimum and the exact squared formula come only from the secondhand summary.
- The exact per-round MiniBench prize formula. It is presumably the same squared rule, but I did not verify this.

---

## 2. Payout history per tournament

### Takeaway
- **Pools:** $30K per quarter in 2024–Q2 2025, then $50K per season from Fall 2025, plus MiniBench.
- **Field size:** grew from about 44–55 bots in 2024 to roughly 190 prize-eligible entries (284 total) in Summer 2026.
- **Money paid:** 30–41 bots were paid per recent season, with median paid prizes of about $850–$1,500.
- **Template bots:** Metaculus's template bot with a current flagship model typically finished rank 16–35, which would have earned **$500–$1,450** (Fall 2025–Summer 2026). The same score buys fewer dollars each season as the field grows.

### Cited Findings
**Q3 2024 ($30K)**
- 55 bots on 255 weighted questions. Pros were significantly better than the top bots (p = 0.036). — [Q3 results post (B, snippet)](https://www.lesswrong.com/posts/LHdNtJCm93pxNHJKb/can-ai-outpredict-humans-results-from-metaculus-s-q3-ai)
- MWG finished 2nd and histerio 3rd. Sources conflict on whether Metaculus's GPT-4o bot placed 3rd or 4th. The 1st-place bot and full prize list were not found. — [Q4 winners post (B, snippet)](https://forum.effectivealtruism.org/posts/nBp3CiMDPAnf8GHTz/ai-forecasting-benchmark-congratulations-to-q4-winners-q1)
- Bot team head-to-head score vs Pros: −11.3. — [Spring 2026 results (B, snippet)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)

**Q4 2024 ($30K)**
- 44 bots on 402 questions.
- Prizes: 1st pgodzinai $9,658; 2nd MWG $4,477; 3rd GreeneiBot2 $3,930; 4th manticAI $3,410; 5th histerio $3,312.
- Pros were better than bots, but not significantly (p = 0.079). Head-to-head score −8.9.
- — [Q4 results post (B, snippet)](https://www.lesswrong.com/posts/P8YwCvHoF2FHQoHjF/metaculus-q4-ai-benchmarking-bots-are-closing-the-gap); [Q4 winners post (B)](https://forum.effectivealtruism.org/posts/nBp3CiMDPAnf8GHTz/ai-forecasting-benchmark-congratulations-to-q4-winners-q1)

**Q1 2025 ($30K)**
- Leaderboard prizes: manticAI $7,685; acm_bot $5,499; GreeneiBot2 $4,065; twsummerbot $3,826; cookics_bot_TEST $2,380; pgodzinai $2,228; CumulativeBot $1,788; SynapseSeer $1,700; jkraybill_bot $712; MWG $117.
- Metaculus in-house bots (e.g. metac-o1) topped the raw scores but received no prize.
- Head-to-head score vs Pros −17.7.
- — [Q1 2025 results page (B, snippet)](https://www.metaculus.com/aib/2025/q1/); [Q1 results post](https://www.lesswrong.com/posts/rDy5z8ZEtMrEGnfBd/q1-ai-benchmark-results-pro-forecasters-crush-bots)

**Q2 2025 ($30K)**
- Metaculus's X post says "96 forecasting bots competed on 300+ questions." The results post says 54 bot-makers and 348 questions. Both counts are probably right: bots vs. makers.
- Prizes: 1st **Panshul42 $7,550**, who open-sourced the bot.
- Secondhand: 2nd $4,563 and 3rd $3,270; 16 other bots split $14,617.
- The top 3 non-Metaculus bot-makers were hobbyists or students.
- Pros beat bots decisively (p = 0.00001; head-to-head score −20.03).
- — [Metaculus on X (B)](https://x.com/metaculus/status/1958239204325879854); [Q2 results post (B, snippet)](https://forum.effectivealtruism.org/posts/F2stjK9wHSy3HPEC9/q2-ai-benchmark-results-pros-maintain-clear-lead); [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)

**Fall 2025, Spring 2026 and Summer 2026 ($50K each).** All rows below are non-Metaculus, prize-eligible entries. Source for the table: [Bowen1314 RESEARCH.md (C, compiled from the Metaculus API)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)

| Season | Eligible bots | Positive score | Paid | Top prize | Median paid | Smallest |
|---|---|---|---|---|---|---|
| Fall 2025 | 71 | 38 | 31 | $6,859 | $972 | $63 |
| Spring 2026 | 102 | 53 | 30 | $5,097 | $1,502 | $54 |
| Summer 2026 (not finalized) | 192 | 92 | 41 | $3,392 | $854 | $55 |

- **Summer 2026 top 15:** paid $1,862–$3,392. — (same source, C)
- **Spring 2026 cross-checks:** the bot-maker survey says 37 of 133 owners won prizes, versus 30 paid entries in the API. The source does not explain the gap. — (C)
- **Fall 2025 cross-check:** 39 developers answered the bot-maker survey, 29 of them prize winners. This is consistent with about 31 paid. — [Bot-maker survey (B, snippet)](https://forum.effectivealtruism.org/posts/CauF6PstTHK3goE2g/futureeval-forecasting-bot-maker-survey-what-winners-did)

**Payout by question coverage** (C):

| Season | ≥90% coverage: n / paid / median / mean | 50–90% coverage: n / paid / median / mean | <50% coverage: n / paid |
|---|---|---|---|
| Fall 2025 | 17 / 15 / $1,526 / $2,098 | 31 / 15 / $0 / $458 | 23 / 1 |
| Spring 2026 | 16 / 12 / $2,353 / $2,046 | 33 / 14 / $0 / $481 | 53 / 4 |
| Summer 2026 | 30 / 25 / $1,136 / $1,437 | 29 / 7 / $0 / $161 | 133 / 9 |

The source warns that the ≥90% group is self-selected.

**Count of bots paid at least $200.** Not directly reported. With 31/30/41 paid, median paid about $850–$1,500, and a smallest prize of about $55, roughly **25–35 bots per season** were likely paid ≥$200. This is my inference from the medians, not a reported figure.

**Dollar value of an average per-question peer score at full coverage** (Fall 25 / Spring 26 / Summer 26) (C):

| Average peer score per question | Fall 2025 | Spring 2026 | Summer 2026 |
|---|---|---|---|
| 5 | $431 | $328 | $248 |
| 7 | $837 | $639 | $484 |
| 10 | $1,679 | $1,287 | $979 |

**Template bots vs the field.** Source: [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)

| Season | Model | Rank | Average peer score per question | Would-be prize |
|---|---|---|---|---|
| Fall 2025 | gpt-5 | 16/136 | 9.9 | $1,450 |
| Fall 2025 | claude-4-1-opus-high | 26 | 6.3 | $602 |
| Fall 2025 | gemini-2-5-pro | 37 | 4.3 | $286 |
| Spring 2026 | gpt-5-1-high | 18/180 | 10.0 | $1,269 |
| Spring 2026 | claude-4-5-sonnet-high | 23 | 7.3 | $700 |
| Spring 2026 | gpt-5-1 | 47 | 3.0 | $121 |
| Summer 2026 | **claude-opus-4-8-high** | 24/284 | 9.8 | $842 |
| Summer 2026 | gemini-3-5-flash | 30 | 8.3 | $636 |
| Summer 2026 | gpt-5-5-high | 35 | 7.3 | $509 |
| Summer 2026 | gemini-3-1-pro | 56 | 3.7 | $136 |

- Old or small models score −13 to −25 per question.
- **The template's default model is gpt-4o; running it unmodified loses.**
- Official confirmation for Fall 2025: "best baseline bot placed 14th out of 134," and a modified bot with agentic search placed 10th. — [WebSearch summary of Metaculus Fall 2025 analysis (B)](https://forum.effectivealtruism.org/posts/CauF6PstTHK3goE2g/futureeval-forecasting-bot-maker-survey-what-winners-did)
- Official confirmation for Spring 2026: the best Metaculus-built bot (GPT-5.1-high) placed 18th. — [WebSearch summary (B)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)

**Top bots in Spring 2026**
- **GreeneiBot2** topped the bot leaderboard and forecast on 288 of 297 scored questions. It was also a top-3 bot in Q4 2024 and Q1 2025.
- The best open-source bot was **nostreambot** (11th, MIT license, by Jan Flatley-Feldman).
- Pros beat the top-10 bot team by only 1.25 points per question, which is not significant (p = 0.247). — [Spring results (B, snippet)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is); figures confirmed in [PR #5205 (A)](https://github.com/Metaculus/metaculus/pull/5205): Pro lead 1.25, 95% CI [−2.37, 4.87]
- **Recurring top names:** pgodzinai, MWG, GreeneiBot2, manticAI (Mantic, a startup), histerio, Panshul42, acm_bot.

**Summer 2026, self-reported**
- One third-party bot reports being 15th of 277 entries, with about 3,240 spot peer points over 256 scored questions as of 2026-09-09. — [WebSearch summary of a third-party repo (C)](https://github.com/napzter13/metaculus-bot)

**MiniBench (six finalized rounds, Jun–Sep 2026)**
- Each round paid $1,000 across 68–114 eligible bots, with **8–13 bots paid** per round.
- Prizes ranged **$51–$196**, with medians of $68–$123.
- Among bots with ≥90% coverage, **20–38% were paid**; mean take was $18–$32.
- — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)

### Inferences
- **Expected payout for a newcomer**, assuming a template-based bot with a current flagship reasoning model (e.g. Claude Opus high-reasoning), a 5+ run median ensemble, and about 95% coverage from now to January:
  - **$0–$1,000 for Fall 2026, central estimate about $300–$600.** Summer 2026 template equivalents would have earned $500–$840, but the field is growing and the start is a little late.
  - A third-party builder independently estimated a 55–65% chance of any prize and an expected value of about $300–400 ([Bowen1314 README (C)](https://github.com/Bowen1314/metaculus-bot)).
  - **MiniBench adds about $20/round in expectation**, roughly $100–150 across a season. It is lumpy, and it does **not** pay faster: MiniBench prizes are batched and "distributed at the same time" as the season's main prizes (Spring and Fall 2026 announcements, checked 2026-10-08).
- **Trend:** dollars per point fall about 25–40% per season as entries grow (71 → 102 → 192 eligible). Expect Fall 2026 to be more crowded than Summer.
- **You do not need the top 10.** In Summer 2026, 41 bots were paid and rank 56 (avg 3.7/question) would still have earned about $136. The cutoff is roughly "average peer score above about +2–3 per question at high coverage."

### Gaps
- An official full prize table for Q3 2024, Fall 2025, Spring 2026 and Summer 2026 (metaculus.com was blocked).
- Official Summer 2026 final standings: not yet finalized as of the secondhand snapshot.
- Exact counts of bots paid ≥$200.

---

## 3. Rules, eligibility, credits, KYC and payment

### Takeaway
- **Core rules:** no human in the loop; one prize-eligible bot per person or team, using a dedicated bot account; every forecast must carry a private reasoning comment; and you must share code or a description and complete the bot-maker survey.
- **Who can win:** adults (18+), except residents of sanctioned regions. Winners must pass identity and residency verification and are paid by bank transfer via Ramp.
- **Free credits:** donated by OpenAI, Anthropic and Google and delivered as an OpenRouter key. Request them through the participation form.
- **Claude models:** I found no restriction. Anthropic is a credit donor, and Claude template bots compete.

### Cited Findings
- **Core rules.** "No human in the loop"; bots must post a comment explaining their reasoning with each forecast; one prize-eligible bot per user; bot makers must share code or a description of how the bot works. — [AIB/FutureEval pages via WebSearch (B)](https://www.metaculus.com/aib/)
- **No human in the loop, in practice.**
  - You may not preview your bot's forecasts on open questions and then change it.
  - You may not rerun a question because you dislike the forecast.
  - Testing belongs in the unscored "bot testing area."
  - Extra bots must be labelled secondary.
  - Bots may not copy the community prediction.
  - — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Commercial bots.** Bots built or run for a for-profit entity with 3+ founders, employees or contractors receive no prize money and no LLM credits, unless fully open-sourced by season end. Personal projects are fine. — (C, same)
- **Who is eligible.**
  - Participants must be 18+.
  - Residents of Cuba, Iran, Syria, North Korea, Russia, and the Crimea/Donetsk/Luhansk regions are excluded, as are Metaculus staff and their families.
  - Winners must verify identity, nationality and residency.
  - Prizes are paid only after all bot-maker surveys for the season are in; prizes unclaimed after 30 days may be forfeited.
  - Taxes and fees are the recipient's responsibility.
  - **Payment is by bank transfer via Ramp, only to countries Ramp supports.**
  - — (C, same)
- **Bot account and token.** You create a bot account and its `METACULUS_TOKEN` via https://www.metaculus.com/futureeval/participate/. You must fill in the first section of the participation form (https://forms.gle/aQdYMq9Pisrf1v7d8; three required questions: email, primary bot username, "Who are you?") before forecasting. The same form takes LLM-credit applications. — [metac-bot-template README (A)](https://raw.githubusercontent.com/Metaculus/metac-bot-template/main/README.md); [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Free LLM credits.**
  - Credits are donated by **OpenAI, Anthropic and Google** and delivered as an **OpenRouter key**.
  - The amount and turnaround are not published, and top-ups are not guaranteed.
  - Credits must be used for the tournament.
  - They do not cover Exa or Perplexity, but OpenRouter's built-in `:online` search is covered.
  - The Metaculus proxy gave no model allowance with the bot token alone.
  - — [Bowen1314 RESEARCH.md / README (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
  - Older official wording: "Metaculus sponsors the LLM and search costs of participants via donations from Anthropic and OpenAI, as well as a partnership with AskNews." — [AIB page via WebSearch (B)](https://www.metaculus.com/aib/)
- **AskNews.** Free for registered builders, one account per person. Limits: 1,000 calls/month and 4,000 per tournament. Latest-news search costs 1 call; archive search costs 5. Request access by emailing contact@asknews.app. — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Other Metaculus contests that allow bots.**
  - Bots **cannot win Metaculus Cup prizes**, though they may enter it for calibration.
  - Bots **are eligible in Market Pulse** tournaments ($7,000 in Spring 2026, $7,500 in the Summer 2026 post). Market Pulse requires numeric group questions and continuous forecast updating.
  - — [Summer 2026 announcement via WebSearch (B)](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)

### Inferences
- **One-time setup for the owner:**
  1. Create a Metaculus account and bot account.
  2. Fill in the form, ticking "apply for credits."
  3. Optionally email AskNews.
  4. At payout: identity and residency check, plus bank details via Ramp.
- **Tax forms:** no source mentioned W-9/W-8BEN specifically. A US payer would normally collect them, but this is unverified (see Gaps).
- **Claude Code as the builder.** A Claude Code agent building and maintaining the bot, with no human editing forecasts, appears consistent with "no human in the loop," which restricts intervention on live forecasts, not who writes the code.
- **Risk:** if the agent "fixes" the bot after looking at its live forecasts on open questions, that could count as a violation. Changes should be driven by resolved questions and the testing area only.

### Gaps
- No official text seen on tax forms (W-9/W-8BEN) or 1099 issuance.
- The exact credit amount granted per participant.
- An explicit statement of model restrictions. None found; Claude is used by Metaculus's own template bots.

---

## 4. Technical setup: API, template repos, run schedule, research tools, cost

### Takeaway
1. Fork `Metaculus/metac-bot-template`.
2. Add secrets: `METACULUS_TOKEN` plus `OPENROUTER_API_KEY` (or Anthropic/OpenAI keys), and optionally `ASKNEWS_SECRET`, Exa or Perplexity keys.
3. Enable GitHub Actions. The template forecasts the live tournament and MiniBench every 20 minutes.

Because question windows are only about 3 hours, the bot must run at least hourly, ideally every 15–20 minutes. Without donated credits a competitive bot costs roughly **$200/season plus about $15 per MiniBench round** (secondhand estimate).

### Cited Findings
- **Template workflows.** `test_bot.yaml` (manual trigger, posts to the bot-testing-area); `run_bot_on_tournament.yaml` (live tournament + MiniBench, **every 20 minutes**); `run_bot_on_metaculus_cup.yaml` (every 2 days).
- **Template setup.** Takes about 5 minutes: fork, add Actions secrets, enable Actions, run Test Bot.
- **Keys.** Required: `METACULUS_TOKEN` and one LLM key (OpenRouter recommended; OpenAI, Anthropic and Perplexity are also supported). Optional research keys: `ASKNEWS_SECRET`, Perplexity, Exa.
- **Running locally.** Python 3.11+ with Poetry. Modes: `test_questions`, `tournament`, `metaculus_cup`. Dry runs via `publish_reports_to_metaculus=False`.
- **Support.** Discord "build a forecasting bot" channel; contact ben@metaculus.com.
- — [metac-bot-template README (A)](https://raw.githubusercontent.com/Metaculus/metac-bot-template/main/README.md)
- **`forecasting-tools` library.**
  - Two pre-built bots: **MainBot** (most accurate) and **TemplateBot** (cheaper).
  - A Metaculus API wrapper: fetch tournament questions, filter them, post predictions (binary values 0.001–0.999) and comments, handle group questions.
  - A litellm wrapper with the Metaculus proxy and cost tracking.
  - `MonetaryCostManager` spend limits; cost is recorded only after a call completes, so concurrent batches can overshoot.
  - Exa/Perplexity keys enable web search.
  - — [forecasting-tools README (A)](https://raw.githubusercontent.com/Metaculus/forecasting-tools/main/README.md)
  - A third-party bot builds on the library's `FallTemplateBot2026` class. — [Bowen1314 README (C)](https://github.com/Bowen1314/metaculus-bot)
- **Submission format.**
  - Binary: a probability in [0.001, 0.999].
  - Multiple choice: every option, each in [0.001, 0.999], summing to 1.
  - Numeric: exactly `inbound_outcome_count + 1` CDF values (201 by default), with minimum and maximum step constraints.
  - A private reasoning comment is required with each forecast.
  - — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Costs and safeguards (secondhand estimates, not measured).**
  - About $0.25–$0.50 per question. About $200 per season plus about $15 per MiniBench round without donated credits.
  - Suggested caps: $1.50/question, $6/run, $12/day.
  - Run every 15 minutes with a file lock; retry failed questions up to 6 times.
  - The author prefers a server over GitHub Actions for reliability.
  - — [Bowen1314 README (C)](https://github.com/Bowen1314/metaculus-bot)
  - One past bot "burned its daily budget in four questions." — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md)
- **Other implementations.** Many public forks exist, including a Claude-based bot built on the template (robcam55/metaculus-bot) and nostreambot (No-Stream/metaculus-bot, forked by napzter13). — [WebSearch results](https://github.com/robcam55/metaculus-bot); [napzter13 fork](https://github.com/napzter13/metaculus-bot)

### Inferences
- **Running the bot from Claude Code.** An autonomous Claude Code agent can fork the template into the owner's GitHub and configure secrets. The owner pastes the keys once, because the agent cannot create Metaculus or OpenRouter accounts on its own. GitHub Actions cron (every 20 minutes) then runs the bot with no agent session needed.
- **Agent's ongoing role:** monitor Actions failures and spend, and adjust the bot between questions using only resolved-question feedback.
- **Cron caveat:** GitHub's scheduled workflows can be delayed or skipped under load. With ~3-hour windows, a 20-minute cron is usually adequate, but missed runs reduce coverage.
- **Budget:** with $500 total, about $200–250 covers a full Fall season plus MiniBench if no credits are granted. Credits, if granted, could make it nearly free.

### Gaps
- An official Metaculus API rate-limit or schema page (blocked). The third-party README shows the bot account API tier as "restricted," which suggests tiered access whose meaning I could not verify.
- Measured monthly API cost for the top bots: none published.

---

## 5. What distinguishes winning bots; published analyses

### Takeaway
1. **The underlying model matters most:** frontier, high-reasoning variants.
2. **Ensembling:** 5+ runs, aggregated by median.
3. **Research breadth:** more than one news or search source.
4. **Clipping, not extremizing:** cap extreme probabilities rather than push them outward.
5. **Reliability:** full coverage, robust parsing, guards against treating unresolved questions as resolved.

Extra cleverness (extremization, logit aggregation) often hurt.

### Cited Findings
Unless marked otherwise, these come from a secondhand synthesis that cites Metaculus notebooks 35291, 38673, 40456, 43337, 43357, 45373, 45382, 45336, 43361 and 43356, and the LessWrong post "AI Forecasting in 2026: What 11 Analyses Say" — [Bowen1314 RESEARCH.md (C)](https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md); [LessWrong synthesis (B)](https://www.lesswrong.com/posts/a82q6yd8zKpYk56cF/ai-forecasting-in-2026-what-11-analyses-say)
- **Model choice:** the model matters most. High-reasoning variants beat standard ones (p = 0.004).
- **Ensembles:** most Fall 2025 winners ensembled 5+ forecasts using the median. Cutting the forecast count backfired.
- **Research breadth:** winners used more research sources (1.75 vs 1.00, r = 0.42, p = 0.006). No single provider dominated, and a bot with no research ranked last.
- **Clipping vs extremizing:** clipping predictions was the strongest differentiator among winners (r = +0.48, p = 0.005). Extremizing correlated negatively (r = −0.30). One bot fell from 20th to 63rd after adding logit aggregation and extremization.
- **Failure modes:** treating unresolved questions as already resolved, which produced extreme 99% forecasts, and parser failures. The advice is a deterministic parser with an LLM fallback.
- **Numeric questions:** use wide intervals; numeric forecasts tend to be too narrow.
- **Scaffolding:** the top five scaffolded bots beat their non-scaffolded baseline by 5–11 peer points per question (Fall 2025). — [WebSearch summary of Metaculus analysis (B)](https://forum.effectivealtruism.org/posts/CauF6PstTHK3goE2g/futureeval-forecasting-bot-maker-survey-what-winners-did)
- **Team size:** aggregating bots into teams showed diminishing returns, with performance declining beyond a team of about 10 (Spring 2026). — [Spring results (B, snippet)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)
- **Bots vs Pros over time** (head-to-head score, 0 = parity):

  | Q3 2024 | Q4 2024 | Q1 2025 | Q2 2025 | Spring 2026 |
  |---|---|---|---|---|
  | −11.3 | −8.9 | −17.7 | −20.0 | −1.25 (not significant) |

  — [PR #5205 (A)](https://github.com/Metaculus/metaculus/pull/5205); [Spring results (B)](https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)
- **Academic background.** "Approaching Human-Level Forecasting with Language Models" (Halawi et al., 2024) used a retrieval + reasoning + aggregation pipeline and approached the crowd aggregate on competitive forecasting platforms. — [arXiv 2402.18563](https://arxiv.org/abs/2402.18563) (from background knowledge; not fetched this session)
- **ForecastBench** (Forecasting Research Institute) is a dynamic, contamination-free benchmark scored by a Brier Index, with a tournament leaderboard. **No cash prize was found.** — [FutureSearch evals page (B)](https://evals.futuresearch.ai/)

### Inferences
- **Recommended recipe for a newcomer:**
  1. Start from the template with the current flagship Claude or GPT high-reasoning model, not the gpt-4o default.
  2. Run 5 independent forecasts and take the median.
  3. Use AskNews (free) plus one web-search source.
  4. Clip binary forecasts to roughly [0.03, 0.97].
  5. Use wide numeric distributions.
  6. Aim for near-100% coverage.

  This matches what the winners did and is about what a Claude Code agent can build in a day.

### Gaps
- Detailed pipelines of the top bots (GreeneiBot2, pgodzinai, Panshul42). Only Panshul42's and nostreambot are open source; I did not fetch their code.

---

## 6. Other recurring cash-prize forecasting competitions open to autonomous bots

### Takeaway
Besides FutureEval and MiniBench, the only confirmed bot-eligible cash contest found is Metaculus **Market Pulse** (about $7.5K per round, harder format). ForecastBench, Prophet Arena and Kalshi/Polymarket offer leaderboards or trading, not prize contests. Bridgewater x Metaculus and the Metaculus Cup are human contests.

### Cited Findings
- **Market Pulse:** bots eligible for prizes; $7,000 (Spring 2026 post) or $7,500 (Summer 2026 post); requires numeric group questions and continuous updating. — [Summer 2026 announcement (B, snippet)](https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament)
- **Metaculus Cup:** bots are not prize-eligible. A third-party site reports a bot placed first in the Summer 2026 Cup, but it says it has not audited the scoring. — [explainx.ai (C)](https://explainx.ai/blog/ai-beats-forecasters-metaculus-cup-coverage-2026)
- **Spring 2026 Cup "Question Links Contest" ($5K):** a one-off. — [WebSearch result (B)](https://forum.nunosempere.com/posts/PaR3pjj7fgQepWb3C/announcing-the-question-links-contest-for-metaculus-s-spring)
- **Bridgewater x Metaculus 2026:** $30K, ran Jan 12–Mar 13, 2026, now closed, aimed at humans. — [Bridgewater page (B)](https://www.bridgewater.com/bridgewater-x-metaculus-2026-competition)
- **Prophet Arena (UChicago):** benchmarks LLMs on live Kalshi/Polymarket events with simulated betting returns. No cash prize found. — [ICLR 2026 poster](https://iclr.cc/virtual/2026/poster/10009102)
- **ForecastBench:** leaderboard only; no prize found. — [FutureSearch evals (B)](https://evals.futuresearch.ai/)
- **Kalshi:** no sponsored bot contest found. An anecdote of an AI turning $35 into $2M on Kalshi is unverified. — [WebSearch summary of ACX post (C)](https://www.astralcodexten.com/p/acxmetaculus-prediction-contest-2026)

### Inferences
- For a single owner, FutureEval plus MiniBench is the practical cash venue. Market Pulse is possible upside for a more capable bot that can update forecasts continuously.

### Gaps
- Good Judgment, Kaggle forecasting and Q-bench: no current bot-eligible cash contests found (not searched exhaustively). ForecastBench prize status was not checked on forecastingresearch.org directly.
