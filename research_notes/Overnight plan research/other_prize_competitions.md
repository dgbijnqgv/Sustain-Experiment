# Other prize competitions for an autonomous coding agent (alongside a Metaculus bot)

Research date: 2026-10-08. Researcher: Claude (subagent), using WebSearch plus raw GitHub fetches.

**Labels**
- **VERIFIED**: I read the primary text myself. Only github.com / raw.githubusercontent.com could be fetched. Every other domain tested (kaggle, drivendata, zindi, aicrowd, topcoder, herox, devpost, huggingface, arcprize, numer.ai, crunchdao, gjopen, forecastbench, mlcontests.com, nvidia, x.com) returned EGRESS_BLOCKED / connect_rejected.
- **SNIPPET**: the claim comes from a WebSearch result summary of the cited URL. I did not read the page myself, so check it before relying on it.
- **ESTIMATE**: my own reasoning or arithmetic. It is not sourced.

The agent profile assumed throughout: Claude Code or Codex on a subscription, with web search, Python, a CPU cloud container and GitHub Actions. There is no paid GPU, only the free Kaggle/Colab GPU. The owner does one-time registration and KYC only.

---

## 0. Key cross-cutting facts

### 0.1 Current open prize competitions (VERIFIED, from the mlcontests.com dataset on GitHub)
Source: `https://raw.githubusercontent.com/mlcontests/mlcontests.github.io/master/competitions.json`, fetched 2026-10-08. It lists 398 competitions; the newest "added" date seen is 15 Sep 2026. It is a curated list and not exhaustive. These are the competitions with a deadline on or after 2026-10-08:

| Deadline | Platform | Prize | Competition |
|---|---|---|---|
| 2026-10-11 | Independent | $5,800 | EUROCONTROL Predict Aircraft Taxi-Out Time |
| 2026-10-11 | Codabench | $4,000 | Weak Lensing Uncertainty under Distribution Shift (DOE) |
| 2026-10-12 | Codabench | $12,000 | Verifiable AI Agents for Quantitative Finance (NVIDIA/Bloomberg) |
| 2026-10-15 | Independent | $27,000 | Design Physics Experiments for Gravitational Waves (SPRIN-D) |
| 2026-10-22 | Kaggle | $77,000 | RSNA Knee Abnormality Detection |
| 2026-10-25 | Codabench | $21,000 | RealPDE |
| 2026-10-25 | Independent | $54,000 | Generative Modeling of Mouse Embryo Development |
| 2026-10-25 | Codabench | $10,000 | Interpretability for AIMO Reasoning |
| 2026-10-26 | Independent | $1,000 | Fusion Reactor Magnetic Geometry |
| 2026-11-02 | Kaggle | $700,000 | ARC Prize 2026 ARC-AGI-2 |
| 2026-11-02 | Kaggle | $850,000 | ARC Prize 2026 ARC-AGI-3 |
| 2026-11-09 | Kaggle | $450,000 | ARC Prize 2026 Paper Track |
| 2026-11-12 | Kaggle | $35,000 | Write a Research Paper on Coding Agents (Gemma 4) |
| 2026-11-15 | Independent | $14,925 | FlagOS: Optimise LLM Operators & Inference Across AI Chips |
| 2026-11-15 | Independent | $13,600 | Wunder Fund: Predict Price Movements from LOB data |
| 2026-11-20 | Codabench | $2,800 | Language-Conditioned Visual Navigation |
| 2026-11-21 | Codabench | $20,000 | Decode Brain Signals |
| 2026-12-02 | Kaggle | $65,000 | Build Coding Agents with Gemma 4 |
| 2026-12-07 | Zindi | $7,500 | Caribbean Voices ASR |
| 2026-12-14 | Kaggle | $50,000 | Enveda CASMI26: Predict 2D Chemical Structures from Mass Spectra |
| 2026-12-31 | CrunchDAO | $52,000 | DataCrunch 2: Predict Cross-sectional Equity Returns (ongoing, weekly) |

The same dataset gives the 2026 platform volume (competitions with a 2026 deadline, summed listed prizes; ESTIMATE from VERIFIED data):
- **Kaggle:** 34 competitions, about $6.36M. This is dominated by AIMO3 ($2.2M) and ARC ($2.0M). A typical featured competition is $50–77k.
- **Zindi:** 26 competitions, about $290k, typically $1.5–46k.
- **DrivenData:** 6 competitions, $227k.
- **CrunchDAO:** 6 competitions, $232k.
- **Devpost:** 9 listed hackathons, about $2.15M, of which $2M is a single Google Gemini event.
- **Hugging Face:** 1 competition, $2k.

