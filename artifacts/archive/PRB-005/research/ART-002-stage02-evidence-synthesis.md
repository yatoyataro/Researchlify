# ART-002 — Stage 02 Evidence & User Research Synthesis

| Field | Value |
|---|---|
| **Artifact ID** | `ART-002` |
| **Purpose** | Synthesize verified desk-research evidence across `RQ-01`..`RQ-06`, catalog evidenced user needs and pain points, and assess evidence quality, bias, and remaining gaps prior to competitive analysis. |
| **Status** | `approved` |
| **Owner** | `Agent 02 (Evidence & User Researcher)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`, `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-022`, `FND-001`..`FND-013`), `DEC-007` |

---

## Assumptions & Limitations

- **Desk-research-only scope (`DEC-007`):** No primary interviews, diary studies, usability tests, or quantitative surveys were executed in this cycle. All user sentiment comes from public community threads, bug trackers, industry reports, SEC filings, and public-health/polling institutions.
- **Self-selection & platform bias:** Reddit (`r/boardgames`, `r/skribbl`, `r/meetup`, `r/Marriage`, `r/googlesheets`, `r/discordapp`) and Hacker News skew toward vocal, tech-literate, or frustrated users; vendor sources (`Duolingo`, `NYT`, `Kahoot`) highlight strengths and curated metrics.
- **Unverified assumptions retained for Stage 03–04:** Exact willingness-to-pay for consumer web subscriptions vs. free/tip-jar/host-pass models, and conversion rates from link-share to repeat play without app install.

---

## Content

### 1. Executive Synthesis Across Research Questions (`RQ-01`..`RQ-06`)

1. **`RQ-01` (Games & Shared Play):** Mainstream browser-first daily games prove massive habit scale (`FND-001`: Wordle 4.2B–5.3B plays/yr; Connections >9M daily players) driven by zero-install browser access and spoiler-free social sharing. Meanwhile, live and async multiplayer browser games suffer acute mobile UX breakage—scroll/keyboard/zoom collisions (`FND-002`), mid-round socket drops without graceful state recovery (`FND-002`), harsh free-tier player caps in quiz hosts like Kahoot (`FND-003`), and unfair timeout/ghosting breakdowns in async board games (`FND-004`). Watch-party video sync is structurally blocked by browser DRM (`FND-009`).
2. **`RQ-02` (Friends, Couples & Hangout Coordination):** Coordination and decision fatigue are genuinely universal (`FND-005`, `FND-006`), yet pure scheduling clones and one-off "Tinder for movies/restaurants" apps suffer rapid post-novelty abandonment because they feel like logistics chores or disposable utilities (`FND-005`, `FND-006`). Similarly, commercial couples apps churn quickly when daily prompts turn into "homework" guilt and asymmetric backlog anxiety behind recurring paywalls (`FND-011`).
3. **`RQ-03` (Casual Learning & Playful Knowledge):** Casual learning has enormous verified demand (`FND-010`: Duolingo reached 52.7M DAU and $1.037B FY25 revenue), yet punitive streak anxiety, XP-grind leagues, and restrictive free-tier energy systems trigger growing learner burnout (`FND-010`). Learners want playful, low-shame, socially connected mastery rather than solitary streak coercion.
4. **`RQ-04` (Hobbies, Tabletop & Collaborative Creativity):** Across reading clubs and casual tabletop groups, users actively reject bloated or spoiler-leaky platforms (Goodreads/Fable, Roll20/Foundry) in favor of DIY Google Sheets or ultra-minimal shared boards (`FND-012`) to preserve spoiler-safe pacing, low prep, and group rituals.
5. **`RQ-05` (Local Community & Third Places):** Institutional evidence confirms elevated young-adult loneliness and the superior mental-health value of recurring in-person/hobby ties (`FND-007`), alongside active organizer flight from Meetup due to sharp 2024–2025 pricing hikes (`FND-008`). However, cold-start network effects and trust/safety moderation pose steep risks for a solo developer.
6. **`RQ-06` (Real-Time Reliability & Optional Local AI):** Baseline WebGPU now ships in Safari 26+ and Android Chrome (`FND-013`), making browser-local small-model AI viable as a privacy-preserving *optional* layer on modern devices—but mobile RAM (~1GB+ for 1B models), thermal throttling, and Firefox Android gaps require deterministic core experiences that work cleanly without AI (`FND-013`).

---

### 2. Evidenced User Needs & Pain Points

