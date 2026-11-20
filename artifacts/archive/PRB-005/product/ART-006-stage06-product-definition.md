# ART-006 — Stage 06 Product Definition (`PRB-005`: Zero-Cost Joyful Social Casual Learning)

| Field | Value |
|---|---|
| **Artifact ID** | `ART-006` |
| **Purpose** | Define the product vision, target users, value proposition, measurable goals (`GOAL-001`..`GOAL-005`), build-vs-adopt rationale, MVP boundaries, explicit non-goals, phased roadmap, and risks for `PRB-005` under the mandatory `$0` dev/prod/deploy constraint (`DEC-008`, `DEC-009`). |
| **Status** | `approved` |
| **Owner** | `Agent 06 (Product Definition Strategist)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-002`, `ART-003`, `ART-004` (`PRB-005`, `RCA-002`..`RCA-004`, `VAL-02`), `ART-005`, `DECISIONS.md` (`DEC-008`, `DEC-009`), `EVIDENCE_LEDGER.md` (`FND-001`, `FND-003`, `FND-010`, `FND-013`–`FND-016`) |

---

## Assumptions & Limitations

- **Unvalidated behavioral hypothesis (`VAL-02`):** Desk research proves massive mainstream demand for daily casual learning (`FND-010`), daily browser puzzle sharing (`FND-001`), and frustration with Duolingo's 25-point Energy system (`FND-014`) and Kahoot's 10-player cap (`FND-003`). However, whether burned-out solo learners retain longer in a **forgiving co-op/social browser ritual** remains a `[TARGET HYPOTHESIS — unvalidated until primary testing]`.
- **Zero-money-cost operational ceiling (`DEC-009`, `FND-016`):** Running at `$0/month` in production is feasible inside verified free tiers (e.g., Cloudflare Pages + `100K` Worker/DO reqs/day + `100K` D1 row writes/day), but viral growth beyond those daily caps hits hard quota cutoffs unless the user later approves stepping off `$0` or shedding live multiplayer load.
- **Stage boundary:** This deliverable defines *what* the product is and why it should exist—not UI wireframes (Stage 08) or technical schemas/APIs (Stage 09).

---

## Content

### 1. Product Vision, Target Users & Value Proposition

#### Product Concept Summary
A **browser-native, zero-cost, guilt-free daily & social brain-play web app** where mainstream learners and friend groups play **3–5 minute curated micro-rounds**—either **solo with a spoiler-free share grid** or **together in zero-account co-op / friendly-duel rooms** (live or 24-hour micro-async)—backed by open/public-domain knowledge corpora, local-first mastery tracking, and optional browser-local AI explanations.

#### Target User Segments
| Segment | Who They Are | Core Job-to-be-Done | Key Pain Relieved (`PRB-005`) |
|---|---|---|---|
| **Primary: Burned-Out Casual Learners** | Mainstream adults/teens who enjoy word/trivia/language curiosity (`Wordle`/`Duolingo` audience) but quit or resent streak coercion and energy batteries. | Enjoy a light 3–5 minute daily brain spark and actually remember what they learned without guilt. | Zero energy/hearts walls (`FND-014`), zero punitive streak wipes, forgiving momentum instead of chore anxiety. |
| **Primary: Social Circle / Group Hosts** | Friend groups, families, couples, and remote Discord/Slack circles (2–30+ people) wanting fun shared trivia or language/culture play. | Drop one link in chat and play a lively round together (live or async over 24h) without installs or paywalls. | No 3–10 player `Kahoot` cap (`FND-003`), no mobile scroll/disconnect frustration (`FND-002`), no multi-week async ghosting (`FND-004`). |
| **Operator: Solo Backend Developer** | Backend-leaning solo builder focused on real-time sync, deterministic data reliability, optional local AI, and `$0` cost. | Build, curate, and operate the entire product solo with `$0` dev/prod/deploy spend and minimal manual moderation. | Open CC0/CC-BY-SA datasets (`FND-015`), local-first personal state + edge room sync (`FND-016`), bring-your-own-group links (no public stranger feeds). |

