# ART-011 — Package A: Developer-Ready Technical Handoff

| Field | Value |
|---|---|
| **Artifact ID** | `ART-011` |
| **Purpose** | Consolidate all approved Stages 01–10 research, problem analysis, product strategy, requirements, UX/IA, architecture, and QA audit outputs into a single developer-ready 23-section handoff package (`Package A`) for `PRB-005` under `$0` dev/prod/deploy rules. |
| **Status** | `approved` |
| **Owner** | `Agent 11 (Documentation & Handoff Specialist)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`..`ART-010`, `DECISIONS.md` (`DEC-006`..`DEC-009`), `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-030`, `FND-001`..`FND-016`), `ISSUES.md`, `SKL-010a` |

---

## Assumptions & Limitations

- **No invented specifications:** Every requirement, flow, architectural component, and metric below derives verbatim from approved upstream artifacts (`ART-001`..`ART-010`).
- **Desk-research caveat (`DEC-007`, `ART-010`):** Behavioral engagement targets (`GOAL-001`, `GOAL-002`) and social-vs-solo play preferences (`VAL-02`) remain unvalidated hypotheses until post-MVP or authorized user testing.
- **Strict `$0` boundary (`DEC-009`):** Engineering assumes zero paid SaaS, APIs, or cloud plans unless the human owner explicitly approves stepping off `$0` at scale.

---

## Content (23 Required Handoff Sections)

### 1. Project Overview
- **Domain & Mandate:** Build a browser-native, zero-cost, guilt-free daily and social casual learning web app targeting mainstream audiences, tailored to a solo backend-leaning developer strong in real-time systems, data reliability, and optional local AI (`DEC-006`, `DEC-008`, `DEC-009`).
- **Selected Problem:** `PRB-005` — Casual Learning Engagement Burnout (Punitive Solo Streaks vs. Joyful Social Mastery).
- **Hard Budget Rule (`DEC-009`):** `$0` across development tooling, open-data licensing, cloud AI inference, baseline production hosting, and end-user access.

### 2. Research & Evidence Summary
- **Corpus:** `30` verified sources (`SRC-001`..`SRC-030`) and `16` findings (`FND-001`..`FND-016`) in [EVIDENCE_LEDGER.md](../../EVIDENCE_LEDGER.md).
- **Key Verified Signals:**
  - Casual learning demand at massive scale (`Duolingo`: `52.7M` DAU, `~130M` MAU, `84%` CURR, `$1.037B` FY25 revenue; `SRC-004`), paired with mid-2025 backlash against its 25-point Energy battery draining even on correct answers (`FND-014` / `SRC-006`).
  - Zero-install browser daily puzzles with spoiler-free chat sharing sustain huge daily habits (`Wordle` `4.2B–5.3B` annual plays, `Connections` `>9M` daily players; `FND-001` / `SRC-007`, `SRC-008`).
  - Casual group hosts hit `3–10` player paywalls on `Kahoot!` (`FND-003` / `SRC-018`) and mobile viewport/socket-drop failures on party/async web games (`FND-002`, `FND-004` / `SRC-009`–`SRC-014`).
  - `$0` feasibility verified via open datasets (`Tatoeba CC0`, `Wikidata CC0`, `Wiktionary CC BY-SA 4.0`, `OpenTriviaDB CC BY-SA 4.0`; `SRC-029`), Cloudflare free tiers (`Pages` unlimited static bandwidth, `Workers`/`DO` `100K` reqs/day with WebSocket Hibernation `20:1` incoming WS ratio & `0` idle duration, `D1` `5M` reads/`100K` writes/day; `SRC-030`), and optional WebGPU/WebLLM (`SRC-022`).

