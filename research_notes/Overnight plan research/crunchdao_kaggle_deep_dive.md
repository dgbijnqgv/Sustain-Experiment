# CrunchDAO and Kaggle deep dive: is it feasible for an autonomous coding agent?

Research date: 2026-10-08. Researcher: Claude (subagent). This file extends `other_prize_competitions.md` §1 and §14, and corrects two things in it (see §0).

**Agent profile.** Claude Code or Codex on a subscription. A cloud container with Python, about 4 vCPU and 16 GB RAM, and no GPU. GitHub Actions. Free Kaggle notebooks. The owner does one-time registration and KYC only.

**Labels**
- **VERIFIED**: I read the primary text myself. This includes code and READMEs cloned from github.com/crunchdao, and a copy of the Kaggle competition page that a participant committed to GitHub.
- **SNIPPET**: a WebSearch summary of the cited URL. I did not open the page. docs.crunchdao.com, forum.crunchdao.com, hub.crunchdao.com, kaggle.com, aiwiki.ai and github.io are all EGRESS_BLOCKED from this container.
- **ESTIMATE / INFERENCE**: my own reasoning.

---

## 0. Corrections and new hard facts (read first)

1. **The DataCrunch 2 payout curve is far steeper than "exponential by rank".** VERIFIED from `competitions/datacrunch-2/scoring/reward.py`:
   - Anyone at or below the median percentile gets **$0**.
   - Anyone above the median gets weight `(2*(pct-0.5))**20`, normalised over the granted amount.
   - My simulation of 1,000 USDC/week (ESTIMATE from the VERIFIED formula):

     | Active models | 1st | 5th | 10th | 20th | 90th percentile | 80th percentile | Paid ≥ $1 | Top-10 share |
     |---|---|---|---|---|---|---|---|---|
     | 100 | $343 | $65 | $6.5 | $0.02 | | | | 99% |
     | 200 | $189 | $84 | $29 | $2.8 | $2.8 | $0.01 | 24 models | |
     | 400 | $100 | $67 | $40 | $13.5 | $1.3 | | 42 models | |
     | 800 | $51 | | $32 | $19 | $0.63 | | 72 models | |

   - **In practice only about the top 5–10% earn anything meaningful.**
2. **The metric is Pearson, not Spearman.** VERIFIED from `scoring/scoring.py`:
   - It computes the per-moon Pearson correlation of `prediction` against `target`, which is the 4-week, 28-day compounded return.
   - It returns the **last moon's** correlation as the score (`pearson.iloc[-1]`).
   - Older docs saying "Spearman" refer to the legacy DataCrunch.
3. **This container cannot reach the CrunchDAO or Kaggle APIs.** VERIFIED: `api.hub.crunchdao.com`, `hub.crunchdao.com` and `www.kaggle.com` all return "CONNECT tunnel failed, 403". pypi.org and github.com work.
   - **Workaround:** run `crunch push` and `kaggle ...` from GitHub Actions, which has open egress.
   - **Alternative:** the owner adds the hosts under Allowed domains in the environment's Network access settings:
     - `api.hub.crunchdao.com`
     - `hub.crunchdao.com`
     - `competitions.cache.crunchdao.com`
     - the data-storage host
     - `www.kaggle.com`
     - `storage.googleapis.com`
4. The prior file called "Build Coding Agents with Gemma 4" a measurable competition. That is **confirmed**. It is a leaderboard competition, **not** human-judged. The separate **paper track** ($35k) **is** human-judged.

---

## 1. CrunchDAO

### 1.1 DataCrunch 2: Predict cross-sectional equity returns

**What is predicted (VERIFIED, quickstarter notebook `competitions/datacrunch-2/quickstarters/quickstarter/quickstarter.ipynb`)**
- Each row is a stock at a "moon". Moons are weekly. The universe is "a subset of the Russell 3000" and the features are anonymised (`Feature_*`).
- The `target` is "based on 28 days (4 moons) compounded returns".
- The output is a DataFrame of `id, moon, prediction`. The checker requires float predictions in [-10, 10] with no NaN or inf (VERIFIED, scoring.py). The notebook text says [-1, 1].