### 0.2 AI-agent capability evidence
- **MLE-bench leaderboard (VERIFIED, github.com/openai/mle-bench README, read 2026-10-08).** The README says: "*Update* (04-24-2026): We are currently not taking any new submissions to the leaderboard..."
  - The top "All" medal rate is Famou-Agent 2.0 (Gemini-3-Pro) at **64.44%**. AIBuildAI (Claude-Opus-4.6) scores **63.11%** and MLEvolve **61.33%** (12h). AIDE with o1-preview in Oct 2024 scored 17.12%.
  - The benchmark setup is "Runtime: 24 hours. Compute: 36 vCPUs with 440GB RAM and one 24GB A10 GPU". That is far more compute than our free Kaggle/Colab setup.
  - The rate counts "Any Medal", which includes bronze. It is measured against frozen, historical leaderboards. **A medal is not prize money.** Cash usually goes only to the top 3–5 places.
- **Meta AIRA₃ (SNIPPET: alphasignal.ai, medium, x.com/AIatMeta).** It finished 8th of about 4,000 teams (gold) in the June 2026 NVIDIA Nemotron reasoning competition on Kaggle. It used an ensemble of "GPT 5.5 with OpenCode plus Claude 4.8 with ClaudeCode", with many parallel long-running agents. 8th place was outside the cash places. The result is self-reported by Meta, announced 2026-09-05.
- **NVIDIA blog "Winning a Kaggle Competition with Generative AI–Assisted Coding" (SNIPPET; developer.nvidia.com is blocked).** The March 2026 **Playground** churn competition was won by "a four-level stack of 150 models, selected from 850". The work was done with "GPT-5.4 Pro, Gemini 3.1 Pro, Claude Opus 4.6—in a human-in-the-loop workflow" by an NVIDIA four-time Grandmaster. Playground competitions do not pay cash.
- **HSE NeuroGolf 2026 (SNIPPET: quantumzeitgeist.com).** The team won a gold medal using "an automated system of 330 ChatGPT-based agents". About 100 teams were disqualified in the NeuroGolf verification process (SNIPPET).
- **Disarray agent "28 medals" (SNIPPET: artificialintelligencedynamics.com, 2026-04-09).** This is a vendor claim. The MLE-bench README lists Disarray at 77.78% under "Additional Leaderboard Submissions" with a "Test-set feedback" caveat (VERIFIED).
- **Sakana ALE-Agent (SNIPPET: LinkedIn post by Takuya Akiba).** It took 1st of 800+ in AtCoder AHC058, a 4-hour optimisation contest, at "approximately $1,300" in cost. It entered with organiser cooperation. Normal AHC rules ban this kind of automation (see §10).
- **ctf-agent (VERIFIED, raw.githubusercontent.com/verialabs/ctf-agent README).** "Built in a weekend, we used it to solve all 52/52 challenges and win **1st place at BSidesSF 2026 CTF**", with a prize of "$1,500". It was built by members of the #1 US CTF team, so it is not representative of a non-elite operator.

---

## 1. Kaggle (featured, research and code competitions)

**Prize pool and paid places.** A typical featured competition is $50k–$77k and pays roughly the top 3–5 places (e.g. Gemma 4 Developer Agent: "$37,000 for first, $18,000 for second, and $10,000 for third", SNIPPET, aiwiki.ai). Fields are large: BirdCLEF+ 2026 had 4,094 teams (SNIPPET, albumentations.ai) and AIRA₃'s competition had about 4,000.

**Entry cost.** $0.

**Rules on AI.** I found no Kaggle-wide ban on AI-generated or agent-generated submissions.
- Rules commonly contain the AMLT clause: "Individual Participants and Teams may use automated machine learning tool(s)... provided that the participant properly licenses the AMLT" (SNIPPET: Titanic, ARC-AGI-3 and Pokémon TCG rules pages).
- Account rule: "You will be disqualified if you make Submissions through more than one Kaggle account, or attempt to falsify an account to act as your proxy" (SNIPPET, ARC Prize 2026 rules on Kaggle). The agent must therefore operate the owner's single account. The account must not be a separate "bot account".
- "Submissions may not use hand labeling or human prediction of the validation or test data" (SNIPPET).
- Winners must deliver "the final model's software code as used to generate the winning Submission and associated documentation" (SNIPPET, ARC-AGI-3 rules). Some hosts add an interview (ARC-AGI-2 1st prize "contingent upon meeting open-source requirements + interview + solution type", SNIPPET). The interview needs the human owner.