#### Value Proposition
- **For learners:** *All the daily spark of Wordle/Connections + real memory retention, with zero energy bars, zero streak punishment, and real friends in the loop.*
- **For friend groups:** *Zero-account, mobile-first co-op & duel rounds for 2–30+ players—live or at your own pace over 24 hours—completely free.*
- **For the solo builder:** *A data-reliability and real-time systems showcase running at `$0` baseline cost with optional on-device WebGPU AI.*

---

### 2. Product Goals & Measurable Success Indicators (`GOAL-NNN`)

*(Explicitly separates verified baseline/cost facts from target product hypotheses.)*

| Goal ID | Goal Statement | Traceability | Success Indicator & Target | Measurement Basis |
|---|---|---|---|---|
| **GOAL-001** | **Deliver guilt-free, joyful 3–5 minute learning sessions** with zero energy/life depletion and forgiving momentum mechanics. | `PRB-005`, `RCA-004`, `FND-010`, `FND-014` | **Hard rule:** `0` energy walls / `0` streak-loss resets.<br>**Target hypothesis:** `>= 65%` round completion rate; `>= 35%` voluntary Day-7 return among un-coached test users. | `[FACT]` (zero-wall design) + `[TARGET HYPOTHESIS — needs Stage 02/post-MVP cohort test]` |
| **GOAL-002** | **Enable frictionless browser-native social play & sharing** across mobile and desktop without accounts or player-count caps. | `PRB-005`, `RCA-002`, `RCA-003`, `FND-001`–`FND-003` | **Hard rule:** Guest join via link in `<= 2` taps with no signup; supports `>= 30` players per room at `$0`.<br>**Target hypothesis:** `< 15s` link-open to active round; `>= 98%` mobile session recovery after brief reconnect. | `[FACT]` (no guest login / no 10-player paywall) + `[TARGET HYPOTHESIS]` |
| **GOAL-003** | **Ensure high-signal, attribution-clean open learning content** via deterministic curation pipelines rather than paid writers. | `DEC-009`, `FND-015`, `SRC-029` | **MVP baseline:** `>= 1,500` curated, deduplicated, difficulty-graded items across `2` flagship tracks (`World/Culture Knowledge` + `Phrases & Words in Context`) sourced from CC0 / CC BY-SA 4.0 datasets with `< 1%` user-flagged ambiguity/error rate. | `[FACT]` (open corpus availability) + `[TARGET QUALITY GATE]` |
| **GOAL-004** | **Operate development, CI/CD, and production at strict `$0/month` cost** while keeping personal mastery data reliable. | `DEC-009`, `FND-016`, `SRC-030` | **Hard rule:** `$0` total spend on dev tools, CI, DB, hosting, and APIs; solo mastery stored client-local (`IndexedDB` + portable backup key); baseline traffic stays within `< 50%` of free-tier daily quotas (`< 50K` edge reqs/day, `< 50K` DB writes/day). | `[FACT]` (verified against Cloudflare Pages/Workers/DO/D1 free-tier limits `SRC-030`) |
| **GOAL-005** | **Provide optional browser-local AI hints & "why" explanations** on capable devices with zero cloud-AI dependency. | `DEC-009`, `FND-013`, `SRC-022` | **Hard rule:** `$0` cloud LLM spend; `100%` of core gameplay/learning works deterministically when WebGPU is absent or disabled; WebGPU local explanations load only on explicit opt-in. | `[FACT]` (`WebGPU` browser matrix `SRC-022`) |

---

### 3. Build-vs-Adopt / Non-Software Justification

Building on Stage 03 (`ART-003`), why is a custom web app warranted instead of adopting/configuring existing tools?