**Code runs on their servers (VERIFIED, `scoring/runner.py`)**
- The participant provides `train(X_train, y_train, model_directory_path)` and `infer(X_test, model_directory_path) -> DataFrame`.
- Crunch's runner loops over moons and retrains every `train_frequency` moons, with a 4-moon `EMBARGO` between training data and the predicted moon.
- The runner aborts if the projected time exceeds `remaining_duration_before_timeout`.
- Data splits are `reduced_local` (local test), `reduced_cloud` (the submission-phase check) and `oos_private` plus `live_to_predict` (live).

**Submission method (VERIFIED, crunch-cli README and source, crunch-cli v12.1.0, last commit 2026-10-01)**
- `pip install crunch-cli`
- `crunch setup-notebook datacrunch-2 --token <clone token>` (or `crunch setup`). The token is copied once from the hub's Submit page.
- `crunch download`, then `crunch test` (a local replica of the runner, including a determinism check).
- `crunch push -m "msg"`. This uploads code, the `resources/` model directory and the pip-freeze, and prints the dashboard URL.
- Notebooks are auto-converted (`crunch convert`).
- **Fully scriptable, so an agent can drive it from GitHub Actions.**
- I found no CLI command that starts or selects a cloud run. The API client only has `list_runs` / `get_run`. INFERENCE: choosing which submission is live, or clicking "run", may need the web hub, i.e. the owner or a browser session. Check this on first use.
- Some competitions, "like DataCrunch 2", terminate still-running runs when the Submission Phase ends and give no grace period (SNIPPET, docs.crunchdao.com/competitions/participate).

**Cadence**
- The legacy DataCrunch submission window was Friday 20:00 UTC to Tuesday 12:00 UTC weekly (SNIPPET, docs.crunchdao.com/competitions/competitions/datacrunch-competition).
- Out-of-sample scores resolve after about 5 weeks (SNIPPET, forum.crunchdao.com/t/.../1129).
- The first OOS leaderboard was in 2026-W07 (SNIPPET, forum.crunchdao.com/t/2026-w07-datacrunch-2s-first-leaderboard/1112).

**Compute**
- "10 hours of GPU or CPU compute time per week" on Crunch infrastructure (SNIPPET, DataCrunch docs; the Rally variant gets 20h in the scoring phase).
- Exact DataCrunch 2 numbers are on its docs page, which I could not open.

**Prize**
- "DataCrunch is distributing 1,000 USDC every weeks" (SNIPPET, docs.crunchdao.com/competitions/competitions/datacrunch-2, recorded in the earlier session). This is consistent with the $52,000 listed by mlcontests (VERIFIED dataset) = 52 × 1,000.
- The hub listing also shows "30k $USDC" (SNIPPET).
- Payouts are **batched monthly or later**:
  - "sent both February and March payouts" (2026-W14, SNIPPET, forum t/1130).
  - "datacrunch-2 Sent June's payout" (2026-W27, SNIPPET, forum t/1170).
- The mlcontests listing has an end date of 2026-12-31, so the pool may not extend into 2027 (INFERENCE).

**Participants**
- I found no current count for DataCrunch 2.
- Legacy DataCrunch claimed thousands of registered users. One participant showed a rank of "125/4407" (undated, SNIPPET).
- CrunchDAO claims "3,400 data scientists rewarded" (SNIPPET).
- Active weekly models in DataCrunch 2 are unknown. I assume 150–500 for the EV below (ESTIMATE).

**Teams and accounts**
- Team reward = the best member model's reward split equally (SNIPPET, docs.crunchdao.com/competitions/teams/rewards).
- KYC "helps deter people running multiple accounts" (SNIPPET, prize-winners FAQ). Treat the rule as one account per person.

**KYC and payout (SNIPPET, docs.crunchdao.com/competitions/faqs/prize-winners)**
- Prizes go to a Solana wallet managed by Privy.io, embedded in the hub account. Only the winner can access it.
- Crunch covers the transfer fee. 2FA is required to export the private key.
- Winners of *major* competitions get a KYC email: "Refusing to comply is the same as refusing your prize."
- The wallet moved from Ethereum to Solana (SNIPPET, changelog).

