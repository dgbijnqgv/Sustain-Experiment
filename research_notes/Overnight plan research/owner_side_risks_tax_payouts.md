# Owner-side practicalities: payouts, tax, account risk, owner time, plan counterfactual

Research date: 2026-10-08. Scope: an individual owner (country unknown, email-only identity) whose AI agents try to earn via (1) Metaculus FutureEval bot-tournament prizes, (2) Apify Store payouts, (3) Kaggle or similar competition prizes.

**NOT TAX OR LEGAL ADVICE.** These are high-level research notes for planning. Rules depend on residence, facts and treaty wording; a local adviser should confirm anything before money moves.

## Evidence labels

- **VERIFIED**: I fetched the primary page in this session and read the quoted text.
- **SNIPPET**: from search-result summaries, secondary sites or vendor blogs. The primary page was blocked (metaculus.com, docs.apify.com, support.ramp.com, wise.com, paypal.com, openai.com and developers.openai.com were all egress-blocked) or wasn't found.
- **REPO-C**: a third-party GitHub file, fetched raw.
- **INFERENCE**: my reasoning or general knowledge, not from a fetched source.

---

## 1. Payout rails

### 1a. Metaculus (FutureEval bot tournaments)

| Claim | Label | Source |
|---|---|---|
| Winners provide eligibility certifications or proof of identity, US tax forms ("IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident"), and payment details, which may go to Metaculus or "via a third-party service as instructed by Metaculus". "Taxes and fees are paid by recipients." | SNIPPET | https://www.metaculus.com/tournament-rules/ (blocked; seen via search 2026-10-08) |
| Metaculus "cannot send monetary prizes, cash equivalents, or physical prizes to individuals located in countries subject to U.S. sanctions or export restrictions". Those participants may still compete for rankings and medals. | SNIPPET | same |
| FutureEval-specific rules: 18+; residents of Cuba, Iran, Syria, North Korea, Russia and Crimea/Donetsk/Luhansk excluded; winners "will be required to verify their identity, nationality, and residency"; prizes are paid only after all bot-maker surveys are in; prizes unclaimed after 30 days may be forfeited; **"Bank transfer through Ramp; country must be on Ramp's supported list."** | REPO-C | https://raw.githubusercontent.com/Bowen1314/metaculus-bot/main/RESEARCH.md (fetched 2026-10-08) |
| No independent source found that says Metaculus uses Ramp. The Ramp detail rests only on the REPO-C file above, so treat it as "reported". | (gap) | searches 2026-10-08 |
| RAND x Metaculus rules: "Payouts may be in cash or cash-equivalents (e.g., prepaid virtual cards or similar), at Metaculus's discretion." | SNIPPET | https://www.metaculus.com/rand/contest-rules/ |
| Metaculus is a US public benefit corporation (Metaculus Inc.), HQ in California (Wikipedia says Santa Cruz; another wiki says Santa Monica). Delaware incorporation is unverified. | SNIPPET | https://en.wikipedia.org/wiki/Metaculus ; https://www.metaculus.com/news/2022/09/12/public-benefit/ |

**Ramp, the payer-side rail:**

- Ramp Bill Pay sends USD via SWIFT to a long alphabetical list of countries. Search summaries say **China and India are both on the USD SWIFT list**.
- Local-currency payouts (for example CNY or INR) are listed in one version of the help article but not the other.
- Ramp charges the *payer* $20 per SWIFT USD wire and doesn't charge the recipient. Intermediary and receiving banks may still deduct fees (typically $10–$30 on USD wires, INFERENCE). Payment usually arrives in 1–5 days.
- Ramp doesn't support choosing the intermediary bank.
- Ramp's card page excludes Cuba, Iran, North Korea, Syria, Russia and Ukraine/Crimea.
- Label: SNIPPET. Sources: https://support.ramp.com/hc/en-us/articles/10593954538259-International-transfers-on-Ramp-Bill-Pay ; https://support.ramp.com/limitations-for-international-bill-pay
- INFERENCE on FX: a USD SWIFT wire into a non-USD account gets converted by the receiving bank, often at 1–3% worse than mid-market. A USD account at the receiving bank, or Wise USD details, avoids this. Wise charges $6.11 per incoming USD wire (see 1c).

### 1b. Apify (Czech: Apify Technologies s.r.o., Prague, CZ VAT ID CZ04788290)