**Compute limits.**
- Code competitions run inside Kaggle notebooks, typically with "Internet access disabled" and a CPU/GPU runtime cap of about 9h (SNIPPET / general knowledge; I could not open the official page).
- Free GPU quota is about 30h/week (SNIPPET, low-authority glossary). A Japanese blog reports it shrinking in 2026 (SNIPPET).
- The 2025 ARC competition used "L4x4s" (SNIPPET).
- API-based LLMs are banned at inference: "Internet access is not available during Kaggle evaluation, and API-based systems such as GPT or Claude are excluded" (SNIPPET, arcprize.org). Claude/Codex can only write the code. Inference must use open-weight models on Kaggle hardware.

**Agent evidence.** See §0.2. Agents win medals often, but prize places in live featured competitions are rare. The best-documented autonomous system (AIRA₃, heavy compute) took 8th, which is unpaid.

**Prize-eligible competitions running Oct 2026 – Mar 2027.** VERIFIED from the dataset:
- RSNA Knee: $77k, closes 10-22. Too late to start.
- ARC-AGI-2/3: closes 11-02, needs elite performance.
- Gemma 4 coding-agent paper: $35k, 11-12. Judged.
- Build Coding Agents with Gemma 4: $65k, 12-02. Measurable. The agent config follows "Google ADK Agent Config specification with additional restrictions to prevent code execution outside of a sandbox" (SNIPPET).
- Enveda CASMI26: $50k, 12-14. About 90 days from launch on 2026-09-15 (SNIPPET, BusinessWire).
- More competitions will launch through Q1 2027. Kaggle ran 68 competitions with $3.668M in prizes in 2025 (SNIPPET, ML Contests report via blog).

**EV for a non-elite autonomous agent (ESTIMATE).**
- P(top-3/5 in a $50k featured competition with 1,000–4,000 teams, free GPU only) is about 0.3–1%.
- That gives roughly $100–400 EV per competition entered, with about 1–2 serious entries a month. Expected value is **~$100–500/month, almost certainly $0 in any given month**.
- The main value is medals and reputation, plus fallback learning for the other tournaments.

**Owner effort.** Phone-verified account (one-time). For a prize: tax form, winner license, possible interview or call, and payout to a bank account.

**KYC/payout.** The owner must be the registered individual. Some host countries are excluded per competition.

---

## 2. DrivenData
- **Pool.** 6 competitions in 2026 for $227k total (VERIFIED dataset). The latest closed on 2026-10-02, and **none were open as of 2026-10-08** in the dataset. Typical prizes are $20–70k across about 3–5 places.
- **AI rules.** I found no platform-wide generative-AI rule (SNIPPET search). Eligibility example: "open to natural persons who are legal residents of a territory and at least eighteen years old... legal entities and organizations are not eligible" (SNIPPET, community.drivendata.org/t/prize-eligibility/7553). Government-sponsored challenges defer to challenge.gov rules (SNIPPET).
- **Compute.** Code-execution competitions use the DrivenData runtime with time limits (SNIPPET, forum thread).
- **EV (ESTIMATE).** Fields are smaller than Kaggle (hundreds of teams), but there are few competitions and many are speech/medical GPU-heavy. About **$0–150/month**.
- **Owner effort.** One-time account. Winners submit code and a write-up, plus a tax form.

## 3. Zindi
- **Pool.** 26 competitions in 2026 for about $290k (VERIFIED dataset). Typical prizes are $1.5k–$46k, usually across the top 3.
- **Open now.** Caribbean Voices ASR, $7.5k, closes 2026-12-07 (VERIFIED dataset).
- **AI rules.** No specific AI rule found. "Top 10 finishers on the private leaderboard get an email requesting their code... 48 hours to respond", and "if code does not reproduce your score on the leaderboard, we will drop your rank" (SNIPPET, zindi.africa/rules and the 2020 announcement).
- **Geography.** "Competitions are open to data scientists worldwide, however, certain Competitions may have geographic restrictions" (SNIPPET, zindi.africa/terms). Many prizes are limited to Africa-resident or national participants (SNIPPET, forum examples).
- **KYC.** "The top 3 winners or team leaders will be required to present Zindi with proof of identification, proof of residence and a letter from your bank" (SNIPPET).
- **IP.** Winning code must be assigned: "assign worldwide copyright in it to Zindi" (SNIPPET, terms).
- **EV (ESTIMATE).** Smaller fields and easier tabular problems, but residency limits and the 48-hour code-response window (the owner must watch email). About **$20–150/month** if the owner is non-African. Check each competition's eligibility.

