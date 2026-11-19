# Workflow: `review`

Portable runbook for scoped or holistic QA audits (`Agent 10`) and revision routing (`ISSUES.md`).

## Steps
1. **Determine Audit Scope**
   - Identify target artifacts (single stage, impacted downstream set after an upstream edit, or full Stage 01–09 / Final Package audit).
   - Query Graphify (`graphify path`, `graphify query`) and `ARTIFACT_INDEX.md` to map upstream/downstream dependencies.
2. **Execute Audit (`Agent 10`)**
   - Follow `agents/10-qa-auditor.md`: check template compliance, `EVIDENCE_LEDGER.md` citations, non-fabrication, causal/prioritization rigor, `GOAL -> REQ -> UX -> ARC -> TEST` traceability, and Package B fidelity to Package A.
   - Never silently rewrite the audited artifact.
3. **Log Tickets (`ISSUES.md`)**
   - Record every finding as `ISS-NNN` with all 12 required fields (`WORKFLOW.md` Section 3).
   - Assign responsible owner per `TEAM.md` Section 4.
4. **Write Review Report & Gate Decision**
   - Save review report in `artifacts/reviews/` using `artifacts/_TEMPLATE.md`.
   - Record decision: `APPROVED`, `APPROVED_WITH_LIMITATIONS`, `REVISION_REQUIRED`, `BLOCKED`, or `NEEDS_HUMAN_REVIEW`.
5. **Revision Loop (If `REVISION_REQUIRED`)**
   - Orchestrator routes each ticket to its owner.
   - Owner revises artifact, bumps revision, and responds on `ISS-NNN`.
   - Agent 10 re-audits fixed artifact (and Orchestrator checks downstream impact).
   - **Escalation:** If the same `critical` issue fails **3** revision attempts (or root cause requires human authority), mark `escalated_human` and stop for user input.
6. **Update State**
   - Sync `ARTIFACT_INDEX.md`, `ISSUES.md`, `STATE.md`, and refresh Graphify if artifacts changed.
