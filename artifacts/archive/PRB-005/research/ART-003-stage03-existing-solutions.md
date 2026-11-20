# ART-003 — Stage 03 Existing Solutions & Gap Analysis

| Field | Value |
|---|---|
| **Artifact ID** | `ART-003` |
| **Purpose** | Fairly evaluate existing software, platforms, and DIY workarounds across `NEED-01`..`NEED-06`, assess non-build alternatives, and isolate genuine evidenced gaps suitable for a solo backend-leaning developer. |
| **Status** | `approved` |
| **Owner** | `Agent 03 (Existing Solutions & Gap Analyst)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`, `ART-002`, `EVIDENCE_LEDGER.md` (`SRC-004`..`SRC-028`, `FND-001`..`FND-013`) |

---

## Assumptions & Limitations

- **Pricing & tier stability:** SaaS pricing (`Kahoot!`, `Luma`, `Meetup`, `Paired`, `StoryGraph`) changes frequently by region and promo cycle; all cited figures reflect sources accessed `2026-11-19` (`SRC-015`, `SRC-018`, `SRC-023`–`SRC-028`).
- **Unverified edge competitors:** Niche indie apps (e.g., newer Discord Activities or regional trivia sites) were not exhaustively benchmarked for internal architecture; gaps reflect documented mainstream incumbents and user workarounds.

---

## Content

### 1. Existing-Solution Landscape & Comparison Matrix

| Need Area | Existing Solution / Workaround | Target Users | Core Verified Capabilities | Verified Pricing / Licensing | Key Strengths | Evidenced Limitations & Tradeoffs | Sources |
|---|---|---|---|---|---|---|---|
| **NEED-01: Live / Browser Party & Trivia Play** | **Jackbox Party Packs** | Friend groups, streamers, remote parties | Host streams main screen; up to 8 active players + Audience join free via phone browser (`jackbox.tv`). | One-time pack purchase per host; guests free. | Polished comedy/writing; zero guest accounts; proven social hit. | Requires video stream (Discord/Zoom lag hurts buzzer/timing games); 8-player active cap; fixed pre-written prompt packs wear out. | `SRC-011`, `SRC-018` |
| **NEED-01** | **Gartic Phone / skribbl.io / Codenames Online** | Casual friend groups & online communities | Instant room link, zero-account browser play, mobile-responsive (`codenames.game`), drawing/word play. | Free (ad/donation supported). | Zero friction link-join; huge mainstream appeal. | Mobile browser viewport/keyboard zoom & scroll bugs (`skribbl`/`Gartic`); WebSocket drops boot players mid-round without resilient state replay. | `SRC-009`, `SRC-010`, `SRC-024` |
| **NEED-01 / NEED-03** | **Kahoot! (vs. Quizizz / TriviaMaker / Discord bots)** | Classrooms, pub quizzes, teams, communities | Polished live trivia with phone-controller PINs, leaderboards, question banks. | Free capped at **10 players** (personal) / **3 players** (business custom); paid tiers + annual lock-in for 50–100+ hosts. | Iconic game-show energy and instant PIN entry. | Harsh free player caps push casual/community hosts into expensive annual plans or ugly Discord bots lacking live game-show UX. | `SRC-018` |
| **NEED-02: Async & Casual Tabletop / Puzzles** | **Board Game Arena (BGA)** | Hobby & casual boardgamers | 1,000+ licensed games; browser real-time & async turn-based; cross-device progression. | Free join/play; host-pays **Premium** (a few $/mo) for Premium titles. | Huge licensed catalog; fair host-pays model. | Cramped/inconsistent mobile touch UX for heavy games; freeze-induced unfair timeout/karma penalties; multi-week async games ruined by ghosting. | `SRC-012`, `SRC-013`, `SRC-014`, `SRC-023` |
| **NEED-01 / NEED-03** | **NYT Games (Wordle / Connections)** | Broad mainstream daily players | Sub-5-min daily puzzles, browser-first, spoiler-free emoji sharing grids, streaks/stats. | Wordle free; full archive/ecosystem bundled in NYT subscription. | Unmatched daily habit (`4.2B` Wordle solves/yr; `9M+` daily Connections players) & group-chat ritual. | Primarily **solo** play + post-hoc emoji text paste; limited real-time co-op, custom friend challenges, or multiplayer twists. | `SRC-007`, `SRC-008` |
| **NEED-03: Casual Learning** | **Duolingo** | Mainstream language/music/math learners | Bite-sized gamified lessons, streaks, XP leagues, AI content scale. | Freemium (ad/energy limits) + Super/Max subscriptions. | 52.7M DAU / $1.037B revenue (`SRC-004`); 84% CURR. | Punitive streak anxiety, XP-grind leagues, and restrictive free energy/lives fuel learner burnout; mostly solitary rather than joyful group play. | `SRC-004`, `SRC-005`, `SRC-006` |
| **NEED-02 / NEED-05: Coordination & Taste Decision** | **When2meet / Partiful / Group Chats / Swipe Clones** | Friend groups, couples | Zero-account grid (When2meet); meme/SMS invites (Partiful); shared swipe match (indie apps). | Free (When2meet/Partiful core). | Zero friction (When2meet) or high vibe (Partiful). | When2meet is 2005 desktop-era & has zero aftercare; Partiful feels over-produced/privacy-heavy for casual hangs; standalone swipe apps forgotten after 1–2 uses. | `SRC-016`, `SRC-017`, `SRC-021` |
| **NEED-05: Couples Rituals** | **Paired / Agapé / Gottman Card Decks** | Couples (local & long-distance) | Daily prompt/quiz unlock (`Paired`), research-backed free decks (`Gottman`). | `Paired`: 1 free daily Q, ~$79.99/yr Premium; `Gottman`: 100% free. | Low entry; `Gottman` proves high quality can be free. | Subscription apps feel like repetitive "homework" with asymmetric backlog guilt; physical/free decks lack real-time shared playfulness or media richness. | `SRC-020`, `SRC-027` |
| **NEED-04: Group Hobby & Spoiler-Safe Tracking** | **Goodreads / StoryGraph / Fable / Owlbear Rodeo / Google Sheets** | Book clubs, casual TTRPG groups, hobbyists | Book stats (`StoryGraph`: free + $49.99/yr Plus); buddy reads (`Fable`); minimalist VTT (`Owlbear`: free tier + storage tiers). | Generous free tiers + modest storage/analytics upgrades. | `Owlbear Rodeo` nails <5-min low-prep VTT; `StoryGraph` nails personal stats. | Book apps leak spoilers or lack anonymous group polls/pace locks, pushing clubs to DIY Google Sheets; heavy VTTs (`Roll20`/`Foundry`) cause prep burnout. | `SRC-021`, `SRC-026`, `SRC-028` |
| **NEED-06: Local Clubs & Third Places** | **Meetup / Luma / Heylo / Discord / FB Groups** | Local hobby organizers & newcomers | Event discovery (`Meetup`), modern RSVP/calendar (`Luma`: free forever for free events), club chat (`Heylo`). | `Meetup`: $175–$300+/yr hikes + Meetup+; `Luma`: free for free events, 5% on tickets ($59–$69/mo Plus). | `Luma` and `Heylo` already deliver strong free organizer UX (`SRC-025`). | `Meetup` pricing alienates clubs; yet **new local discovery platforms still face brutal geographic cold-start & trust/safety burden** for a solo dev. | `SRC-015`, `SRC-025` |