| Claim | Label | Source |
|---|---|---|
| Minimum payout is $20 for PayPal **and Wise** and $100 for other methods (bank wire), per current developer docs. An older help-center FAQ says PayPal $20 and wire $100. The "$100 Wise minimum" in the brief doesn't match Apify's dev docs; it matches Apify's *affiliate* program and Leanpub. Amounts under the minimum carry over to the next month. | SNIPPET | https://docs.apify.com/platform/actors/publishing/monetize/monthly-payouts ; https://help.apify.com/en/articles/10057167-how-developer-payouts-work |
| Invoice is generated on the 11th, with a 3-day review window, and auto-approved on the 14th. The help center says payment goes out on days 15–22. | SNIPPET | same |
| KYC is an AML requirement. For individuals, the name must exactly match the legal ID ("no nicknames or aliases"), and the ID needs a sharp photo; screenshots and paper copies are auto-rejected. Changing billing details (beyond the payment method) forces re-verification. If KYC isn't done by payout time, earnings roll over. | SNIPPET | same |
| Company details: Vodickova 704/36, Prague 1; company ID 04788290. | SNIPPET | https://docs.apify.com/legal |
| No Apify page found listing which countries PayPal/Wise payouts support, or how VAT and self-billing work for developer payouts. | (gap) | |

**PayPal (recipient side):**

- PayPal Payouts: the **sender pays** the payout fee and recipients pay no receiving fee. Currency conversion adds a spread; third parties estimate it at about 3–4% over wholesale.
- PayPal says **payouts that need currency conversion aren't available to China, India and Thailand**.
- Label: SNIPPET. Sources: https://developer.paypal.com/docs/payouts/standard/reference/faq ; https://developer.paypal.com/payouts/supported-features ; https://tipalti.com/payments-hub/paypal-international-transaction-fees/

**PayPal by country (all SNIPPET):**

- **China mainland:** individual accounts reportedly **cannot receive payments**; a business account is needed. Withdrawal to a mainland bank costs a flat $35 and takes 3–7 days. China's annual $50k personal FX quota is also relevant (INFERENCE). Sources: https://www.paypal.com/c2/webapps/mpp/using-paypal ; https://wise.com/en-cn/blog/paypal-in-china ; https://www.skydo.com/people-ask/does-paypal-work-in-china
- **India:** can receive international payments. Needs an RBI purpose code (for example P0802 for software services). Funds reportedly **auto-convert to INR and auto-withdraw** with no USD balance held. All-in cost per competitor blogs is about 4.4% + $0.30 + 3–4% FX + 18% GST on the fee. Treat these as possibly inflated; the sources sell competing services. A FIRA or bank advice is needed for records. Sources: https://www.xflowpay.com/blog/withdraw-money-from-paypal-india ; https://web.skydo.com/blog/paypal-in-india-charges-review-alternatives
- **Hong Kong:** withdrawal to a local bank is free for HK$1,000 or more, otherwise HK$3.50. Source: https://www.paypal.com/hk/webapps/mpp/paypal-fees (archived copy)
- **Taiwan:** withdrawal of TWD to E.SUN is free. USD to an E.SUN USD account costs 2.5%. Conversion costs 2.5–3%. Source: https://securepayments.paypal.com/tw/digital-wallet/paypal-consumer-fees
- **Singapore:** no personal fee data found. PayPal is generally fully available (INFERENCE).
- **US, EU and UK:** fully supported. Cost is mostly FX if the payout isn't in your currency (INFERENCE).

### 1c. Wise

- Wise USD account details are **not available** to residents of (per Wise help, SNIPPET): Afghanistan, Bangladesh, Belarus, Burundi, Cameroon, CAR, Chad, **China**, Rep. Congo, DR Congo, Cuba, Eritrea, Guinea-Bissau, Iran, Iraq, Libya, Myanmar, Nigeria, North Korea, Pakistan, Russia, Serbia, Somalia, South Sudan, Sri Lanka, Sudan, Syria, Türkiye, UAE, Ukraine, Venezuela, Yemen. The list as returned also included "Nevada", which looks like an error.
  - India: Wise *personal* USD details are restricted. Wise is generally not usable for receiving into an Indian personal account, though Wise Business India has limited support (INFERENCE; verify).
  - Source: https://www.wise.com/help/articles/2978028/how-do-i-open-account-details-to-receive-money
