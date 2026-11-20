# ART-005 — Stage 05 Problem Prioritization & Top-3 Recommendation

| Field | Value |
|---|---|
| **Artifact ID** | `ART-005` |
| **Purpose** | Score and rank all validated Stage 04 problem candidates (`PRB-001`..`PRB-006`) using the customized `DEC-006` rubric (including explicit `Fun / delight` and `Audience breadth` criteria), run sensitivity checks, and recommend the Top 3 problems for human rank approval. |
| **Status** | `approved` *(User selected `PRB-005` via `DEC-008` with `DEC-009` zero-money-cost constraint)* |
| **Owner** | `Agent 05 (Problem Prioritization Analyst)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-003`, `ART-004`, `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-028`, `FND-001`..`FND-013`), `DECISIONS.md` (`DEC-006`, `DEC-007`) |

---

## Assumptions & Limitations

- **Judgment vs. measurement:** `Evidence strength` and empirical market/user counts are grounded in `EVIDENCE_LEDGER.md`, whereas `Fun / delight`, `Audience breadth`, `Solo backend & real-time/AI feasibility`, and `Risk & constraints` reflect structured analyst judgment anchored to explicit 1–5 definitions. Integer scores (`1–5`) are used intentionally to avoid false mathematical precision.
- **Close tie between Rank #1 and Rank #2:** As shown in Section 4 (Sensitivity Analysis), `PRB-001` (`4.50`) and `PRB-005` (`4.40`) sit within `0.10` points and swap order under an evidence/frequency-heavy weighting. Human choice between them depends on product appetite (pure social play vs. playful casual learning).

---

## Content

### 1. Customized Prioritization Rubric & Weight Rationale (`DEC-006`)

Adapted from `WORKFLOW.md` Section 6 to reflect the user's explicit criteria (`Fun / delight`, `Audience breadth`), desk-research grounding (`Evidence strength`), and solo developer profile (`backend`, `real-time systems`, `data reliability`, `optional local AI`):

| Criterion | Weight | 1 (Lowest) | 3 (Moderate) | 5 (Highest) |
|---|---:|---|---|---|
| **Fun / delight** | **20%** | Purely utilitarian chore | Situational novelty or utility-wrapped fun | Inherently playful, joyful, emotionally rewarding, shareable social loop |
| **Audience breadth** | **15%** | Tiny hyper-niche | Meaningful multi-segment niche (e.g., book clubs or couples) | Broad mainstream appeal across demographics, ages, and friend circles |
| **User impact / pain intensity** | **15%** | Minor annoyance | Noticeable friction with tolerable workarounds | Acute recurring breakage, burnout, paywall block, or spoiled shared joy |
| **Evidence strength** | **20%** | Unverified assumption | Consistent qualitative community reports (`moderate`) | Multiple corroborated primary/official/empirical + behavioral sources (`strong`) |
| **Solo backend & real-time/AI feasibility** | **15%** | Heavy art/content ops, moderation army, or cold-start trap | Feasible solo with moderate content or integration load | Direct leverage of real-time sync, deterministic state reliability & optional local AI |
| **Frequency / repeat engagement** | **10%** | One-off or rare annual use | Bi-weekly / monthly / occasional party use | Daily or multiple-times-weekly recurring ritual |
| **Risk & constraints** | **5%** | Severe legal/IP/moderation/cold-start trap | Manageable differentiation or retention risk | Low, well-bounded risk for a solo operator |
| **Total** | **100%** | — | — | — |

---

### 2. Prioritization Matrix (All 6 Candidates)

