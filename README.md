# Portable AI Web-App Discovery & Planning Team

A repository-canonical, cross-IDE (**Antigravity** and **Claude Code**) multi-agent system for researching, validating, planning, auditing, and packaging web application discoveries into:
- **Package A:** Developer-ready technical development handoff (`Agent 11`).
- **Package B:** Plain-language client research overview, presentation outline, executive summary, FAQ, quality review, and traceability report (`Agent 13`).

> **Current status:** System configured and idle (`STATE.md`). No project discovery has started; supply a project goal and invoke `start-discovery` to begin.

---

## Repository Structure

- **Root canonical state & governance:**
  `AGENTS.md`, `TEAM.md`, `WORKFLOW.md`, `STATE.md`, `DECISIONS.md`, `ARTIFACT_INDEX.md`, `SKILL_REGISTRY.md`, `EVIDENCE_LEDGER.md`, `ISSUES.md`, `CHANGELOG.md`
- **Role specifications:** `agents/orchestrator.md` and `agents/01-*.md` through `agents/13-*.md`
- **Portable workflows:** `workflows/` (`start-discovery.md`, `resume.md`, `review.md`, `finalize.md`)
- **Deliverable workspace:** `artifacts/` (`research`, `problem-analysis`, `product`, `requirements`, `ux`, `architecture`, `reviews`, `client-package`, plus `_TEMPLATE.md`)
- **IDE thin adapters:**
  - Antigravity: `.agents/skills/`, `.agents/workflows/`, `.agents/rules/`
  - Claude Code: `CLAUDE.md`, `.claude/commands/`, `.claude/skills/`, `.claude/settings.json`, `.claude/CLAUDE.md`
- **Knowledge graph:** `graphify-out/` (generated; do not hand-edit) & `docs/GRAPHIFY.md`
- **Validation:** `scripts/validate_system.py`

---

## How to Use

### In Antigravity
1. Open `E:\Codes\WebDevResearchTeam` as your workspace.
2. Antigravity automatically loads `AGENTS.md` and `.agents/rules/graphify.md`, and discovers `.agents/skills/` and `.agents/workflows/`.
3. Trigger workflows or ask the Orchestrator:
   - `/start-discovery` (or *"Start discovery for <your project goal>"*)
   - `/resume` (continue from `STATE.md` checkpoint)
   - `/review` (run Agent 10 QA audit and route `ISSUES.md` tickets)
   - `/finalize` (compile Package A & Package B and run Final Audit Checklist)

### In Claude Code
1. Open a session in `E:\Codes\WebDevResearchTeam`.
2. Claude Code reads `CLAUDE.md` (which points to `AGENTS.md`, `STATE.md`, `WORKFLOW.md`, and `TEAM.md`).
3. Use `/start-discovery`, `/resume`, `/review`, or `/finalize` (from `.claude/commands/`), or instruct Claude directly to follow the corresponding `workflows/*.md` runbook.

### Switching IDEs Mid-Project
No migration is needed:
1. Finish or checkpoint the current session (`STATE.md` and registries updated, `graphify update .` run).
2. Open the same repository in the other IDE and run `/resume`.
3. Do **not** run two sessions simultaneously against the same `STATE.md` / artifact files.

---

## Updating Graphify & Skills

- **Refresh knowledge graph** after milestone or file changes:
  ```powershell
  graphify update .
  ```
  See [docs/GRAPHIFY.md](docs/GRAPHIFY.md) for query commands, exclusions, provenance rules, and semantic extraction options.
- **Verify or add skills:** Installed local & pinned GitHub skills (`SKL-001`..`SKL-010b`) are tracked in [SKILL_REGISTRY.md](SKILL_REGISTRY.md) and mirrored in `.agents/skills/` and `.claude/skills/`. Adding new external skills requires Agent 12 evaluation and human approval.
- **Verify system integrity:**
  ```powershell
  python scripts/validate_system.py
  ```