## 4. AIcrowd
- **Current.** ARC (Alignment Research Center) White-Box Estimation Challenge 2026, "$150,000+" total (SNIPPET, aicrowd.com).
  - **Phase 2 closes 2026-10-17 23:59 UTC** (SNIPPET, discourse.aicrowd.com).
  - **AI explicitly allowed**: "LLM use is fully permitted and encouraged, but must be disclosed transparently" (SNIPPET).
  - Scoring is measurable: "final-layer MSE only". It is CPU-friendly (FLOP budget 2^41 per MLP, 120s, 8GB) and allows 10 submissions/day.
  - Prizes require an OSI-approved code license.
- **Other.** NeurIPS 2026 has 16 accepted competitions (SNIPPET, blog.neurips.cc 2026-07-28). Some of them run on AIcrowd.
- **EV (ESTIMATE).** This is a one-off. It is worth a 9-day sprint because it is measurable, CPU-only and AI-welcome, but the remaining Phase 2 pool is unknown. Long-run platform EV is about **$0–200/month**.

## 5. Topcoder
- **Marathon Match Tournament 2026.** Runs "June 1, 2026 to March 31, 2027" with at least 6 matches (SNIPPET, internshala). The listed match windows are Jun 17–24, Aug 5–12, Sep 23–30 and **Nov 4–11** (SNIPPET).
- **Prizes are small.** The 2025 cycle paid "Champion: $6,000; 2nd $2,000; 3rd $500; 4th-8th $200" (SNIPPET, topcoder.com/marathon-match-tournament/overview). Individual MM prizes have historically been a few hundred dollars (SNIPPET, a 2018 MM100 example: $250/$150/$75).
- **AI rules.** No 2026 AI policy found. The general rule is "participants are free to use any method they want, as long as it's not explicitly prohibited" (SNIPPET). An old 2017 line, "all the code you submit must be written on your own", predates generative AI. Topcoder now runs an "AI Reviewer" on challenges (SNIPPET, LinkedIn).
- **Fit (ESTIMATE).** Marathon Matches are heuristic optimisation with automatic scoring, which LLM agents are good at (AHC058 evidence). Prizes are small. Payout needs a Topcoder member account with tax form and a Payoneer/PayPal-type wallet.
- **EV (ESTIMATE).** **$0–100/month.**

## 6. HeroX
- Sponsor-judged challenges, often NASA or other government. They frequently require citizenship/residency and narrative proposals. HeroX takes a fee from the sponsor (SNIPPET, older article).
- No AI policy found.
- **EV (ESTIMATE).** About **$0**. Judging is subjective and slow (2–4 months), and many challenges are US-only. Skip.

## 7. Devpost hackathons
- **Pools.** Large but subjective. Examples: Google Gemini $2M (closed 2026-08-17); Ruya AI $27.5k; Airia $7k across 6 prizes (SNIPPET).
- **Odds.** For the Gemini competition, "10 prizes... 2,000+ applicants" means about 0.4–0.5% per entrant (SNIPPET, discuss.ai.google.dev). Devpost guidance puts registrant-to-submission conversion at 5–33% (SNIPPET).
- **AI rules.** These vary per event.
  - MLH guide: "may use LLM/ChatGPT/AI, but must state how they did so in their Devpost submission... if you do not credit your AI usage, you will be disqualified"; the project must not be a "reskin of an existing AI tool" (SNIPPET, guide.mlh.io).
  - youCode 2026: "heavily AI-generated submissions without significant original input may not qualify" (SNIPPET).
  - Devpost's own "Build With AI: Basics 2026" encourages coding agents, with a $2.5k pool (SNIPPET).
  - Most events require a demo video and judging by humans. No evidence found of an autonomous agent winning.
- **EV (ESTIMATE).** **$0–100/month.** This is judged, marketing-like work, which is the opposite of the owner's goal.

## 8. Hugging Face competitions
- Only 1 HF-platform competition in 2026 ($2k; VERIFIED dataset). HF-hosted hackathons such as Build Small ($48k+, closed 2026-06-15) are judged (SNIPPET).
- **EV (ESTIMATE).** About **$0**. Skip, but watch for occasional measurable competitions.

## 9. AI Mathematical Olympiad and ARC Prize
- **AIMO.** Progress Prize 3 was $2.2M and ended 2026-04-15 (SNIPPET). No AIMO4 had been announced as of my searches. The related Codabench "Interpretability for AIMO Reasoning" ($10k) closes 2026-10-25 (VERIFIED dataset).
- **ARC Prize 2026.** The overall pool is "$2M" across 3 tracks. Submissions are due 2026-11-02, papers 2026-11-08, results 2026-12-04 (SNIPPET, arcprize.org).
  - "Internet access is not available during Kaggle evaluation, and API-based systems such as GPT or Claude are excluded" (SNIPPET).
  - Prize code must be released under a "permissive public domain license, such as CC0 or MIT-0" (SNIPPET).
  - ARC-AGI-3 milestone prizes ($25k/$10k/$2.5k) on 2026-06-30 and 2026-09-30 **have already passed**. Milestone 1 went to Tufa Labs (SNIPPET, alphasignal.ai).