| Rank | Problem ID & Short Title | Fun / Delight (20%) | Audience Breadth (15%) | Impact (15%) | Evidence (20%) | Solo Backend/RT/AI Fit (15%) | Frequency (10%) | Risk (5%) | Weighted Score (/5.00) | Decision |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **#1** | **`PRB-001` — Fragile Mobile Sessions & Host Paywalls in Casual Group Browser Games** | 5 *(J)* | 5 *(E+J)* | 4 *(E)* | 4 *(M)* | 5 *(J)* | 4 *(E+J)* | 4 *(J)* | **4.50** | **Top 3 — Recommended #1** |
| **#2** | **`PRB-005` — Casual Learning Engagement Burnout (Solo Streaks vs. Joyful Social Mastery)** | 4 *(J)* | 5 *(E)* | 4 *(E)* | 5 *(M)* | 4 *(J)* | 5 *(E)* | 3 *(J)* | **4.40** | **Top 3 — Strong #2** |
| **#3** | **`PRB-006` — Spoiler Leakage & Brittle Spreadsheet Overhead in Hobby & Media Circles** | 4 *(J)* | 3 *(J)* | 4 *(E)* | 3 *(M)* | 5 *(J)* | 3 *(E+J)* | 4 *(J)* | **3.70** | **Top 3 — Focused #3** |
| **#4** | `PRB-004` — Couples & Close-Dyad Ritual Burnout ("Homework" & Paywalls) | 4 *(J)* | 3 *(J)* | 3 *(E)* | 3 *(M)* | 4 *(J)* | 3 *(E)* | 3 *(J)* | **3.35** | Defer / Drop |
| **#5** | `PRB-002` — Group Hangout "Poll Fatigue" & Disposable Decision-Utility Churn | 3 *(J)* | 5 *(E)* | 3 *(E)* | 3 *(M)* | 4 *(J)* | 2 *(E)* | 2 *(J)* | **3.30** | Reject |
| **#6** | `PRB-003` — Local Club Cost Squeeze & Newcomer Third-Place Cold Start | 3 *(J)* | 4 *(E)* | 4 *(E)* | 4 *(M)* | 2 *(J)* | 3 *(J)* | 1 *(E+J)* | **3.25** | Reject |

*Annotation key: `(M)` = Measured/documented evidence strength; `(E)` = Grounded in `EVIDENCE_LEDGER.md` observations/metrics; `(J)` = Structured analyst judgment.*

---

### 3. Score Justification & Evidence Traceability

#### Top 3 Promising Problems

1. **Rank #1 — `PRB-001`: Fragile Mobile Sessions & Host Paywalls in Casual Group Browser Games (`4.50 / 5.00`)**
   - *Why it leads:* Highest combined **Fun / delight (`5`)**, **Audience breadth (`5`)**, and **Solo backend/RT/AI fit (`5`)**. NYT daily puzzles (`FND-001`) prove tens of millions play zero-install browser games and share results in group chats, while live/async multiplayer alternatives break on mobile viewports & socket drops (`FND-002`: `SRC-009`–`SRC-011`), price out casual 11–50+ player hosts (`FND-003`: `SRC-018`), or suffer multi-week ghosting and freeze penalties (`FND-004`: `SRC-012`–`SRC-014`).
   - *Developer leverage:* Directly rewards backend mastery in **idempotent reconnect hydration, deterministic state machines, resilient WebSocket/micro-async turn timers, and optional local WebGPU/WebLLM prompt generation or smart dropout bot fill-in** (`FND-013`). "Bring-your-own-group" invite links eliminate stranger moderation and geographic cold start.

2. **Rank #2 — `PRB-005`: Casual Learning Engagement Burnout — Solo Streak Coercion vs. Joyful Social Mastery (`4.40 / 5.00`)**
   - *Why it's a near-tie #2:* Carries the **strongest quantitative + qualitative evidence (`5`)** and **daily habit ceiling (`5`)** in the entire dataset. Duolingo's official SEC filings (`SRC-004`: 52.7M DAU, ~130M MAU, $1.037B FY25 revenue) prove massive mainstream appetite, while 2025–2026 backlash over streak anxiety and energy limits (`SRC-006`), alongside Kahoot's 10-player cap (`SRC-018`) and Wordle/Connections' social sharing (`SRC-007`, `SRC-008`), reveals a clear opening for **forgiving, playful, co-op/duel browser learning rituals**.
   - *Developer leverage & caveat:* High backend value (spaced-repetition reliability, real-time co-op/duel sync, optional local AI hints/explanations without cloud LLM cost). Slightly lower feasibility (`4`) and higher risk (`3`) than `PRB-001` due to domain content curation needs and crowded incumbents.

3. **Rank #3 — `PRB-006`: Spoiler Leakage & Brittle Spreadsheet Overhead in Shared Hobby & Media Circles (`3.70 / 5.00`)**
   - *Why it rounds out the Top 3:* A crisp, under-served **pure data-reliability & stateful sync problem** (`Feasibility: 5`). Book/watch/narrative circles visibly build complex Google Sheets (`SRC-021`) because global trackers (`Goodreads`/`Fable`) leak spoilers and lack blind group voting/anonymous scoring (`FND-012`).
   - *Developer leverage & caveat:* Server-enforced spoiler progress gates, synchronized "everyone finished chapter N -> reveal reactions" moments, and optional local AI spoiler-safe recaps (`FND-013`). Narrower audience breadth (`3`) and lower weekly cadence (`3`) keep it behind `PRB-001` and `PRB-005`.

