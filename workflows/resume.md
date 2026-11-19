# Workflow: `resume`

Portable runbook to resume an interrupted or cross-IDE discovery session without repeating approved work.

## Steps
1. **Startup & Conflict Check**
   - Read `AGENTS.md` and active IDE entrypoint (`CLAUDE.md` if Claude Code, `.agents/` if Antigravity).
   - Read `STATE.md` to identify current stage, last completed gate, active/next agent, last writer IDE, and open blockers.
   - If `STATE.md` shows an unexpected change or concurrent session conflict, pause and reconcile with the user before editing.
2. **Graph-First Orientation**
   - Check `graphify-out/graph.json`. If present and fresh, run `graphify query "<current stage or task>"` and `graphify explain` on relevant concepts/artifacts.
   - If missing or stale, use scoped search (`rg`) on `ARTIFACT_INDEX.md`, `ISSUES.md`, and `DECISIONS.md`, and run `graphify update .` when appropriate.
3. **Inspect Open Tickets & Registries**
   - Read `ISSUES.md` for any `open`, `in_progress`, or `fixed_pending_verify` tickets.
   - Read `DECISIONS.md` and `ARTIFACT_INDEX.md` for approved upstream dependencies.
4. **Resume at Checkpoint**
   - Do **not** rerun stages marked `approved` or `completed` unless an open `ISS-NNN` ticket routes rework there.
   - Issue a fresh Task Brief (`TEAM.md` Section 3) to the active/next agent (or resolve open revision loop first).
5. **Session End**
   - Update `STATE.md` (`Active IDE / Last Writer`, `Last Updated`, progress table, next action), registries, and Graphify (`graphify update .`).
   - Output concise handoff: accomplished, pending, blockers, next step, files changed, approvals needed.
