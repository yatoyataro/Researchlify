# CLAUDE.md — Claude Code Entrypoint

This file is the **thin Claude Code adapter** for the canonical team system defined in the repository root.
It does **not** replace or fork the canonical instructions.

## Canonical Sources (Read First)
1. [AGENTS.md](AGENTS.md) — Core operating principles, graph-first orientation, approval/security rules, and session protocol.
2. [STATE.md](STATE.md) — Current project stage, blockers, last writer IDE, and next action.
3. [TEAM.md](TEAM.md) & [WORKFLOW.md](WORKFLOW.md) — Roster (Orchestrator + Agents `01`–`13`), pipeline gates, revision loop, and traceability standards.
4. `agents/*.md` & `workflows/*.md` — Role specs and runbooks (`start-discovery`, `resume`, `review`, `finalize`).

## Claude Code Commands & Skills
- Slash commands in `.claude/commands/` (`start-discovery`, `resume`, `review`, `finalize`) invoke the canonical `workflows/*.md` runbooks.
- Both `.claude/skills/` and `.agents/skills/` contain the verified local and commit-pinned skills (`SKL-001`..`SKL-010b` in `SKILL_REGISTRY.md`).
- **Portability notes:**
  - *Portable across both IDEs:* All markdown state/registries, `agents/*.md`, `workflows/*.md`, `artifacts/`, and `graphify` CLI queries (`graphify query/explain/path/section/update`).
  - *Claude-native only:* `.claude/settings.json` `PreToolUse` / `SessionStart` advisory hooks (`graphify hook-guard`) and `.claude/commands/*.md` slash triggers. Antigravity uses `.agents/rules/` and `.agents/workflows/` for the equivalent triggers.
  - *Sub-agents:* If Claude Code spawns subagents (e.g., via Agent tool), pass the specialist's `agents/XX-*.md` spec and Task Brief (`TEAM.md` Section 3), and keep canonical state writes (`STATE.md`, `ARTIFACT_INDEX.md`, `ISSUES.md`) serialized through the Orchestrator.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. When the answer is under a Markdown heading, `graphify section "<heading>"` prints that section's text, so the .md need not be opened. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
