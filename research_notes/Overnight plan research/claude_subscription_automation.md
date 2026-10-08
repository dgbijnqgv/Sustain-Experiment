# Running recurring autonomous work on a Claude Max 20x subscription (researched 2026-10-08)

**Question.** What does Anthropic permit, and what limits apply, when an individual Max 20x subscriber ($200/month) uses the *subscription* (not API credits) for recurring autonomous work that benefits them? The test case is a Metaculus FutureEval forecasting bot: cash prizes go to the subscriber, there is no human in the loop, and the bot fetches questions, researches them, and posts forecasts.

**Labels.**
- **VERIFIED** means I read the primary source myself (curl or WebFetch) on 2026-10-08.
- **SNIPPET** means search-result text or secondary reporting, not checked against a primary source.

**Access notes.**
- code.claude.com docs (raw `.md`), support.claude.com, anthropic.com/legal, claude.com/blog and raw.githubusercontent.com were all fetchable.
- These were blocked by the egress proxy: thenextweb, gigazine, thenewstack, news.ycombinator, autonomee.ai and metaculus.com.
- The `gh` API is scoped to session repos, so I read the GitHub mirrors through raw.githubusercontent.com instead.

---

## 1. Decisive primary-source quotes

### 1.1 Consumer Terms (VERIFIED). https://www.anthropic.com/legal/consumer-terms, page shows "Effective October 8, 2025"

- Scope: these terms govern "Claude.ai, Claude Pro, and other products and services that we may offer for individuals". The Claude Code legal page confirms that Free, Pro and Max fall under them.
- **Automation clause (§3):** "Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through automated or non-human means, whether through a bot, script, or otherwise."
  - The question is therefore whether Anthropic "explicitly permit[s]" each mode. Sections 1.3 to 1.5 below show that it does, in writing, for routines, `claude -p`, setup-token scripts/CI and the GitHub Action.
- **Account sharing:** "You may not share your Account login information, Anthropic API key, or Account credentials with anyone else. You also may not make your Account available to anyone else."
- **No resale or competing models:** "To develop any products or services that compete with our Services, including to develop or train any artificial intelligence or machine learning algorithms or models or resell the Services."
- **No non-commercial restriction on paid use.** The only "personal, non-commercial" language is about evaluation: "Use of our Services for evaluation purposes are for your personal, non-commercial use only." Winning prize money with Claude's help is not restricted.
- **Financial clause (not triggered by Metaculus):** "To rely upon the Services, the Materials, or the Actions to buy or sell securities or to provide or receive advice about securities, commodities, derivatives, or other financial products or services". Metaculus is a scored forecasting tournament, not trading. This clause would matter for real-money prediction-market trading such as Kalshi or Polymarket.
- **Enforcement:** "We may suspend or terminate your access to the Services (including any Subscriptions) at any time without notice to you if we believe that you have breached these Terms". Also: "if you have a Subscription, we may terminate the Subscription at any time for any other reason" (with a pro-rata refund).

### 1.2 Claude Code "Legal and compliance" page (VERIFIED). https://code.claude.com/docs/en/legal-and-compliance, current as of 2026-10-08

- Plan mapping: "Consumer Terms of Service - for Free, Pro, and Max users".
- "Claude Code usage is subject to the Anthropic Usage Policy. **Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK.**"
  - Read literally, this describes what the limits *assume*. It is not a prohibition.
- "**OAuth authentication** is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications."
- "**Developers** building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication through Claude Console or a supported cloud provider. Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users. Moreover, developers may not collect, store, or intermediate Claude.ai credentials or session tokens — sign-in to a Claude account must complete through Anthropic's own flow."
- "...Nor does it prevent an end user from signing in to the unmodified Claude Code binary with their own Claude subscription..."
- "Anthropic reserves the right to take measures to enforce these restrictions and may do so without prior notice."
- **Interpretation, product vs. own task:**
  - The restrictions target (i) products or services that interact with Claude for other people ("on behalf of their users") and (ii) third-party apps or harnesses that take or relay subscription tokens.
  - A subscriber running the *unmodified Claude Code binary* on their *own* task, with nobody else using it, is outside both.
  - The residual grey area is the phrase "developers building products or services ... including those using the Agent SDK ... should use API key". Someone could call a tournament bot a "product", but nothing is offered to anyone else.