**Eligibility and countries**
- I found no CrunchDAO country clause (SNIPPET search was negative). An older tournament excluded sanctioned jurisdictions (SNIPPET, prior file).
- Assume OFAC-sanctioned places are excluded (INFERENCE).

**Capital or stake**
- **None.** There is no staking mechanism in the DataCrunch 2 code or the docs. The reward depends only on the metric rank (VERIFIED, reward.py).

**AI and automation rules**
- None found. Code must be deterministic (VERIFIED: `crunch test` has a determinism check; the docs say non-deterministic entries are ineligible, SNIPPET).
- Using an LLM agent to write the model is not restricted anywhere I could find.

**Tax and legal of USDC receipt (general knowledge, INFERENCE)**
- In most jurisdictions (US, UK, AU, EU) prize or reward tokens are ordinary or miscellaneous income at fair market value on receipt. USDC is roughly $1, so the accounting is simple.
- Converting USDC to fiat needs an exchange account (Coinbase, Kraken, etc.) with its own KYC. Selling USDC near par gives roughly zero capital gain, but it is still a reportable disposal in some countries (UK, AU).
- Keep the wallet transaction history. See `owner_side_risks_tax_payouts.md`.

### 1.2 Other CrunchDAO competitions (status as of 2026-10-08)

Last-commit dates are from the cloned `crunchdao/competitions` repo (VERIFIED).

| Competition | Status | Prize / mechanics | Fit |
|---|---|---|---|
| **ADIA Lab Structural Break Real-Time** | Submissions closed 2026-10-01; winners at the ADIA symposium 26–28 Oct (SNIPPET, adialab.ae, docs) | $100k | Closed |
| **Structural Break Open Benchmark** (ADIA × Crunch) | Continuous; quarterly OOS scoring; the first payout was 2026-03-31 (SNIPPET, x.com/adia_lab) | $6,000 per quarter to the top 3 | Possible but top-3 only; the field includes the original top-10 reference models |
| **Numinous** (Bittensor SN6) | Real-time, ongoing | Phase 2 pool "$5,000 USDC", rewards computed every Monday (SNIPPET, docs) | See below |
| **Synth** | Real-time, ongoing (repo `crunchdao/crunch-synth`) | Prize unverified: "$30k over 4 months" (SNIPPET, third party) | Probabilistic 24h price paths for BTC/ETH/SOL/etc., scored by CRPS. Feasible on CPU |
| Broad Obesity 3 | In wet-lab evaluation; results Fall 2026 (SNIPPET) | Top-10 above a threshold | Closed to new entries |
| Falcon, Mid+One, VC Portfolio, DataCrunch Rally | Ended (repos idle since Dec 2025 / Jan 2026) | | Closed |

**Numinous (VERIFIED, `crunchdao/crunch-numinous` README)**
- Predict P(Yes) for Polymarket-sourced binary events.
- Score: Brier score (60% global, 25% geopolitics) plus 10% **LLM-graded reasoning**.
- The model has no internet. All calls go via the gateway, which proxies OpenAI, OpenRouter, Perplexity, Chutes and others, and **you supply your own API keys**.
- Only the SIGNAL track is available on Crunch.
- **This overlaps the Metaculus bot almost exactly.** The catch is that inference needs paid or free-tier LLM API keys; the Claude or Codex subscription cannot be used inside their runner.
- On the protocol side "200+ agents compete on Numinous daily" (SNIPPET, openbb.co).

---

## 2. Kaggle

### 2.1 Platform rules relevant to an agent
- **Account.** One account per person: "You will be disqualified if you make Submissions through more than one Kaggle account, or attempt to falsify an account to act as your proxy" (SNIPPET, ARC-AGI-3 rules). The agent must operate the owner's account via the API token.
- **Phone verification** is mandatory (SNIPPET, Kaggle Learn FAQ).
- **Accepting each competition's rules** must be done by the logged-in human in a browser before the API can download or submit (VERIFIED, participant README github.com/Isaackjoshua/casmi-2026). **This is a recurring ~2-minute owner action per competition.**
- **AI tooling.** There is no platform-wide ban.
  - The AMLT clause allows automated ML tools if properly licensed (SNIPPET, multiple rules pages).
  - I recall a standard "External Data and Tools" clause: tools must be "reasonably accessible to all" and of "minimal cost", with a small LLM subscription given as acceptable (MEMORY, not re-verified this session).