- Fees (SNIPPET): $6.11 per incoming USD wire, ACH receipts free, SWIFT receipt fees vary. Conversion runs about 0.4–0.6% for major currencies and about 2% for USD→INR (third-party estimate). Sources: https://wise.com/gateway/v1/us/disclosures/long-form ; https://www.wise.com/help/articles/2978013/what-are-the-fees-and-limits-for-receiving-money
- If you move to an unsupported country, your account details deactivate (SNIPPET).

### 1d. Kaggle and others

- Older Kaggle-hosted rules: winners may have to complete tax forms before receiving prizes, and Kaggle provides the forms. Label: SNIPPET. Source: https://www.soa.org/Files/programs/predictive-analytics/kaggle-contest-rules.pdf
- Residents of Cuba, Iran, Syria, North Korea and Sudan are reportedly barred from participating. Label: SNIPPET. Source: https://dcase.community/articles/dcase2019-challenge-task1-leaderboards-launched
- Some US-government-sponsored competitions restrict prizes to US citizens or permanent residents (America COMPETES Act). Label: SNIPPET. Source: https://undark.org/article/kaggle-data-science-dhs/
- One winner reported receiving about 70% of a prize under default W-8BEN handling, i.e. 30% withheld. Label: SNIPPET. Source: https://discourse.aicrowd.com/t/question-about-the-round-1-of-unity-s-obstacle-tower-challenge-email/974
- AIcrowd example: prize money won't be sent to Cuba, Iran, North Korea, Sudan, Syria, Russia, Crimea, Quebec, Brazil or Italy (competition-specific). Label: SNIPPET. Source: https://www.aicrowd.com/challenges/objde/challenge_rules
- INFERENCE: Kaggle prizes usually also require licensing the winning code (often open source) and a write-up or model documentation, which costs extra owner time.

### 1e. Summary matrix (INFERENCE built from the above)

| Jurisdiction | Metaculus (Ramp USD SWIFT) | Apify via PayPal ($20 min) | Apify via Wise ($20 min) | Apify via bank wire ($100 min) |
|---|---|---|---|---|
| US | OK (ACH/wire) | OK | OK | OK |
| EU / UK | OK; FX at bank | OK; about 3–4% FX unless held in USD | OK; best FX | OK |
| Singapore / Hong Kong | OK | OK | OK | OK |
| Taiwan | OK (USD account recommended) | OK; 2.5–3% FX/withdrawal | OK | OK |
| India | Listed as supported; FIRA/purpose code needed | Works but auto-INR, high all-in cost | Personal USD details restricted | Probably the best route (USD wire to bank; FEMA purpose code) |
| China mainland | Listed as supported; SAFE quota and declaration friction | **Personal accounts reportedly can't receive** | **Not available** | Possible; bank FX scrutiny |
| Sanctioned (CU/IR/KP/SY/RU/occupied UA) | **No prize** | No | No | No |

---

## 2. Tax (high level; NOT tax advice)

### 2a. US person

- **Prizes** (Metaculus, Kaggle) are taxable as ordinary "other income" (Form 1040, Schedule 1, line 8). This is general knowledge, consistent with IRS treatment of prizes.
  - Hobby-style prizes generally aren't subject to SE tax. SE tax can apply if competing is a trade or business (INFERENCE).
- **1099 thresholds (OBBBA):** 1099-MISC/NEC reporting rose from $600 to **$2,000 for payments made on or after 2026-01-01**, inflation-indexed from 2027. This covers 1099-MISC prizes (box 3). Backup-withholding threshold reportedly also $2,000. Label: SNIPPET. Sources: https://onpay.com/insights/1099-reporting-threshold-updates/ ; https://advertisinglaw.fkks.com/post/102kyn8/ ; https://beancount.io/blog/2026/07/19/obbba-1099-nec-misc-threshold-2000-small-business-guide
  - **Income is still taxable below the threshold.**