---

### 2. Build-vs-Adopt / Configure Evaluation (Non-Software & Existing-Tool Check)

Before concluding any gap warrants a new web app, each need area is tested against non-build alternatives:

1. **Local Club Discovery & Scheduling (`NEED-06` & pure calendar polling in `NEED-02`):**
   - *Verdict:* **Adopt/Configure existing tools (`Luma`, `Heylo`, `Discord`, native chat polls).**
   - *Why:* `Luma` is already free for free events with calendar sync, SMS/WhatsApp reminders, and co-hosts (`SRC-025`), and `Heylo` already serves free recurring clubs (`SRC-015`). Building another standalone When2meet or Meetup clone faces severe retention decay (for scheduling utilities) or geographic cold-start/moderation impossibility (for a solo developer).
2. **Watch-Party Video Synchronization (`FND-009`):**
   - *Verdict:* **Do NOT build.** Browser DRM/HDCP intentionally breaks third-party stream capture (`SRC-019`), and `Teleparty` already handles account-matched sync.
3. **Casual TTRPG Battlemaps (`NEED-04` subset):**
   - *Verdict:* **Adopt `Owlbear Rodeo` (`SRC-026`)** for pure map/token tabletop play—it already solved the low-prep VTT gap well.
4. **Pure Daily Word/Puzzle Clones (`NEED-01` subset):**
   - *Verdict:* **Do NOT build a generic Wordle clone.** NYT Games dominates solo daily habits (`SRC-007`, `SRC-008`). Opportunity exists only where **live/micro-async multiplayer, group reliability, shared state, or cooperative/social delight** is broken today.

---

### 3. Evidenced Gaps & Opportunity Areas (Mapped to `FND-NNN` & Developer Fit)

