# Autonomous operator routine

Standing instructions for every scheduled maintenance session. Read this file,
`PLAN.md` and `ops/LEDGER.md` before acting.

The development container can reach only GitHub and package registries. All
live work therefore happens in GitHub Actions: trigger workflows and read their
logs with the GitHub MCP tools (`actions_run_trigger`, `actions_list`,
`get_job_logs`).

## Hard rules (never break these)

1. **No spending.** Never buy, upgrade or enter payment details. Write
   proposals under *Proposals* in the ledger. The owner approves anything above
   $100 in total.
2. **Metaculus: no human in the loop.** Never look at the bot's forecasts or
   reasoning on questions that are still open, and never change code, prompts
   or config because of them. Never rerun a question to get a different answer.
   - Tournament logs print counts and errors only; keep it that way.
   - Allowed inputs: CI errors, coverage counts, the bot-testing-area, and
     resolved questions.
   - **One prize bot per person:** never start a second bot, for example from
     Codex.
3. **Legal data only.** Use official public APIs or open data that allow
   commercial reuse. No login or CAPTCHA bypass, and no personal data.
4. **No fake signals or spam.** No fake reviews, no self-runs to inflate Store
   stats, and no promotional posting.
5. **Leave a trail.** End every session by updating `ops/LEDGER.md`, then
   commit and push to `claude/ai-revenue-generation-ume6vn`.

## Each session, in order

1. **Setup detection.** List recent runs of `forecast-bot-tournament.yaml`.
   - **Jobs skipped:** `BOT_ENABLED` is unset, so setup is still pending. Note
     it under *Blocked* and stop.
   - **Runs succeed but print "not set yet":** secrets are missing. Note it and
     stop.
   - **First time they run for real:** trigger `forecast-bot-test.yaml` with
     `publish=true` once. It posts to Metaculus's unscored bot-testing-area.
     Check that it succeeded.
2. **Bot health.**
   - For failed tournament runs, read only the failure output. Fix the root
     cause, run the offline tests (`python -m unittest test_run test_cli_llm
     test_mc`), push, then run the test workflow.
   - A `claude -p` authentication error means the owner's token expired or was
     revoked. Ask the owner for a new `CLAUDE_CODE_OAUTH_TOKEN`.
3. **Coverage.** Run `forecast-bot-coverage.yaml`, record its counts in the
   ledger, and compare them with last time. If main-tournament coverage of
   closed questions is below 90%, investigate missed runs. Use run timestamps,
   not forecasts. Propose an external trigger if GitHub cron is the cause.
4. **Targets still current.** Run `metaculus-meta.yaml` (metadata only).
   - If a FutureEval tournament newer than `mc.SEASON_TOURNAMENT` has started
     (Spring 2027 is expected around January), switch `SEASON_TOURNAMENT` to
     its slug, run the offline tests, push, and run the test workflow.
   - If the newest MiniBench question opened more than 3 days ago, find where
     MiniBench moved (Metaculus announcements, `forecasting-tools` releases)
     and set the `MINIBENCH_ID` variable or ask the owner to. If MiniBench has
     ended, set `RUN_MINIBENCH=false` so no runs are spent on it.
5. **Learning, monthly, from resolved questions only.** Once 20 or more have
   resolved, the owner may be asked to read the bot's score on Metaculus.
   Code changes must rest on resolved questions or on bot-testing-area runs,
   never on open ones.
6. **Optional channels.** Only after the owner has said yes in the ledger:
   - **Apify:** run `apify.yaml` stats, and `tender-feed-live-check.yaml`
     weekly.
7. **Ledger, commit, push.**

## Backlog (Actors)

1. Pharma/MedTech Signal Monitor: field-level diffs of ClinicalTrials.gov plus
   openFDA approvals and recalls.
2. Rulemaking Docket Tracker: Federal Register linked to Regulations.gov, with
   comment deltas and deadlines.

## Stop rules

- **Day 60:** under 10 Actor users means no new Actors.
- **Day 120:** under $20 of revenue means writing a pivot proposal and telling
  the owner.
- **Forecast bot:** if the average peer score on resolved questions is below 0
  after 40 or more have resolved, propose stopping the model spend.
