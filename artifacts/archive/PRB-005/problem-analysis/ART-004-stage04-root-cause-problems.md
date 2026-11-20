# ART-004 — Stage 04 Root Cause & Problem Analysis

| Field | Value |
|---|---|
| **Artifact ID** | `ART-004` |
| **Purpose** | Separate observable symptoms from structural root causes (`RCA-NNN`), validate causal chains against `EVIDENCE_LEDGER.md`, and formulate bounded, evidence-backed problem statements (`PRB-NNN`) for Stage 05 prioritization. |
| **Status** | `approved` |
| **Owner** | `Agent 04 (Root Cause & Problem Analyst)` |
| **Revision** | `v1.1` *(Fixed `ISS-002`: removed typo `FND-020` in `RCA-006`)* |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`, `ART-002`, `ART-003`, `EVIDENCE_LEDGER.md` (`FND-001`..`FND-013`) |

---

## Assumptions & Limitations

- **Desk-research causal boundary (`DEC-007`):** Because no live interviews or product telemetry analyses were run, some behavioral causal links (e.g., exact share of churn caused by emotional guilt vs. prompt repetition) are explicitly marked `[HYPOTHESIS — needs validation]` rather than treated as proven fact.
- **No "missing app" tautologies:** Every `RCA-NNN` traces to technical, economic, incentive, or behavioral mechanisms rather than "lack of a dedicated app."

---

## Content

### 1. Symptoms vs. Structural Root Causes (`RCA-NNN`)

| RCA ID | Domain | Observable Symptom(s) | Structural Root Cause | Evidence Status (`FND-NNN` / Hypothesis) |
|---|---|---|---|---|
| **RCA-001** | Mobile Browser Real-Time Play | Canvas scrolls/zooms mid-stroke, virtual keyboard squishes UI, players are booted on brief Wi-Fi/cellular switches (`SRC-009`, `SRC-010`, `SRC-011`). | Desktop-first browser engines + naive ephemeral WebSocket state: games keep round state in volatile connection memory without idempotent reconnect tokens, touch-action isolation, or viewport-safe input modes. | **Evidenced** (`FND-002`, `FND-004`) + technical mechanism (`SRC-009`, `SRC-010`, `SRC-013`). |
| **RCA-002** | Group Quiz & Party Host Economics | Casual/community hosts hit 3–10 player walls on Kahoot or 8-player active caps on Jackbox (`SRC-018`) and fall back to clunky chat bots. | Enterprise/classroom SaaS pricing models monetize seat/player counts via annual subscriptions, misaligning with sporadic mainstream social hosts. | **Evidenced** (`FND-003`, `SRC-018`). |
| **RCA-003** | Async Social Pacing Mismatch | Multi-week async board games end in ghosting or unfair freeze penalties (`SRC-013`, `SRC-014`); live party games fail when friends cannot align a 90-minute slot (`FND-005`). | Binary session architecture: existing games assume either *strictly synchronous* presence (all online together) or *unbounded multi-week* turns, lacking forgiving micro-async turns, drop-in/dropout grace, and deterministic bot/AI fill-in. | **Evidenced symptom** (`FND-004`, `FND-005`); **Causal Hypothesis** that micro-async + graceful fill-in resolves abandonment (`[HYPOTHESIS — needs validation]`). |
| **RCA-004** | Solo Streak & Energy Monetization | Learners suffer streak burnout, anxiety, and paywall resentment (`SRC-006`) despite high initial desire for casual learning (`SRC-004`). | Engagement-maximization via loss aversion: solo learning apps use punitive daily streak loss and restrictive energy/hearts to drive ad views and subscription upgrades, decoupling habit from social joy. | **Evidenced** (`FND-010`, `SRC-004`, `SRC-006`); **Causal Hypothesis** on how much social co-play retains lapsed streak-burnout users (`[HYPOTHESIS — needs validation]`). |
| **RCA-005** | Coordination "Split-Brain" & Utility Churn | Friends ignore When2meet links, split RSVPs between Partiful and chat, or abandon swipe decision apps after 1–2 nights (`SRC-016`, `SRC-017`, `FND-006`). | Disconnected context & zero ongoing loop: external polling tools strip conversation context and provide no persistent social memory/ritual once a single time or movie is picked. | **Evidenced** (`FND-005`, `FND-006`). |
| **RCA-006** | Dyadic "Homework" & Asymmetric Effort | Couples abandon prompt apps within weeks/months after accumulating unanswered question backlogs (`SRC-020`). | Synchronized daily-quota UX: forcing both partners onto identical daily prompt queues turns asymmetric schedules into visible relationship scorecards and subscription guilt. | **Evidenced** (`FND-011`, `SRC-020`). |
| **RCA-007** | Spoiler Leakage & Group-State Blindness in Hobby Apps | Book/media clubs abandon Goodreads/Fable for DIY Google Sheets with hidden columns and formula hacks (`SRC-021`). | Individual-first data models: consumer media trackers organize comments and ratings globally by title rather than scoping visibility to each group's current chapter/episode progress gate. | **Evidenced** (`FND-012`, `SRC-021`). |
| **RCA-008** | Local Community Fee Squeeze & Cold-Start Friction | Meetup organizers flee $175–$300+/yr hikes (`SRC-015`), while young adults stay lonely despite craving recurring in-person hobby ties (`SRC-001`–`SRC-003`). | Two-sided marketplace rent-seeking + trust/density barrier: incumbent platforms extract organizer rents once network effects lock in, while new platforms face geographic cold-start and newcomer social anxiety. | **Evidenced** (`FND-007`, `FND-008`, `SRC-015`). |
| **RCA-009** | Browser DRM Video Isolation | Discord + Teleparty watch parties suffer black screens and cumulative audio/video drift (`SRC-019`). | Intentional OS/browser HDCP & DRM capture blocks prevent third-party apps from reading or re-syncing commercial streaming video frames. | **Evidenced** (`FND-009`, `SRC-019`). |

---

### 2. Evidence-Backed Problem Statements (`PRB-NNN`)

#### `PRB-001` — Fragile Mobile Sessions & Host Paywalls in Casual Group Browser Games
- **Affected Users:** Mainstream friend groups, families, remote coworkers, and casual community hosts (groups of 3–30+ people) trying to play quick social, drawing, word, or trivia games together.
- **Context & Trigger:** When a group drops a browser game link in chat (live on a call/couch or asynchronously across busy schedules) and participants join primarily from mobile browsers on variable Wi-Fi/cellular connections.
- **Root Causes:** `RCA-001` (volatile socket state + mobile viewport/scroll/keyboard collisions), `RCA-002` (seat/player-count paywalls on quiz hosts), `RCA-003` (rigid synchronous-only or unbounded multi-week async pacing).
- **Consequence:** Rounds stall or drop players mid-turn without clean state recovery, mobile touch UX ruins gameplay, hosts hit 3–10 player caps or content repetition, and groups abandon shared play prematurely.
- **Supporting Evidence:** `FND-001`, `FND-002`, `FND-003`, `FND-004`, `FND-013`.
- **Problem Boundaries & Exclusions:** **Excludes** synchronized DRM streaming video (`RCA-009` / `FND-009`), heavy licensed Euro-boardgames (`BGA`'s territory), and 3D AAA/native-app gaming.

#### `PRB-002` — Group Hangout "Poll Fatigue" & Disposable Decision-Utility Abandonment
- **Affected Users:** Friend groups and couples trying to pick a time, movie, restaurant, or low-key weekend activity.
- **Context & Trigger:** When "let's do something soon" in a group chat triggers availability grids (`When2meet`), over-produced event pages (`Partiful`), or endless scrolling (`Netflix`/delivery apps).
- **Root Causes:** `RCA-005` (split-brain context between chat and external links, plus one-off utility design lacking recurring social memory).
- **Consequence:** Hosts bear exhausting project-management labor, friends ignore polls or scroll 20–45 minutes without deciding, and standalone swipe/poll utilities are forgotten after 1–2 uses.
- **Supporting Evidence:** `FND-005`, `FND-006`.
- **Problem Boundaries & Exclusions:** **Excludes** formal corporate calendar scheduling (`Calendly`) and large public ticketed conferences (`Luma`/`Eventbrite` territory).

#### `PRB-003` — Local Club Organizer Cost Squeeze & Newcomer Third-Place Friction
- **Affected Users:** Volunteer local hobby club organizers (running, board games, books, language tables) and lonely young adults seeking recurring in-person community.
- **Context & Trigger:** When volunteer organizers face sharp incumbent subscription hikes (`Meetup`) or newcomers try to find welcoming recurring micro-groups without awkward mega-mixers.
- **Root Causes:** `RCA-008` (incumbent rent-seeking + geographic cold-start & stranger trust/safety friction).
- **Consequence:** Volunteer clubs shut down or fragment across ad-hoc chats, while lonely young adults fail to bridge online interest into recurring in-person "weak-tie" friendships.
- **Supporting Evidence:** `FND-007`, `FND-008`.
- **Problem Boundaries & Exclusions:** **Excludes** commercial dating apps and high-moderation open public social feeds.

#### `PRB-004` — Couples & Close-Dyad Ritual Burnout ("Homework Guilt" & Subscription Fatigue)
- **Affected Users:** Romantic couples (local and long-distance) and close 2-person friend/sibling pairs.
- **Context & Trigger:** When pairs adopt prompt/quiz apps (`Paired`, `Agapé`) to feel closer during busy weeks, only to hit repetitive canned questions, recurring ~$80/yr paywalls, and asymmetric unanswered backlogs.
- **Root Causes:** `RCA-006` (daily-quota scorekeeping exposing effort asymmetry) and `RCA-005` (canned prompt fatigue).
- **Consequence:** Tools meant to spark delight instead generate guilt, obligation, and rapid uninstallation within weeks or months.
- **Supporting Evidence:** `FND-011`, `FND-006`, `FND-013`.
- **Problem Boundaries & Exclusions:** **Excludes** clinical couples therapy or mental-health crisis counseling.

#### `PRB-005` — Casual Learning Engagement Burnout (Punitive Solo Streaks vs. Joyful Social Mastery)
- **Affected Users:** Mainstream casual learners (trivia buffs, language explorers, music/ear-training hobbyists, curious adults) who enjoy 5–10 minute daily brain play.
- **Context & Trigger:** When learners move past initial onboarding in dominant apps (`Duolingo`) and encounter streak-loss anxiety, XP-league grinding, free-tier energy caps, and solitary drills.
- **Root Causes:** `RCA-004` (loss-aversion streak/energy monetization) + `RCA-002`/`RCA-003` (lack of forgiving, playful small-group or co-op learning arenas).
- **Consequence:** Learning turns from curiosity and play into guilt-driven chore maintenance, causing eventual burnout or passive streak-preservation without real enjoyment.
- **Supporting Evidence:** `FND-010`, `FND-001`, `FND-003`, `FND-013`.
- **Problem Boundaries & Exclusions:** **Excludes** accredited K-12/university LMS grading, enterprise compliance training, and exam-prep cramming.

#### `PRB-006` — Spoiler Leakage & Brittle Spreadsheet Overhead in Shared Hobby & Media Circles
- **Affected Users:** Book clubs, serialized TV/podcast/anime watch circles, and casual narrative/tabletop groups reading or progressing at uneven speeds.
- **Context & Trigger:** When a group tries to discuss chapters/episodes, collect blind/anonymous ratings, and track shared club history without spoiling slower members.
- **Root Causes:** `RCA-007` (global, un-gated social threads on `Goodreads`/`Fable`) + `RCA-005` (lack of spoiler-locked group state).
- **Consequence:** Clubs either risk ruining twists for members or force one organizer to build and maintain fragile Google Sheets with hidden columns and manual formulas.
- **Supporting Evidence:** `FND-012`, `FND-013`.
- **Problem Boundaries & Exclusions:** **Excludes** DRM video streaming playback (`RCA-009`) and heavy rule-automated VTTs (`Foundry`/`Roll20`).

---

### 3. Causal Assumptions & Validation Needs List

| ID | Linked Problem | Unvalidated Causal Hypothesis | Impact if Wrong | Validation Method (Post-Stage 05 if Selected) |
|---|---|---|---|---|
| **VAL-01** | `PRB-001` | Reconnect-resilient state + micro-async/drop-in turns materially increase repeat group completion over pure live rooms. | Effort spent on async/reconnect reliability wouldn't lift repeat sessions if prompt monotony is the true blocker. | Mobile-device group playtest + dropout/rejoin telemetry check. |
| **VAL-02** | `PRB-005` | Learners burned out by solo streak guilt will engage more joyfully with cooperative/friendly-duel social learning rituals than solo drills. | If most casual learners prefer private solo anonymity (`Wordle`), social co-play may be smaller than solo+share. | Compare solo-with-shareable-grid vs. 2–6 player co-op loop in interviews. |
| **VAL-03** | `PRB-006` | Spoiler-locked progress reveals and blind group voting appeal beyond niche book clubs to mainstream TV/movie/hobby circles. | Market could remain a smaller subset of organized book clubs (`Audience breadth` risk). | Survey/interview casual TV/anime/book-club groups on willingness to leave chat/Sheets. |
| **VAL-04** | `PRB-002` / `PRB-004` | Turning one-off decisions or dyad prompts into persistent playful rituals prevents 1-to-2-session abandonment. | Utility churn may be structural even with playful wrappers. | Cohort retention check on a lightweight concierge/prototype test. |

---

## Next Steps / Unresolved Issues

- **Stage 04 Gate Check:** All 6 problems (`PRB-001`..`PRB-006`) clearly name affected users, context, consequence, `RCA-NNN`, `FND-NNN`, and explicit exclusions; symptoms vs. root causes are separated; unvalidated causal hypotheses are flagged (`VAL-01`..`VAL-04`).
- **Next Stage:** Hand off to **Agent 05 (Problem Prioritization Analyst)** to apply the customized rubric from `DEC-006` (including explicit `Fun / delight` and `Audience breadth` criteria), score all 6 `PRB-NNN` candidates, run sensitivity checks, and present the **Top 3** + rejected candidates before pausing for human decision.
