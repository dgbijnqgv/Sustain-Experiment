# shiteven.fun: policy fit for monetization routes (researched Oct 2026)

**Method:** official pages could not be fetched directly (proxy block), so quotes come from search extracts of those pages. Re-check the live wording. **Q** = quoted policy text. **Inf** = my inference.

## 1. Web portals

**CrazyGames**
- Q: "CrazyGames is a website for an audience aged 13 or more. Your game must be PEGI 12 compliant." (https://docs.crazygames.com/requirements/gameplay/). The FAQ lists "inappropriate themes or content" and "games that do not adhere to PEGI-12 guidelines" as initial-QA rejection reasons (https://docs.crazygames.com/faq/).
- Chat, Q: "We require you to add chat moderation. The simplest solution is a profanity filter… Your game should disable your chat based on the game settings. In case of complaints, we will require you to disable chat alltogether." (https://docs.crazygames.com/requirements/multiplayer/). SDK setting: `disableChat` (https://docs.crazygames.com/sdk/game/).
- Data: collecting data beyond the SDK requires a T&C/privacy notice (https://docs.crazygames.com/requirements/technical/).
- PEGI yardstick: PEGI 12 allows only "mild" bad language (https://pegi.info/what-do-the-labels-mean). Under PEGI's criteria that apply from June 2026, social-casino and free-to-play slot content rates **PEGI 18**, and paid random items rate PEGI 16 (https://pegi.info/news/pegi-expands-age-rating-criteria-interactive-risk-categories; https://esportslegal.news/2026/03/30/pegi-2026-new-risk-ratings/).
- Comparable games that are live: *Poop Clicker 2* (https://www.crazygames.com/game/poop-clicker-2), *Doodieman Voodoo* (https://www.crazygames.com/game/doodieman-voodoo), *You vs 100 Skibidi Toilets* (https://www.crazygames.com/dk/game/you-vs-100-skibidi-toilets) and *Skibidi Toilets: Infection* (https://www.crazygames.com/game/skibidi-toilets-infection). I found no live title with a swear word and no documented title rejection.
- Inf: scatological themes pass. A title containing "shit" probably exceeds "mild" language for PEGI 12 and is a likely rejection. "Sewer Slots" is the clearest blocker, because under the 2026 PEGI criteria it pushes the game to PEGI 18.

**Poki**
- Q, out of scope: "cheating, gambling, alcohol, or tobacco", along with sexual content and bullying (https://developers.poki.com/guide/content-player-safety). Q, deal terms ban "defamatory, discriminatory, obscene, inflammatory, racist, sexual… content" (https://sdk.poki.com/deals).
- Chat, Q: "Poki does not allow any chat systems in games with the exception of those covered by Poki Guardian, our moderation tooling that is slowly being rolled out to select games." Poki suggests an emoji system instead (https://sdk.poki.com/external-resources). Usernames, Q: "implement strict profanity filtering using the provided bad words list" (https://developers.poki.com/guide/requirements-quality).
- Comparable games that are live: *Royal Flush Merge*, where you fight poop monsters with plungers (https://poki.com/en/g/royal-flush-merge); *Hit the Fan*, which has "poop bombs" (https://poki.com/en/g/hit-the-fan); *Troll Toilet Quest 1/2*, sold on "bathroom humor" (https://poki.com/en/g/troll-toilet-quest-1); and *Skibidi Shooter* (https://poki.com/en/g/skibidi-shooter).
- Inf: poop humour is accepted when the title is a euphemism ("Hit the Fan", not the swear word). Open chat, slots and a profane title are each grounds for rejection on their own. Poki is the strictest portal.

**GameDistribution**
- Q, every submission is manually reviewed by "content specialists". The guidelines restrict explicit alcohol, drug or sexual references, discriminatory material and excessive violence. For "games with user-input content, such as custom player names or chat options, mechanisms should be in place to prevent the use of inappropriate language" (https://static.gamedistribution.com/developer/developers-guidelines.html).
- Inf: GameDistribution syndicates to thousands of sites, many of them kids' sites, so expect it to treat slots and a profane title as "unclear-to-no". The existing filtered chat may pass.

**GamePix**
- Q: games "must not contain… explicit or suggestive content". Also no external links, external analytics, third-party SDKs or privacy-policy links (https://partners.gamepix.com/guidelines/submission). The site ToS bars "vulgar, obscene, or offensive" user content (https://company.gamepix.com/vg5-terms-of-service/).
- Inf: the no-external-links/SDK rule may clash with the LLM HTTP API and an external game server. Ask GamePix before submitting.

**itch.io**
- Itch does not curate game content for profanity. Its 2025 crackdown targeted sexual content; creators must follow their payment processors' acceptable-use policies (https://itch.io/updates/update-on-nsfw-content; https://techcrunch.com/2025/07/27/itch-io-is-the-latest-marketplace-to-crack-down-on-adult-games/).
- Inf: itch can host the game **as-is**. Income is pay-what-you-want or donations only. Comparable games: the "tag toilet" listings (https://itch.io/games/free/tag-toilet) and *Fart Game* (https://megalithic-mainframe.itch.io/fart-game).

**Newgrounds**
- Rating guide, as summarised on the fan wiki: E allows "damn, hell, crap and turd". T allows "shit" (https://newgrounds.wiki.gg/wiki/Age_Ratings).
- Inf: the original game fits a **T rating** on Newgrounds. Newgrounds is good for exposure, but income is limited to small ad revenue share or Supporter perks; the payout details come from a fan wiki and may be out of date (https://newgrounds.fandom.com/wiki/Revenue_Sharing).

## 2. Ad networks

**Google AdSense / Ad Manager / H5 Games Ads (AFG)**
- Shocking-content Publisher Restriction, Q: covers content that "prominently features obscene or profane language", e.g. "swear or curse words, variations and misspellings". Its gruesome-content examples include "human or animal waste". The result is **restricted ad serving**, not a ban (https://support.google.com/publisherpolicies/answer/10437538).
- Online gambling restriction, Q: applies to "real-money gambling… where money or other items of value are paid or wagered… to win real money or prizes" (https://support.google.com/publisherpolicies/answer/10437963). Inf: free slots with no prize do not appear to trigger this restriction. Google's *advertiser* policy defines social casino as "simulated gambling… no opportunity to win something of value" (https://support.google.com/adspolicy/answer/15132179).
- User content, Q: if a page runs ads, "all of the content on those pages, including comments, must follow the Publisher Policies". Violations lead to ad removal at page level and then site level. Google ads are also barred from pages where live chat is the "primary focus" (https://blog.google/products/adsense/your-guide-user-generated-content/; https://blog.google/products/adsense/manage-risks-associated-with-user-comments/).
- H5 Games Ads: AdSense policies apply; application/beta, approval "not guaranteed" (https://adsense.google.com/start/h5-games-ads/; https://developers.google.com/ad-placement/docs/beta).
- COPPA: AdSense lets you tag a site or ad request for child-directed treatment. Google may also treat a site as child-directed on its own (https://support.google.com/adsense/answer/3248194).
- Inf: AdSense is **open as-is in principle**, but the title and toilet content will likely be "restricted", which lowers fill and eCPM. H5 Games Ads approval with a profane domain is doubtful.

**AdinPlay and other .io networks**
- AdinPlay (owned by Venatus) is the main .io ad network (paper.io, skribbl.io). It publishes no content policy, and approval is manual (https://adinplay.com/about; https://www.applixir.com/adinplay-alternatives-for-web-game-developers-2026/).
- Venatus, Q: sites must "pass a stringent human audit process"; bans hate speech, drugs, firearms, adult content (profanity not listed) (https://www.venatus.com/brand-safety).
- Playwire bans content that "promotes profanity, expletives, or inappropriate language" (https://www.playwire.com/code-of-conduct).
- Freestar requires brand-safe content without "profane speech", and moderation of all monetized UGC (https://freestar.com/publisher-quality-requirements/).
- Inf: whether AdinPlay or Venatus would accept the game is **unclear** and needs an enquiry. Playwire and Freestar are **no** while the title is profane.

## 3. Payments

- **Stripe**, Q: prohibits "games of chance including gambling, internet gambling, casino games, sweepstakes and contests… with a monetary or material prize". It restricts "sale of in-game currency or game items, unless the business is the operator of the virtual world" (https://stripe.com/legal/restricted-businesses). Inf: selling cosmetics or currency as the game's operator is allowed. Slots that pay out nothing of value are not a prize game, **unless** paid currency can be wagered in them (see Kater below).
- **Ko-fi**: content offered for sale must follow Stripe's and PayPal's policies. The terms restrict "raffles, lotteries, giveaways or games of chance where a fee is…" (https://help.ko-fi.com/hc/en-us/articles/360007937553-Ko-fi-Content-Guidelines; https://more.ko-fi.com/terms). Inf: donations and supporter tiers are fine as-is.
- **Xsolla**: Xsolla reviews games for "adult content… and other prohibited or restricted content". The publisher is "solely responsible" for legal compliance of "skill-based games, loot boxes, and virtual currencies" (https://xsolla.com/terms-of-use; https://developers.xsolla.com/get-started/work-in-pa/legal-aspects/). Inf: Xsolla's content review is unclear for this game. Its main use would be a web shop for cosmetics.

## 4. Legal (California operator)

- **COPPA:** the amended Rule has been in force since June 23, 2025, and the compliance deadline was **April 22, 2026** (https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect). Persistent identifiers, including IP addresses, count as personal information. Collecting them only to support internal operations is exempt (https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312). Letting a child make personal information public, which open chat does, counts as "collection" unless the operator deletes "all or virtually all" personal information before posting (https://www.law.cornell.edu/cfr/text/16/312.2). The "directed to children" factors include subject matter, animated characters and audience composition (https://www.lw.com/en/insights/ftc-publishes-updates-to-coppa-rule).
  - Inf: cartoon poop humour attracts kids, which is a real risk factor. Minimal compliance:
    - add a **neutral age screen** (enter birth year, no default, no hint about the "right" answer);
    - for under-13s, disable free chat (presets or emotes only), avoid storing their IP beyond session or anti-abuse needs, and send child-directed ad tags;
    - **state in the privacy policy** what is collected (IP, approximate geolocation for factions, chat logs, LLM API data) and how long it is kept;
    - offer a contact point for parental deletion requests.
- **CCPA:** applies only above **$26,625,000** in revenue (2025–26), or if the business buys, sells or shares the personal information of 100,000 or more consumers, or earns 50% or more of revenue from selling it (https://cppa.ca.gov/announcements/2024/20241217.html). Inf: out of scope on revenue; very large audiences with behavioural ads could hit the 100,000 "sharing" test.
- **CA Digital Age Assurance Act (AB 1043):** from **Jan 1, 2027**, app developers must request and apply OS age signals. The website API requirement was dropped (https://en.wikipedia.org/wiki/California_Digital_Age_Assurance_Act; https://www.alstonprivacy.com/california-enacts-digital-age-verification-law/). Inf: minimal effect on a browser game.
- **Simulated gambling:**
  - California has no loot-box statute. *Mai v. Supercell* held that loot boxes are not "slot machines" under the California Penal Code. The Ninth Circuit affirmed on standing grounds in 2024 (https://www.courtlistener.com/opinion/9602384/mai-v-supercell-oy/).
  - **AB 831 (2025)** targets sweepstakes casinos with cash-redeemable prizes (https://calmatters.digitaldemocracy.org/bills/ca_202520260ab831).
  - **The risk:** *Kater v. Churchill Downs* (9th Cir. 2018) held that purchasable virtual chips were a "thing of value" under **Washington** law (https://law.justia.com/cases/federal/appellate-courts/ca9/16-35010/16-35010-2018-03-28.html). Inf: Sewer Slots is low-risk while currency is earn-only. Once currency can be bought, Sewer Slots becomes a social-casino mechanic, with exposure in WA, an 18+ PEGI rating, and closed doors on the portals. Keep paid currency out of the slots, or remove the slots.

## 5. The "clean build" variant

Proposed changes: rename to "Poop Battle .io", keep chat to preset emotes, and remove the slots. Inf, based on the policies above:
- **Poki:** this variant would now match accepted games (Royal Flush Merge, Hit the Fan). Emote-only chat is exactly what Poki recommends. Achievement and boss names with "Shit" still need cleaning. Plausible.
- **CrazyGames:** likely to pass PEGI 12. CrazyGames would even allow filtered text chat if it honours `disableChat`.
- **GameDistribution and GamePix:** likely acceptable. GamePix also needs the external links removed.
- **Earthworm Finance:** no gambling element as far as I can tell, so probably fine.
- **Geo-IP factions:** present them as region flags, not stored location. Portal SDKs and server logs should not keep IPs longer than necessary.
- **LLM API:** keep it on the developer's own domain, not in the portal build.

## Bottom line

| Route | Open as-is? | Changes needed |
|---|---|---|
| Own site + AdSense/Ad Manager | Unclear, leaning yes with restricted demand | Moderate chat or keep it off ad pages; add privacy policy; set child-directed tags for under-13s; expect lower eCPM from profanity/"waste" restriction |
| H5 Games Ads (AFG) | Unclear (beta, discretionary) | Clean title/domain improves odds; same policy fixes |
| AdinPlay / Venatus | Unclear | Ask directly; clean build safer |
| Playwire / Freestar | No | Remove profanity; moderate UGC |
| CrazyGames | No (title language, slots → PEGI 18) | Rename, remove slots, honour `disableChat`, profanity filter, privacy notice |
| Poki | No (chat, gambling, title) | Rename; emote-only chat; remove slots; scrub "Shit" from achievements and boss names; filter usernames |
| GameDistribution | Unclear, leaning no | Clean build; username/chat filtering |
| GamePix | No | Clean build; strip external links/SDKs/API calls |
| itch.io | Yes | Content warning tag; donations/PWYW only |
| Newgrounds | Yes (rated T) | None material; low income |
| Stripe / Ko-fi (donations, cosmetics) | Yes | Do not let purchased currency feed Sewer Slots |
| Xsolla web shop | Unclear | Content review; same slots caveat |
| COPPA / privacy compliance | Not compliant as-is (risk) | Neutral age gate; under-13 chat off; IP minimisation; privacy policy |
| CCPA | Not triggered (below thresholds) | Privacy policy and opt-out still advisable |