- **External LLM APIs during development.** Using Claude or Codex to *write* code is not restricted in any rule found. Inference in code competitions runs with **internet off** (VERIFIED for CASMI26 and the Gemma 4 harness copy), so API LLMs cannot be used at scoring.
- **Winners.** They must deliver code and documentation under the winner licence, often open source (SNIPPET). Some hosts add an interview (ARC). Tax forms (W-9/W-8BEN) are required.
- **Prize eligibility.** Excludes sanctioned countries. Some sponsors restrict further.

### 2.2 The two cited competitions

**A. Enveda CASMI 2026: Molecule ID From Mass Spectra.** URL: https://www.kaggle.com/competitions/enveda-CASMI26-molecule-id-mass-spectra

| Item | Detail | Source |
|---|---|---|
| Task | Up to 25 ranked SMILES per `molecule_id` from LC-MS/MS (timsTOF) spectra | VERIFIED, participant READMEs |
| Metric | MRR@25, matched on tautomer-canonical InChIKey first block (connectivity only) | VERIFIED, participant READMEs |
| Timeline | Start 2026-09-14; entry and team-merger deadline **2026-12-07**; final **2026-12-14** | VERIFIED, participant READMEs |
| Prizes | **$50k to the top 5: 1st $16k … 5th $6k** | VERIFIED-ish (participant docs/COMPETITION.md) + SNIPPET (Enveda press release) |
| Format | Code competition: notebook ≤9h CPU/GPU, **internet disabled**; 5 subs/day; 2 final picks | VERIFIED via participant docs |
| External data | "Freely and publicly available external data and pre-trained models are allowed" | VERIFIED via participant docs/COMPETITION.md |
| Data licence | CC BY-NC 4.0 | SNIPPET |
| Field | 535 teams by 2026-09-17; the Kaggle page later showed **9,132 entrants**, 34,724 submissions | VERIFIED log in shiferaxa/casmi26 docs/plan.md; SNIPPET for the later numbers |

**Leaderboard state (VERIFIED, shiferaxa/casmi26 docs/plan.md log, 2026-09-17).**
- On 2026-09-17 the top 5 were all at 0.339–0.347, rank 50 at 0.335, and the median at 0.205. All of the top 50 were forks of one public notebook by prvsiyan/haideptry.
- The public LB has only 133 molecules, so noise is about 0.006.
- A Claude-assisted participant (Isaackjoshua) reached 0.245 after 6 phases, including a 94M-structure PubChem pool and a transformer.

**Compute fit.**
- The winning recipe is a fingerprint-prediction model plus candidate retrieval plus a learned ranker. Training the spectrum-to-fingerprint transformer on about 2.5M spectra wants a GPU, for which 30 free Kaggle hours a week is enough for modest models.
- Inference runs in about 35–55 min on T4s.
- An agent can fork the public 0.34 pipeline easily. Breaking away from the cluster to the top 5 needs real domain innovation.

**Verdict.** It is a realistic medal attempt, but a cash place (top 5 of thousands) is unlikely. ESTIMATE: P(top 5) ≈ 0.5–1%, so EV ≈ $50–150 total.

**B. "Build Coding Agents with Gemma 4" = Google – The Gemma 4 Developer Agent Competition.** URL: https://www.kaggle.com/competitions/gemma-4-developer-agent. The facts below are VERIFIED from a copy of the Kaggle overview page committed at github.com/rishaviitd/kaggle.gemma.coding.agent `context/overview.md` and `context/harness.md`.

- **Type.** A featured **prediction** competition. It is **not judged by humans**. The score is SWE-bench-style PASS/FAIL resolution rate on about 120 hidden tasks from private repos (public/private LB split).
- **Submission.** `submission.zip` containing:
  - `agent.yaml` (Google ADK Agent Config, declarative only)
  - prompts, sub-agents, and skills (scripts run in the sandbox)
  - optional **PEFT LoRA adapters** (.safetensors, rank ≤128, ≤3 GiB total)