| Existing / Non-Software Alternative | Why It Fails `PRB-005` + `DEC-009` | Why Custom Web App Wins |
|---|---|---|
| **Duolingo (Free Tier)** | Enforces 25-point Energy battery draining on correct answers (`FND-014`), streak anxiety, and solo-only drills. | Zero energy bars, forgiving weekly/rolling mastery, and genuine friend co-op/duel rounds. |
| **Kahoot! / Quizizz** | Kahoot free personal tier caps at `10` players (`3` business custom; `FND-003`) and requires live host screen-sharing; no spaced-repetition personal mastery. | Zero-paywall 2–30+ player rooms, dual live + 24h micro-async pacing, plus personal spaced-repetition memory. |
| **NYT Wordle / Connections** | Primarily solo static daily puzzles; no adaptive spaced repetition or live co-op rooms (`FND-001`). | Retains the beloved zero-install browser & spoiler-free share grid while adding personalized mastery and live/async multiplayer. |
| **Anki / Paper Flashcards / Discord Bots** | High setup toil (`Anki`), solitary grind, or clunky text-only Discord bots lacking mobile visual/audio polish (`SRC-018`). | Instant link-based mobile play with reliable real-time state, audio/visual polish, and pre-curated open tracks. |

---

### 4. Solution Concept, MVP Scope, Explicit Non-Goals & Phased Roadmap

#### Core Product Loops (High-Level Concept)
1. **Daily 5-Card Ritual (Solo + Shareable):** A fast daily themed set (3–5 minutes) using deterministic spaced-repetition scheduling + spoiler-free emoji summary card (`🟩🟨⬜`) for group chats.
2. **Instant Co-Op / Friendly Duel Rooms (2–30+ Players):** Host picks a track/difficulty, shares a room link (no account required), and plays either **Live Synchronized** (real-time buzzer/reveal with reconnect state recovery) or **24-Hour Micro-Async** (everyone completes the same seeded 5-round set within 24h, with live partial reveal + zero freeze penalties).
3. **Zero-Guilt Mastery Ledger:** Tracks concepts *learned and retained* (warmth/mastery bars, "comeback bonus" for returning after breaks) rather than punishing missed days. Stored locally in the browser with a one-click portable export/sync code (`$0` user-account DB overhead).
4. **Optional "Local Tutor" Toggle:** On WebGPU-capable devices, users can opt in to download a small local model once to get conversational "explain why this answer works" notes offline; all other users get fast deterministic rule/etymology/fact notes pulled from curated open metadata.

#### MVP Scope (Phase 1 — Must-Have Only)
- **2 Curated Open-Data Tracks:**
  1. *Phrases & Words in Context* (sourced from `Tatoeba CC0` + `Wiktionary` open lexical data).
  2. *World, Culture & Science Trivia* (sourced from `Wikidata CC0` + `OpenTriviaDB CC BY-SA 4.0` with automated quality filtering and attribution).
- **Modes:** Solo Daily Ritual + Instant Co-Op / Friendly Duel Room (Live & 24h Micro-Async) + Spoiler-Free Share Card.
- **Reliability Core:** Zero-account guest play, resilient WebSocket reconnect hydration, mobile-first touch/keyboard-safe layout, and local-first personal mastery persistence (`IndexedDB` + portable sync token).
- **Zero-Cost Deployment:** Static bundle + edge room/daily-seed endpoints running entirely inside verified free tiers (`$0/month`), using open-source dev/test tooling only.

#### Explicit Non-Goals (Out of Scope)
- **NO** paid accounts, subscriptions, ads, energy/hearts bars, or streak-freeze microtransactions.
- **NO** cloud LLM/TTS/image API calls that incur per-request billing.
- **NO** open public leaderboards, stranger chat rooms, or user-generated public feeds (prevents solo-dev moderation & spam nightmares).
- **NO** K-12/university LMS integrations, gradebooks, certificates, or formal exam prep.
- **NO** native iOS/Android app-store binaries in MVP (responsive browser/PWA only).
- **NO** scraping or shipping copyrighted courses, lyrics, or proprietary media.