### 1.3 Support article 15036540, "Use the Claude Agent SDK with your Claude plan" (VERIFIED, page says "Updated today")

https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
- "**Update October 7, 2026:** Claude Max and Team plans now include monthly API credits, which cover the Claude Agent SDK, `claude -p`, the Claude API, and Claude Managed Agents. **You can still use the Claude Agent SDK, `claude -p`, and third-party apps with your subscription limits.**"
- "**Update June 15, 2026:** We've paused the previously-announced changes to Claude Agent SDK usage. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription limits."
- This is the most explicit current permission: Anthropic says, in writing, that `claude -p` and the Agent SDK may run on subscription limits.

### 1.4 Support article 17154008, "Monthly API credits for Max and Team plans" (VERIFIED, new 2026-10-07)

https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans
- Credit amounts: "Max 5x $100", "**Max 20x $200**" per month.
- Purpose: "Use them to build Claude into your own apps and agents with the Claude API."
- Covers: "The Claude API (Messages API and Message Batches API) / The Playground / Claude Managed Agents / The Claude Agent SDK".
- Does not cover: "Interactive Claude Code in the terminal, IDE, desktop, or web / Extra usage ...".
- Expiry: "Doesn't roll over. Unused credits expire at the end of each billing cycle."
- Plan limits unaffected: "Separate from your plan limits. The credits don't change your usage limits in Claude, Claude Code, or Claude Cowork."
- When credits run out: "If the organization has no other credits, API requests stop until your next monthly credits arrive. Usage is never charged to your Claude plan."
- Eligibility: claim after "Seven days on the plan", by linking exactly one Console org.
- FAQ, "Does this cover `claude -p`?":
  - "API credits cover `claude -p` and the Claude Agent SDK when you run them yourself with an API key from your linked Claude Console organization ... When you're signed in with your Claude plan instead, `claude -p` and Agent SDK usage still draw from your plan's usage limits and don't use your API credits."
  - "**Runs started by the Claude Code GitHub Action, an IDE extension or the Claude desktop app count as Claude Code usage**, so API credits don't cover them, even with `-p`."