### 3. Problem Statements & Root-Cause Analysis
- **Primary Problem (`PRB-005` in `ART-004`):** Mainstream casual learners and social circles abandon or resent learning tools when solo streak-loss anxiety, energy caps, and per-player quiz paywalls turn curiosity into punitive chores.
- **Root Causes:** `RCA-004` (loss-aversion streak/energy monetization), `RCA-002` (seat/player-count SaaS paywalls), `RCA-003` (missing micro-async + live dual pacing), `RCA-001` (naive mobile viewport & volatile socket recovery).

### 4. Prioritization & Rationale
- Evaluated `6` validated problem candidates (`PRB-001`..`PRB-006`) under `DEC-006` weights (`Fun/delight 20%`, `Evidence 20%`, `Breadth 15%`, `Impact 15%`, `Solo Backend/RT/AI Fit 15%`, `Frequency 10%`, `Risk 5%`) in `ART-005`.
- Top 3: `PRB-001` (`4.50`), `PRB-005` (`4.40`, flipping to **`#1` at `4.75`** under evidence/habit-conservative weights), `PRB-006` (`3.70`).
- User selected **`PRB-005`** (`DEC-008`) paired with **`DEC-009`** (`$0` dev/prod/deploy).

### 5. Product Vision, Goals & Success Indicators
From `ART-006`:
- **`GOAL-001`:** Zero-guilt 3–5 min rounds (`0` energy walls / `0` streak resets; target hypothesis `>=65%` completion, `>=35%` Day-7 return).
- **`GOAL-002`:** `<=2`-tap guest link join for `2–30+` players (`$0`, live or 24h async; `<15s` to play, `>=98%` reconnect recovery hypothesis).
- **`GOAL-003`:** `>=1,500` curated, deduplicated, attribution-clean items across `2` MVP tracks (`<1%` defect rate).
- **`GOAL-004`:** Strict `$0/month` budget (`<50%` daily free-tier quota baseline, client-local personal state).
- **`GOAL-005`:** Optional opt-in WebGPU local explanations (`100%` deterministic fallback when unavailable).

### 6. Target Users / Personas (With Evidence Status)
All three archetypes in `ART-008` are labeled **`provisional`** (`DEC-007` desk-research basis):
1. **Maya (Streak-Fatigued Daily Puzzler)** — wants 3–5 min guilt-free morning ritual + chat share grid (`FND-001`, `FND-010`, `FND-014`).
2. **Devon (Chat-Group Host)** — wants instant Discord/WhatsApp link for 4–25+ friends with zero 10-player cap (`FND-002`, `FND-003`).
3. **Sam (Busy Async Buddy)** — wants 24h self-paced seeded rounds with spoiler-blind group comparison (`FND-004`, `FND-005`).

### 7. MVP Scope, Exclusions & Phased Roadmap
- **MVP (Phase 1):** `2` curated open tracks (*Phrases & Words in Context*; *World, Culture & Science Trivia*), Solo Daily + Practice, Live & 24h Async Rooms (`2–50` players), Spoiler-Free Share Grid, Local-First Mastery (`IndexedDB` + JSON/string backup), Deterministic Curation CLI, `$0` Cloudflare deploy.
- **Explicit Non-Goals:** Subscriptions, ads, energy/hearts bars, cloud LLM APIs, public stranger feeds/leaderboards, LMS/exam grading, native app-store binaries in MVP, copyrighted content.
- **Roadmap:** Phase 1 (MVP) -> Phase 2 (Opt-in WebGPU Local Tutor + Web Audio ear-training track) -> Phase 3 (WebRTC P2P offload / custom local decks / human gate if traffic nears `100K` daily reqs).