- **1099-K:** reverted to **more than $20,000 AND more than 200 transactions** (OBBBA §70432; IRS FS-2025-08). PayPal won't issue a 1099-K for small Apify payouts. Label: SNIPPET. Source: https://www.cpapracticeadvisor.com/2025/10/23/irs-issues-new-faqs-on-20000-form-1099-k-threshold-under-obbba/171575/
- **Apify income:**
  - It's selling software/services, so it's self-employment income: Schedule C plus Schedule SE (INFERENCE, standard treatment).
  - SE tax is 15.3% (12.4% Social Security + 2.9% Medicare) on 92.35% of net profit. It's owed when net SE earnings reach $400 or more (about $433 of Schedule C profit). The 2026 Social Security wage base is $184,500. Half of SE tax is deductible. Label: SNIPPET. Source: https://www.journalofaccountancy.com/news/2025/oct/social-security-wage-base-and-cola-announced-for-2026/
  - Apify is a foreign (Czech) payer, so it likely issues no 1099 and the owner self-reports (INFERENCE).
  - **Subscription costs used to build Actors (for example the Claude plan) may be partly deductible business expenses on Schedule C** if they're ordinary and necessary and allocated to business use. This is INFERENCE and worth checking, because it changes the counterfactual.
  - Quarterly estimated tax is only relevant if you'd owe $1,000 or more at filing (INFERENCE).

### 2b. Non-US person: US-source prizes (Metaculus Inc., Kaggle/Google LLC)

- A US payer paying a nonresident alien a prize generally **withholds 30%** under §1441 and reports it on **Form 1042-S**, unless a valid W-8BEN claims a treaty rate. Without a W-8 on file, the default 30% applies. Label: SNIPPET. Sources: https://www.irs.gov/government-entities/indian-tribal-governments/powwow-prizes ; https://universityfinance.richmond.edu/payroll/international/prizes.html
- Prizes are generally sourced by the **payer's residence**, so a US payer makes them US-source. Label: SNIPPET. Source: university payroll guidance in search results.
- **Treaty relief** comes only through the treaty's "Other Income" article, and only when it gives exclusive taxing rights to the residence country. Several university payroll offices say treaty exemption is "not generally applicable" to prizes in practice. Label: SNIPPET.
  - OECD-style other-income articles (exclusive residence taxation) appear in many EU and UK treaties with the US. I couldn't verify the specific article text this session, so this is INFERENCE.
  - **US–India** (Art. 23) gives the source state taxing rights, so no relief: 30% likely stays. Label: SNIPPET. Source: https://sbsandco.com/blog/management-support-services-vis-a-vis-other-income-an-analysis-on-position-under-treaties
  - **US–China** (Art. 21/22): wording not verified.
  - **Singapore, Hong Kong and Taiwan have no comprehensive US income-tax treaty.** The US–Taiwan Expedited Double-Tax Relief Act passed the House 423-1 (Jan 2025) but is still in Senate Finance as of Sept 2026, so 30% applies with no treaty relief. Label: SNIPPET. Source: https://fapa.org/?p=24885 ; https://www.taxesforexpats.com/country-guides/taiwan/us-taiwan-tax-treaty.html
- Recovering over-withheld tax needs a **1040-NR** filing. For prizes of a few hundred dollars this is usually uneconomic (INFERENCE).
- **Practical:** for a non-treaty or source-taxing country, model Metaculus/Kaggle prizes as **70% of face value** before home-country tax and FX.

### 2c. Non-US person: Apify (Czech payer)

- No US withholding: it isn't a US payer (INFERENCE).
- Czech withholding on payments to non-resident individuals for software/services sold through a marketplace is unlikely, but I didn't verify it (gap).
- **EU owners:** the payout is B2B services income. In some states you may need to register a business, and possibly get a VAT ID for reverse charge when invoicing a Czech company. Check locally (INFERENCE).
- Apify may report seller income under EU DAC7. Unverified whether software sales fall within DAC7 "relevant activities" (gap).

### 2d. Does small foreign prize or side income have to be declared? (examples; verify locally)

- **UK:**
  - The £1,000 trading allowance applies to *gross* trading income across all side activities. Above it, register for Self Assessment; for 2026/27 the deadline is 5 Oct 2027.
  - Gambling and lottery wins are tax-free. Skill-competition prizes entered of your own accord *may* be treated as professional receipts (one HMRC letter c.2017).
  - Apify income is likely trading income.
  - Label: SNIPPET. Sources: https://www.bytestart.co.uk/self-employed-tax/trading-allowance/ ; https://www.christopherfielden.com/short-story-tips-and-writing-advice/are-writing-competition-prizes-taxable.php
