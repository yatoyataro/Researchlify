# ART-013 — Package B: Client Presentation Outline

| Field | Value |
|---|---|
| **Artifact ID** | `ART-013` |
| **Purpose** | 17-section slide/presentation outline translating approved discovery findings and `PRB-005` zero-cost product plan for stakeholder walkthroughs. |
| **Status** | `approved` |
| **Owner** | `Agent 13 (Client-Facing Research Synthesizer & Humanizer)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-001`..`ART-011`, `DECISIONS.md`, `EVIDENCE_LEDGER.md`, `SKL-004`, `SKL-006` |

---

## Assumptions & Limitations

- Slide speaking notes reflect desk-research evidence only (`DEC-007`); expected engagement targets are labeled as hypotheses to verify in playtesting.

---

## Content (17 Presentation Sections)

### 1. Project introduction
- Title: Guilt-Free Social Casual Learning at Zero Cost (`PRB-005`).
- Goal: Identify a broad, fun web app problem backed by evidence and suited to a solo backend developer (`real-time sync`, `data reliability`, `optional local AI`) with `$0` budget (`DEC-009`).

### 2. Context and current situation
- Mainstream consumers love short daily browser games (`Wordle`, `Connections`) and casual learning (`Duolingo`), yet juggle fragmented mobile tools when trying to learn or play with friends (`ART-001`).

### 3. Research approach
- Five-stage desk research across 30 verified sources (`SEC` filings, official product docs, `W3C` specs, and community forums; `SRC-001`..`SRC-030`), zero fabricated interviews (`DEC-007`).

### 4. What we investigated
- Five consumer clusters: browser party/daily games, group hangout coordination, casual learning, hobby/reading circles, and local clubs (`ART-001`, `ART-002`).

### 5. Key findings
- `Wordle` saw `4.2B` solved games in 2025; `Connections` tops `9M` daily players (`SRC-007`, `SRC-008`).
- `Duolingo` hit `52.7M` DAU and `$1.037B` FY25 revenue (`SRC-004`), yet its 25-point Energy system triggers free-user frustration (`SRC-006`).
- `Kahoot!` caps free personal hosts at `10` players (`3` on business custom games; `SRC-018`).

### 6. Identified problem
- `PRB-005`: Casual learners and social groups lose the joy of learning when solo apps punish missed days or drain energy on correct answers, while group quiz tools gate friends behind paywalls (`ART-004`).

### 7. Evidence supporting the problem
- Official SEC data (`SRC-004`), Class Central 2025 Energy report (`SRC-006`), Kahoot support caps (`SRC-018`), and mobile disconnect/viewport reports (`SRC-009`..`SRC-014`).

### 8. Existing solutions
- Fair look at `Duolingo`, `Kahoot!`, `NYT Games`, `Anki`, and Discord bots (`ART-003`): each solves part of the puzzle, none blends guilt-free daily memory with `$0` multi-player friend rooms.

### 9. Identified gap
- A forgiving, zero-account browser space supporting both 5-card daily solo habits and 2-to-30+ player co-op or 24-hour async rounds (`GAP-02`).

### 10. Why we prioritized this problem
- Ranked top 2 overall (`4.40/5.00`) and `#1` (`4.75/5.00`) under evidence-and-habit sensitivity (`ART-005`), then chosen by the user alongside a strict `$0` constraint (`DEC-008`, `DEC-009`).

### 11. Proposed solution
- Browser-native daily & social brain-play web app: zero energy bars, zero signup, spoiler-free share grids, and link-based friend rooms (`ART-006`).

### 12. How the solution works
- Solo play runs locally from CDN-cached open-data packs (`IndexedDB` mastery + portable backup code).
- Multiplayer rooms sync via hibernatable Cloudflare Durable Objects (`20:1` WS ratio, `0` idle duration) with reconnect tokens and pre-reveal answer protection (`ART-009`).

### 13. Major application capabilities
- Two curated open tracks (`Phrases & Words in Context` + `World/Culture Trivia`), Live and 24h Async room pacing, WCAG 2.1 AA mobile UI, card issue flagging, and Phase 2 opt-in WebGPU local tutor (`ART-007`, `ART-008`).

### 14. Scope and limitations
- MVP excludes subscriptions, ads, cloud LLMs, public stranger feeds, LMS grading, and native app-store apps.
- Relies on desk research until `VAL-02` cohort testing; `$0` Cloudflare tier caps at `100K` daily Worker/DO requests (`SRC-030`).

### 15. Expected benefits
- Target hypothesis: removes paywall/streak friction for learners and showcases solo backend reliability (`GOAL-001`..`GOAL-005`). Explicitly labeled as targets to prove in testing, not guaranteed metrics.

### 16. Recommended next steps
- Build and audit the open-corpus curation pipeline (`>=1,500` clean items), ship the static+edge MVP (`Package A` Milestones 1–4), and run `VAL-02` mobile playtests.

### 17. Conclusion
- `PRB-005` combines verified mainstream demand, clear incumbent pain, and a realistic `$0` engineering architecture ready for implementation handoff (`ART-011`).