### 8. Requirements Specification (`REQ-NNN`)
Full specifications in [ART-007](../requirements/ART-007-stage07-requirements.md):
- **Must (MVP):** `REQ-001` (Guilt-free 5-card daily), `REQ-002` (4-tier local spaced repetition), `REQ-003` (Spoiler-free emoji share), `REQ-004` (Zero-account link join `2–50`), `REQ-005` (Live Sync + 24h Micro-Async), `REQ-006` (Idempotent reconnect hydration), `REQ-007` (Open-corpus curation CLI `>=1,500` items), `REQ-008` (Rate-limited card flags), `REQ-009` (Checksummed JSON/string export/import), `REQ-010` (Quota guardrails & `48h` room expiry).
- **Post-MVP:** `REQ-011` (`Should`, Phase 2 opt-in WebGPU AI), `REQ-012` (`Could`, Phase 2 Web Audio track).

### 9. Use Cases, Stories, Acceptance Criteria & Business Rules
- Business Rules `BR-01`..`BR-11` (`ART-007` Section 2): zero lockout on mistakes, `1d->3d->7d->21d` intervals, manual copy fallback, display-name sanitization (`2–20` chars), pre-reveal server-side answer stripping in rooms, `(roundIndex, idempotencyKey)` deduplication, deterministic ETL validation (`<=220` chars, zero unescaped HTML), `<=5` flags/day, checksummed `max(tier)` import merge, `>=85%` quota room-shedding w/ Solo fallback, explicit opt-in AI download notice.
- Acceptance Tests: `TEST-001`..`TEST-010` (`ART-007` Section 4).

### 10. Non-Functional Requirements
- `REQ-NFR-001` (`<250 KB` gzipped shell, `<2.0s` 4G interactive, CDN immutable packs)
- `REQ-NFR-002` (Deterministic daily seeds, idempotent writes, versioned local migrations)
- `REQ-NFR-003` (`320–430px` `100dvh`, `touch-action: manipulation`, `>=16px` inputs)
- `REQ-NFR-004` (WCAG 2.1 AA: `>=4.5:1` contrast, `>=44x44px` targets, keyboard `1–4`, `aria-live`, `prefers-reduced-motion`)
- `REQ-NFR-005` (Zero PII, zero ad trackers, `<=48h` room TTL)
- `REQ-NFR-006` (Server-authoritative room state, HMAC tokens, rate limits)
- `REQ-NFR-007` (CC0 vs. CC BY-SA 4.0 separation & attribution).

### 11. User Journeys & Flows (`UX-NNN`)
Defined in [ART-008](../ux/ART-008-stage08-ux-ia.md):
- `UX-001` (Solo Daily Ritual & Share), `UX-002` (Host Creates & Shares Room `<=3` clicks), `UX-003` (Guest Joins `<=2` taps & Reconnects), `UX-004` (Mastery Ledger & Portable Backup), `UX-005` (Phase 2 Opt-In Local AI + Deterministic Fallback).

### 12. Information Architecture & Screen Inventory
- Flat 5-route IA (`ART-008` Section 3): `/`, `/play/:mode`, `/room/new`, `/room/:code`, `/mastery`, `/about`.
- All 5 canonical screen states (`default`, `loading`, `empty`, `error/degraded`, `unauthorized/expired`) mapped per screen.

### 13. UX/Accessibility Considerations & Wireframes
- Mobile Safari/Chrome anti-zoom/scroll safeguards, non-color-only feedback icons, keyboard hotkeys `1–4` + `Tab`/`Enter`/`Esc`, and mobile `375px` text wireframes (`A` Play Hub, `B` Active Round Runner, `C` Room Summary & Share) in `ART-008` Sections 4–5.

### 14. System Architecture (`ARC-NNN`)
Defined in [ART-009](../architecture/ART-009-stage09-technical-architecture.md) (`v1.1`):
- `ARC-001`: Cloudflare Pages + Workers + SQLite-backed Durable Objects (WebSocket Hibernation).
- `ARC-002`: Client-local `IndexedDB` + `localStorage` fallback + checksummed portable export/import.
- `ARC-003`: Build-time sharded static JSON packs + deterministic UTC daily manifests.
- `ARC-004`: Server-authoritative DO state machine + HMAC-SHA256 `WebCrypto` tokens + idempotent submissions.
- `ARC-005`: TypeScript + Vite/Preact + Vitest + Playwright + GitHub Free/Actions (`$0` toolchain).
- `ARC-006`: Phase 2 progressive-enhancement `WebLLM` (`WebGPU`) adapter.