| Gap ID | Linked Needs & Findings |Genuine Unmet Gap (What Existing Tools Miss) | Solo Backend / Real-Time / Data-Reliability / Local-AI Fit |
|---|---|---|---|
| **GAP-01** | `NEED-01`, `NEED-02` (`FND-001`, `FND-002`, `FND-003`, `FND-004`) | **Resilient Mobile-First Group Party & Social Micro-Game Engine (Live + Drop-In Async):** Existing browser party/quiz games either break on mobile viewports & drop WebSocket state mid-round (`SRC-009`, `SRC-010`), lock 11–50 player groups behind annual SaaS paywalls (`SRC-018`), or trap async players in multi-week ghosting/unfair timeout penalties (`SRC-012`–`SRC-014`). No mainstream browser platform combines **zero-install link join + deterministic reconnect/state recovery + flexible live-or-daily-async turn pacing + fresh/customizable rounds** without 10-player paywalls. | **Exceptional fit:** Event-sourced / deterministic state machine, WebSocket reconnect hydration, zero-loss turn persistence, host-friendly room links, optional local AI for prompt/clue generation or bot fill-in when a friend drops. |
| **GAP-02** | `NEED-03`, `NEED-01` (`FND-010`, `FND-001`, `FND-003`) | **Joyful, Guilt-Free Social & Co-Op Casual Learning Rituals:** Dominant learning apps (`Duolingo`) monetize solo streak anxiety and energy limits (`SRC-004`, `SRC-006`), while quiz platforms (`Kahoot`) target classrooms/enterprises with 10-player caps (`SRC-018`). Mainstream learners lack **playful, forgiving co-op/duel browser rituals** (trivia, language, music/ear-training, visual/cultural literacy) where friends or casual circles learn together in 3–5 minute sessions without punitive streaks or classroom SaaS friction. | **Strong fit:** Authoritative spaced-repetition / mastery state + real-time head-to-head/co-op sync + anti-cheat/latency-fair scoring + optional local AI (WebGPU/WebLLM on capable devices) for adaptive explanations, pronunciation/hints, or custom topic decks without cloud LLM burn. |
| **GAP-03** | `NEED-04`, `NEED-05` (`FND-012`, `FND-006`, `FND-011`) | **Spoiler-Safe, Pace-Locked Shared Ritual Space for Media/Book Clubs & Friend Circles:** Book/watch/hobby groups resort to brittle Google Sheets (`SRC-021`) because Goodreads/Fable leak spoilers and lack anonymous group voting/pace-gating, while couples/friend apps feel like paid "homework" (`SRC-020`) and one-off swipe pickers are forgotten after one night (`FND-006`). What's missing is a **lightweight, stateful, spoiler-gated shared ritual table** (progress-locked reactions, blind reveals, mutual picks, season/club history) with zero homework guilt. | **Strong fit:** Access-controlled progressive reveal state (server-enforced spoiler locks per chapter/episode/round), real-time reveal moments ("everyone answered -> reveal together"), reliable shared archive, optional local AI for spoiler-safe recaps/discussion sparks. |
| **GAP-04** | `NEED-05`, `NEED-02` (`FND-005`, `FND-006`, `FND-011`) | **Zero-Guilt Asynchronous Micro-Games & Shared Taste Loops for Couples / Close Dyads:** Existing couples apps (`Paired`) charge ~$80/yr for canned daily prompts that create backlog guilt (`SRC-020`, `SRC-027`). Yet free `Gottman Card Decks` is static and solo-screen only. Dyads want playful, asymmetric-safe micro-rituals (predict-your-partner, collaborative taste/bucket boards, quick playful challenges) with zero backlog shame. | **Moderate–Strong fit:** Low-ops persistent state, real-time/async reveal sync; however narrower audience breadth than broader friend/party/casual-learning groups unless framed for *both* couples and best friends. |
| **GAP-05** | `NEED-06` (`FND-007`, `FND-008`) | **Zero-Fee Local Hobby Club Matchmaking / Recurring Table Organizer:** `Meetup` fee hikes pushed organizers out (`SRC-015`), but `Luma` and `Heylo` already cover free event RSVPs well (`SRC-025`). Remaining gap is matching solo newcomers to recurring micro-tables (board games, language tables, running/book circles) without platform fees. | **Weak solo-dev fit:** Heavy geographic cold-start density requirement and real-world trust/safety/moderation risk (`FND-007`, `FND-008`). |

---

## Next Steps / Unresolved Issues

- **Stage 03 Gate Check:** All major incumbents (`Jackbox`, `Gartic Phone`, `skribbl.io`, `Codenames`, `Kahoot`, `BGA`, `NYT Games`, `Duolingo`, `When2meet`, `Partiful`, `Paired`, `Gottman`, `StoryGraph`, `Owlbear Rodeo`, `Meetup`, `Luma`) are fairly evaluated with verified `SRC-NNN` citations; non-build alternatives are explicitly separated (`GAP-05` / watch-party DRM / pure scheduling clones); gaps trace cleanly to `NEED-01`..`NEED-06`.
- **Next Stage:** Hand off to **Agent 04 (Root Cause & Problem Analyst)** to separate symptoms from structural root causes (`RCA-NNN`) and formulate crisp, testable problem statements (`PRB-NNN`).
