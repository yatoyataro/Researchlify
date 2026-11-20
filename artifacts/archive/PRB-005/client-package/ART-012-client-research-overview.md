# ART-012 — Package B: Client Research Overview

| Field | Value |
|---|---|
| **Artifact ID** | `ART-012` |
| **Purpose** | Plain-language overview of research findings, prioritized problem (`PRB-005`), zero-cost product proposal, scope, limitations, and next steps for stakeholders. |
| **Status** | `approved` |
| **Owner** | `Agent 13 (Client-Facing Research Synthesizer & Humanizer)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`..`ART-011`, `DECISIONS.md` (`DEC-006`..`DEC-009`), `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-030`, `FND-001`..`FND-016`), `SKL-004`, `SKL-006` |

---

## Assumptions & Limitations

- All findings come from public desk research accessed on November 19, 2026 (`DEC-007`). No live user interviews, surveys, or usability tests have been run yet.
- Expected user retention numbers (`65%` completion, `35%` Day-7 return) are planning targets to test after launch, whereas market metrics (`52.7M` Duolingo DAUs, `9M+` NYT Connections players) and hosting quotas (`100K` free edge requests per day) are verified facts.

---

## Content

### 1. Project overview

This discovery project looked across mainstream consumer web categories to find fun, evidence-backed web app opportunities suited to a solo backend developer who specializes in real-time systems, reliable data handling, and optional on-device AI. Following a five-stage review and human priority selection (`DEC-008`), we chose to focus on casual learning engagement burnout (`PRB-005`) under a strict zero-money-cost rule (`DEC-009`) for development, production, deployment, and end users.

### 2. What we investigated

We examined five everyday consumer behaviors where people play, socialize, or learn online (`ART-001`, `ART-002`):
1. Browser party games and daily puzzle habits (`Wordle`, `Connections`, `Jackbox`, `Gartic Phone`, `skribbl.io`, `Board Game Arena`, `Kahoot!`).
2. Group hangout planning and shared decision tools (`When2meet`, `Partiful`, movie and restaurant pickers).
3. Casual learning apps and retention mechanics (`Duolingo` SEC filings, community reports, and trivia platforms).
4. Hobby and reading groups (`Goodreads`, `StoryGraph`, `Fable`, `Owlbear Rodeo`, custom Google Sheets).
5. Local community clubs and third places (`Meetup`, `Luma`, `Heylo`, U.S. Surgeon General and Pew Research studies).

We also verified technical constraints for running free web apps: mobile browser WebGPU support (`SRC-022`), open public-domain datasets (`SRC-029`), and free-tier cloud limits (`SRC-030`).

### 3. What we discovered

Four clear patterns stood out across 30 consulted sources (`EVIDENCE_LEDGER.md`):
- Millions of mainstream users enjoy quick daily browser games when they can start with one click and share results without spoilers. `Wordle` logged `4.2 billion` solved puzzles in 2025 (`5.3 billion` plays in 2024), and `Connections` draws more than `9 million` daily players (`FND-001`).
- Casual learning has huge paid and daily demand, led by Duolingo at `52.7 million` daily active users, roughly `130 million` monthly active users, and `$1.037 billion` in 2025 revenue (`SRC-004`). Yet its mid-2025 switch to a 25-point "Energy" battery that drains even on correct answers capped many free learners at 3 or 4 lessons and drew sharp pushback against streak pressure and paywalls (`FND-010`, `FND-014`).
- Casual quiz hosts face tight free limits. `Kahoot!` caps free personal hosts at `10` players and business custom games at `3` players (`FND-003`), while browser party games often break on mobile keyboards or drop players on brief Wi-Fi switches (`FND-002`).
- Zero-cost open content and hosting are practical for a solo builder. Public datasets like `Tatoeba` (`CC0 1.0`), `Wikidata` (`CC0 1.0`), `OpenTriviaDB` (`CC BY-SA 4.0`), and `Wiktionary` (`CC BY-SA 4.0`) supply free material (`FND-015`), and Cloudflare's free tier covers unlimited static bandwidth plus `100,000` daily Workers and Durable Objects requests (`FND-016`).

### 4. Why the problem matters

People want lighthearted daily curiosity and shared brain play with friends, yet existing tools push them toward two unpleasant choices: solo apps that guilt-trip them over missed days or drain an energy meter on right answers (`FND-014`), or live group quiz tools that cut off groups at 10 people (`FND-003`). When learning feels like a taxed chore, casual learners quit.

### 5. Existing solutions

No current free tool combines forgiving daily solo play, flexible friend rooms, and personal memory tracking (`ART-003`):
- `Duolingo` excels at mobile habit loops and breadth, but gates free learners with its Energy battery and centers on solitary streak pressure.
- `Kahoot!` delivers lively phone-controller quizzes, but locks larger friend groups behind paid plans and lacks spaced-repetition review.
- `NYT Wordle` and `Connections` nail zero-install daily sharing, but stay mostly single-player without personal memory tracking or live co-op rooms.
- `Anki` and Discord bots are free, but require heavy manual setup or lack polished mobile UX.