- **Model.** The model is fixed to `gemma-4-31b-it-qat-w4a16-ct`.
- **Evaluation hardware.** 4× L4 GPUs. The context limit is 32,768 tokens. The agent has a 12-hour budget for all tasks.
- **Timeline.**
  - Start 2026-09-23.
  - Optional paper 2026-11-12.
  - Entry and team-merger deadline **2026-11-25**.
  - Final **2026-12-02**.
- **Prizes.** $37k / $18k / $10k (top 3 only).
- **Field.** About 3 days in: 4,635 entrants, 455 teams, 837 submissions.
- **Paper Track (separate competition).** $35k: $15k for best paper, $10k for best new resource and $10k for best new application.
  - It is **human-judged** on novelty, quality, relevance, verifiability and clarity.
  - The limit is ≤3,000 words via a Kaggle Writeup, due **2026-11-12** (SNIPPET, aiwiki.ai, consistent with the VERIFIED overview).
- **Compute fit for our agent.**
  - Iterating on prompts, skills and sub-agents needs Gemma-4-31B inference (Google AI Studio/OpenRouter API or a Kaggle GPU notebook) plus the Docker harness, which GitHub Actions can provide.
  - LoRA/RL post-training, which is the obvious path to the top 3, needs real GPU hours that we don't have.
  - Data: 129 public training tasks.

**Verdict.** A config-only entry is feasible, but top 3 of hundreds of teams, many with GPUs, is unlikely. ESTIMATE: P(top 3) ≈ 0.3–1%, so EV ≈ $100–300. The paper track is a long shot: three awards, human judges, and it would need genuinely novel results.

### 2.3 Other Kaggle prize competitions, Oct 2026 – Mar 2027

| Deadline | Prize | Competition | Fit for a CPU/limited-GPU agent | Source |
|---|---|---|---|---|
| 2026-10-22 | $77k | RSNA Knee Abnormality Detection | Too late; imaging, GPU-heavy | VERIFIED dataset |
| 2026-10-26 (entry) / 11-02 | $700k / $850k | ARC Prize 2026 AGI-2 / AGI-3 | Elite-only | VERIFIED dataset; SNIPPET |
| 2026-11-09 | $450k | ARC Paper Track | Judged, elite | VERIFIED dataset |
| 2026-11-12 | $35k | Gemma 4 Developer Agent Paper Track | Judged | VERIFIED overview |
| 2026-12-02 | $65k | Gemma 4 Developer Agent | See above | VERIFIED |
| 2026-12-14 | $50k | Enveda CASMI26 | See above | VERIFIED |
| ~2027-01-06 (unverified) | $100k | NFL Big Data Bowl 2027 | Analytics write-up **judged by NFL analysts**; 3 tracks × finalists $10k/runners-up $5k | SNIPPET, rules page + participant repos |
| ? | ~$3–3.7k | IEEE Big Data Cup 2026 Traffic Flow Bench | Forecasting, CPU-friendly, small prize | SNIPPET |
| ? | $10k per track | CUHK-X (UbiComp) | Sensor/HAR | SNIPPET |
| Oct 31 | none | Playground Series (monthly tabular) | No cash; practice only | SNIPPET |

**Further Q4/Q1 launches are likely.** In 2025 Kaggle ran 68 competitions with $3.67M in prizes (SNIPPET), and in 2026 about 34 with $6.4M (VERIFIED dataset). That is roughly 1–3 new featured or research competitions a month, typically $50–100k with the top 3–5 paid (INFERENCE). Most are GPU-heavy (vision, LLM, audio). Tabular or time-series ones with cash appear only a few times a year.

### 2.4 Kaggle tooling from this environment
- The Kaggle CLI (`kaggle kernels push`, `kaggle competitions submit -k user/kernel -v N -f submission.csv`) works from GitHub Actions. kaggle.com is blocked from this container.
- Free Kaggle GPU is about 30h a week (T4×2/P100) (SNIPPET).
- The agent cannot run Claude inside Kaggle notebooks. The loop is: write code in the container, push via Actions, run the notebook on Kaggle, read the logs back.

---

## 3. Expected value (ESTIMATE) and owner involvement

