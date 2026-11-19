# Workflow: `start-discovery`

Portable runbook to initialize and execute a new web-app discovery & planning project.

## Preconditions
- User has supplied (or is ready to supply) a real project goal/domain.
- Do **not** auto-run this workflow during system setup.

## Steps
1. **Orient & Check State**
   - Read `AGENTS.md`, `STATE.md`, `WORKFLOW.md`, and `SKILL_REGISTRY.md`.
   - Confirm `STATE.md` is `IDLE` (or confirm with the user before resetting/starting a new project if an active project exists).
   - Check Graphify status (`graphify-out/graph.json`); run `graphify update .` if stale or missing.
2. **Project Intake (`Agent 00`)**
   - Capture available context from the user per `agents/orchestrator.md` (industry, stakeholders, current tools/pain points, goal, constraints, known evidence, assumptions, research permissions, desired deliverables).
   - Ask only the highest-value missing clarifications; otherwise log transparent assumptions in `DECISIONS.md` / `STATE.md`.
   - Record the project brief and update `STATE.md` (`Workflow Status: in_progress`, `Current Stage: 12`).
3. **Capability & Skill Setup (`Agent 12`)**
   - Review `SKILL_REGISTRY.md` (especially `SKL-006`..`SKL-010` or domain-specific skills).
   - If external skills are recommended, present risks and wait for explicit human approval before installing.
4. **Sequential Pipeline (`Stages 01 -> 09`)**
   - Execute `Agent 01` through `Agent 09` strictly in order using the Task Brief Contract (`TEAM.md` Section 3).
   - After each stage: verify deliverable against `artifacts/_TEMPLATE.md` and stage gate criteria, update `ARTIFACT_INDEX.md`, `EVIDENCE_LEDGER.md`, `DECISIONS.md`, and `STATE.md`.
   - Stop immediately at any human approval gate (external user research, paid tools, scope/tradeoff decisions, or `BLOCKED` status).
5. **Cross-Artifact QA Audit (`Agent 10`)**
   - Run `workflows/review.md` on the full Stage 01–09 artifact set before proceeding to handoff/client packaging.
6. **Handoff & Finalization**
   - Run `workflows/finalize.md` once Stage 10 approves.
   - Refresh Graphify (`graphify update .`) and deliver final summary.
