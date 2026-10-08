# .io game monetization: research notes for shiteven.fun

Researched 2026-10-08. **Method caveat:** direct page fetches were blocked by the sandbox's egress policy, so every fact below comes from search-engine snippets of the cited pages. Labels used: **[V]** = stated on the platform's own page or in a primary news report; **[C]** = a developer's or seller's own claim, or a third-party guide; **[old]** = from before 2024.

## 1. Portals (CrazyGames, Poki, GameDistribution)

**CrazyGames**
- **Your own servers are expected.** The FAQ says "we only host the game files. For multiplayer servers, you'll need your own solution" [V] (https://docs.crazygames.com/faq/). Bots, lobbies, and region/latency routing are therefore the developer's job. The docs have no rules on bots or regions [V, absence].
- **Launch stages.** Basic Launch lasts 7–21 days. It ends at 7 days plus 500 plays, or automatically at 21 days. Monetization is off during Basic Launch. Promotion depends on playtime, conversion to gameplay, and retention, all benchmarked against other games [V] (https://docs.crazygames.com/resources/basic-launch-metrics/, https://docs.crazygames.com/requirements/intro/). One third-party guide says multiplayer games that need a larger audience can skip Basic Launch [C] (https://portalready.world/portals/crazygames/).
- **Multiplayer requirements for Full Launch.** The SDK must report the room (`updateRoom`, `isJoinable`). The game also needs invite links, the "Instant Multiplayer" flow, rooms that persist across rounds, a `disableChat` preference, and mandatory chat moderation (at minimum a profanity filter) [V] (https://docs.crazygames.com/requirements/multiplayer/).
- **Money.** Full Launch is required, along with the SDK, no non-SDK ads, and no other portal's branding. Payouts are monthly with a €100 minimum. Exclusivity is not required [V] (FAQ). The main docs publish no revenue split. The only published figures, 60% of ads and 70% of IAP to the developer, come from the terms of a 2026 game jam [C] (https://app.cinevva.com/guides/publish-game-crazygames). IAP runs through Xsolla and is invite-only [C].
- **Scale.** CrazyGames claims 50M+ monthly players [C]. An independent report put it at 35M MAU in early 2025 [V] (https://gamesbeat.com/crazygames-hits-35m-users-for-browser-games-and-launches-social-multiplayer-features/).
- **Early traffic for a new game.** One 1v1 .io game reported 6,100 impressions on day 2 at a 0.4% CTR, which is only about 25 plays [C] (https://fxf8.itch.io/larss-io/devlog/1586849/launching-a-1v1-strategy-game-on-crazygames-04-ctr-and-what-im-learning). An unverified comment reports 4,350 plays by day 3 [C] (https://www.youtube.com/watch?v=5L8yAej08Rk).

**Poki**
- **External servers are allowed once approved.** Outgoing requests are blocked by default. Multiplayer games on external servers are exempt after Poki approves them through the Custom CSP setting, and they must supply a privacy statement [V] (https://sdk.poki.com/requirements). The optional Netlib is P2P/WebRTC, alpha quality, and has no lobby discovery [V] (https://github.com/poki).
- **Restrictions.** Only Poki ads are allowed. UI for buying currency or removing ads must be stripped out. Username entry needs a strict profanity filter. Chat and UGC need prior approval [V] (https://sdk.poki.com/new-requirements). A third-party summary adds "web exclusive", "kid-safe, no gambling", and "no IAP" [C] (https://x.com/autonom_games/status/2069642887164510699).
- **Split.** Poki keeps 50% of revenue from traffic it brings. The developer keeps 100% of revenue from traffic they bring themselves. Non-exclusive games get a one-time license fee instead [V] (https://sdk.poki.com/deals).
- **Scale.** 1B plays/month (June 2025). Top developers earn $50k–$1M per year [V/C, Poki PR] (https://app.dealroom.co/news/feed/poki-hits-1b-monthly-plays-as-developer-first-model-boosts-top-studio-revenues-tenfold-1). Only 227 new games were added in 2025, so curation is tight [C] (https://mobidictum.com/pokis-web-gaming-interview-michiel-van-amerongen/).

**GameDistribution (Azerion):** No current split or multiplayer rules were found. A secondhand figure gives €0.3–0.9 per 1k plays for 2019–21, skewed to tier-3 countries [C, old] (https://github.com/pocketagent98-ai/html5-game-opportunity-report). There are unverified forum complaints about missing payouts (https://tools.malwaretips.com/url-scan/html5.gamedistribution.com).

**Revenue per play on portals**
- About $5 per 1k plays on CrazyGames (50k plays ≈ $250) [C, secondhand] (GitHub report above).
- €1.20 per 1k plays from 451k CrazyGames plays across eight single-player games [C, old] (https://donislawdev.com/earnings-and-statistics-from-my-8-games-android-ios-webgl/).
- A guide estimates $200–2,000 per month for a "well-performing" portal game [C, unsourced] (https://app.cinevva.com/guides/web-game-monetization).
- Working range used below: **$1–5 per 1k plays**, with US and Chromebook traffic at the top of the range.

## 2. Ads on your own domain

| Network | Entry bar | Notes |
|---|---|---|
| AdinPlay (Venatus since 2023) | Unpublished. A review says it favors established portals and that solo devs struggle; one dev waited weeks with no reply [C] | Golf Royale (.io): ~870k impressions (250k video) ≈ **€400 total**; CPMs about **€1.2 video / €0.25 banner** [C, old] (https://www.indiehackers.com/post/how-much-money-i-made-serving-ads-to-120k-users-on-my-free-game-d221dc674c, https://forum.codergautam.dev/t/monetizing-a-game-with-adinplay-how-ads-revenue-work/17532) |
| Google H5 Games Ads (Ad Placement API / AFG) | Closed beta, discretionary approval [V] (https://developers.google.com/ad-placement/docs/beta). Golf Royale was told the minimum was 5M non-iframed impressions per month [C, old] | Gives AdSense sites interstitials and rewarded ads, which are otherwise restricted [V] (https://support.google.com/publisherpolicies/answer/11975916) |
| Playwire | 500k pageviews/month, or 1k DAU for apps [C, FAQ mirror] (https://backiee.wasmer.app/https_www_playwire_com/faq) | Out of reach for this site |
| Venatus | Unpublished. One source claims about 500k PV [C] (https://blog.nitropay.com/nitro-vs-playwire-vs-venatus-which-ad-network-is-right-for-gaming-publishers/) | Out of reach for this site |
| Nitro (Overwolf) | 100k views/month [C, Nitro blog]; net-7 payouts [V] | Built for wikis and guide sites; fit for game sites unclear |
| CPMStar | Open | Golf Royale got 60k impressions ≈ **$10** [C, old] |

- **Per player:** Golf Royale's 120k portal-referred uniques earned about €3.3 per 1k uniques in total.
- **Per session:** two banners plus one video per session works out to roughly $1.5–2.5 per 1k sessions at the CPMs above. Treat this as an estimate.
- **Comparison:** this is equal to or below what portals pay, and portals also bring the traffic.

## 3. Other revenue

- **Payer conversion.** I found no .io-specific number. The benchmarks are 2–5% for Facebook Instant Games, with ARPDAU of $0.05–0.50 [V, Meta guidance] (https://developers.facebook.com/documentation/games/monetize/best-practices), and 1.83% of mobile gamers paying [C, Unity via Xsolla] (https://xsolla.com/blog/ways-to-maximize-web-game-revenue). An anonymous no-signup web game will almost certainly convert at the low end of these, below 1% [my inference].
- **Real .io models.** Slither.io charged $3.99 to remove ads and sold no power-ups [V] (https://en.wikipedia.org/wiki/Slither.io). Shell Shockers is "majority ads, but also cosmetics" [V] (https://newsletter.gamediscover.co/p/deep-dive-shell-shockers-multi-million). Krunker runs a paid skin economy [C]. A Flippa-listed browser FPS with "1M users" sells ads plus virtual currency for **$3,333/month profit**. Its revenue has been falling since 2024 [C, seller] (https://flippa.com/12102696).
- **Portal compatibility.** Poki forbids IAP and ad-removal purchases. CrazyGames IAP is invite-only. Stripe, Ko-fi, or Patreon only work for traffic on your own domain. I found no published Patreon or Ko-fi totals for an .io game.
- **Legal flag.** California AB 831 bans dual-currency sweepstakes casinos and took effect 2026-01-01 [V] (https://sbcamericas.com/2025/10/14/newsom-signs-california-sweepstakes-ban/). The slot machine stays safer if its currency **can never be bought for or redeemed into money** [my inference]. Selling the slot's coins is the riskiest monetization option open to shiteven.

## 4. Costs and scaling

- **VPS prices.** Hetzner raised cloud prices 30–43% on 2026-04-01 [C, tracker] (https://agentdeals.dev/hetzner-pricing-2026). CPX11 went from about €3.85 to €5.49 per month excluding VAT. A September 2026 post says the cheapest regular plan is now CPX12 (1 vCPU, 2 GB) and that the CX line is unavailable [C] (https://www.vincentschmalbach.com/hetzner-cheap-cloud-unavailable-price-increases/). Hetzner includes about 20 TB of traffic per month [C]. Budget **$6–15/month per server**. DigitalOcean and OVH are similar at this tier (not checked in this pass).
- **Players per server.** Slither.io's hardest problem was making each server stable at 600 players [V, interview] (https://www.pocketgamer.com/articles/070063/r/). A Flippa listing advertises 250 players per server [C] (https://flippa.com/12800116). At shiteven's scale, one small VPS should hold 50–200 CCU if the code is efficient. Bandwidth (binary/msgpack deltas) usually becomes the limit before CPU does [C] (https://lowendtalk.com/discussion/comment/1103595/). This needs a load test with bot clients.
- **How small devs scale.** Run one Node process per room with a player cap and spawn a new room when it fills. CrazyGames' `updateRoom` model assumes this pattern. Add a second region (US-East plus EU) only when sustained CCU exists in both. Spreading a small population across many rooms or regions empties them, so consolidate first [C] (https://velthorite.com/blog/why-your-multiplayer-game-dies-at-100-players-and-how-to-fix-it-before-launch).
- **Break-even.** At $1–5 per 1k plays, one ~$8/month VPS is paid for by about 2–8k plays per month. Server cost is not the constraint. Traffic is.

## 5. Case studies and traffic sources

- **Slither.io (2016):** more than $100k/day from ads and the $3.99 ad-removal purchase. This is a WSJ-reported claim by the developer [C] (https://www.loopinsight.com/2016/06/20/slither-io-game-goes-viral-brings-developer-100k-a-day/). Growth came from YouTube.
- **Agar.io:** became 2015's breakout hit largely through YouTube [V] (https://en.wikipedia.org/wiki/.io_games).
- **ZombsRoyale:** got PewDiePie and Jacksepticeye videos [V] (https://en.wikipedia.org/wiki/ZombsRoyale.io).
- **Shell Shockers:** "low seven figures annually," almost all from the web version. Its audience is 47.6% US, 39% on Chromebooks, and mostly aged 10–15 [C, founder] (https://newsletter.gamediscover.co/p/deep-dive-shell-shockers-multi-million). It passed 35M plays on CrazyGames by 2021 [C, PR] (https://europeangaming.eu/portal/latest-news/2021/08/20/98169/shell-shockers-passes-35-million-game-plays-on-crazygames-web-portals/). School Chromebooks and portals were its channels.
- **Krunker:** bought by FRVR in May 2022, claiming 200M+ players [V] (https://www.gamedeveloper.com/press-release/frvr-acquires-popular-free-to-play-shooter-krunkerio).
- **Mope.io, Starve.io, Diep.io:** bought by Addicting Games in 2020–21. Addicting Games, including ev.io, was then sold to Enthusiast Gaming for **$34.4M** [V] (https://investgame.net/news/enthusiast-gaming-acquires-addicting-games-for-34-4m/). Diep.io was resold to 3AM Experiences in 2024 [V] (https://en.wikipedia.org/wiki/Diep.io). The exit market is real but concentrated in a few buyers.
- **Small and mid-size listings:**
  - Golf Royale: 120k players and about €400 total, which the developer said was "enough to keep the servers running" [C].
  - A real-time multiplayer browser game with a CrazyGames partnership asked $7,999 [C] (https://flippa.com/12800116).
  - Hurricane.io reported about $660/month net [C] (https://flippa.com/11920317).
- **Failure modes.** Mope.io filled servers with bots showing fake "500/500" counts, which coincided with player and revenue decline [C] (https://medium.com/@GamingArchivist/mope-io-from-a-72-million-player-phenomenon-to-6-months-of-total-corporate-abandonment-and-the-0ddba0bc7d93). A forum thread says players judge games by visible population [C]. Lemnis Gate shut down on low CCU [V].
- **Traffic sources.**
  - YouTube: historically the main viral engine.
  - Reddit: one r/gamedev post gave knckout.io 13k views [C] (https://toucharcade.com/community/threads/beta-knckout-io-the-first-and-only-io-of-its-kind.311398/). Another developer had 37k plays in 3 months, "mostly Reddit/itch" [C].
  - iogames.space and other list sites: no traffic numbers found. Developers list on them by default [C] (https://phaser.discourse.group/t/our-phaser-game-jellobomb-club-launched-back-in-september/258).
  - TikTok: no 2024–26 .io case with numbers found.

## Bottom line for shiteven

**Most realistic path.**
1. Have Claude add room sharding (cap of about 30–50 per room), clearly labeled bots that keep each room at roughly 8+ entities, mobile touch controls, a profanity filter, and the CrazyGames SDK (ads, `updateRoom`, invites).
2. Submit to **CrazyGames first**. It needs no exclusivity, supports your own server, and the Basic Launch verdict comes within 7–21 days.
3. Before submitting, make a portal build that **removes or disables the slot machine** and mutes the crudest content. Poki is a long shot: it is kid-safe, bans gambling, and allows chat only with approval.
4. Keep shiteven.fun as the home for the full version, with an optional Ko-fi or Stripe "supporter" cosmetic. **Never sell the slot currency.**
5. Skip AdinPlay, Playwire, Venatus, and Nitro until the site has about 100k–500k monthly views.

**Required traffic.** $200 net plus about $15 in servers means roughly $215 gross. At $1–5 per 1k plays, that takes **45k–215k portal plays per month**. That is about **1,500–7,000 plays per day**, or roughly **10–50 average CCU** (peaks at 2–3×) at 10-minute sessions. On its own domain, the same $215 would take about 100k sessions per month, which is not achievable with no audience.

**Time.** The SDK and room work is about 1–2 weeks of Claude time. Basic Launch takes 1–3 weeks, and the first payout needs €100 and comes monthly. The best case is roughly **3–4 months to the first $200 month**. A realistic case is 6+ months, and that is only if the game passes CrazyGames' benchmarks. Most games don't, and failing them means income near $0.

**Main risks.**
1. Content and policy rejection: the poop theme, simulated gambling, and open chat on a portal whose audience is children (COPPA moderation load).
2. Cold start: portal players see empty rooms, so retention metrics fail.
3. A single shared world can't absorb a portal spike, so sharding is mandatory.
4. Ad rates in the sources are mostly anecdotal and partly from 2018–2020.
5. Revenue decays without updates (see the Flippa FPS listing). Two hours a week only covers admin if Claude ships the content updates.
6. Spend: budget about $10–15/month for servers. Nothing in this plan needs to exceed the $100 approval threshold.