- **EV (ESTIMATE).** About **$0** for a non-elite agent with 3.5 weeks left. The field is dominated by research labs.

## 10. Advent of Code, CodeChef, Codeforces and AtCoder (no cash, or AI banned)
- **Codeforces.** Under the 2024-09-14 rule, pasting a problem "into an AI system to get ready-made code" and similar uses are banned in rated rounds (SNIPPET, codeforces.com/blog/entry/133941). There is no cash anyway.
- **Advent of Code 2025.** It removed the global leaderboard, cut to 12 puzzles, and the FAQ says not to use AI (SNIPPET, thenewstack.io). No cash.
- **CodeChef.** No meaningful cash for global open contests (general knowledge, unverified).
- **AtCoder Heuristic Contest.** AHC rules version 20250616 explicitly prohibit "automatically sending a large number of the same or different prompts to generate multiple candidates, then evaluating or selecting among them" (SNIPPET, info.atcoder.jp/entry/ahc-llm-rules-en). On 2026-07-30 AtCoder proposed a "with AI division" for long AHCs (SNIPPET, atcoder.jp/posts/ahc_new_ai_rule_en). Sponsored AHC prizes are usually for Japan residents (general knowledge).
- **Verdict.** Skip for income. Possibly revisit an AtCoder AI division if it adds prizes.

## 11. Gitcoin, Optimism Retro Funding and open-source retro funding
- **Optimism.** L2BEAT Governance Review #81 (2026-01-12) says Season 9 changes "pause Retro Funding" (SNIPPET). The Season 8 budget was up to 5M OP (SNIPPET, gov.optimism.io).
- **Gitcoin.** GG24 (Oct–Nov 2025) distributed $1.8M. GG25 (2026) was planned as a single-domain (d/acc), coalition-funded round in Q2; I found no confirmation that it ran (SNIPPET, gov.gitcoin.co).
- **Fit (ESTIMATE).** These reward ecosystem adoption and community voting, which means marketing. That conflicts with the owner's goal. **EV about $0** in the next 6 months.

## 12. Forecasting contests other than Metaculus
- **Good Judgment Open.** No cash. The Economist 2026 challenge prize is publication; the university challenge prize is workshop tickets (SNIPPET, goodjudgment.com, gjopen.com). Skip.
- **ForecastBench (FRI).** A benchmark leaderboard only; no cash prize found (SNIPPET).
- **Prophet Arena (UChicago).** A benchmark that uses Kalshi/Polymarket questions; no prize (SNIPPET).
- **Kalshi/Polymarket.** Real-money trading, not contests. I found no sponsored bot contest (SNIPPET). Trading puts capital at risk and Polymarket's US status is complicated. Out of scope.
- **"Q-bench".** Nothing found under that name.
- **Metaculus.** Already in the plan: FutureEval Fall 2026 at $50–58k, plus MiniBench at $1k per 2 weeks (SNIPPET, metaculus.com/aib). Rules include "no human in the loop... one prize-eligible bot per user" (SNIPPET).

## 13. Numerai (main tournament and Signals): staking required
**How it pays (VERIFIED, github.com/numerai/docs, master branch).**
- staking.md: "By staking on Numerai... you give Numerai permission to payout or burn the NMR at stake... positive scores are rewarded with more NMR, while negative scores cause staked NMR to be _burned_."
- Unstaked models earn nothing (SNIPPET).
- atomic-blockchain-staking.md, "Payouts Settings":

| Tournament | Clip | Stake threshold | Multipliers |
|---|---|---|---|
| Crypto | 1 | 10000 | 0.1xCORR + 1xMMC |
| Signals | 1 | 36000 | 4xALPHA + 8xMPC |
| Numerai | 1 | 72000 | 3xCORR + 9xMMC |

- The legacy clip was ±5%/round. **Clip 1 means up to 100% of a round's stake can burn in theory.**
- `payout_factor = min(1, stake_threshold / total_at_risk)`.

**Scale.** About 870,000 NMR staked, more than 5,000 staked models and about 600 staked accounts (SNIPPET, yellow.com citing nmrdash, May 2026). Assuming most of it sits in the main tournament, the payout factor is about 72k/870k, roughly 0.08 (ESTIMATE). NMR traded at about $8.4–10 in Aug–Oct 2026 (SNIPPET, several price sites).

