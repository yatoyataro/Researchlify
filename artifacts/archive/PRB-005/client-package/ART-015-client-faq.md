# ART-015 — Package B: Client FAQ

| Field | Value |
|---|---|
| **Artifact ID** | `ART-015` |
| **Purpose** | Plain-language answers to key stakeholder questions covering selection rationale, evidence, scope, `$0` architecture limits, evaluation criteria, and next decisions. |
| **Status** | `approved` |
| **Owner** | `Agent 13 (Client-Facing Research Synthesizer & Humanizer)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`..`ART-011`, `DECISIONS.md` (`DEC-006`..`DEC-009`), `EVIDENCE_LEDGER.md`, `SKL-004`, `SKL-006` |

---

## Assumptions & Limitations

- Answers reflect approved discovery artifacts (`ART-001`..`ART-011`) grounded in desk research (`DEC-007`).

---

## Content

### 1. Why was `PRB-005` selected over the other problem ideas?
Six problem candidates were scored against explicit criteria including fun/delight (`20%`), evidence strength (`20%`), audience breadth (`15%`), user pain (`15%`), solo backend fit (`15%`), repeat frequency (`10%`), and risk (`5%`) (`DEC-006`, `ART-005`). Pure party games (`PRB-001`) scored `4.50` and casual learning burnout (`PRB-005`) scored `4.40`, with `PRB-005` flipping to first place (`4.75`) when weighting market evidence and daily habit frequency higher. Following Stage 05 review, you selected `PRB-005` with a strict `$0` budget rule (`DEC-008`, `DEC-009`).

### 2. What evidence proves this is a real problem?
Duolingo's Q4 2025 SEC filing confirms `52.7 million` daily active users and `$1.037 billion` in annual revenue (`SRC-004`), while NYT `Wordle` (`4.2B` solved in 2025) and `Connections` (`9M+` daily players) show huge mainstream demand for short daily browser rituals (`SRC-007`, `SRC-008`). At the same time, Class Central's 2025 analysis documents user backlash against Duolingo's 25-point Energy battery draining on right answers (`SRC-006`), and Kahoot's support docs confirm free personal games cap at `10` players (`SRC-018`).

### 3. Who is this app built for?
Three main groups (`ART-006`, `ART-008`, labeled `provisional` pending live interviews): casual daily learners burned out by streak anxiety or energy bars, friend-group hosts wanting to run quick trivia or language games for 2 to 30+ people without paying per seat, and busy friends who prefer 24-hour asynchronous rounds over coordinating live schedules.

### 4. What existing solutions were considered, and why not just use them?
We evaluated `Duolingo`, `Kahoot!`, `NYT Wordle/Connections`, `Anki`, and Discord quiz bots (`ART-003`). `Duolingo` restricts free sessions via Energy; `Kahoot!` caps free personal rooms at `10` players and lacks memory review; `NYT Games` are mostly single-player; and `Anki` or Discord bots demand manual setup or offer clunky mobile UX.

### 5. Why is a web app the right format instead of a native mobile app or non-software alternative?
A mobile-first browser app opens directly from a chat link in under 15 seconds with zero app-store install or `$99/year` developer account fees (`GOAL-002`, `DEC-009`), while supporting real-time synchronized rooms, local browser persistence (`IndexedDB`), and optional on-device WebGPU AI (`SRC-022`).

### 6. What will the MVP actually do?
The Phase 1 MVP delivers two curated open-data tracks (*Phrases & Words in Context* and *World, Culture & Science Trivia*), a 5-card Solo Daily Ritual with zero energy bars, spoiler-free emoji share grids, 2-to-30+ player rooms in Live or 24-hour Async mode, automatic mobile reconnect recovery, local mastery tracking with exportable backups, and 1-click bad-card flagging (`ART-007`, `ART-008`).

### 7. What is explicitly out of scope?
Subscriptions, ads, energy meters, streak-loss wipes, paid cloud AI APIs, open public stranger feeds or chat moderation, school LMS/exam grading, native iOS/Android app-store binaries in MVP, and any copyrighted course material (`ART-006`).

### 8. How can development, production, and deployment really cost `$0`?
The stack relies on open-source build tools (`TypeScript`, `Vite`, `Vitest`, `Playwright`, `GitHub Actions` free tier), free CC0/CC-BY-SA datasets (`Tatoeba CC0`, `Wikidata`, `Wiktionary`, `OpenTriviaDB`; `SRC-029`), client-local browser storage so solo play uses zero database writes, and `Cloudflare Pages` plus `Workers`/`Durable Objects` (`100K` free reqs/day with WebSocket Hibernation) and `D1` (`5M` reads/`100K` writes/day; `SRC-030`).

### 9. What are the main risks and limitations?
First, no live user interviews have been run yet (`DEC-007`), so engagement rates (`65%` completion, `35%` Day-7 return) are hypotheses to test (`VAL-02`). Second, raw open datasets contain uneven items that need strict automated filtering and clear `CC BY-SA 4.0` attribution (`FND-015`). Third, Cloudflare's free tier enforces hard daily caps (`100K` reqs/day); if traffic exceeds the `85%` safety cap (`~2,900` 10-player live rooms/day), new rooms shed cleanly to Solo offline play until `00:00 UTC` or a `$5/month` upgrade (`ART-009`).

### 10. How will success be evaluated?
Technically via `TEST-001`..`TEST-010` (`ART-007`): `<250 KB` gzipped bundle, `>=1,500` clean items (`<1%` error flags), verified zero-spoiler room payloads, and mobile reconnect recovery. Product-wise via post-MVP cohort playtests checking round completion, Day-7 return, and room link join speed (`GOAL-001`, `GOAL-002`).

### 11. What decisions or inputs are needed from the client/owner next?
Two small choices before coding Milestone 1: confirm which default language pair(s) to bundle in Track 1 (*Phrases & Words in Context*, e.g., Spanish, Japanese, or French from `Tatoeba CC0`), and decide whether to run a 5-to-8 person pre-build interview/playtest (`VAL-02`) or validate directly with a live MVP prototype.

### 12. What are the immediate next steps?
Authorize entry into implementation using Package A (`ART-011`), starting with Milestone 1 (`corpus-cli`) to validate open-dataset quality and attribution before wiring the Solo PWA and Durable Object rooms.