### 6. The problem we recommend addressing

We recommend solving `PRB-005`: helping mainstream casual learners and small friend circles enjoy quick, guilt-free daily and social learning in any browser, with zero energy bars, zero streak penalties, and zero per-player fees (`DEC-008`, `DEC-009`). Although pure party gaming (`PRB-001`) scored slightly higher on raw playfulness (`4.50` vs. `4.40`), `PRB-005` carried the strongest market evidence (`5/5`) and daily habit potential (`5/5`), flipping to first place under evidence-weighted scoring (`ART-005`).

### 7. Our proposed solution

We propose a browser-first web app with two connected ways to play (`ART-006`), both running at zero money cost:
1. A 3-to-5-minute Daily 5-Card Ritual that tracks what you remember locally in your browser without punishing missed days, and produces a spoiler-free emoji grid (`🟩🟨⬜`) to share in group chats.
2. Zero-account friend rooms for 2 to 30+ players via a short invite link, supporting both live synchronized rounds and 24-hour asynchronous rounds where busy friends play on their own schedule and compare results afterward.

### 8. What the proposed web application will do

At MVP launch (`ART-007`, `ART-008`, `ART-009`), the app will include:
- Two curated open-data tracks: *Phrases & Words in Context* (`Tatoeba CC0` and `Wiktionary`) and *World, Culture & Science Trivia* (`Wikidata` and `OpenTriviaDB`).
- Instant play with zero signup, using browser storage (`IndexedDB`) plus a one-click backup file or transfer code so progress moves between devices without a user database.
- Reconnect-safe multiplayer rooms powered by edge actors that keep scores accurate if a player's mobile signal drops and strip answer keys until each round closes.
- Mobile-safe screens built to WCAG 2.1 AA accessibility standards, with large tap targets and full keyboard support.
- Built-in card flagging so users can report confusing questions (`<= 5` per day) for cleanup in future updates.

### 9. Project scope

The MVP stays tight to protect solo build speed and the `$0` budget (`ART-006`):
- Included in Phase 1: the two open tracks, Solo Daily + Practice, Live and 24-hour Async rooms (`2` to `50` players max), emoji share cards, local backup/restore, and rate-limited `$0` Cloudflare deployment.
- Deferred to Phase 2 (after testing): opt-in on-device WebGPU AI explanations (`GOAL-005`, `SRC-022`) and a browser-synthesized Web Audio music ear-training track.
- Explicitly excluded: paid subscriptions, ads, energy meters, streak wipes, paid cloud AI APIs, public stranger feeds or chat moderation, K-12 grading tools, native mobile app-store builds, and copyrighted course material.

### 10. Expected value

If validated with real players, this design aims to give solo learners a low-stress daily curiosity habit while letting friend groups play trivia and language rounds together without hitting a 10-person paywall (`GOAL-001`, `GOAL-002`). For the developer, it showcases deterministic open-data pipelines and resilient real-time sync at `$0` baseline cost (`GOAL-003`, `GOAL-004`). These product outcomes are expected goals, not yet proven results (`ART-010`).

### 11. Research limitations and considerations

Three practical caveats apply before building (`ART-002`, `ART-006`, `ART-010`):
- All evidence comes from public documents, SEC filings, and community forums rather than interviews with target users (`VAL-02`).
- Raw open datasets contain duplicate or uneven questions, so automated quality filtering and clear `CC BY-SA 4.0` attribution (`OpenTriviaDB`, `Wiktionary`) are mandatory (`FND-015`).
- Free-tier hosting has hard daily caps (`100,000` edge requests per day on Cloudflare Workers and Durable Objects; `SRC-030`). At roughly `29` counted requests per 10-player live room using WebSocket Hibernation, the `85%` safety cap handles roughly `2,900` live rooms per day (`ART-009`), after which new rooms pause gracefully until `00:00 UTC` unless a `$5/month` upgrade is approved later.

### 12. Recommended next steps

1. Run a small validation check (`VAL-02`) with 5 to 8 casual learners and two mobile friend groups once prototype tracks are ready, testing whether social rooms or solo daily grids drive stronger return play.
2. Build Milestone 1 (`corpus-cli`) first to verify that automated filtering yields at least `1,500` clean, fun cards (`GOAL-003`).
3. Follow the five-milestone plan in Package A (`ART-011`) when authorized to enter implementation.

### 13. Conclusion

Focusing on `PRB-005` pairs a proven mainstream market (`52.7M` daily learners, `9M+` daily puzzle players) with clear incumbent friction (Energy caps, streak anxiety, and 10-player quiz paywalls). By keeping personal memory data local in the browser, sourcing public-domain and Creative Commons packs, and using hibernatable edge rooms only for shared multiplayer play, a solo backend engineer can build and run the complete MVP at `$0` money cost.
