# ART-007 — Stage 07 Business Analysis & Requirements Specification

| Field | Value |
|---|---|
| **Artifact ID** | `ART-007` |
| **Purpose** | Translate approved product goals (`GOAL-001`..`GOAL-005`) and constraints (`DEC-007`, `DEC-008`, `DEC-009`) into testable functional requirements, non-functional requirements, business rules, use cases, acceptance tests (`TEST-NNN`), and end-to-end traceability. |
| **Status** | `approved` |
| **Owner** | `Agent 07 (Business Analyst & Requirements Engineer)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-004` (`PRB-005`), `ART-006` (`GOAL-001`..`GOAL-005`), `DECISIONS.md` (`DEC-007`, `DEC-008`, `DEC-009`), `EVIDENCE_LEDGER.md` (`FND-001`–`FND-004`, `FND-010`, `FND-013`–`FND-016`) |

---

## Assumptions & Limitations

- **No primary user testing (`DEC-007`):** Quantitative performance/quota thresholds (`< 250 KB`, `<= 30` room players baseline, `24h` async window) are engineering targets grounded in desk research (`SRC-009`, `SRC-018`, `SRC-030`) rather than field telemetry.
- **Strict `$0` constraint (`DEC-009`):** All requirements assume zero paid third-party services, zero cloud LLM calls, and zero user-account databases in MVP.

---

## Content

### 1. Actors, Roles & Permission Matrix

| Actor | Identity Model | Permitted Actions | Prohibited / Guarded Actions |
|---|---|---|---|
| **Solo Learner** | Local browser profile (`IndexedDB` + optional portable backup key) | Play Daily 5-Card Ritual, practice tracks, view mastery ledger, export/import backup, opt in to local AI (`Phase 2`), copy emoji share grid. | Cannot mutate global daily seeds or view future daily answer keys prematurely. |
| **Room Host** | Anonymous guest + signed `hostToken` stored in session/local storage | Create room (choose track, pacing `Live` or `24h Async`, max players `2–50`), share invite URL/code, start/advance live round, close room. | Cannot forge other players' answers, exceed `$0` room/rate limits, or upload unvetted public text. |
| **Room Participant** | Anonymous guest + signed `playerToken` + sanitized display name | Join room via link/code in `<= 2` taps, submit answers once per round (idempotent), reconnect & restore mid-round state, view round reveals & final summary. | Cannot read unopened round answer keys from client payload, advance host-locked live stages, or spam duplicate submissions. |
| **Curator / Solo Operator** | Offline CLI / CI build-time maintainer | Run open-corpus ingestion/validation scripts, publish versioned static packs & daily seed manifests, review aggregated defect flags (`<1%` threshold). | Never runs paid runtime moderation or edits production user state manually. |

---

### 2. Functional Requirements (`REQ-NNN`)