- **Germany (EU example):**
  - A prize tied to a performance or work is taxable. Non-professional one-off "sonstige Einkünfte" have a **€256/yr Freigrenze** (all-or-nothing).
  - Prizes tied to a professional activity count as business income.
  - Regular Apify sales are likely gewerblich: register a Gewerbe; Kleinunternehmer VAT rules apply (INFERENCE).
  - Label: SNIPPET. Source: https://www.steuertipps.de/lexikon/p/preisgelder ; https://www.vlh.de/arbeiten-pendeln/beruf/preisgelder-im-amateursport-steuerfrei-oder-steuerpflichtig.html
- **Singapore:**
  - Gambling and lottery winnings aren't taxable (windfalls).
  - Awards tied to a trade or profession are taxable.
  - Foreign-sourced income received by individuals is generally exempt (general knowledge; confirm with IRAS).
  - Apify income from a Singapore-based activity is probably taxable trade income (INFERENCE).
  - Label: SNIPPET. Sources: https://www.iras.gov.sg/IRASHome/Individuals/Locals/Working-Out-Your-Taxes/What-is-Taxable-What-is-Not/Winnings--Toto--4D--etc--/ ; https://www.snpc.org.sg/2017/01/13/tax-treatment-of-sports-awards-2/
- **Hong Kong:**
  - The system is territorial. Salaries tax covers employment only. A non-employment prize is generally outside salaries tax.
  - Profits tax applies if you run a HK business; the source of the profits is the key question.
  - Label: SNIPPET. Source: https://kaizencpa.com/Knowledge/info/id/113.html
- **Taiwan:**
  - Regular income tax applies to Taiwan-source income. Foreign income counts only toward the **Basic Income Tax (AMT, 20%)**, and only when foreign income is TWD 1M or more and basic income is over about TWD 7.5M (individual vs household is unclear). Small foreign prizes are therefore effectively not taxed.
  - Domestic competition prizes are taxable as "competition/prize income".
  - Label: SNIPPET. Source: https://taxsummaries.pwc.com/taiwan/individual/taxes-on-personal-income ; https://kaizencpa.com/faq/info/id/852.html
- **India:**
  - Residents are taxed on worldwide income.
  - Winnings from "games of any sort" are taxed at a flat 30% plus 4% cess (31.2%) with no deductions (s.115BB; renumbered under the Income Tax Act 2025, effective 1 Apr 2026). Some advisers argue professional prize money is business income at slab rates instead.
  - A foreign tax credit for US withholding is possible (DTAA/FTC Form 67) (INFERENCE).
  - Apify income is export of services: slab rates or presumptive s.44ADA. GST registration is only needed above ₹20 lakh, and exports are zero-rated (INFERENCE).
  - Label: SNIPPET. Sources: https://www.incometaxindia.gov.in/w/section-115bb-39 ; https://www.businesstoday.in/amp/personal-finance/tax/story/how-worlds-youngest-chess-champion-d-gukeshs-rs1145-cr-prize-shrinks-by-rs4-cr-the-tax-math-explained-457680-2024-12-17
- **China mainland:**
  - Residents are taxed on worldwide income. Overseas income must be self-declared in the annual reconciliation (2025 tax year due **30 Jun 2026**).
  - A prize is likely "incidental income" at a flat 20%. Apify income is likely labour remuneration or business income.
  - **Enforcement has risen since late 2025**: the State Taxation Administration (STA) uses CRS data, and local bureaus are sending self-inspection notices for 2022–2024.
  - Label: SNIPPET. Sources: https://mobile.chinadaily.com.cn/html5/2026-01/20/content_013_696e8858ed50ccabe1520a9e.htm ; https://www.china-briefing.com/news/china-crs-tax-enforcement-compliance-tips/ ; https://www.caixinglobal.com/2026-01-17/china-limits-offshore-tax-push-to-recent-years-102404665.html

---

## 3. Account-risk register

Likelihood and impact are my judgements (INFERENCE), grounded in the cited terms.

