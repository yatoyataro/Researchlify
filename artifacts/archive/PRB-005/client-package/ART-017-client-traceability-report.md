# ART-017 — Package B: Client Claim Traceability Report

| Field | Value |
|---|---|
| **Artifact ID** | `ART-017` |
| **Purpose** | Trace every substantive client-facing claim, statistic, capability, scope exclusion, and limitation in Package B (`ART-012`..`ART-015`) back to approved upstream artifacts (`SRC/FND/PRB/DEC/GOAL/REQ/ARC`). |
| **Status** | `approved` |
| **Owner** | `Agent 13 (Client-Facing Research Synthesizer & Humanizer)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-012`..`ART-015`, `ART-001`..`ART-011`, `DECISIONS.md`, `EVIDENCE_LEDGER.md` |

---

## Assumptions & Limitations

- Every metric in Package B derives exclusively from `EVIDENCE_LEDGER.md` or engineering calculations verified in `ART-009` (`v1.1`). Items labeled `hypothesis` or `provisional` carry explicit flags below.

---

## Content

### 1. Claim-to-Artifact Traceability Matrix

| Package B Claim / Capability | Location(s) | Upstream Source / Artifact ID(s) | Verification Status |
|---|---|---|---|
| `30` public sources consulted, zero live interviews/surveys run (`desk research only`) | `ART-012` §3, `ART-013` §3, `ART-014`, `ART-015` §9 | `DEC-007`, `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-030`) | **Verified Fact** |
| `Wordle`: `5.3B` plays (2024), `4.2B` solved (2025); `Connections`: `>9M` daily players | `ART-012` §3, `ART-013` §5, `ART-014`, `ART-015` §2 | `SRC-007`, `SRC-008`, `FND-001` | **Verified Fact** |
| `Duolingo`: `52.7M` DAU, `~130M` MAU, `84%` CURR, `$1.037B` FY25 revenue | `ART-012` §3, `ART-013` §5, `ART-014`, `ART-015` §2 | `SRC-004`, `FND-010` | **Verified Fact** |
| Duolingo mid-2025 25-point Energy system draining on correct answers (3–4 free lessons) & backlash | `ART-012` §3–4, `ART-013` §5, `ART-014`, `ART-015` §2 | `SRC-006`, `FND-014` | **Verified Fact** |
| `Kahoot!` free caps (`10` personal / `3` business custom); browser mobile scroll & disconnect bugs | `ART-012` §3–5, `ART-013` §5, `ART-014`, `ART-015` §2 | `SRC-009`–`SRC-014`, `SRC-018`, `FND-002`–`FND-004` | **Verified Fact** |
| Problem selection: `PRB-005` (`4.40` baseline, `4.75` evidence-weighted `#1`) + `$0` constraint | `ART-012` §1, §6; `ART-013` §10; `ART-014`; `ART-015` §1 | `DEC-006`, `DEC-008`, `DEC-009`, `ART-005` | **Verified Decision** |
| Open datasets (`Tatoeba CC0 1.0`, `Wikidata CC0 1.0`, `OpenTriviaDB CC BY-SA 4.0`, `Wiktionary CC BY-SA 4.0`) | `ART-012` §3, §8; `ART-014`; `ART-015` §8 | `SRC-029`, `FND-015`, `REQ-007`, `REQ-NFR-007` | **Verified Fact** |
| Cloudflare `$0` tier limits (`Pages` unlimited bandwidth; `Workers`/`DO` `100K` reqs/day, `20:1` WS ratio, `0` idle duration; `D1` `5M` reads/`100K` writes/day; `~2,900` 10-player rooms/day at `85%`) | `ART-012` §3, §11; `ART-013` §12, §14; `ART-014`; `ART-015` §8–9 | `SRC-030`, `FND-016`, `ART-009` §6 (`v1.1`), `REQ-010` | **Verified Fact + Engineering Calc** |
| Phase 2 WebGPU local AI (`Safari 26+`, `Android Chrome 121+`, `~1GB+` mobile VRAM limits, `100%` deterministic fallback) | `ART-012` §9; `ART-013` §13; `ART-014`; `ART-015` §5 | `SRC-022`, `FND-013`, `GOAL-005`, `REQ-011`, `ARC-006` | **Verified Fact** |
| MVP capabilities (2 tracks, Solo Daily + Live/24h Async `2–50` players, `<=2`-tap join, reconnect recovery, local `IndexedDB` + backup, `<250 KB`, WCAG 2.1 AA, `48h` room expiry, card flags) | `ART-012` §7–9, `ART-013` §11–13, `ART-014`, `ART-015` §6–7 | `ART-006`..`ART-009` (`REQ-001`..`REQ-010`, `REQ-NFR-001`..`007`, `UX-001`..`005`, `ARC-001`..`005`) | **Approved Spec** |
| Target user personas (`Maya`, `Devon`, `Sam`) | `ART-015` §3 | `ART-008` §1 (`provisional`) | **Provisional** (`needs VAL-02`) |
| Behavioral success targets (`>=65%` completion, `>=35%` Day-7 return, `<15s` join, `>=98%` recovery) | `ART-012` §10–11, `ART-013` §15, `ART-014`, `ART-015` §9–10 | `ART-006` §2 (`GOAL-001`, `GOAL-002`), `ART-004` (`VAL-02`) | **Target Hypothesis** (`unvalidated`) |

### 2. Items Flagged for Clarification / Future Decision
1. **Default Language Pair(s) for MVP Track 1 (`Phrases & Words in Context`):** Open minor question carried from `ART-007` and surfaced in `ART-015` §11.
2. **Pre-Build vs. Post-MVP User Validation (`VAL-02`):** Surfaced in `ART-012` §12 and `ART-015` §11 for human preference.

---

## Next Steps / Unresolved Issues

- **Stage 13 Gate Check:** All 6 required Package B deliverables (`ART-012`..`ART-017`) are complete, humanized under `SKL-004`/`SKL-006`, consistent with `Package A` (`ART-011`), and 100% traced.
- **Next Stage:** Execute **Stage 10F (Agent 10: Final Audit Checklist across Package A + Package B)** per `workflows/finalize.md`.