#### Phased Roadmap
| Phase | Focus | Entry / Exit Gate |
|---|---|---|
| **Phase 1: Zero-Cost MVP** | 2 open-data curated tracks, Solo Daily + Live/24h-Async Room, Local-First Mastery, Spoiler-Free Share Grid, `$0` static+edge deploy. | Complete Stage 07–11 specs; post-build playtest validates `<15s` mobile join, reconnect recovery, and `<1%` broken questions (`VAL-02`). |
| **Phase 2: Local AI & New Open Tracks** | Opt-in WebGPU/WebLLM conversational explanations & smart distractor hints (`SRC-022`); Web Audio synthesized music/ear-training track (`$0` asset cost). | Triggered after Phase 1 demonstrates Day-7 organic repeat engagement and clean free-tier headroom (`<50%` daily quota). |
| **Phase 3: Resilience at Scale** | Optional WebRTC P2P room offload for large live rooms + custom friend-imported CSV/JSON study decks (client-side only); human review of `$5/mo` tier only if viral traffic exceeds `100K` daily reqs. | Triggered only when free-tier daily traffic approaches `70–80%` of `SRC-030` hard limits. |

---

### 5. Product Risks & Validation Checkpoints

| Risk / Assumption | Severity | Mitigation Built into Product Definition | Validation Checkpoint |
|---|---|---|---|
| **R-01: Open dataset noise / boring phrasing (`FND-015`)** | High | Deterministic filtering, ambiguity scoring, difficulty tiering, and `"Report bad question"` local/lightweight flag before scaling tracks. | Audit 100-item random sample across both tracks (`<1%` defect gate in `GOAL-003`). |
| **R-02: Social vs. solo preference uncertainty (`VAL-02`)** | High | Ship *both* Solo Daily (with shareable grid) and 2–30+ Co-Op Rooms sharing one deterministic engine—value does not collapse if one mode dominates. | Observe solo vs. room-link share ratio in early test cohorts. |
| **R-03: `$0` free-tier hard cutoff on viral spike (`FND-016`)** | Medium-High | Keep solo play `100%` static/local (`0` edge hits after cache), cache daily seeds aggressively at CDN edge, and enforce graceful room-creation rate limits before hitting `100K` daily cap. | Load-estimate requests-per-session in Stage 09 (`ARC`) and verify graceful degradation. |
| **R-04: CC BY-SA 4.0 attribution & ShareAlike scope (`SRC-029`)** | Medium | Separate CC0 data (`Tatoeba CC0`, `Wikidata`) from CC BY-SA 4.0 (`OpenTriviaDB`, `Wiktionary`), display explicit source attribution, and publish curated open question packs openly if ShareAlike applies. | Legal/license verification checklist in Stage 07 & Stage 09. |
| **R-05: Local WebGPU failure on older phones (`FND-013`)** | Low-Medium | Strictly opt-in enhancement (`GOAL-005`); core UX relies `0%` on WebGPU/WebLLM. | Test core flow with WebGPU disabled across Safari/Chrome/Firefox. |

---

## Next Steps / Unresolved Issues

- **Stage 06 Gate Check:** `GOAL-001`..`GOAL-005` trace directly to `PRB-005`, `DEC-008`, and `DEC-009`; non-goals and MVP boundaries are unambiguous; build-vs-adopt alternatives are weighed; targets explicitly separate hard `$0` architectural facts from unvalidated product hypotheses.
- **Next Stage:** Hand off to **Agent 07 (Business Analyst & Requirements Engineer)** to translate `GOAL-001`..`GOAL-005` into testable functional requirements, non-functional requirements, business rules, and acceptance criteria (`REQ-NNN`, `TEST-NNN`).