**Agents are welcome.** Numerai frames 2026 as an "Era of Agents" and offers "Numerai Skills and the Numerai Model Context Protocol (MCP)" for "fully agentic research loops" (SNIPPET, blog.numer.ai). Its July 2026 press release says these enable "increasingly autonomous participation by AI systems" (SNIPPET, decrypt.co). There have been $3.2M of NMR buybacks in 12 months (SNIPPET).

**EV (ESTIMATE).**
- A decent but non-elite model (CORR about 0.015, MMC about 0) scores roughly 0.045 × 0.08, which is about +0.36% per round on the stake at risk.
- Atomic staking locks a separate stake per round over a ~20-trading-day resolution window. Capital deployed therefore earns roughly 0.3–0.5%/month in expectation, with large variance from CORR swings and NMR price moves.
- On $1,000 of NMR that is about **$3–5/month expected**, against a realistic ±20–50% drawdown risk from burns plus token volatility.
- Negative MMC models, which are common for generic GBDT models on the public data, have negative EV.
- **Verdict.** Not worth it as income unless the owner wants to risk capital. At most, run unstaked for 3+ months to build a track record (zero cost) and stake only if MMC is consistently positive.

**KYC.** A wallet (Privy embedded) and buying NMR via Coinbase or Uniswap. US residents can participate (general knowledge). Tax reports are issued each January (VERIFIED, staking.md).

## 14. CrunchDAO (incl. ADIA Lab and DataCrunch 2)
- **DataCrunch 2: Predict Cross-sectional Equity Returns.** Listed at $52,000, ongoing to 2026-12-31 (VERIFIED dataset).
  - "DataCrunch is distributing 1,000 USDC every weeks" (SNIPPET, docs.crunchdao.com/competitions/competitions/datacrunch-2).
  - The task is a weekly ranking of about 3,000 liquid US equities, scored by Spearman correlation. "The payouts are distributed according to an exponential function of your position on the leaderboards" (SNIPPET).
  - Compute is 10h GPU/CPU per week on Crunch infrastructure (SNIPPET).
  - Payouts are in USDC on Solana. A 2026-W14 forum post says "sent both February and March payouts" (SNIPPET, forum.crunchdao.com/t/2026-w14-datacrunch-2-payouts/1130).
- **No capital at risk, no staking.**
- **ADIA Structural Break Real-Time.** $100k (40k first, tiers down to 3k for 10th). Closed 2026-10-01; final evaluation is late October (SNIPPET). The Open Benchmark paid $6k to the top 3 quarterly (SNIPPET, x.com/adia_lab).
- **KYC.** "Your prize will be transferred to your Solana wallet, which is managed by Privy.io"; "If you took part in a major competition... you will receive an email with instructions on how to complete the KYC process... Refusing to comply is the same as refusing your prize" (SNIPPET, docs.crunchdao.com/competitions/faqs/prize-winners). An older tournament excluded sanctioned jurisdictions (SNIPPET).
- **AI rules.** None found. Code must be deterministic: "or the entry will be ineligible for any rewards" (SNIPPET, structural-break docs).
- **EV (ESTIMATE).** With 1,000 USDC/week paid exponentially by rank, a mid-to-upper-ranked model might earn about $5–40/week, or **$20–150/month**. Payouts are recurring and machine-scored, and there is no marketing. The live equity signal is noisy, so the ranking is partly luck.

## 15. Puzzle and CTF competitions with cash prizes
- Proven: BSidesSF 2026 1st place, $1,500, by an autonomous agent (VERIFIED, see §0.2).
- CAI claims the $50k top prize at Neurogrid CTF 2025, but "with humans teleoperating via Human-In-The-Loop" (SNIPPET, arXiv 2512.02654).
- Explicit agent tracks:
  - AAA-CTF: "build agents that discover flags without any human intervention" (SNIPPET, cybercup.ai).
  - CSAW LLM CTF: any LLM allowed (SNIPPET).
  - PwnSec 2026 split the field into human and AI tracks (SNIPPET).
- **Rules vary.** Many CTFs with cash prizes restrict by student status or country, and payout goes to a registered human team.
- **EV (ESTIMATE).** **$0–150/month.** Cash CTFs are sporadic (a few a month on CTFtime, often with small or regional prizes). Competition from AI-equipped elite teams is now intense. The infrastructure also overlaps with legitimate security work.
- **Safety caveat.** Keep strictly to authorised CTF infrastructure.

## 16. Issue bounties
Already rated weak and skipped as instructed.

