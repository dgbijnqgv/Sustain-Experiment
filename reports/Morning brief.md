# Morning brief (2026-10-08)

## Your question: why API pricing on a subscription?

The bot's model calls now run through **Claude Code itself** (`claude -p`)
instead of a pay-per-token API.

- **Primary:** your Max plan's **included $200/month of API credits**.
  Anthropic added these on 7 Oct. They're otherwise unused, and keeping the bot
  on them leaves your weekly limit alone.
- **Fallback:** your **subscription**, through a `claude setup-token` token.
  Anthropic documents this "for CI pipelines, scripts".

So you pay **$0 cash**, and running locally isn't needed. Codex is a backup
only, on your own machine: OpenAI discourages using a ChatGPT login in CI.

## What I did tonight

1. **Six research tracks plus an independent red-team review:**
   - Claude subscription policy
   - Codex subscription policy
   - free models and how Metaculus runs the tournament
   - other prize competitions
   - your side: tax, payouts and risks
   - CrunchDAO and Kaggle
2. **Rebuilt the bot to run on your plan:**
   - high effort, with a forecasting system prompt;
   - API credits first, falling back to the subscription;
   - a command-line tool (`mc.py`) for listing, submitting and checking
     coverage;
   - logs mask digits, so they never show forecasts;
   - secrets reach only the steps that need them.
3. **Tested:** 25 offline tests pass. Live `claude -p` research and forecasts
   work, for both binary and numeric questions. CI is green.
4. **Fixed every critical item the review found.** The biggest was that
   **GitHub's scheduler is unreliable**: it fired once in about 7 hours here,
   while questions are open for only about 1.5 hours. Hence the external
   15-minute trigger in step 6 below.

## The honest numbers

| | |
|---|---|
| Expected value | **~$105/month pre-tax** (~$74 after 30% US withholding) with a reliable trigger; ~$64 without one |
| First cash | Around Mar–May 2027. Prizes are paid 3 times a year. |
| Chance of a $200/month season | 3–8% |
| Cash cost | $0 |
| Your time | ~45 minutes now, then ~10–15 hours a year, mostly prize paperwork |
| Most likely way to reach $200 | Downgrade to Max 5x **and** run the bot, worth ~$147/month. Your call: you kept 20x on purpose. |

One more thing: tonight's work used about $68 of usage at API prices, which
put your 7-day limit at "warning" until about Oct 14. I stopped launching new
research when I noticed.

## What I need from you (about 45 minutes)

Details are in `PLAN.md` §8.

1. **Metaculus:** create a bot account and token at
   metaculus.com/futureeval/participate, then fill in the participation form.
2. **API credits:** claim the Max plan's credits (claude.ai → Settings →
   Billing → link a Console organization). Create an API key there and **don't
   add a card** to that organization.
3. **Subscription token:** run `npx -y @anthropic-ai/claude-code setup-token`
   and copy the token.
4. **Make this repo public.** That gives unlimited Actions minutes and turns on
   MiniBench. If you'd rather keep it private, the bot runs the main tournament
   only.
5. **Add GitHub settings:**
   - Secrets: `METACULUS_TOKEN`, `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`.
   - Variables: `BOT_ENABLED=true` and `RUN_MINIBENCH=true`.
6. **Set up the trigger:** create a cron-job.org job that calls GitHub's
   workflow_dispatch every 15 minutes, with a fine-grained token limited to
   Actions on this repo.
7. **Reply with:**
   - your country of tax residence;
   - yes or no to the optional tender feed and CrunchDAO;
   - yes or no to downgrade-plus-bot.

After that it runs on its own:
- The Monday/Thursday check-in picks up your setup, runs the test, and tracks
  coverage and failures.
- GitHub emails you if a run fails.
