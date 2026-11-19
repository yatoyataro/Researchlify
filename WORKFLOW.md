# WORKFLOW.md — Execution Protocol, Gates & Standards

Canonical lifecycle, quality gates, revision loop, evidence, prioritization, traceability, and deliverable standards.

---

## 1. Workflow Commands

Portable runbooks live in `workflows/`:
- [workflows/start-discovery.md](workflows/start-discovery.md) — Intake project goal, verify Graphify & skills, initialize project state, run sequential stages with gates.
- [workflows/resume.md](workflows/resume.md) — Orient via `STATE.md` and Graphify, resume from the active checkpoint without repeating approved stages.
- [workflows/review.md](workflows/review.md) — Run Agent 10 scoped or holistic QA audit, log tickets in `ISSUES.md`, route revisions, verify fixes.
- [workflows/finalize.md](workflows/finalize.md) — Verify all gates & Final Audit Checklist, assemble Package A (Agent 11) and Package B (Agent 13), run final QA, mark complete.

---

## 2. Stage Gates & Statuses

Every stage artifact and review uses these canonical statuses:
- Lifecycle statuses: `proposed`, `in_progress`, `blocked`, `under_review`, `approved`, `completed`.
- QA audit decisions (Agent 10):
  - `APPROVED` — Meets all stage and traceability criteria; proceed.
  - `APPROVED_WITH_LIMITATIONS` — Explicit limitations recorded; does not invalidate downstream stage; proceed with documented caveats.
  - `REVISION_REQUIRED` — One or more `ISSUES.md` tickets opened; return to owning agent before proceeding.
  - `BLOCKED` — Missing permissions, missing evidence, external dependency, or unresolved human decision; halt dependent work.
  - `NEEDS_HUMAN_REVIEW` — Tradeoff, policy, risk, or scope conflict requires human decision.

**Gate enforcement rules:**
1. Orchestrator verifies every stage deliverable against `artifacts/_TEMPLATE.md` and the stage's gate criteria before advancing.
2. Agent 10 performs a mandatory cross-artifact audit after Stage 09 (before Package A/B) and a separate final audit after Stage 13.
3. No agent may substitute a missing human decision or missing access permission.
4. Changes to an approved upstream artifact trigger impact analysis via `ARTIFACT_INDEX.md` / Graphify and targeted re-review of affected downstream artifacts only, followed by a final holistic consistency check.

---

## 3. Revision Loop & Escalation Protocol

1. **Log ticket:** Reviewer (Agent 10 or Orchestrator) adds `ISS-NNN` to `ISSUES.md` with all 12 required fields (ID, description, severity, evidence/example, artifact & section, responsible agent, required action, dependencies/affected artifacts, status, reviewer, revision number, resolution & verification).
2. **Assign owner:** Orchestrator routes the ticket to the responsible agent (`TEAM.md` Section 4) with the target artifact and context.
3. **Revise:** Owner updates the artifact, increments its revision number, records changes, and updates the ticket response.
4. **Verify:** Reviewer inspects the updated artifact and marks the ticket `verified`/`closed` or re-opens with incremented revision number.
5. **Cascade check:** Orchestrator updates `STATE.md`, `ARTIFACT_INDEX.md`, and checks downstream artifacts for impact.

**Escalation limit (anti-infinite-loop):**
- Maximum **3 revision attempts** for the same `critical` (or blocking `high`) issue.
- If unresolved after 3 revisions—or sooner if root cause is ambiguous or requires human policy/access—stop and escalate to the **Human** with options.
- Never lower QA standards just to close a ticket.

---

## 4. Traceability Chain & ID Conventions

Maintain end-to-end traceability:

```text
Evidence (SRC/FND) -> Problem (PRB) -> Root Cause (RCA) -> Prioritization -> Product Goal (GOAL)
-> Requirement (REQ) -> User Flow / UX (UX) -> Architecture (ARC) -> Test / Acceptance (TEST) -> Client Claim
```

| Prefix | Entity | Registry / Location |
|---|---|---|
| `SRC-NNN` | Source consulted | `EVIDENCE_LEDGER.md` |
| `FND-NNN` | Research finding / observation | `EVIDENCE_LEDGER.md` |
| `PRB-NNN` | Validated problem candidate | `artifacts/problem-analysis/` |
| `RCA-NNN` | Root cause / contributing factor | `artifacts/problem-analysis/` |
| `DEC-NNN` | Key project or architecture decision | `DECISIONS.md` |
| `GOAL-NNN` | Product goal / success indicator | `artifacts/product/` |
| `REQ-NNN` | Functional / non-functional / rule requirement | `artifacts/requirements/` |
| `UX-NNN` | User journey, flow, or screen spec | `artifacts/ux/` |
| `ARC-NNN` | Technical architecture decision / component | `artifacts/architecture/` |
| `TEST-NNN` | Acceptance / QA verification criterion | `artifacts/requirements/` & `artifacts/reviews/` |
| `ISS-NNN` | Review issue / rework ticket | `ISSUES.md` |
| `SKL-NNN` | Evaluated or assigned skill | `SKILL_REGISTRY.md` |