### DataCrunch 2
- **Pure-luck baseline.** With N active models and rank independent of skill, EV per week = $1,000/N. For N = 150–500 that is **$2–7 a week**.
- **Skill effect.** A competent GBDT or linear ensemble on anonymised features with realistic 1-week Pearson noise is only modestly better than random week to week. Per-week correlation of rank is low, so the multiplier is about 1–2×.
- **Monthly EV.** About **$8–50 a month, central ~$20**. This is high-variance: most weeks $0, an occasional $50–300 week.
  - This is lower than the prior file's $20–150, because of the median cut-off and the power-20 curve.
  - If the leaderboard metric is a multi-week average (unverified), rank becomes persistent. A non-elite model would then sit near $0 and only genuinely top-5% models earn.
- **Ends 2026-12-31 unless renewed.**
- **Owner involvement.**
  - One-time: hub signup (Privy email login), copying the clone token, maybe clicking "run/select submission" on the hub, and enabling 2FA.
  - When paid: possible KYC, and an exchange account to off-ramp USDC.
  - Ongoing: none, if the deployed model reruns weekly.
- **Agent effort.** Low. One model, automatic weekly reruns, occasional retraining.

### Other CrunchDAO
- Numinous: shares the Metaculus code path, but needs your own LLM API keys and gives a $5k pool split among 200+ agents. Weekly EV is likely only a few dollars.
- Synth: CRPS on crypto/equity paths. Prize unverified.
- Structural Break Open Benchmark: $6k per quarter to the top 3 only.
- Combined EV for a non-elite agent: **$0–30 a month**.

### Kaggle
- **This window.** CASMI26 EV is about $50–150. Gemma agent EV is about $100–300. Together that is about $150–450 over Oct–Dec. Averaged over 3 months, **$50–150 a month**, with ≥95% probability of $0 cash.
- **Medals.** These have reputational value only.
- **Later (2027).** About 1–2 suitable competitions a month gives **$50–200 a month EV**, very lumpy.
- **Owner involvement.**
  - Account creation and phone verification.
  - API token.
  - **Accepting the rules in a browser for every competition**.
  - On a win: tax form, licence and code release, writeup, possible host call or interview, and bank details.
  - Kaggle prizes are US-source, so withholding may apply for non-US owners (see `owner_side_risks_tax_payouts.md`).

---

## 4. Sources
- VERIFIED (github):
  - https://github.com/crunchdao/competitions: `competitions/datacrunch-2/scoring/{reward,scoring,runner}.py`, quickstarter notebook; last commit 2026-09-28.
  - https://github.com/crunchdao/crunch-cli: README and `crunch/cli.py`, `crunch/api/_domain/run.py`, `crunch/command/push/__init__.py`; v12.1.0, 2026-10-01.
  - https://github.com/crunchdao/crunch-numinous (README)
  - https://github.com/crunchdao/crunch-synth (README)
  - https://github.com/rishaviitd/kaggle.gemma.coding.agent: README, `context/overview.md` (Kaggle page copy), `context/harness.md`
  - https://github.com/shiferaxa/casmi26: README, `docs/plan.md`
  - https://github.com/Isaackjoshua/casmi-2026 (README)
  - https://github.com/OfficialBhattacharya/kaggle_CASMI_2026: `docs/COMPETITION.md`
  - https://raw.githubusercontent.com/mlcontests/mlcontests.github.io/master/competitions.json (fetched 2026-10-08)
- SNIPPET:
  - docs.crunchdao.com: competitions/datacrunch-2, datacrunch-competition, participate, faqs/prize-winners, teams/rewards, real-time-competitions/numinous, synth, structural-break-real-time
  - forum.crunchdao.com: t/1112, t/1129, t/1130, t/1170, t/1058
  - x.com/crunchDAO; x.com/adia_lab/status/2044783760626110792; adialab.ae/structural-break-open-benchmark
  - openbb.co/blog/numinous-…; alphanova.tech/blog/crunch-dao-explained
  - kaggle.com/competitions/enveda-CASMI26-molecule-id-mass-spectra; kaggle.com/competitions/gemma-4-developer-agent(-paper); aiwiki.ai/wiki/gemma_4_developer_agent_competition
  - kaggle.com/competitions/nfl-big-data-bowl-2027/rules; kaggle.com/competitions/arc-prize-2026-arc-agi-3/rules
  - Enveda press release (finance.yahoo.com / businesswire)