| # | Risk | Evidence | Likelihood | Impact | Mitigations |
|---|---|---|---|---|---|
| A1 | **GitHub Actions: "unrelated activity" clause.** GitHub-hosted runners may not be used "for any activity unrelated to the production, testing, deployment, or publication of the software project associated with the repository". The terms also bar serverless or CDN-style use, cryptomining, and disproportionate server burden. Consequences: job termination, Actions restrictions, the repo disabled, or "in some cases, suspension or termination of your GitHub account". | VERIFIED: https://github.com/github/docs/blob/main/content/site-policy/github-terms/github-terms-for-additional-products-and-features.md | Low–medium. A cron bot that runs the repo's own code (for example a forecasting bot that *is* the project) is arguably "running the software project". Many Metaculus template bots use exactly this pattern via `metac-bot-template`. Heavy scraping or a long-running daemon raises the risk. | High: the GitHub account is the agent's whole workspace. | Keep the bot code *in* that repo and the job short and bounded (minutes, not hours). Don't scrape GitHub. Avoid many parallel repos running crons. Consider a separate GitHub account only if GitHub's ToS allows a machine account (one free machine account per person is allowed; INFERENCE, verify). Keep secrets in Actions secrets. |
| A2 | **GitHub Actions: schedule unreliability.** Public repos auto-disable scheduled workflows after **60 days of no repo activity**. Scheduled runs can be delayed or dropped under load. | VERIFIED: raw github/docs `events-that-trigger-workflows.md` (fetched 2026-10-08) | High (a certainty if the repo is idle) | Medium: missed forecasts lower the score. | The bot commits a heartbeat or log, or the owner re-enables the workflow. Monitor run status. Use a private repo (2,000 free min/month on the Free plan; INFERENCE) or a routine as backup. |
| A3 | **GitHub AUP: automated bulk or inauthentic activity** (spam PRs, automated starring, "excessive automated bulk activity"). | VERIFIED: raw `github-acceptable-use-policies.md` §4 | Low unless the agent spams issues or PRs (for example bounty hunting) | High | Never let the agent mass-open PRs or issues on others' repos. Rate-limit any outward-facing actions. |
| B1 | **Anthropic consumer terms: automated access.** Prohibited "to access the Services through automated or non-human means, whether through a bot, script, or otherwise" except via an API key "or where we otherwise explicitly permit it". Anthropic may suspend "at any time without notice". | VERIFIED: https://www.anthropic.com/legal/consumer-terms (effective 2025-10-08 version shown) | See B2/B3 | Very high: losing the plan stops all agent work, and appeals reportedly succeed rarely. Secondary claim: 1.7k of 52k appeals succeeded, H2-2025 (SNIPPET: https://autonomee.ai/blog/claude-code-account-suspended-banned-safe-usage/). | |
| B2 | **Claude Code routines, cloud sessions and `claude setup-token` CI tokens on a Pro/Max plan.** These are **first-party, documented** uses, i.e. "explicitly permitted". The routines docs say routines are "available on Pro, Max, Team, and Enterprise" and "draw down subscription usage the same way interactive sessions do". Hourly caps apply (100 scheduled runs/hr per account; 30/hr per routine for Run now/API). The minimum interval is 1 hour. Research preview. The authentication docs document `claude setup-token` as a 1-year OAuth token "for CI pipelines, scripts". The GitHub Actions docs support `CLAUDE_CODE_OAUTH_TOKEN` on Pro/Max. | VERIFIED: https://code.claude.com/docs/en/routines.md ; https://code.claude.com/docs/en/authentication.md ; https://code.claude.com/docs/en/github-actions.md | **Low** for the owner's own account running unmodified Claude Code on their own repos | Very high | Use only first-party surfaces (routines, cloud sessions, the Claude Code GitHub Action, `claude -p` with your own login). Don't share tokens or run for third parties. Stay within "ordinary, individual usage" (the legal page says advertised limits "assume ordinary, individual usage of Claude Code and the Agent SDK"). |
| B3 | **Claude subscription via third-party harnesses or SDK apps.** OAuth from Free/Pro/Max is "designed to support ordinary use of Claude Code and other native Anthropic applications". Developers "should use API key authentication" and may not "route requests through Free, Pro, or Max plan credentials on behalf of their users". Enforcement can come "without prior notice". Technical blocking reportedly started 2026-01-09; terms and docs were clarified 2026-02-19/20 (OpenCode, OpenClaw and similar). | VERIFIED: https://code.claude.com/docs/en/legal-and-compliance ; SNIPPET: https://winbuzzer.com/2026/02/19/anthropic-bans-claude-subscription-oauth-in-third-party-apps-xcxwbn/ | **Medium–high** if the agent stack uses a non-Anthropic harness with a subscription token | Very high | Don't extract or reuse the OAuth token in custom scripts or other tools. Use a paid API key for any custom SDK app or for the Metaculus bot's own LLM calls; Metaculus also gives free OpenRouter credits. |
| B4 | **Headless `claude -p` from cron on a subscription.** This is a gray zone. A GitHub issue asking the docs to warn about bans (#36324, 2026-03-19) was **closed as not planned** with no visible staff answer. The docs advertise `claude -p` "for scripts and CI/CD", recommend `--bare` for scripts, and note `--bare` "doesn't use your subscription login". | VERIFIED: https://github.com/anthropics/claude-code/issues/36324 ; https://code.claude.com/docs/en/headless.md | Low–medium (my estimate). The official CI-token path exists, but volume or 24/7 patterns may trigger abuse heuristics. | Very high | Prefer routines (first-party scheduling) over self-hosted cron. Keep runs few and human-scale. Don't run multiple accounts (multi-account bans reported; SNIPPET: https://metricnexus.ai/blog/anthropic-banning-multiple-claude-accounts). |
| C1 | **OpenAI ChatGPT plan via Codex automation.** The consumer Terms forbid "Automatically or programmatically extract data or Output". Codex docs say API keys are "the right default for automation", and ChatGPT-managed auth in CI is an "advanced" path for trusted runners, with a warning: "Do not use this workflow for public or open-source repositories". Codex has first-party **Automations** (scheduled tasks) in the Codex/ChatGPT app. Plus has a 5-hour + weekly limit (5-hour cap restored 2026-08-25), shared with ChatGPT Work. No reports found of suspensions for `codex exec` cron. | SNIPPET: https://openai.com/policies/terms-of-use/ ; https://developers.openai.com/codex/noninteractive ; https://openai.com/academy/codex-automations/ ; https://pasqualepillitteri.it/en/news/12697/openai-5-hour-codex-chatgpt-work-limit-plus | Low for first-party Automations/cloud tasks. Low–medium for copying `auth.json` into GitHub Actions. | High (if the owner also relies on ChatGPT) | Use Codex Automations or cloud tasks rather than exported tokens. Never put `auth.json` in a public repo's CI. Use an API key for unattended CI. |
| D1 | **Apify KYC mismatch.** The name must exactly match the government ID (no aliases); screenshots and paper copies are auto-rejected; billing changes force re-KYC. Payouts roll over until it's fixed. An email-only identity has to become a legal-name identity, and the PayPal/Wise/bank account name should match the same legal name (INFERENCE; PayPal and Wise both do their own KYC). | SNIPPET: Apify docs above | Medium (first attempt) | Low–medium: a delay, not a loss, unless the account is closed for misrepresentation. | Use your legal name in Apify billing from day one. Use your own PayPal or Wise in the same name. Use a valid passport or ID photo. Don't use a business entity unless you actually have one. |
| D2 | **Metaculus KYC, residency and forfeiture.** Identity, nationality and residency are verified. Prizes go only to non-sanctioned residents. 30-day claim window; the prize is held until all bot surveys are in. The "one prize-eligible bot per person" rule means operating multiple bots or accounts under one identity risks disqualification. A for-profit entity with 3+ people gets no prize unless the bot is open-sourced. | REPO-C + SNIPPET | Low–medium | Medium (loss of the prize) | Register the bot under the owner's real identity. Fill in the bot-maker survey. Watch the email inbox (an agent can monitor it but can't sign). Keep the code inspectable. Never manually adjust live forecasts ("no human in the loop"). |
| D3 | **Tax-form errors.** A W-8BEN claiming an invalid treaty benefit, or a missing W-8, leads to 30% withholding or later IRS issues. A W-9 given by a non-US person is a false certification. | INFERENCE | Low | Medium | Fill W-8BEN Part II only when the treaty's other-income article clearly applies; otherwise accept 30%. |
| D4 | **Payment-rail freezes.** PayPal may hold or limit new accounts receiving business payments on a personal account. The Wise account deactivates if you move to an unsupported country. China/India FX controls apply. | SNIPPET (PayPal HK commercial vs personal; Wise help) | Low–medium | Low–medium | Pick the cheapest compliant rail per country (1e). Consider a PayPal Business account where personal accounts can't receive (China). |