---

## 5. Research & Evidence Standards

- Every factual claim in `EVIDENCE_LEDGER.md` records: Finding ID, claim/observation, Source ID & link, source type (`primary`, `secondary`, `official`, `academic`, `user-provided`, `interview`, `survey`, `observation`, `other`), date accessed/collected, publication date (if known), concise excerpt (only when needed/permitted), interpretation/context, evidence strength & rationale, confidence/uncertainty, limitations/bias/alternatives, and linked IDs.
- Prefer primary/official/peer-reviewed sources; verify claims beyond search snippets; corroborate critical claims.
- Never cite unconsulted sources, fabricate URLs, or imply user interviews/surveys occurred unless actually executed with consent.

---

## 6. Problem Prioritization Framework

Starting configurable rubric (adjust and justify in `DECISIONS.md` per project):

| Criterion | Default Weight | Scale Guidance (1–5) |
|---|---:|---|
| User impact / severity | 25% | 1 = minor annoyance; 5 = severe blocker / safety / compliance loss |
| Frequency / reach | 20% | 1 = rare edge case; 5 = daily across majority of target users |
| Evidence strength | 20% | 1 = unverified assumption; 5 = multiple corroborated primary sources |
| Feasibility | 15% | 1 = prohibitive cost/tech/policy risk; 5 = straightforward within constraints |
| Strategic alignment / value | 10% | 1 = tangential; 5 = directly unlocks core user/org goal |
| Risk & constraints | 10% | 1 = high unresolved legal/privacy/adoption risk; 5 = low manageable risk |

Distinguish measured data from judgment, avoid false precision, and run sensitivity checks where small weight shifts change rank order.

---

## 7. Artifact Standards

All deliverables in `artifacts/` must follow [artifacts/_TEMPLATE.md](artifacts/_TEMPLATE.md) containing: Title & ID, Purpose, Status, Owner, Revision/Version, Date Created/Updated, Sources / Input Artifacts, Assumptions & Limitations, Content, and Next Steps / Unresolved Issues.

---

## 8. Concurrent Session Safety

- Avoid running two active sessions writing to `STATE.md`, registries, or the same artifact simultaneously.
- Serialize writes to canonical root files through the Orchestrator.
- Neither Antigravity nor Claude Code natively locks shared markdown files across independent sessions; **if a conflict or unexpected timestamp/revision change in `STATE.md` is detected at startup, pause and reconcile explicitly with the user before overwriting.**

---

## 9. Final Deliverables & Audit Checklist

### Package A — Technical Development Handoff (Agent 11)
Must cover all 23 sections defined in [agents/11-documentation-handoff.md](agents/11-documentation-handoff.md) (project overview, research/evidence, root causes, prioritization, vision/goals, users/personas with evidence status, MVP scope/roadmap, requirements, use cases/stories/rules/acceptance, NFRs, journeys/flows, IA/page inventory, UX/a11y/wireframes, system architecture, components, DB/ERD, API/integrations, security/privacy/ops/deployment, implementation sequence/milestones, QA/test plan, requirement-to-test traceability, risks/assumptions/open decisions, artifact index/citations).

### Package B — Client-Facing Research & Project Proposal (Agent 13)
Must cover all 6 deliverables defined in [agents/13-client-synthesizer.md](agents/13-client-synthesizer.md): Client Research Overview (13 sections), Client Presentation Outline (17 sections), Executive Summary (2–5 min read), Client FAQ, Communication Quality Review, and Traceability Report. Both packages derive from the same approved artifacts.

### Final Audit Checklist (Gate to `completed`)
- [ ] All mandatory stages completed or explicitly waived by human decision.
- [ ] All `critical` and `high` `ISSUES.md` tickets resolved or transparently accepted by authorized human.
- [ ] Evidence is traceable (`EVIDENCE_LEDGER.md`) and not fabricated.
- [ ] Sources were consulted, appropriate, and cited.
- [ ] Problem statements and root causes are evidence-supported.
- [ ] Prioritization criteria, weights, rationale, and sensitivity check are documented.
- [ ] Product goals, MVP scope, and non-goals are clear.
- [ ] Requirements are testable, prioritized, and traceable.
- [ ] UX flows and accessibility considerations align with requirements.
- [ ] Technical architecture supports requirements and constraints and is justified.
- [ ] Risks, privacy, security, constraints, and limitations are documented.
- [ ] Technical package (Package A) is coherent and developer-ready.
- [ ] Client package (Package B) is accurate, plain-language, and appropriately humanized.
- [ ] Client-facing claims trace to approved artifacts (`Traceability Report`).
- [ ] Expected benefits are explicitly distinguished from proven outcomes.
- [ ] `ARTIFACT_INDEX.md`, `STATE.md`, `DECISIONS.md`, `ISSUES.md`, `SKILL_REGISTRY.md`, and `EVIDENCE_LEDGER.md` are current.
- [ ] Graphify is current (`graphify-out/graph.json`) or its status/limitations are disclosed.
- [ ] Next step and any required human decisions are explicitly listed.