| ID | Priority | Traceability | Requirement Statement | Validation / Business Rules & Edge Cases |
|---|---|---|---|---|
| **REQ-001** | **Must (MVP)** | `GOAL-001`, `PRB-005`, `FND-014` | **Guilt-Free 5-Card Daily & Practice Ritual:** The system shall allow any user to complete unlimited practice rounds and the Daily 5-Card Ritual with **zero energy/life depletion** and **non-punitive momentum** (tracking rolling active days and learned-item count rather than resetting progress to `0` after a missed day). | **Rule BR-01:** Incorrect answers prompt immediate feedback + deterministic explanation and reschedule the card sooner; they never lock the user out. **Edge:** Local timezone rollover uses user's local calendar date for Daily Ritual display while fetching deterministic UTC-keyed daily seed ID. |
| **REQ-002** | **Must (MVP)** | `GOAL-001`, `PRB-005` | **Deterministic Local Mastery Scheduler:** The system shall maintain per-item spaced-repetition mastery (`New`, `Learning`, `Familiar`, `Mastered`) deterministically in browser storage (`IndexedDB`) across MVP tracks (*Phrases & Words in Context*; *World, Culture & Science Trivia*). | **Rule BR-02:** Correct streak intervals advance cleanly (`1d -> 3d -> 7d -> 21d`); missed items step back one tier without wiping total mastered count. **Edge:** Fallback to `localStorage` or in-memory session notice if private browsing blocks `IndexedDB`. |
| **REQ-003** | **Must (MVP)** | `GOAL-002`, `FND-001` | **Spoiler-Free Share Card Generator:** Upon completing a Daily Ritual or multiplayer room, the system shall generate a copyable plain-text emoji summary grid (`🟩`/`🟨`/`⬜`) showing score/round pattern without revealing prompts or answers. | **Rule BR-03:** Clipboard write failure displays a selectable modal fallback for manual copy on strict mobile browsers. |
| **REQ-004** | **Must (MVP)** | `GOAL-002`, `FND-003` | **Zero-Account Room Creation & Link Join:** A host shall create a room in `<= 3` clicks and share a short URL/code allowing `2–50` guests (`>= 30` target) to join with only a display name (no email, password, or install). | **Rule BR-04:** Display names sanitized (plain text only, `2–20` chars, whitespace normalized, basic profanity/control-char strip). **Edge:** Duplicate display names auto-disambiguated (`Alex #2`); invalid/expired room codes show clear recovery CTA ("Start a new room"). |
| **REQ-005** | **Must (MVP)** | `GOAL-002`, `FND-004`, `RCA-003` | **Dual Room Pacing (`Live Sync` & `24h Micro-Async`):** Rooms shall support (a) **Live Sync** (shared lobby, synchronized per-question timer `15–45s`, simultaneous reveal when all answer or timer expires) and (b) **24-Hour Micro-Async** (players join anytime within 24h, play the identical 5-card seeded round at their own pace, and see blind-until-completed peer results). | **Rule BR-05:** Answer keys remain server-side until the player submits (async) or round closes (live). **Edge:** In Live Sync, if a participant drops mid-round, round advances cleanly on timer without locking the room; in Async, inactive players never penalize completed peers. |
| **REQ-006** | **Must (MVP)** | `GOAL-002`, `FND-002`, `RCA-001` | **Idempotent Reconnect & State Hydration:** The system shall persist active room/player state on the server edge actor and issue a signed `playerToken` stored locally so page refreshes, tab switches, or brief Wi-Fi/cellular drops restore exact round progress without duplicate score submissions. | **Rule BR-06:** Every answer submission includes `(roundIndex, submissionIdempotencyKey)`; duplicate retries return the original recorded result (`HTTP 200` / ack) without double-scoring. |
| **REQ-007** | **Must (MVP)** | `GOAL-003`, `DEC-009`, `FND-015` | **Deterministic Open-Corpus Curation Pipeline:** Build-time ingestion tools shall compile `>= 1,500` clean, deduplicated, difficulty-tagged items across the 2 MVP tracks from verified open corpora (`Tatoeba CC0`, `Wikidata CC0`, `Wiktionary CC BY-SA 4.0`, `OpenTriviaDB CC BY-SA 4.0`) with deterministic quality checks and license tags per item. | **Rule BR-07:** Reject items with HTML entities unescaped, length `> 220` chars, missing/duplicate distractors, or missing license metadata. Generate static JSON shard bundles for `$0` CDN delivery. |
| **REQ-008** | **Must (MVP)** | `GOAL-003` | **Lightweight Card Issue Reporting:** Users shall be able to flag an ambiguous, broken, or inaccurate card (`1` click + optional reason category); flags are queued/aggregated safely without exposing public user text. | **Rule BR-08:** Rate-limited per session (`<= 5` flags/day); flagged items are suppressed locally for that user immediately and reviewed offline by the operator before next static pack release. |
| **REQ-009** | **Must (MVP)** | `GOAL-004`, `DEC-009` | **Local-First Export & Portable Sync Code:** Users shall be able to export and import their personal mastery state as a compact JSON file or compressed sync string so progress transfers across devices with `$0` account-server storage. | **Rule BR-09:** Import validates schema version and checksum before merging (`max(masteryTier)` conflict resolution), preventing data loss on bad input. |
| **REQ-010** | **Must (MVP)** | `GOAL-004`, `DEC-009`, `FND-016` | **Free-Tier Quota Guardrails & Auto-Expiry:** Multiplayer rooms shall auto-expire `48h` after completion/inactivity, daily puzzle seeds shall cache aggressively at the CDN edge (`>= 24h` TTL), and room creation/WebSocket messaging shall enforce rate limits so daily traffic remains within `$0` free-tier limits. | **Rule BR-10:** If edge daily quota nears ceiling (`>= 85%`), room creation returns a clear friendly notice ("Live rooms at daily capacity—Solo Daily & Practice remain 100% available offline/locally") rather than crashing silently. |
| **REQ-011** | **Should (Phase 2)** | `GOAL-005`, `FND-013` | **Opt-In Local WebGPU "Why" Tutor:** On devices supporting WebGPU with adequate memory, users may explicitly opt in to download a small local language model (`~360M–1B`) once to request plain-language explanations or memory mnemonics offline; unsupported devices use deterministic open-metadata notes seamlessly. | **Rule BR-11:** Model download requires explicit user tap showing approximate download size; zero automatic background weight downloads on mobile data. |
| **REQ-012** | **Could (Phase 2)** | `GOAL-001`, `DEC-009` | **Web Audio Ear-Training Track:** Future expansion track using pure Web Audio API tone synthesis (intervals, chords, rhythms) requiring `$0` audio file hosting or music licensing. | Out of MVP (`Phase 2` only). |