---

## 4. Owner time cost (INFERENCE: my estimates, ranges for a first-timer)

| Item | One-time (h) | Ongoing |
|---|---|---|
| Metaculus account, bot account, participation form, credits request (+ AskNews email) | 0.5–1 | |
| Metaculus prize claim: KYC (ID + residency), W-9/W-8BEN, Ramp bank details, bot survey | 1–2 per claim season (+1–2 h the first time for a non-US person checking treaty eligibility) | about 1 h per season with a prize |
| Apify account, billing details, KYC upload, payout method | 1–2 (+1–3 if KYC is rejected) | invoice review on the 11th–14th (auto-approves): 0–10 min/month |
| PayPal or Wise account + their own KYC | 0.5–2 each | occasional re-verification |
| Agent infrastructure (repos, secrets, routines/CI tokens, Claude/OpenRouter keys) | 1–3 | 0.5–1 h/month fixing breakages, re-enabling workflows, reconnecting GitHub (routines pause if GitHub auth lapses, and turn off after 72 h) |
| Kaggle (phone verification; per-prize rules, code licence, write-up, tax forms) | 0.5 | 2–6 h per prize won |
| Bookkeeping (export statements, FX rates, receipts, cost allocation of the AI subscription) | 0.5 setup | 15–30 min/month |
| Annual tax filing, US person (Schedule 1 + C + SE; DIY software) | 2–4 the first year | 1–3 h/yr extra (or about $100–$300+ more to a preparer) |
| Annual tax filing, non-US (declare foreign income; claim FTC for US withholding) | 1–4 the first year | 1–3 h/yr. A 1040-NR refund claim is 5–10 h and usually not worth it under about $1k. |
| **Total** | **about 8–20 h in year 1** | **about 10–20 h/yr after that** (more if prizes recur) |

