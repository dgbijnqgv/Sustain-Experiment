# Game income plan (Big Taro Games)

October 2026. Inputs: about 2 owner-hours a week; the owner is a solo game designer with
bigtarogames.com, which lists Backrooms, Paper Crane Harness and Grains as in progress.
The research is in `research_notes/Game income research/`:
- `web_game_portals.md`
- `assets_games_tabletop.md`
- `ugc_jams_gigs.md`

## What the evidence says

No game channel reliably nets $200/month in year 1 at 2 hours a week. The real
successes fall into two groups:
- **Prize pools judged on design.** Money is already waiting there, so this is the
  same pattern that makes Metaculus work.
- **A steady stream of small, polished games on portals that bring their own players.**

| Channel | 3 mo | 6 mo | 12 mo | Owner h/wk | Verdict |
|---|---|---|---|---|---|
| Platform contests and hackathons (Reddit/Devvit, Meta Horizon) | $0 | $0–150 | $50–250, lumpy | 1–2 in bursts | **Do** |
| Web games on CrazyGames (Poki later, if one does well) | $0–20 | $10–80 | $30–250, likely ~$75 | ~2 | **Do** |
| Code tools and plugins (Unity, Fab, itch) | $0–30 | $20–100 | $50–200 | 1.5–2 | Later, if the games produce reusable code |
| Reddit games (Devvit) | $0 | $0–50 | $0–200 | ~1 | Fold into the hackathons |
| Roblox | $0 | $0–25 | $0–100 | 1–2 | Skip for now |
| Freelancing | $0–50 | $0–150 | $50–300 | 2+, client-bound | Skip; breaks the time limit |
| Tabletop, Fortnite, YouTube, templates | ~$0 | | | | Skip |

Platform rules that matter:
- **itch.io and Unity:** AI use must be disclosed.
- **Poki:** may reject games that lean too heavily on AI. It also requires 5 years of web
  exclusivity for its revenue share.
- **CrazyGames:** open submission, a 2-week trial launch, and monthly payouts once
  earnings reach €100.
- **Newgrounds and DriveThruRPG:** ban AI content.

## Plan

1. **Ship small web games to CrazyGames, one or two a month.**
   - The owner supplies the design and the taste.
   - Claude Code builds, tests and iterates, then prepares the submission.
   - Each game has an original twist; no clones.
   - The games also give the studio a portfolio and players.
2. **Enter every big platform contest.**
   - Reddit runs a $40–45k games hackathon 2–3 times a year: January, June and
     October in 2025–26. The next one is likely around January 2027.
   - Meta Horizon runs design and prototype contests. The 2026 design-document contest
     paid 22 prizes of $7.5k–$20k.
   - AI drafts the entries and the owner signs off.
   - A watcher will flag new contests.
3. **Keep the Metaculus bot running.** It costs no owner time, about $105/month pre-tax
   is expected, and it uses the plan's API credits. Building games uses the
   subscription, not those credits, so the two don't compete.
4. **Fix the site's follow form.** `site.config.js` has an empty `followEndpoint`, so
   no emails are collected. Players gathered by each game should land on a mailing list.

**Central case at month 12:** about $200/month pre-tax across all three income
streams: bot about $105, games about $75, contests averaged. The range is wide: the
contests are lumpy and portal income is very uneven. A shortfall in year 1 is
likelier than not.

## Owner's 2 hours a week

| Time | Task |
|---|---|
| 1 h | Play the week's build and give design notes |
| 0.5 h | Approve and upload (accounts, tax forms and ID stay with the owner) |
| 0.5 h | Contest sign-off when one is open |

## Update: shiteven.fun comes first

The owner already has a finished multiplayer .io game, shiteven.fun. It makes more
sense to monetize that than to build new games. The research is in:
- `research_notes/Game income research/io_game_monetization.md`
- `research_notes/Game income research/shiteven_policy_fit.md`

**Where the money is.** CrazyGames is the realistic route.
- It accepts self-hosted multiplayer servers and has no exclusivity requirement.
- Every game goes through a 7–21 day trial with ads off. Retention and how many
  visitors start playing decide whether it goes live with ads; most games don't pass.
- Ads on the game's own domain don't pay at its current traffic. Premium ad
  networks want 100k–500k pageviews a month, and Playwire and Freestar ban profanity.

**Why the game needs a separate portal build:**
- CrazyGames requires a PEGI 12 rating, which allows only mild language.
- Slot machines now push a game to PEGI 18, so Sewer Slots must go from that build.
- Poki bans gambling and open chat.
- Poop humour itself passes: portals host Poop Clicker, Royal Flush Merge and Skibidi
  games. Every such title uses a euphemism, though; none contains a swear word.

So the plan is a "clean" build from the same code:
- a renamed title, with "shit" also removed from achievement and boss names;
- emote-only chat;
- no slots, and probably no worm stock market;
- no public AI API links.

shiteven.fun itself stays as it is.

**Engineering (Claude does it):**
- Split the single world into capped rooms.
- Label bots honestly. Mope.io's fake "full" servers coincided with its decline.
- Add the CrazyGames SDK: rooms, invite links, instant multiplayer.
- Run a load test.
- Add a neutral age screen on shiteven.fun, with preset chat only for under-13s, and
  update its privacy policy for the amended COPPA rule (compliance date April 22, 2026).
- Never let players buy the slot currency. California AB 831 and *Kater v. Churchill
  Downs* (a federal appeals case under Washington law) make paid slot currency a
  gambling risk.

**What it takes:**
- About 45k–215k portal plays a month, roughly 10–50 average concurrent players,
  for $200/month.
- Best case is 3–4 months to the first $200 month; realistically 6+ months.
- Costs about $15/month for a server.

**Risks:**
- The game fails the trial.
- Rooms are empty at launch.
- Ad rates in the research are old or anecdotal.
- Income decays without content updates.

### Owner decision (2026-10-08): the name stays "Shiteven" everywhere

There will be no renamed portal build, which makes Poki and Playwire/Freestar
unavailable. The title probably rules out CrazyGames too: it requires PEGI 12, and no
listed game there or on Poki has a swear word in its title. A submission with the
name kept costs only time, so it is worth trying if the owner accepts emote-only chat
and no slots in that build.

Revised order:
1. **Own domain.** Add supporter perks and cosmetics through Ko-fi or Stripe; these are
   open as-is. Then add ads (AdSense with restricted serving, or AdinPlay) once traffic
   justifies them.
2. **Traffic.** The name is a meme asset. Use short gameplay clips (the game already
   records sessions), Reddit's web-game communities, iogames.space, and itch.io and
   Newgrounds listings that link to the site. The owner posts; nothing is automated.
3. **Compliance before ads or payments.** Add an age screen, preset chat for
   under-13s, and an updated privacy policy.
4. **Optionally, a CrazyGames submission with the name kept.**

Expected income is lower than the portal plan and depends on current traffic, which
is still unknown.
