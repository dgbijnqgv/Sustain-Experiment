# Shiteven marketing strategy

October 2026. Shiteven is a separate brand from Big Taro Games.

## Starting point

- **Players:** none today. Historically about 10 a day, 300 unique players in total,
  and a peak of 7 at once, all from the owner's school.
- **Live site vs GitHub:** 41 of 43 client files on shiteven.fun match the GitHub copy
  byte for byte. Only `privacy.html` and `terms.html` differ.
- **Constraints:**
  - The name stays.
  - No portals (Poki/CrazyGames).
  - About 2 owner-hours a week; playtesting doesn't count toward that.

## Why this strategy

- **What grew .io games:** YouTube for Agar.io, Slither.io and ZombsRoyale. Shell
  Shockers spread through school Chromebooks (39% of its players, mostly aged 10–15).
  Small games get their launch spikes from Reddit (13k–37k views or plays).
- **Shiteven's only proven channel** is word of mouth at a school.
- **Its one unique asset** is the public AI-play API: LLMs can join a live arena and
  fight bosses and humans. The "AI Tournament" is already announced as coming soon.

## The strategy: "AIs throwing poop at each other"

1. **Measure first (week 1).**
   - Count visits, play starts, minutes played, next-day returns and peak concurrency.
   - Record where players came from using `?ref=` links.
   - Everything stays server-side, with no third-party trackers and IPs hashed daily.
   - Without this, no channel can be judged.
2. **The AI Tournament as the hook (weeks 1–3).**
   - Launch a weekly bracket in which different AI models play live through the
     existing API, each clearly labelled.
   - Add a public results page and auto-recorded highlight clips.
   - Anyone can enter their own bot through the API.
   - Claude runs it autonomously on the cheapest model tier, at a few dollars a month
     of plan API credits.
   - Audience: developers and AI-curious people on X, Reddit (r/LocalLLaMA,
     r/ClaudeAI, r/singularity), Hacker News and YouTube. The crude name helps here.
3. **Clips (ongoing).**
   - A GitHub Actions job records the real client spectating bot and AI fights and
     cuts 15–30 second vertical clips.
   - The owner posts 2–3 a week to YouTube Shorts and TikTok (TikTok requires users
     to be 13+).
   - Claude drafts the captions.
4. **One launch week, then little upkeep.** Owner posts drafted by Claude to:
   - r/WebGames, r/iogames and r/playmygame;
   - iogames.space and other .io list sites;
   - an itch.io page linking to the site;
   - a "Season 2 / AI invasion" message to the original school players.
5. **Monetize only after measured return play:**
   - supporter perks and cosmetics via Ko-fi or Stripe;
   - then ads (AdSense restricted serving or AdinPlay);
   - before either, an age screen, preset chat for under-13s and a privacy update.

## Owner time per week

About 1.5–2 hours:
- 30 minutes posting clips;
- 30 minutes replying on Reddit, Discord and in comments;
- deploying builds Claude prepares;
- the launch week takes a few hours more.

## Honest odds

- **Most likely:** a launch spike of hundreds to a few thousand visits, then a small
  core of returning players.
- **Chance of $200/month within 12 months:** roughly 10–20%.
- **Upside:** an AI-tournament clip spreading on X or Hacker News.
- **Risks:**
  - School web filters may block a profane domain.
  - The kid-heavy audience brings COPPA duties.
  - Retention without friends present is unproven.

**Status (2026-10-09): parked.** The owner won't spend time on shiteven, and the AI API
isn't to be the focus. Without owner time to post or deploy, there is no viable route.