At a $100/month earning target, 15 h/year of owner time is about $80/h of owner time *if* the gross is realised. Each hour of owner time materially lowers the effective hourly rate if the earnings come in below target.

---

## 5. Counterfactual: Claude plan prices and Max 5x vs 20x

| Item | Label | Source |
|---|---|---|
| Pro is $20/month (or $17/month billed annually at $200). Max is "From $100", monthly billing only. | VERIFIED | https://claude.com/pricing (fetched 2026-10-08) |
| Max 5x is $100/month and Max 20x is $200/month (web prices; mobile may differ). Usage per 5-hour session is 5x or 20x Pro. Max has a weekly limit across all models (amount not published); Anthropic may add other caps. "Both tiers get priority access to new models, features, and products." The article lists **no feature differences between 5x and 20x other than usage capacity**. | VERIFIED | https://support.claude.com/en/articles/11049741-what-is-the-max-plan |
| Pricing page: Max (both tiers) adds higher output limits, priority access at high-traffic times and early access over Pro. Fable model: Pro gets it via usage credits; Max 5x and 20x get "50% of weekly limits". Claude Code, Opus/Sonnet/Haiku, connectors, context up to 1M and usage credits are shared across all three. | VERIFIED | https://claude.com/pricing |
| Routines: the current docs list only **hourly** caps (the same for all plans) and say routines draw on the subscription's usage. Launch coverage (April 2026) cited daily caps: Pro 5/day, Max 15/day (same for 5x and 20x), Team/Enterprise 25. The current official page doesn't show daily caps, so the launch caps may be superseded. | VERIFIED (current docs) / SNIPPET (launch caps): https://www.implicator.ai/anthropic-ships-claude-code-routines-cloud-automations-that-run-without-your-mac/ | |
| Over the limit: with usage credits turned on, routines continue on metered overage; otherwise runs are rejected until the window resets. | VERIFIED | routines.md |

### Counterfactual arithmetic (INFERENCE)

- **Downgrading from Max 20x to Max 5x saves $100/month ($1,200/yr) guaranteed, in after-tax money**, with no KYC, no tax filing, no account risk and no owner hours. The only cost is 4x less session and weekly capacity.
- **Revenue needed to match that $100/month after tax:**
  - US person, 22% bracket, Apify (income tax + SE tax ≈ 34.5% marginal): about **$153/month of net Apify payout ≈ $190/month of customer spend** at an 80% developer share.
  - US person, 22% bracket, prize: about $128/month of prizes.
  - Non-US person, 30% US withholding, no treaty: about $143/month of gross prizes before home-country tax and FX.
- **Caveat:** if the subscription is a deductible business expense for the Apify activity, the after-tax cost of keeping 20x is lower. That partially closes the gap for a US person with real Schedule C income.
- **Downgrade test:** check whether the agent workload (routines + interactive work) has stayed under about 25% of 20x capacity in recent weeks (claude.ai/settings/usage). If it has, Max 5x likely suffices and the downgrade dominates on expected value.
