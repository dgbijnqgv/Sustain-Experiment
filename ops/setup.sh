#!/usr/bin/env bash
# One-time owner setup for the forecasting bot. Run it on your own computer:
#
#   bash ops/setup.sh
#
# It does every step that can be scripted (repository visibility, secrets,
# variables, a live test run, checking the trigger) and stops only where you
# must act in a browser: logins, Metaculus's bot token and form, the Anthropic
# billing page, a GitHub token and the cron-job.org job.
#
# Tokens never go through chat or this script's output: `gh secret set` asks
# for each one with hidden input and sends it straight to GitHub.
#
# Needs: GitHub CLI (`gh`, logged in as the repo owner) and Node.js (`npx`).
# Safe to re-run: finished steps are detected and skipped.
set -euo pipefail

REPO="dgbijnqgv/Sustain-Experiment"
BRANCH="claude/ai-revenue-generation-ume6vn"
DISPATCH_URL="https://api.github.com/repos/$REPO/actions/workflows/forecast-bot-tournament.yaml/dispatches"

bold() { printf '\n\033[1m%s\033[0m\n' "$*"; }
say() { printf '%s\n' "$*"; }
pause() { read -r -p "${1:-Press Enter when done...}" _; }
ask_yes() { local a; read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy] ]]; }
open_url() {
  say "  -> $1"
  if command -v open >/dev/null 2>&1; then open "$1" >/dev/null 2>&1 || true
  elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$1" >/dev/null 2>&1 || true
  elif command -v start >/dev/null 2>&1; then start "" "$1" >/dev/null 2>&1 || true
  fi
}
has_secret() { gh secret list -R "$REPO" --json name -q '.[].name' | grep -qx "$1"; }
set_secret() {
  say "  Now paste it at \"? Paste your secret\" and press Enter (nothing shows as you paste)."
  until gh secret set "$1" -R "$REPO"; do say "  That didn't work; try again."; done
}

bold "0/7  Checking tools"
command -v gh >/dev/null || { say "Install the GitHub CLI first: https://cli.github.com, then run: gh auth login"; exit 1; }
gh auth status >/dev/null 2>&1 || gh auth login
[ "$(gh api "repos/$REPO" -q .permissions.admin)" = "true" ] || { say "Your gh login is not an admin of $REPO."; exit 1; }
command -v npx >/dev/null || command -v claude >/dev/null || say "Note: Node.js (npx) not found; step 4 will need it: https://nodejs.org"

bold "1/7  Your Claude plan"
say "  Max 20x: Opus forecasts everywhere (fits its \$200/month of API credits)."
say "  Max 5x:  Opus for the main tournament, Sonnet for MiniBench (overflow uses the plan)."
read -r -p "  Which plan will you be on? [20/5] (default 20) " PLAN
PLAN="${PLAN:-20}"

bold "2/7  Repository visibility"
VIS="$(gh repo view "$REPO" --json visibility -q .visibility)"
MINIBENCH=true
if [ "$VIS" != "PUBLIC" ]; then
  say "  Public repos get unlimited Actions minutes, which MiniBench needs."
  say "  The repo holds code, plans and research only; its full history was"
  say "  scanned for tokens and personal data (none found). Secrets stay secret."
  if ask_yes "  Make $REPO public?"; then
    gh repo edit "$REPO" --visibility public --accept-visibility-change-consequences
  else
    MINIBENCH=false
    say "  Staying private: MiniBench off, main tournament only."
  fi
else
  say "  Already public."
fi

bold "3/7  Metaculus bot token"
if has_secret METACULUS_TOKEN; then say "  Already set."; else
  say "  In the browser: log in or sign up, create a BOT account, and copy its token."
  open_url "https://www.metaculus.com/futureeval/participate/"
  pause "  Got the bot token copied? Press Enter only (paste it at the NEXT prompt)..."
  set_secret METACULUS_TOKEN
fi
say "  Also fill in the first section of the participation form (tick the credits request)."
open_url "https://forms.gle/aQdYMq9Pisrf1v7d8"
pause "  Press Enter when the form is submitted (or to do it later)..."

bold "4/7  Claude credentials"
if has_secret ANTHROPIC_API_KEY; then say "  API key already set."; else
  say "  Primary: the plan's included API credits. At claude.ai -> Settings -> Billing,"
  say "  claim them by linking a Console organization. Do NOT add a card there, so it"
  say "  can never overspend. Then create an API key in that Console organization."
  say "  (Not claimable yet? Skip; the subscription token below works on its own.)"
  open_url "https://claude.ai/settings/billing"
  if ask_yes "  Do you have the API key copied?"; then set_secret ANTHROPIC_API_KEY; fi