| Need ID | User Segment | Evidenced Pain Point / Unmet Need | Supporting Findings | Evidence Strength |
|---|---|---|---|---|
| **NEED-01** | Casual friend groups, remote teams, families, party hosts | Play lively real-time or micro-async browser games on phones without scroll/keyboard layout breakage, socket disconnects wiping rounds, or 3–10 player host paywalls. | `FND-001`, `FND-002`, `FND-003`, `FND-004` | `strong` / `moderate` |
| **NEED-02** | Busy friends & async hobby players | Enjoy multi-turn social games or shared challenges over days/hours without 2-hour scheduling hurdles, unfair freeze timeouts, or mid-game ghosting ruining the table for everyone. | `FND-004`, `FND-005` | `moderate` |
| **NEED-03** | Mainstream casual learners & trivia/language/skill enthusiasts | Learn and test knowledge in genuinely fun, bite-sized, socially playable loops without punitive streak guilt, ad/energy walls, or lonely flashcard grinding. | `FND-010`, `FND-001`, `FND-003` | `strong` |
| **NEED-04** | Book clubs, watch/media circles, casual hobby & tabletop groups | Coordinate pace-locked, spoiler-safe shared media/hobby rituals (chapters, episodes, lightweight maps/prompts, anonymous votes) without maintaining brittle Google Sheets or heavy pro tools. | `FND-012`, `FND-006` | `moderate` |
| **NEED-05** | Couples & close dyads/small friend circles | Share light, non-cringe, playful rituals and mutual taste discovery without "relationship homework" guilt, asymmetric unanswered backlogs, or expensive monthly subscriptions. | `FND-011`, `FND-006` | `moderate` |
| **NEED-06** | Local hobby organizers & newcomers | Host and discover recurring low-stakes local clubs without $175–$300+/yr incumbent paywalls or overwhelming public mega-events. | `FND-007`, `FND-008` | `strong` (macro need) / `moderate` (app migration) |

---

### 3. Evidence Quality, Bias & Missing-Evidence Audit

| Dimension | Assessment | Concrete Gaps / Missing Evidence |
|---|---|---|
| **Macro Behavioral & Market Scale** | **High quality** (`SRC-001`, `SRC-002`, `SRC-003`, `SRC-004`, `SRC-007`, `SRC-008`, `SRC-018`, `SRC-022`). Official SEC filings, HHS, Pew, Gallup, NYT, Kahoot docs, and W3C specs. | Missing direct funnel conversion telemetry for indie browser social games/clubs (e.g., exact % drop-off on mobile reconnects vs. account walls). |
| **Pain Points & Workarounds** | **Moderate quality** (`SRC-009`..`SRC-017`, `SRC-019`..`SRC-021`). Authentic unsolicited user complaints and DIY spreadsheet/bot workarounds. | Community threads over-represent dissatisfied power users; silent majority churn reasons (e.g., boredom vs. UX friction) are under-measured without interviews. |
| **Monetization & Willingness to Pay** | **Mixed / Incomplete.** Strong backlash documented against recurring subscriptions for couples/meetup organizers/casual quizzes (`SRC-015`, `SRC-018`, `SRC-020`), while NYT Games & Duolingo succeed at massive scale (`SRC-004`, `SRC-007`). | No primary pricing sensitivity data for one-time "host pass" vs. cosmetics/pack purchases vs. free-with-tips models in indie web apps. |

---

### 4. Ready-to-Run Primary Follow-Up Protocol (Deferred Pending User Authorization)

Because Stage 01–05 is strictly desk-research-only (`DEC-007`), **no outreach or interviews were conducted**. Once the user selects a top-ranked problem after Stage 05, the recommended pre-Stage-06/07 validation protocol (adapted from `user-research` skill `SKL-008a`) is:
- **Method 1 (5–8 contextual interviews, 30 min each, Mom Test past-behavior focus):** Recruit from the selected problem's target segment to verify the last 2 times their session/ritual broke down and what workaround they actually used.
- **Method 2 (Mobile-browser stress check / Wizard-of-Oz session test with 2–3 small friend groups):** Observe drop-off, reconnect recovery, and unprompted laughter/delight on real iOS Safari and Android Chrome connections.

---

## Next Steps / Unresolved Issues

- **Stage 02 Gate Check:** Every substantive claim maps to `SRC-001`..`SRC-022` and `FND-001`..`FND-013` in `EVIDENCE_LEDGER.md`; biases and missing primary evidence are explicitly stated; zero primary research was fabricated.
- **Next Stage:** Hand off to **Agent 03 (Existing Solutions & Gap Analyst)** to objectively compare current tools, workarounds, and build-vs-adopt alternatives across `NEED-01`..`NEED-06`.