#### Rejected / Deferred Candidates (Ranks #4–#6)

- **`PRB-004` — Couples & Close-Dyad Ritual Burnout (`3.35` — Defer/Drop):** Real dissatisfaction with "homework" guilt and ~$80/yr subscriptions (`SRC-020`, `SRC-027`), but free `Gottman Card Decks` already exists (`SRC-027`), audience breadth is narrower (`3`), and dyadic retention often decays once novelty fades. *(Note: Best aspects of playful dyad micro-rituals can be served naturally as a 2-player mode inside `PRB-001`.)*
- **`PRB-002` — Group Hangout Poll Fatigue & Choice Paralysis (`3.30` — Reject):** High breadth (`5`), yet low repeat retention (`2`) and high graveyard risk (`2`): indie movie-swipe and When2meet clones are routinely abandoned after 1–2 uses (`FND-006`), and a single "dictator text" in WhatsApp/iMessage already beats dedicated scheduling apps (`FND-005`).
- **`PRB-003` — Local Club Cost Squeeze & Third-Place Friction (`3.25` — Reject):** Despite compelling macro loneliness data (`SRC-001`–`SRC-003`) and Meetup price backlash (`SRC-015`), **free incumbents `Luma` and `Heylo` already address organizer pricing (`SRC-025`)**, and a new local discovery marketplace imposes extreme geographic cold-start and physical trust/safety moderation burdens (`Feasibility: 2`, `Risk: 1`) unsuitable for a solo backend builder.

---

### 4. Sensitivity & Uncertainty Analysis

| Sensitivity Scenario | Weight Adjustments | New Top 3 Scores (`PRB-001` / `PRB-005` / `PRB-006`) | Rank Order Impact |
|---|---|---|---|
| **Baseline (`DEC-006`)** | Fun 20, Breadth 15, Impact 15, Evidence 20, Fit 15, Freq 10, Risk 5 | **`4.50`** / **`4.40`** / **`3.70`** | `PRB-001` > `PRB-005` > `PRB-006` |
| **Scenario A: Evidence & Habit Conservative** | Evidence `20->30%`, Freq `10->15%`; Fun `20->15%`, Fit `15->10%` | **`4.60`** / **`4.75`** / **`3.55`** | **`PRB-005` flips to #1** (+0.15 over `PRB-001`); Top 3 set unchanged |
| **Scenario B: Delight & Solo-Tech Leverage** | Fun `20->25%`, Fit `15->20%`; Evidence `20->15%`, Impact `15->10%` | **`4.60`** / **`4.35`** / **`3.80`** | **`PRB-001` widens #1 lead** (+0.25 over `PRB-005`); Top 3 set unchanged |
| **Scenario C: Downside Evidence Stress** | Penalize `PRB-001` Impact `4->3` & `PRB-006` Evidence `3->2` (baseline weights) | **`4.35`** / **`4.40`** / **`3.50`** | `PRB-005` edges #1 by `0.05`; Top 3 set remains strictly `{PRB-001, PRB-005, PRB-006}` |

**Sensitivity Conclusion:** Across all tested perturbations, **`PRB-001`, `PRB-005`, and `PRB-006` robustly hold the Top 3 positions**, while `#4–#6` stay below `3.40`. Only **#1 vs. #2** is sensitive to whether the user prioritizes **maximum fun + solo real-time/reliability leverage (`PRB-001`)** or **maximum empirical market proof + daily learning habit (`PRB-005`)**.

---

## Next Steps / Unresolved Issues

- **Human Decision Gate (`DEC-007`):** Execution is **paused after Stage 05**. Please confirm:
  1. Do you approve **Rank #1 (`PRB-001`: Fragile Mobile Sessions & Host Paywalls in Casual Group Browser Games)** to move forward into **Stage 06 (Product Definition)**, OR
  2. Would you prefer to advance **Rank #2 (`PRB-005`: Joyful Social Casual Learning)** or **Rank #3 (`PRB-006`: Spoiler-Safe Hobby/Media Circles)** instead?
- **Validation Note:** Whichever problem is chosen, `VAL-01`..`VAL-03` (`ART-004`) should be verified via lightweight mobile/user validation if primary user access is later authorized.
