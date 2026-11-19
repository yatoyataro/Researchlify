---
name: stage-qa-audit
description: >-
  Run Agent 10 QA and cross-artifact consistency audits, log tickets in
  ISSUES.md, and route revisions back to owning agents. Use during stage
  reviews, post-architecture audits, or final Package A/B verification.
---

# Stage QA Audit Adapter

Follow the canonical auditor spec and review workflow:
1. Read `agents/10-qa-auditor.md` and `workflows/review.md`.
2. Verify target deliverables against `artifacts/_TEMPLATE.md`, `EVIDENCE_LEDGER.md`, `DECISIONS.md`, and `WORKFLOW.md` traceability rules.
3. Log every finding as `ISS-NNN` in `ISSUES.md` and assign the responsible owner per `TEAM.md`. Never silently rewrite another agent's artifact.
4. Enforce the 3-revision escalation cap on `critical` issues.
