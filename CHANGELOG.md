# CHANGELOG.md — System & Project Changelog

Tracks major changes to the portable team architecture, skill registry, Graphify configuration, and project deliverables.

---

## [1.1.0] - 2026-11-19

### Added
- Installed, pinned, and verified user-approved GitHub skills (`SKL-006`..`SKL-010b`: `humanizer`, `discovery-process`, `user-research`, `research-synthesis`, `accessibility-review`, `web-design-guidelines`, `writing-plans`, `requesting-code-review`) across `.agents/skills/` and `.claude/skills/`.
- Mirrored local team skills (`SKL-001`..`SKL-004`) to `.claude/skills/` for full Antigravity/Claude Code parity.
- Initialized Git repository, `.gitignore`, Graphify Git hooks (`graphify hook install`), and configured remote `origin` (`https://github.com/yatoyataro/Researchlify.git`).

## [1.0.0] - 2026-11-19

### Added
- Canonical portable root files: `AGENTS.md`, `TEAM.md`, `WORKFLOW.md`, `STATE.md`, `DECISIONS.md`, `ARTIFACT_INDEX.md`, `SKILL_REGISTRY.md`, `EVIDENCE_LEDGER.md`, `ISSUES.md`, `CHANGELOG.md`, `README.md`.
- Complete agent specifications in `agents/` (`orchestrator.md` and `01` through `13`).
- Portable workflow runbooks in `workflows/` (`start-discovery.md`, `resume.md`, `review.md`, `finalize.md`).
- Artifact directory structure under `artifacts/` with standard header template `artifacts/_TEMPLATE.md`.
- Thin IDE adapters for Antigravity (`.agents/skills/`, `.agents/workflows/`, `.agents/rules/`) and Claude Code (`CLAUDE.md`, `.claude/commands/`, `.claude/skills/`, `.claude/settings.json`).
- Graphify integration (`docs/GRAPHIFY.md`, `.graphifyignore`) and project-scoped Graphify indexing.
- Validation script `scripts/validate_system.py` verifying file references, adapters, and system integrity.
