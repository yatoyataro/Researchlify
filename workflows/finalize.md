# Workflow: `finalize`

Portable runbook to assemble, verify, and deliver **Package A (Technical Handoff)** and **Package B (Client Proposal)**.

## Preconditions
- Stages `01`–`09` are `approved` (or `APPROVED_WITH_LIMITATIONS` with explicit human-accepted caveats).
- Stage `10` cross-artifact audit passed (`APPROVED` or `APPROVED_WITH_LIMITATIONS`) with zero unresolved `critical` or blocking `high` issues in `ISSUES.md`.
- Do **not** finalize if critical blockers remain.

## Steps
1. **Gate Pre-Check (`Agent 00`)**
   - Verify `STATE.md`, `ARTIFACT_INDEX.md`, `ISSUES.md`, and `EVIDENCE_LEDGER.md`. Confirm all mandatory gates are satisfied or human-waived in `DECISIONS.md`.
2. **Assemble Package A (`Agent 11`)**
   - Follow `agents/11-documentation-handoff.md` to compile all 23 technical handoff sections from approved artifacts without inventing or altering requirements/architecture.
   - Register Package A in `ARTIFACT_INDEX.md`.
3. **Generate Package B (`Agent 13`)**
   - Check `SKILL_REGISTRY.md` for an approved/verified humanizer skill; otherwise use built-in synthesis (`agents/13-client-synthesizer.md` + `.agents/skills/client-humanizer-synthesis/SKILL.md`).
   - Produce all 6 client deliverables in `artifacts/client-package/` (Overview, Presentation Outline, Executive Summary, FAQ, Communication Quality Review, Traceability Report).
   - Register Package B deliverables in `ARTIFACT_INDEX.md`.
4. **Final QA Audit (`Agent 10`)**
   - Run `workflows/review.md` across both Package A and Package B against the **Final Audit Checklist** (`WORKFLOW.md` Section 9).
   - Route any findings back to Agent 11, Agent 13, or upstream owners as appropriate; re-verify until `APPROVED` (or `APPROVED_WITH_LIMITATIONS`).
5. **Finalize State & Knowledge Graph**
   - Update `STATE.md` (`Workflow Status: completed`), `ARTIFACT_INDEX.md`, `CHANGELOG.md`, and `DECISIONS.md`.
   - Run `graphify update .` and verify graph freshness.
   - Present both separated packages, residual limitations, and recommended next human decisions.