### 15. Component & Module Design
Six decoupled modules (`ART-009` Section 1):
1. `corpus-cli` (offline CC0/CC-BY-SA ETL & validator)
2. `client-core` (deterministic scheduler, daily seed picker, checksum backup codec)
3. `client-ui` (accessible PWA views & state stores)
4. `edge-router` (Worker REST endpoints, rate limiter, HMAC verify)
5. `room-actor` (Hibernatable DO SQLite state machine + `48h` cleanup alarm)
6. `local-ai-adapter` (Phase 2 lazy WebGPU module).

### 16. Database Design & ERD
Dual-boundary schema (`ART-009` Section 3 `v1.1`):
- **Static Shards / Client `IndexedDB`:** `CONTENT_SHARD_ITEM`, `LOCAL_MASTERY_ITEM`, `LOCAL_ACTIVE_DAY`.
- **DO SQLite (per room, `48h` TTL):** `ROOM_ACTOR`, `ROOM_PLAYER`, `ROOM_SUBMISSION`.
- **Cloudflare D1 (global `$0` metadata):** `CARD_FLAG_AGGREGATE`, `DAILY_QUOTA_COUNTER`.

### 17. API & Integrations
- **REST (`Worker`):** `GET /api/daily/:utcDate/:track` (CDN `24h` cache), `POST /api/rooms`, `POST /api/rooms/:code/join`, `GET /api/rooms/:code/hydrate`, `POST /api/flags`.
- **WebSocket (`/api/rooms/:code/ws`):** `host_start_round`, `submit_answer` -> `room_state`, `round_started`, `player_progress`, `round_revealed`, `room_completed` (with `Async24h` also supporting HTTP answer POST).
- **External Integrations (`$0`):** Build-time open data imports (`Tatoeba CC0`, `Wikidata CC0`, `Wiktionary`, `OpenTriviaDB`); zero runtime third-party SaaS APIs.

### 18. Security, Privacy, Reliability, Deployment & Operations
- Threat model covers pre-reveal answer stripping (`TEST-005`), `$0` quota exhaustion (`85%` room shedding + per-IP/room rate limits), plain-text XSS sanitization, SQLite transaction idempotency, HMAC token signing, and CC BY-SA 4.0 license compliance (`ART-009` Section 5).
- Quota math (`SRC-030`): `~29` counted DO reqs per 10-player Live room (`20:1` incoming WS ratio, `0` idle duration) -> `~2,900` 10-player rooms/day inside `85%` of `100K` free-tier daily cap at `$0/month` (`ART-009` Section 6).

### 19. Implementation Sequence, Milestones & Dependencies (`SKL-010a` Structured Plan)
1. **Milestone 1 (`corpus-cli` + `CONTENT_SHARD_ITEM`):** Build open-corpus ETL + deduplication/attribution tests (`TEST-006`) -> emits `>=1,500` clean static items.
2. **Milestone 2 (`client-core` + Solo PWA):** Implement spaced-repetition engine, `IndexedDB` + checksum export/import (`TEST-001`, `TEST-002`, `TEST-007`), and Solo Daily/Practice UI (`TEST-009`). Depends on M1 shards.
3. **Milestone 3 (`edge-router` + `room-actor` DO):** Implement HMAC tokens, Live & 24h Async DO state machine, WebSocket Hibernation, idempotency, and `48h` cleanup alarm (`TEST-003`, `TEST-004`, `TEST-005`, `TEST-008`).
4. **Milestone 4 (Multiplayer UI + `$0` CI/Deploy):** Wire `/room/new` & `/room/:code` reconnect hydration, Playwright mobile/a11y suite (`TEST-009`), and GitHub Actions -> Cloudflare Pages/Workers `$0` deploy.
5. **Milestone 5 (Phase 2 Post-Validation):** Opt-in WebGPU `local-ai-adapter` (`TEST-010`) + Web Audio track after primary cohort testing (`VAL-02`).