---

## Summary table (EV = ESTIMATE, per month, for a competent non-elite autonomous agent)

| Venue | Capital at risk | AI allowed? | Machine-scored? | Owner effort | EV/month |
|---|---|---|---|---|---|
| CrunchDAO DataCrunch 2 | $0 | No ban found | Yes, weekly | KYC + Solana wallet | $20–150, recurring |
| Kaggle featured/code | $0 | Yes (AMLT clause); 1 account; no API at inference | Yes | Account, tax form, possible interview | $100–500 (lumpy; usually $0) |
| AIcrowd ARC White-Box (to Oct 17) | $0 | Explicitly yes, with disclosure | Yes (MSE) | Account; OSI license | One-off lottery ticket |
| Zindi | $0 | No ban found; 48h code review | Yes | ID, residence, bank letter; geo limits | $20–150 |
| Topcoder MM tournament | $0 | Not explicit | Yes | Account, tax, payout wallet | $0–100 |
| CTF (cash) | $0 | Varies; some AI tracks | Yes (flags) | Team registration | $0–150 |
| Numerai (staked) | NMR stake (burnable) | Yes, actively encouraged | Yes | Wallet, buy NMR | about 0.3–0.5% of stake, ± large variance |
| DrivenData | $0 | Unknown | Yes | Account, tax | $0–150 (nothing open now) |
| Devpost / HeroX / HF hackathons | $0 | Disclosure required | No (judged) | Video, judging | about $0–100 |
| GJOpen / ForecastBench / Prophet Arena | $0 | n/a | n/a | n/a | $0 (no cash) |
| Gitcoin / Optimism retro | $0 | n/a | No (voting) | Marketing | about $0 |
| ARC Prize / AIMO | $0 | Offline open-weights only | Yes | Interview, open source | about $0 |
| Codeforces / AoC / CodeChef / AHC | n/a | Banned or no cash | n/a | n/a | $0 |

## Ranking: top picks to add alongside the Metaculus bot
1. **CrunchDAO DataCrunch 2 (weekly USDC, no stake).** This is the closest fit to "income that waits for machine-verifiable work". It is a recurring weekly payout with no capital and no marketing. The agent iterates models on CPU and Crunch's 10h/week compute. The owner does one KYC and wallet setup. Also watch the CrunchDAO hub for new ADIA-style competitions; these pay $6k–100k to the top 3–10.
2. **Kaggle measurable competitions (CASMI26 to Dec 14, Gemma 4 coding agents to Dec 2, and new Q4/Q1 launches).** This has the highest upside, but returns are lumpy. Kaggle medals are attainable; cash places (top 3–5) are rare. Choose tabular or time-series competitions, or competitions that fit within free Kaggle GPU limits. Use the owner's single account; no bot or proxy account.
3. **AIcrowd ARC White-Box Estimation (Phase 2, closes 2026-10-17).** This is an immediate, cheap sprint. LLM use is "fully permitted and encouraged", scoring is a pure MSE metric, and it runs on CPU. After it closes, monitor AIcrowd and Codabench (NeurIPS 2026 track) for similar measurable, AI-friendly competitions.
4. **Zindi (globally eligible competitions only) and Topcoder Marathon Matches (Nov 4–11 window).** These are lower prizes but smaller fields with automatic scoring. Zindi requires the owner to answer code requests within 48h. Topcoder heuristic-optimisation contests suit agents.
5. **(Optional, conditional) Numerai unstaked → small stake.** Numerai welcomes agents (MCP/Skills), but money requires staking burnable NMR. Expected return is about 0.3–0.5%/month on stake, with larger downside variance. Add only as a zero-cost unstaked track record. Stake only with money the owner is willing to lose.

**Skip for income:** Devpost, HeroX and HF hackathons (judged or marketing), GJOpen/ForecastBench/Prophet Arena (no cash), Gitcoin/Optimism (paused, or voting-based), ARC Prize/AIMO (elite and offline), Codeforces/AoC/CodeChef/AHC (no cash or AI banned).

---

## Source URLs (accessed 2026-10-08)
VERIFIED (read directly):
- https://raw.githubusercontent.com/openai/mle-bench/main/README.md
- https://raw.githubusercontent.com/mlcontests/mlcontests.github.io/master/competitions.json
- https://raw.githubusercontent.com/numerai/docs/master/numerai-tournament/staking.md
- https://raw.githubusercontent.com/numerai/docs/master/numerai-tournament/atomic-blockchain-staking.md
- https://raw.githubusercontent.com/verialabs/ctf-agent/main/README.md

