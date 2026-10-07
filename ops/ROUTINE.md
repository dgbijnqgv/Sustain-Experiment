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
   - Allowed inputs: CI errors and stack traces, cost totals, the
     bot-testing-area, and questions that have already resolved.
   - When reading tournament run logs, look only at errors and the cost and
     count summary.
3. **Legal data only.** Use official public APIs or open data that allow
   commercial reuse. No login or CAPTCHA bypass, and no personal data.
4. **No fake signals or spam.** No fake reviews, no self-runs to inflate Store
   stats, and no promotional posting.
5. **Leave a trail.** End every session by updating `ops/LEDGER.md`, then
   commit and push to `claude/ai-revenue-generation-ume6vn`.

## Each session, in order

1. **Forecast bot health.**
   - List the recent runs of `forecast-bot-tournament.yaml`.
   - If any failed, read only the failure output. Fix the root cause, run the
     offline tests, push, then trigger `forecast-bot-test.yaml`.
   - If runs are being skipped, setup is incomplete. Note that in the ledger
     under *Blocked*.
2. **Forecast bot cost.** Sum the "Run cost" lines across the week's runs and
   compare the total with the approved budget. If the season total is on track
   to pass it, set the per-run cap lower and note it in the ledger. Do not
   pause the bot without the owner, because skipped questions score zero.
3. **Forecast bot learning.** Do this only from resolved questions, about
   monthly, once some have resolved. Write findings in the ledger, and change
   code only on evidence from resolved questions.
4. **Apify.** Once `APIFY_TOKEN` exists:
   - Run the `Apify` workflow with task `stats` and record users, runs and
     failures in the ledger.
   - Run `tender-feed-live-check.yaml` weekly, and fix any source that broke.
5. **Build.** Only when everything above is healthy, and at most 3 Actors in
   total. Take the next item from the backlog below. Publish only after a clean
   live check.
6. **Ledger, commit, push.**

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