fi
if has_secret CLAUDE_CODE_OAUTH_TOKEN; then say "  Subscription token already set."; else
  say "  Fallback: a subscription token. A browser login opens; the token is printed"
  say "  in this terminal. Copy it, then paste it at the next prompt."
  if command -v claude >/dev/null; then claude setup-token; else npx -y @anthropic-ai/claude-code setup-token; fi
  set_secret CLAUDE_CODE_OAUTH_TOKEN
fi

bold "5/7  Bot settings"
gh variable set RUN_MINIBENCH -R "$REPO" --body "$MINIBENCH"
if [ "$PLAN" = "5" ]; then
  gh variable set MINIBENCH_FORECAST_MODELS -R "$REPO" --body "claude-code/sonnet"
else
  gh variable delete MINIBENCH_FORECAST_MODELS -R "$REPO" >/dev/null 2>&1 || true
fi
say "  RUN_MINIBENCH=$MINIBENCH, plan=Max ${PLAN}x."

bold "6/7  Live test on Metaculus's unscored practice area"
say "  Starting the test workflow (takes ~5-15 minutes)..."
STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
gh workflow run forecast-bot-test.yaml -R "$REPO" --ref "$BRANCH" -f publish=true
RUN_ID=""
for _ in $(seq 20); do
  sleep 5
  RUN_ID="$(gh run list -R "$REPO" --workflow forecast-bot-test.yaml --event workflow_dispatch -L 5 \
    --json databaseId,createdAt -q ".[] | select(.createdAt >= \"$STARTED\") | .databaseId" | head -n 1)"
  [ -n "$RUN_ID" ] && break
done
[ -n "$RUN_ID" ] || { say "  The test run didn't appear; check the Actions tab, then re-run this script."; exit 1; }
if gh run watch "$RUN_ID" -R "$REPO" --exit-status --interval 30 >/dev/null; then
  say "  Test passed. Turning the tournament bot on."
  gh variable set BOT_ENABLED -R "$REPO" --body true
else
  say "  Test FAILED. The bot stays off. Details: gh run view $RUN_ID -R $REPO --log-failed"
  say "  Tell Claude in the session; it can read the run and fix it."
  exit 1
fi

bold "7/7  Reliable trigger (every 15 minutes)"
say "  GitHub's own schedule skips runs; questions are open only ~1.5 hours."
say "  a) Create a GitHub token: repository access = only $REPO,"
say "     permission Actions = Read and write, expiry 1 year. Copy it."
open_url "https://github.com/settings/personal-access-tokens/new?name=forecast-bot-trigger&description=cron-job.org+trigger+for+the+forecast+bot&target_name=dgbijnqgv&expires_in=365&actions=write"
say "     (If the form isn't pre-filled, set those fields by hand.)"
pause "  Token copied? Press Enter only (it goes into cron-job.org, not here)..."
say "  b) At cron-job.org (free account), create a job:"
say "     URL:      $DISPATCH_URL"
say "     Schedule: every 15 minutes"
say "     Advanced -> Request method: POST"
say "     Headers:  Authorization: Bearer <the token from a>"
say "               Accept: application/vnd.github+json"
say "     Body:     {\"ref\":\"$BRANCH\"}"
say "     Then click 'Test run' (it should return HTTP 204)."
open_url "https://console.cron-job.org/"
pause "  Press Enter after the test run..."
SINCE="$(date -u -d '-10 minutes' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-10M +%Y-%m-%dT%H:%M:%SZ)"
if gh run list -R "$REPO" --workflow forecast-bot-tournament.yaml --event workflow_dispatch -L 5 \
     --json createdAt -q ".[] | select(.createdAt > \"$SINCE\") | .createdAt" | grep -q .; then
  say "  Trigger works: GitHub received the dispatch."
else
  say "  No dispatched run seen in the last 10 minutes. Check the job's URL, method,"
  say "  headers and body, then re-run this script (finished steps are skipped)."
fi

bold "Done"
say "The bot now forecasts on its own. GitHub emails you if a run fails, and the"
say "twice-weekly check-in tracks coverage. Last thing: tell Claude your country of"
say "tax residence, and yes/no to CrunchDAO, the tender feed and downgrade-plus-bot."