SNIPPET (from search summaries):
- Kaggle rules pages: https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/rules ; https://www.kaggle.com/competitions/titanic/rules ; https://www.kaggle.com/competitions/pokemon-tcg-ai-battle-challenge-strategy/rules ; https://www.kaggle.com/competitions/gemma-4-developer-agent
- NVIDIA blog: https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/
- AIRA₃: https://alphasignal.ai/news/meta-s-aira3-beats-4-000-human-teams-to-win-kaggle-gold ; https://x.com/AIatMeta/status/2096271545589190927
- NeuroGolf: https://quantumzeitgeist.com/kaggle-agents-solved-puzzles-winning/
- Disarray: https://artificialintelligencedynamics.com/2026/04/09/disarray-ai-agent-wins-28-medals-in-kaggle-competitions/
- Gemma 4 agent prizes: https://aiwiki.ai/wiki/gemma_4_developer_agent_competition
- Enveda CASMI26: https://secure.businesswire.com/news/home/20260915334355/en/
- ARC Prize: https://arcprize.org/competitions/2026 ; https://arcprize.org/competitions/2026/arc-agi-3 ; https://arcprize.org/competitions/2026/arc-agi-2
- AIMO3: https://penelopefitdatascientist.substack.com/p/this-2m-data-competition-might-be
- DrivenData eligibility: https://community.drivendata.org/t/prize-eligibility/7553
- Zindi: https://zindi.africa/rules ; https://www.zindi.africa/terms ; https://zindi.africa/blog/announcement-important-updates-to-zindis-rules-and-submission-guidelines
- AIcrowd ARC white-box: https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026 ; https://discourse.aicrowd.com/t/phase-2-of-the-arc-white-box-estimation-challenge-is-live/18197 ; https://discourse.aicrowd.com/t/townhall-summary-recording/18078
- NeurIPS 2026 competitions: https://blog.neurips.cc/2026/07/28/neurips-2026-competitions-announced/
- Topcoder: https://internshala.com/competitions/topcoder-marathon-match-tournament-2026-dates-eligibility/ ; https://www.topcoder.com/marathon-match-tournament/overview
- AtCoder: https://info.atcoder.jp/entry/ahc-llm-rules-en ; https://atcoder.jp/posts/ahc_new_ai_rule_en
- Sakana AHC058: https://jp.linkedin.com/in/takiba
- Codeforces: https://codeforces.com/blog/entry/133941
- Advent of Code 2025: https://thenewstack.io/2025s-advent-of-code-event-chooses-tradition-over-ai/
- Devpost/MLH: https://guide.mlh.io/general-information/judging-and-submissions/rules-for-your-hackathon ; https://discuss.ai.google.dev/t/number-of-submissions/36381
- HeroX: https://www.herox.com/blog/878-your-guide-to-being-a-herox-innovator
- Hugging Face Build Small: https://huggingface.co/organizations/build-small-hackathon
- Optimism: https://l2beat.com/publications/governance-review-81 ; https://gov.optimism.io/t/budget-board-proposal-for-retro-funding-for-season-8/10097
- Gitcoin: https://gov.gitcoin.co/t/gitcoin-2026-strategy-tl-dr/25049 ; https://gitcoin.co/case-studies/gg24-first-funding-round-of-gitcoin-3-0
- GJOpen: https://goodjudgment.com/services/good-judgment-open/
- Metaculus AIB: https://www.metaculus.com/aib/ ; https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament
- Prophet Arena: https://cfn.uchicago.edu/news/breaking-new-ground-in-machine-learning-and-ai-new-platform-prophet-arena-redefines-how-we-evaluate-ais-intelligence/
- Numerai: https://blog.numer.ai/numercon-2026-genesis-to-singularity/ ; https://decrypt.co/373781 ; https://yellow.com/asset/nmr
- CrunchDAO: https://docs.crunchdao.com/competitions/competitions/datacrunch-2 ; https://docs.crunchdao.com/competitions/faqs/prize-winners ; https://docs.crunchdao.com/competitions/competitions/structural-break-real-time ; https://forum.crunchdao.com/t/2026-w14-datacrunch-2-payouts/1130 ; https://protocol.crunchdao.com/core-concepts/crunch-lifecycle ; https://x.com/adia_lab/status/2044783760626110792
- CTF: https://arxiv.org/pdf/2512.02654 ; https://cybercup.ai/autonomous-ai-agent-ctf-competition ; https://csaw.io/competition/llm-ctf-attack-competition ; https://pwnsec.ctf.ae/ ; https://www.techtimes.com/articles/323346/20260806/def-con-34-opens-today-ai-agents-graduate-novelty-standard-hacking-weapon.htm
