# DECISIONS.md — Decision Log

Record all architectural, prioritization, scope, capability, and governance decisions here.

---

## Decision Record Format

| ID | Date | Owner | Status | Decision | Rationale | Rejected Alternatives | Affected Artifacts |
|---|---|---|---|---|---|---|---|

---

## Recorded Decisions

| ID | Date | Owner | Status | Decision | Rationale | Rejected Alternatives | Affected Artifacts |
|---|---|---|---|---|---|---|---|
| `DEC-001` | 2026-11-19 | Orchestrator (System Setup) | `approved` | Keep canonical team definitions, registries, state, workflows, and artifacts in repository root; treat `.agents/` (Antigravity) and `CLAUDE.md` / `.claude/` (Claude Code) as thin adapters. | Guarantees cross-IDE portability and prevents state drift between Antigravity and Claude Code. | Storing team specs inside `.agents/` or `.claude/` only (breaks portability). | `AGENTS.md`, `TEAM.md`, `WORKFLOW.md`, `CLAUDE.md`, `.agents/` |
| `DEC-002` | 2026-11-19 | Orchestrator (System Setup) | `approved` | Standardize on Graphify CLI (`graphify query/explain/path/section/update`) as primary graph access method, with scoped search/read fallback. | `graphify 0.9.111` CLI works deterministically across both Antigravity and Claude Code without requiring external MCP daemon configuration. | Dual conflicting MCP + CLI instructions or mandatory MCP server setup. | `AGENTS.md`, `docs/GRAPHIFY.md`, `CLAUDE.md`, `.agents/rules/graphify.md` |
| `DEC-003` | 2026-11-19 | Agent 12 / Orchestrator | `approved` | Keep external GitHub skills (`SKL-006`..`SKL-010`) in `awaiting_approval` status until a human explicitly approves installation. | Enforces operating principle #10 and security policy against installing unreviewed external instructions/scripts. | Auto-cloning or installing third-party GitHub skills without approval. | `SKILL_REGISTRY.md`, `agents/12-skill-research.md`, `agents/13-client-synthesizer.md` |
| `DEC-004` | 2026-11-19 | User / Agent 12 | `approved` | Install user-approved external skills (`SKL-006`..`SKL-010b`) into `.agents/skills/` and `.claude/skills/` pinned to audited commit SHAs, copying only Markdown/template files. | Ensures cross-IDE native discovery on Windows without symlink issues and excludes unreviewed upstream scripts. | Installing whole repositories or enabling symlinks on Windows. | `SKILL_REGISTRY.md`, `.agents/skills/`, `.claude/skills/`, `STATE.md` |
| `DEC-005` | 2026-11-19 | User / Orchestrator | `approved` | Track `graphify-out/graph.json`, `GRAPH_REPORT.md`, and `graph.html` in Git (`https://github.com/yatoyataro/Researchlify.git`), while ignoring local machine cache/paths (`graphify-out/cache/`, `.graphify_python`, `.graphify_root`, etc.). | Preserves shared project knowledge graph across machines/IDEs without committing local filesystem paths or cache blobs. | Ignoring all of `graphify-out/` or committing machine-specific paths. | `.gitignore`, `docs/GRAPHIFY.md` |