---

### 3. Non-Functional Requirements (`REQ-NFR-NNN`)

| ID | Category | Traceability | Measurable Target & Verification Rule |
|---|---|---|---|
| **REQ-NFR-001** | Performance & Bundle Size | `GOAL-004`, `DEC-009` | Initial MVP app shell `< 250 KB` gzipped; static assets & content shards served via CDN cache (`Cache-Control: immutable` for versioned packs); first interactive render `< 2.0s` on simulated 4G mobile. |
| **REQ-NFR-002** | Data Reliability & Determinism | `GOAL-002`, `GOAL-003` | `100%` deterministic daily seed selection (same UTC date + track = identical 5 cards globally); idempotent answer writes; schema-validated local storage migrations (`version` field) preventing silent progress wipe. |
| **REQ-NFR-003** | Mobile Viewport & Touch UX | `PRB-005`, `FND-002`, `RCA-001` | Layout fits `320px–430px` viewports using `100dvh` without horizontal overflow; interactive play surfaces isolate `touch-action: manipulation` to block accidental double-tap zoom; all inputs `>= 16px` font-size to prevent iOS Safari auto-zoom. |
| **REQ-NFR-004** | Accessibility (WCAG 2.1 AA) | `GOAL-001`, `SKL-008c` | Full keyboard navigation (`Tab`, `1–4` number shortcuts, `Enter/Space`, `Esc`), visible `:focus-visible` outlines, text contrast `>= 4.5:1`, interactive touch targets `>= 44x44 CSS px`, `aria-live="polite"` updates for round transitions/reveals, and `prefers-reduced-motion` support. |
| **REQ-NFR-005** | Privacy & Zero-PII | `GOAL-004`, `DEC-009` | Zero email/phone/OAuth collection; zero third-party ad/analytics cookies; room state ephemeral (`<= 48h` TTL post-close). |
| **REQ-NFR-006** | Security & Fair Play | `GOAL-002`, `GOAL-004` | Server-authoritative room state & answer verification; answer keys never leaked in pre-reveal API/WebSocket payloads; strict schema/length sanitization on display names & room parameters; per-IP/room WebSocket message throttling. |
| **REQ-NFR-007** | Open-Data License Hygiene | `GOAL-003`, `SRC-029` | Every curated pack records source license (`CC0 1.0` vs. `CC BY-SA 4.0`); UI displays clear attribution in Credits/About; CC BY-SA curated trivia derivative packs remain openly downloadable under compatible ShareAlike terms. |

---

### 4. Core Use Cases & Acceptance Test Criteria (`TEST-NNN`)

