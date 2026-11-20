# ISSUES.md — QA Findings, Rework Tickets & Blockers

Maintained by **Agent 10** and **Orchestrator**.
Every review finding must become a structured ticket below. After **3 unsuccessful revisions** of the same `critical` issue (or sooner if unclear), escalate to **Human**.

---

## 1. Required Ticket Fields

`Issue ID` (`ISS-NNN`) | `Description` | `Severity` (`critical`, `high`, `medium`, `low`) | `Finding Evidence / Example` | `Artifact & Section` | `Responsible Agent` | `Required Action` | `Dependencies / Affected Artifacts` | `Status` (`open`, `in_progress`, `fixed_pending_verify`, `verified_closed`, `escalated_human`, `waived_human`) | `Reviewer` | `Revision Number` | `Resolution & Verification`

---

## 2. Active & Historical Tickets

| Issue ID | Description | Severity | Finding Evidence / Example | Artifact & Section | Responsible Agent | Required Action | Dependencies / Affected | Status | Reviewer | Rev # | Resolution & Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ISS-001` | `ART-009` references an unspecified `POST /api/daily/check` endpoint in the `GET /api/daily` row and omits the `D1` `DAILY_QUOTA_COUNTER` entity from the ERD despite storing daily quota counters in `D1` (`Section 6`). | `medium` | `ART-009` Section 4 footnote (`or server POST /api/daily/check`) vs. Endpoints table; Section 3 ERD vs. Section 6 D1 description (`daily quota counter rollup`). | `ART-009` Sections 3, 4, 6 | `Agent 09` | Clarify Solo Daily offline verification vs. Room server-side `correctIndex` withholding (`TEST-005`), remove undefined `POST /api/daily/check` mention, and add `DAILY_QUOTA_COUNTER` to the ERD. | `ART-007` (`TEST-005`), `ART-009` | `verified_closed` | `Agent 10` | `1` | Verified in `ART-009` `v1.1`: `DAILY_QUOTA_COUNTER` added to ERD and Solo vs. Room anti-spoiler contract clarified cleanly. |
| `ISS-002` | `ART-004` `RCA-006` cites non-existent `FND-020` alongside `FND-011`. | `low` | `ART-004` Section 1 (`RCA-006`: `Evidenced (FND-020 / FND-011, SRC-020)`), whereas `EVIDENCE_LEDGER.md` ends at `FND-016`. | `ART-004` Section 1 (`RCA-006`) | `Agent 04` | Remove erroneous `FND-020` reference and retain `FND-011, SRC-020`. | `ART-004` (non-blocking; `PRB-004` deferred) | `verified_closed` | `Agent 10` | `1` | Verified in `ART-004` `v1.1`: erroneous `FND-020` removed; `FND-011, SRC-020` intact. |