### 20. QA & Test Plan
- **Unit & ETL Tests (`Vitest`):** Scheduler intervals, checksum corruption rejection (`TEST-007`), corpus hygiene & license validation (`TEST-006`).
- **Actor & Contract Tests (`Miniflare` / `wrangler` local):** Idempotent double-tap dedup (`TEST-004`), anti-spoiler payload inspection (`TEST-005`), rate limiting & `85%` quota shedding (`TEST-008`).
- **E2E Mobile & Accessibility Tests (`Playwright`):** `360px` mobile viewport, zero horizontal overflow, keyboard `1–4` navigation, reconnect after simulated offline/reload (`TEST-001`–`TEST-004`, `TEST-009`, `TEST-010`).

### 21. Requirement-to-Test Traceability
Complete matrix in `ART-007` Section 5 & `ART-008` Section 6:
- `REQ-001`/`002` -> `TEST-001`, `TEST-009` | `REQ-003` -> `TEST-002` | `REQ-004`/`005` -> `TEST-003` | `REQ-006` -> `TEST-004` | `REQ-NFR-006` -> `TEST-005` | `REQ-007`/`NFR-007` -> `TEST-006` | `REQ-009` -> `TEST-007` | `REQ-010` -> `TEST-008` | `REQ-NFR-003`/`004` -> `TEST-009` | `REQ-011` -> `TEST-010`.

### 22. Risks, Assumptions, Unresolved Questions & Human Decisions
- **Active Decisions:** `DEC-006` (rubric), `DEC-007` (desk-research only), `DEC-008` (`PRB-005` selected), `DEC-009` (`$0` dev/prod/deploy).
- **Unresolved / Deferred:** `VAL-02` (live user cohort test of social vs. solo retention); default language pair choice for Track 1 (parameterizable in M1 manifest); scale decision if traffic exceeds `85K` daily Worker/DO reqs (`$5/mo` step-up vs. shedding).

### 23. Artifact Index & Citations
- **Canonical Deliverables:** [ART-001](../research/ART-001-stage01-discovery-context.md), [ART-002](../research/ART-002-stage02-evidence-synthesis.md), [ART-003](../research/ART-003-stage03-existing-solutions.md), [ART-004](../problem-analysis/ART-004-stage04-root-cause-problems.md), [ART-005](../problem-analysis/ART-005-stage05-prioritization.md), [ART-006](ART-006-stage06-product-definition.md), [ART-007](../requirements/ART-007-stage07-requirements.md), [ART-008](../ux/ART-008-stage08-ux-ia.md), [ART-009](../architecture/ART-009-stage09-technical-architecture.md), [ART-010](../reviews/ART-010-stage10-qa-audit.md).
- **Registries:** [EVIDENCE_LEDGER.md](../../EVIDENCE_LEDGER.md) (`SRC-001`..`SRC-030`, `FND-001`..`FND-016`), [DECISIONS.md](../../DECISIONS.md) (`DEC-001`..`DEC-009`), [ISSUES.md](../../ISSUES.md) (`ISS-001`, `ISS-002` closed), [ARTIFACT_INDEX.md](../../ARTIFACT_INDEX.md).

---

## Next Steps / Unresolved Issues

- **Stage 11 Gate Check:** All 23 required sections of `Package A` are compiled, versioned, and cross-referenced directly to approved upstream artifacts with zero invented requirements.
- **Next Stage:** Execute **Stage 13 (Agent 13: Client-Facing Research Synthesizer & Humanizer — Package B)** and **Stage 10F (Final Package Audit)**.