| Test ID | Linked `REQ` | Scenario & Preconditions | Expected Verifiable Outcome (Pass/Fail) |
|---|---|---|---|
| **TEST-001** | `REQ-001`, `REQ-002` | **Guilt-Free Mistake & Comeback:** User gets 3/5 wrong on Daily Ritual, closes browser for 3 days, then returns. | Zero energy block; missed cards schedule back into `Learning` queue; rolling consistency/mastered count is preserved (not reset to `0`). |
| **TEST-002** | `REQ-003` | **Spoiler-Free Share Grid:** User completes Daily Ritual on mobile Chrome & iOS Safari and taps "Share Result". | Clipboard (or fallback copy box) contains 5-emoji grid (`🟩`/`🟨`/`⬜`), date/track title, and app URL—zero question text or answers included. |
| **TEST-003** | `REQ-004`, `REQ-005` | **Zero-Account 30-Player Room Join:** Host creates Live or 24h Async room; 30 simulated guests open link and enter display names. | All 30 join with `0` signup screens and `$0` paywall blocks; `24h Async` players get identical 5 cards and cannot see peer answers until submitting their own. |
| **TEST-004** | `REQ-006`, `REQ-NFR-002` | **Mid-Round Mobile Reconnect & Double-Tap:** Player answers Q2, drops network for 10s (or switches Wi-Fi->LTE), reloads page, and double-taps Q3 option. | Reload hydrates exact room state at Q3 with Q1–Q2 preserved; Q3 double-tap records exactly `1` score entry via idempotency key. |
| **TEST-005** | `REQ-NFR-006` | **Anti-Spoiler Payload Inspection:** Inspect network/WebSocket JSON sent to client before round reveal. | `correctIndex` / answer string is absent (`null`/omitted) until server emits `round_revealed` or `async_submitted`. |
| **TEST-006** | `REQ-007`, `REQ-NFR-007` | **Open-Corpus Curation & Attribution:** Run build-time curation script on raw `Tatoeba CC0` + `OpenTriviaDB` inputs. | Outputs `>= 1,500` validated items with `0` unescaped HTML artifacts, `0` duplicate prompts, and valid `license`/`attribution` fields per shard. |
| **TEST-007** | `REQ-009` | **Local Mastery Export/Import Recovery:** User exports mastery JSON/code on Device A, corrupts 1 character in a negative test, then imports valid backup on Device B. | Corrupted payload fails checksum cleanly with zero overwrite; valid payload restores exact `Learning/Familiar/Mastered` counts. |
| **TEST-008** | `REQ-010` | **Free-Tier Quota Protection:** Simulate room creation spam / edge quota threshold trigger (`>= 85%` simulated budget). | Rate limiter blocks spam cleanly (`429`) and degraded mode keeps Solo Daily + Practice `100%` operational offline/locally. |
| **TEST-009** | `REQ-NFR-003`, `REQ-NFR-004` | **Mobile Viewport & Keyboard Accessibility:** Navigate full Solo + Room play on `360px` viewport and desktop keyboard-only (`Tab`/`1–4`/`Enter`). | Zero horizontal scroll, zero iOS input auto-zoom, `>= 44x44px` buttons, visible focus rings, `aria-live` announces question & reveal result. |
| **TEST-010** | `REQ-011`, `GOAL-005` | **Opt-In Local AI Fallback:** Run full round on browser without WebGPU (e.g., Firefox Android / WebGPU disabled). | Zero errors or broken UI; "Explain" button serves deterministic open-metadata note instantly with `$0` network calls. |

---

### 5. End-to-End Traceability Matrix (`FND/PRB -> GOAL -> REQ -> TEST`)

| Evidence / Problem | Product Goal | Requirements (`REQ-NNN` / `REQ-NFR-NNN`) | Verification (`TEST-NNN`) |
|---|---|---|---|
| `FND-010`, `FND-014` (`PRB-005`) | `GOAL-001` | `REQ-001`, `REQ-002`, `REQ-012` (`Phase 2`), `REQ-NFR-004` | `TEST-001`, `TEST-009` |
| `FND-001`–`FND-004` (`PRB-005`) | `GOAL-002` | `REQ-003`, `REQ-004`, `REQ-005`, `REQ-006`, `REQ-NFR-002`, `REQ-NFR-003`, `REQ-NFR-006` | `TEST-002`, `TEST-003`, `TEST-004`, `TEST-005`, `TEST-009` |
| `FND-015`, `DEC-009` | `GOAL-003` | `REQ-007`, `REQ-008`, `REQ-NFR-007` | `TEST-006` |
| `FND-016`, `DEC-009` | `GOAL-004` | `REQ-009`, `REQ-010`, `REQ-NFR-001`, `REQ-NFR-005` | `TEST-007`, `TEST-008` |
| `FND-013`, `DEC-009` | `GOAL-005` | `REQ-011` (`Phase 2`) | `TEST-010` |

---

## Next Steps / Unresolved Issues

- **Stage 07 Gate Check:** Zero orphan requirements; every MVP requirement maps upward to `GOAL-001`..`GOAL-005` and downward to `TEST-001`..`TEST-010` with edge cases, validation rules, and `$0` constraints.
- **Open Minor Question (Non-Blocking for Stage 08):** Exact default language-pair selection for MVP Track 1 (*Phrases & Words in Context*, e.g., Spanish/Japanese/French from `Tatoeba CC0`) can be parameterized in the static pack manifest during Stage 09/build without blocking UX design.
- **Next Stage:** Hand off to **Agent 08 (UX & Information Architecture Planner)** to design user journeys, IA, screen states, WCAG 2.1 AA accessibility specs, and text wireframes (`ART-008`).