- FAQ: "Is this the same as the Agent SDK credits announced in June? No. That credit isn't available."
- Supplemental Credit Terms (VERIFIED, https://www.anthropic.com/legal/credit-terms, effective March 4, 2024): "Customer may not transfer or sell Credits ... and Credits may only be used by the holder of the Anthropic account to which the Credits are associated."

### 1.5 Explicit first-party automation documentation (VERIFIED)

**Routines.** https://code.claude.com/docs/en/routines
- "Put Claude Code on autopilot."
- "Routines run autonomously as full Claude Code cloud sessions: there is no permission-mode picker, and the session runs shell commands ... and calls any connectors you include, all without stopping for approval".
- "Routines belong to your individual claude.ai account ... their runs count against your account's usage and limits."

**Long-lived token for scripts and CI.** https://code.claude.com/docs/en/authentication
- "For CI pipelines, scripts, or other environments where interactive browser login isn't available, generate a one-year OAuth token with `claude setup-token`".
- "This token authenticates with your Claude subscription and requires a Pro, Max, Team, or Enterprise plan. It can only make model requests, so it can't establish Remote Control sessions or fetch claude.ai connectors."
- `CLAUDE_CODE_OAUTH_TOKEN`: "Use this for CI pipelines and scripts where browser login isn't available."
- "Bare mode does not read `CLAUDE_CODE_OAUTH_TOKEN`." In other words, `--bare` requires an API key.
- "Cloud sessions always use your subscription credentials."

**GitHub Actions.** https://code.claude.com/docs/en/github-actions
- "`CLAUDE_CODE_OAUTH_TOKEN`: an OAuth token that authenticates with your Claude subscription, available on Pro, Max, Team, and Enterprise plans."
- "With a `prompt` input, the Claude Code GitHub Action runs in automation mode on any GitHub event, including a cron schedule."
- "If you authenticate with an OAuth token, runs use your Claude subscription instead of API billing."
- "For a secret shared across repositories, authenticate with an API key ... since an OAuth token is tied to the subscription of the person who ran `claude setup-token`."
- "GitHub runs scheduled workflows only from the default branch and, in public repositories, disables the schedule after 60 days without repository activity."

**claude-code-action docs/setup.md** (VERIFIED, raw.githubusercontent.com/anthropics/claude-code-action/main/docs/setup.md): "`CLAUDE_CODE_OAUTH_TOKEN` for OAuth token authentication (Pro and Max users can generate this by running `claude setup-token` locally)". The README intro no longer lists OAuth among the auth methods, but setup.md still documents it.

**Headless mode.** https://code.claude.com/docs/en/headless: "Run Claude Code programmatically ... available as a CLI for scripts and CI/CD." No subscription restriction is stated, apart from bare mode needing an API key.

**Agent SDK overview** (https://code.claude.com/docs/en/agent-sdk/overview), quoted twice on the page:
- "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods described in the Quickstart instead."
- This targets third-party developers' *products*. It does not cover a subscriber's own use.

### 1.6 Usage Policy (VERIFIED). https://www.anthropic.com/legal/aup, "Effective September 15, 2025"

- No clause on gambling, betting, wagers, prediction markets, contests or prize money (searched the fetched text).
- Relevant general clauses:
  - "Engage in actions or behaviors that circumvent the guardrails or terms of other platforms or services". The bot must follow Metaculus rules: one prize-eligible bot per user, a reasoning comment with each forecast, code or description disclosure.
  - "Plagiarize or submit AI-assisted work without proper permission or attribution". FutureEval explicitly permits bots, so this is satisfied.
  - "Utilize automation in account creation or to engage in spammy behavior".
  - "Coordinate malicious activity across multiple accounts".
- High-risk "Finance" covers advice to individuals or consumers. Posting a probability on a scored tournament question is not advice to a consumer.

### 1.7 Usage limits (VERIFIED). Support article 11049741, "What is the Max plan?"

- "Max 20x includes 20 times the Pro plan's per-session usage allowance."
- "Your session-based usage limit will reset every five hours. Max plans also have a weekly usage limit that applies across all models."
- "...we may limit your usage in other ways, such as weekly and monthly caps or model and feature usage, at our discretion."
- Article 11145838: "usage limits that are shared across Claude and Claude Code".
- Usage credits (article 12429409) let you continue past the limits at standard API rates. They are opt-in.

---

## 2. Enforcement history, 2025–2026 (what triggered each event)

| Date | Event | Trigger / target | Source |
|---|---|---|---|
| 2025-07-28 (effective Aug 28) | Weekly caps added to Pro/Max | Users running Claude Code "continuously in the background, 24/7", plus "account sharing and reselling access". Anthropic said fewer than 5% of subscribers were affected. Max 20x guidance at the time: 240–480 h Sonnet 4 / 24–40 h Opus 4 per week | SNIPPET: TechCrunch https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/ ; VentureBeat |
| 2026-01-09 | Server-side block on subscription OAuth tokens used outside the official Claude Code client. Thariq Shihipar (Anthropic): "we tightened our safeguards against spoofing the Claude Code harness after accounts were banned for triggering abuse filters from third-party harnesses using Claude subscriptions". He acknowledged some bans were erroneous | Third-party harnesses **spoofing** Claude Code with subscription tokens | SNIPPET (search summaries of X post, autonomee.ai) |
| 2026-02-19 | Legal & compliance docs updated: Agent SDK developers "should use API key". Thariq reportedly called it "a docs clean up that caused some confusion" and said nothing was changing for personal Agent SDK/Max use | Docs change; no enforcement against personal use reported | SNIPPET (alternativeto.net, autonomee.ai). Current wording VERIFIED in 1.2 |
| 2026-04-04 12:00 PT | **OpenClaw cutoff.** Subscription limits stopped covering third-party harnesses (OpenClaw first, others to follow). Users had to buy extra usage or use an API key. One-time credit equal to one month of the plan (redeem by Apr 17); up to 30% off usage bundles. Boris Cherny (head of Claude Code): "Our subscriptions weren't built for the usage patterns of these third-party tools." Email cited "outsized" strain on capacity | **Third-party harnesses** (non-Anthropic agent apps) drawing heavy, always-on load through subscription OAuth. **Claude Code and Cowork stayed covered** | SNIPPET (TNW, gigazine, implicator, inbenta; primaries blocked) |
| 2026-04-14 | Routines launched (research preview) with daily caps of Pro 5, Max 15, Team/Ent 25 | — | VERIFIED: blog https://claude.com/blog/introducing-routines-in-claude-code |
| 2026-05-13 | Announced: from Jun 15, Agent SDK, `claude -p` and third-party apps would move to a separate monthly credit ($20 Pro / $100 Max 5x / $200 Max 20x), with API billing beyond it | Cost of programmatic use | SNIPPET (thenewstack, letsdatascience, dev.to) |
| 2026-06-15 | **Paused**: "nothing has changed". Anthropic reportedly promised advance notice before any future change | — | VERIFIED (support 15036540) |
| 2026-10-07 | Max/Team get monthly API credits ($200 for Max 20x); `claude -p` and SDK still allowed on subscription limits | — | VERIFIED (support 15036540, 17154008) |

- Scale (SNIPPET, unverified): a third-party guide citing the Transparency Hub says 1.45M accounts were banned in H2 2025, with about 1,700 successful appeals out of 52k.
- Commonly cited ban triggers (SNIPPET): third-party tools or spoofed clients, multiple accounts, region or payment mismatch, account sharing.
- **I found no report** of a ban for a single user running first-party `claude -p`, routines or the GitHub Action on their own task.

---

## 3. Per-option assessment

### (a) Claude Code routine, scheduled cloud session. Verdict: **ALLOWED**

- **Why allowed:** this is a first-party feature built for exactly this. "Put Claude Code on autopilot." It runs autonomously with no approvals and counts against the subscription.
- **Non-coding work:** nothing limits routines to coding.
- **Reading of "ordinary, individual usage":** it holds as long as volume stays within plan limits. It describes how limits are calibrated; it is not a ban.
- **Residual risks:**
  - Research preview: "Behavior, limits, and the API surface may change."
  - Limits or policy could tighten again.

**Routine limits** (VERIFIED, https://code.claude.com/docs/en/routines, unless noted):
- **Minimum interval:** "The minimum interval is one hour; expressions that run more frequently are rejected." Presets are hourly, daily, weekdays and weekly; custom cron is set via `/schedule update`. Runs exactly on the hour can start "several minutes late", so use e.g. :07.
- **Start-rate caps** (current docs): 100 scheduled runs (including one-off runs) per hour per account; 30 Run-now/API fires per hour per routine; 100 Run-now per hour per account; 100 API fires per hour per account. "None of these hourly limits has overage."
- **Daily cap, conflicting sources:**
  - The launch blog (2026-04-14, VERIFIED) says "Max users can run up to 15 routines per day ... You can run extra routines beyond these limits with extra usage." This applies to Max 5x and 20x alike.
  - The **current docs page does not mention any daily cap** and lists only the hourly caps above. No changelog entry mentions removing it.
  - **Treat 15 runs/day as possibly still enforced.** An hourly schedule means 24 runs/day, which would need extra usage if the cap is live.
  - Safe design: run every 2 hours (12/day) and batch every newly opened question into each run.
- **Subscription usage:** "Routines draw down subscription usage the same way interactive sessions do." On hitting the limit: "Without usage credits, additional runs are rejected until your usage window resets."
- **Concurrency:** not documented. Cloud sessions "share rate limits with all other Claude and Claude Code usage within your account. Running multiple tasks in parallel consumes more rate limits proportionately. There is no separate compute charge for the cloud VM."
- **Max run duration:** no documented session wall-clock cap.
  - Documented limits: foreground Bash 2 min by default, up to 10 min.
  - Commands moved to the background get "up to 30 more minutes".
  - SessionStart hooks are cancelled after 600 s.
  - The setup script is cached only if it finishes in about 5 min.
  - VM: about 4 vCPU, 16 GB RAM, 30 GB disk (cloud-environments).
- **Fresh session, repo cloned:** yes. "Each run creates a new session"; "Each repository you add is cloned on every run ... starting from the default branch"; pushes go to `claude/`-prefixed branches unless the prompt says otherwise.
  - State such as forecast logs or posted-question IDs persists only by committing to the repo, or through an external store.
  - If GitHub disconnects, runs are skipped for up to 72 h, then the routine turns off.
- **Env vars and secrets:**
  - The environment has env vars, but they are "visible to anyone who uses the environment".
  - On Pro/Max, use **network secrets**: "an API key or token you store on a cloud environment so Claude can call that API ... without seeing the key. Anthropic's agent proxy adds the key to requests for the hosts you list". Bearer is the default type.
  - Use one for the Metaculus API token on `www.metaculus.com`. Requests to secret hosts bypass the allowlist.
- **Network allowlist:**
  - The Default environment is **Trusted** (package registries, GitHub, cloud SDKs only), so metaculus.com and news sites are blocked with `403 host_not_allowed`.
  - The levels are None, Trusted, **Full** ("Any domain") and Custom (your own list).
  - For open-ended web research use **Full**, or Custom plus `www.metaculus.com`.
  - Observed in this session (a cloud session): the WebFetch tool goes through the session egress proxy and returned EGRESS_BLOCKED for non-allowlisted hosts. WebSearch is server-side and worked.
- **Connectors:** claude.ai connectors work in routines and bypass the allowlist.
- **API trigger:** `POST https://api.anthropic.com/v1/claude_code/routines/<id>/fire` with a bearer token. It can be fired from elsewhere, but it counts toward the same per-routine hourly caps.

### (b) `claude -p` on the subscriber's own computer via cron, logged in with the subscription. Verdict: **ALLOWED** (lowest friction, minor grey)

- **Explicit permission:**
  - Support 15036540: "You can still use the Claude Agent SDK, `claude -p`, and third-party apps with your subscription limits."
  - The auth docs offer `setup-token` "For CI pipelines, scripts".
  - This meets the Consumer Terms exception "where we otherwise explicitly permit it".
- **Conditions:**
  - Use the unmodified Claude Code binary.
  - No other users and no credential sharing.
  - Do not use `--bare`, which needs an API key.
  - Make sure `ANTHROPIC_API_KEY` is unset, or it overrides the subscription.
- **Grey residue:**
  - The May 2026 plan to move `claude -p` off subscription limits was only *paused*.
  - The legal page's "ordinary, individual usage" language exists.
  - Hourly 24/7 operation is the "running Claude Code continuously in the background, 24/7" pattern behind the 2025 weekly caps. That pattern was handled with caps, not bans.
- **Practical:**
  - The computer must be on.
  - Usage shares the 5-hour and weekly windows with the subscriber's interactive use.
  - When limits are hit, runs fail unless usage credits are enabled.
  - `--max-turns` and `--allowedTools` keep runs bounded.

### (c) claude-code-action or `claude -p` in GitHub Actions on a cron, with `CLAUDE_CODE_OAUTH_TOKEN`. Verdict: **ALLOWED**, with caveats

- **Explicitly documented:**
  - "runs in automation mode on any GitHub event, including a cron schedule".
  - "If you authenticate with an OAuth token, runs use your Claude subscription instead of API billing."
  - Support 17154008 confirms that GitHub Action runs "count as Claude Code usage".
- **Caveats:**
  - The token is personal ("tied to the subscription of the person who ran `claude setup-token`"). Keep it in your own repo's secrets; do not share it across an org or with collaborators.
  - The one-year token can't fetch claude.ai connectors.
  - GitHub-side cost: hourly runs at about 5–10 min each come to roughly 3.6k–7.2k runner-min/month. That exceeds GitHub Free's 2,000 private-repo minutes (SNIPPET-level knowledge of GitHub pricing). Public repos have free minutes, but forecasts and prompts become public and the schedule is disabled after 60 days without repo activity.
  - The action rejects bot actors on scheduled runs unless they are listed in `allowed_bots`.
  - Prior note (Plan financial and policy check/anthropic_policy.md) called using it as a "production LLM backend" a conflict with "ordinary, individual usage". On the current text, this is the subscriber's own automation, not a product for others, so I rate it Allowed. It is about as grey as (b).

### (d) Agent SDK (Python/TS) on subscription OAuth. Verdict: **GREY**, leaning allowed for strictly personal use

- **For:** support 15036540 says "Claude Agent SDK ... still draw[s] from your subscription limits."
- **Against:**
  - The legal page says "Developers building products or services ... including those using the Agent SDK, should use API key authentication".
  - The SDK overview says the same for third-party developers' products.
  - The Feb 2026 docs episode showed the SDK is where Anthropic's wording is most restrictive.
- **Clean alternative:** use the **Max 20x $200/month API credits** with an API key from the linked Console org.
  - This runs under the Commercial Terms, so there is no automation question and no subscription-limit drain.
  - The credits cover the Agent SDK, `claude -p` with an API key, and the Messages/Batch API.
  - They do not roll over. When they run out, "API requests stop until your next monthly credits arrive" unless you buy credits.

---

## 4. Cost and feasibility estimate (ESTIMATE; inputs partly SNIPPET)

**List prices** (VERIFIED in prior note, platform.claude.com pricing, 2026-10-08), per MTok:
- Opus 5.5: $4 in, $5 (5m) / $8 (1h) cache write, $0.20 cache read, $20 out.
- Sonnet 5.5: $2 / $2.50 / $4 / $0.10 / $10.

**Caching:** the subscription cache TTL is 1 h (costs.md, VERIFIED: "The lifetime is an hour on a subscription"). Web search on the API costs about $10 per 1k searches.

**Per question, one Claude Code research-and-forecast pass:**
- Base context (system prompt, tools, CLAUDE.md) is about 20–30k tokens.
- About 6–10 WebSearch and 3–6 WebFetch calls, each adding about 1–5k tokens.
- About 15–25 turns, with context growing from about 25k to about 70k tokens.
- Unique tokens: about 50–150k, which matches the brief's 30–150k. Processed tokens, including cache reads, are about 0.6–1.5M.

**API-equivalent cost, Opus 5.5:**
- Cache reads: about 1M × $0.20 = $0.20.
- Cache writes: about 70k × $8 = $0.56.
- Output plus thinking: 15–30k × $20 = $0.30–0.60.
- Searches: about $0.08.
- **About $1.1–1.5 per question.** Sonnet 5.5 is about $0.6–0.8.
- A 5-sample ensemble that reuses one research pass adds about $0.5–1. A full 5× re-research would cost about 5×.

**Empty polling runs:** each routine run that finds no new questions still costs about $0.15–0.30, from base context plus the API calls. At 12–24 runs/day, that is about $15–50/week.

**Volume:**
- FutureEval has 300–400 questions per season, plus MiniBench at about 60 questions per 2 weeks. That is about 50–60 questions/week, or **about 300–700 per 3 months** as the brief assumed.

**Weekly capacity of Max 20x:** about $1.74–2.2k API-equivalent per week (FinOps LLM about $1.86k; GitHub issue anthropics/claude-code#99330 about $1,827 for the week of 2026-09-30). SNIPPET, from prior notes.

**Load:**
- Base case: 55 questions/week × $1.3 = about $72, plus polling of about $30, giving **about $100/week, or roughly 5% of weekly capacity**.
- Heavy case: 5× ensemble with full re-research at about $6.5/question gives about $360 + $30 = **about 21%**.
- **Either way it fits within weekly limits**, leaving most of the allowance for the subscriber's other use.

**5-hour windows:** a burst of 30 or more questions opening at once (MiniBench rounds, season start), at about $40–200 API-equivalent, could hit a 5-hour window, especially on top of interactive use. Spread the work across runs, process at most N questions per run, and keep a queue.

**API-credit alternative:** 700 questions × about $1.3 = about $900 over 3 months, against about $600 of credits ($200 × 3). That covers about 2/3 on Opus 5.5, or all of it on Sonnet 5.5 or with the Batch API at 50% off for the forecasting step.

---

## 5. Anthropic statements on competitions, tournaments and prize money

- **No Anthropic statement found** that addresses using Claude to enter competitions or prediction tournaments, or to win prize money (searched the AUP, Consumer Terms, support and docs).
- The terms contain no non-commercial restriction for paid plans. The AUP has no contest or gambling clause.
- Constraints that do apply:
  - The AUP clauses against circumventing other platforms' terms and against unpermitted AI-assisted submissions. FutureEval explicitly permits bots, so both are satisfied as long as Metaculus rules are followed.
  - The Consumer Terms securities/commodities/derivatives clause. It is not triggered by Metaculus, but would be by trading-based markets.
- Context (SNIPPET): Metaculus has said FutureEval/AIB participants can get "API credits provided courtesy of OpenAI and Anthropic" (Spring 2026 page, https://www.metaculus.com/aib/2026/spring/). Anthropic actively supports Claude-powered entries, through the API route.
- Metaculus's general rules (SNIPPET, https://www.metaculus.com/tournament-rules/) make bots ineligible for prizes "unless a competition specifically permits otherwise". FutureEval does permit them. It requires one prize-eligible bot per user, a reasoning comment with each forecast, and a code or description submission to claim prizes.

---

## 6. Bottom line

1. **Routines (a): Allowed.** This is the most "explicitly permitted" path. Practical limits:
   - Interval of 1 hour or more.
   - Possibly 15 runs/day on Max (launch blog), although current docs show only hourly caps. Design for 12/day.
   - Network must be Full or Custom with metaculus.com allowed.
   - Store the Metaculus token as a network secret.
   - State lives in the repo.
2. **Local `claude -p` cron (b): Allowed.** It is explicitly allowed on subscription limits per the Oct 7, 2026 support text. The computer must be on.
3. **GitHub Action with OAuth token (c): Allowed.** It is documented for cron and subscription. Watch Actions minutes and token hygiene.
4. **Agent SDK on OAuth (d): Grey.** Use the $200/month Max API credits with an API key instead. That is fully clean.
5. **Usage** of about 300–700 questions per 3 months comes to about 5–20% of Max 20x weekly capacity. This is feasible; the main risk is burstiness against 5-hour windows.
6. **Biggest risk is policy change, not current prohibition:**
   - The routines research preview could change.
   - The paused Agent SDK/`claude -p` billing split could be revived (with advance notice).
   - Anthropic reserves termination "at any time without notice".
   - Keep a fallback path on API credits.

## Sources (fetched 2026-10-08 unless marked SNIPPET)
- https://code.claude.com/docs/en/legal-and-compliance
- https://code.claude.com/docs/en/routines
- https://code.claude.com/docs/en/cloud-environments
- https://code.claude.com/docs/en/claude-code-on-the-web
- https://code.claude.com/docs/en/authentication
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/costs
- https://code.claude.com/docs/en/agent-sdk/overview
- https://code.claude.com/docs/en/desktop-scheduled-tasks: local tasks have a 1-hour minimum interval and fire only while the app is open and the computer is awake
- https://support.claude.com/en/articles/15036540
- https://support.claude.com/en/articles/17154008
- https://support.claude.com/en/articles/11145838
- https://support.claude.com/en/articles/11049741
- https://support.claude.com/en/articles/12429409
- https://www.anthropic.com/legal/consumer-terms (eff. 2025-10-08)
- https://www.anthropic.com/legal/aup (eff. 2025-09-15)
- https://www.anthropic.com/legal/credit-terms (eff. 2024-03-04)
- https://claude.com/blog/introducing-routines-in-claude-code (2026-04-14)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/setup.md
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- SNIPPET: TechCrunch 2025-07-28; VentureBeat; TNW 2026-04-04; implicator.ai; gigazine 2026-04-05; inbenta; alternativeto.net 2026-02; thenewstack (Jun 2026 pause); letsdatascience; autonomee.ai; FinOps LLM; GitHub issue anthropics/claude-code#99330; Metaculus AIB Spring 2026 page; Metaculus tournament rules
