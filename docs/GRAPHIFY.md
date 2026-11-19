# Graphify Integration Guide (`docs/GRAPHIFY.md`)

## 1. Purpose in This Project
[Graphify](https://github.com/Graphify-Labs/graphify) provides a persistent, queryable knowledge map (`graphify-out/`) over the repository's instructions, agent specs, workflows, registries, artifacts, and (when present) code. Agents query Graphify first to orient quickly, inspect cross-artifact dependencies, and reduce full-repo file reads.

---

## 2. Verified Installation & Version
- **Installed CLI:** `graphify 0.9.111` (via `uv tool install graphifyy`, executable at `graphify`).
- **Project-scoped IDE setup:**
  - Antigravity: `graphify install --project --platform antigravity` (writes `.agents/skills/graphify/SKILL.md`, `.agents/rules/graphify.md`, `.agents/workflows/graphify.md`).
  - Claude Code: `graphify install --project --platform claude` (writes `.claude/skills/graphify/`, `.claude/settings.json` hooks, `.claude/CLAUDE.md`, and `CLAUDE.md` section).
- **Primary access method:** **Graphify CLI** (`graphify query`, `graphify explain`, `graphify path`, `graphify section`, `graphify update`), ensuring identical behavior in Antigravity, Claude Code, and terminal sessions without requiring a separate MCP server process.

---

## 3. Graph Output Locations (Generated — Do Not Hand-Edit)
Inside `graphify-out/`:
- `graphify-out/graph.json` — persistent NetworkX node-link JSON database used by all query commands.
- `graphify-out/GRAPH_REPORT.md` — summary report (god nodes, community cohesion, surprising connections, suggested questions).
- `graphify-out/graph.html` — interactive visualization generated alongside `graph.json` and `GRAPH_REPORT.md` (not emitted when `--no-viz` is passed).

---

## 4. Exclusions (`.graphifyignore`)
`.graphifyignore` excludes `.git/`, `graphify-out/`, `.env*`, key/cert files, Python virtualenvs/caches, and `app/` build outputs (`node_modules/`, `.next/`, `dist/`, `build/`).

---

## 5. Verified Commands & Query Patterns

```powershell
# Rebuild / incrementally update structural graph (AST + Markdown links/headings, no LLM key needed)
graphify update .

# Force rebuild when files were deleted or graph shrunk
graphify update . --force

# Broad BFS orientation query (use --dfs for path tracing, --budget N to cap tokens)
graphify query "How do revision loops route issues?"

# Inspect a node and its neighbors
graphify explain "WORKFLOW.md — Execution Protocol, Gates & Standards"

# Trace shortest path between two concepts/files (use --undirected for bidirectional markdown links)
graphify path "WORKFLOW.md" "ISSUES.md" --undirected

# Extract a specific Markdown heading and its subsections without reading the whole file
graphify section "2. Stage Gates & Statuses"

# List highest-degree hub nodes
graphify god-nodes --top 10
```

> **Note on Markdown & Semantic Extraction (`v0.9.111`):**
> `graphify update .` runs offline deterministic extraction—including Graphify's Markdown extractor (`extract_markdown`, indexing document nodes, headings, and Markdown links/citations)—with zero API keys. Deeper LLM semantic extraction of prose concepts (`INFERRED` edges) requires either `GEMINI_API_KEY`/`GOOGLE_API_KEY` (`graphify extract .`) or running `/graphify` inside an assistant session using subagents.

---

## 6. Refresh & Session Startup Procedure

### Session Startup
1. Check that `graphify-out/graph.json` exists and is not stale relative to recent edits.
2. Run `graphify query` / `graphify explain` / `graphify path` / `graphify section` for your assigned stage before opening multiple raw files.
3. Verify critical facts directly in the target source/artifact file.

### Refresh Cadence
- Refresh after significant milestones (new stage artifacts, updated `ARTIFACT_INDEX.md` / `DECISIONS.md` / `TEAM.md`, or structural changes), not after every trivial edit.
- Run `graphify update .` (or `graphify update . --force` after deletions) and record freshness in `STATE.md`.

---

## 7. IDE Differences & Fallback

| Surface | Integration | Fallback |
|---|---|---|
| **Antigravity** | `.agents/rules/graphify.md` (always-on rule), `.agents/skills/graphify/`, `.agents/workflows/graphify.md`, plus CLI calls in `run_command`. | If `graphify` CLI is unavailable or graph is stale: use `rg` / targeted `read_file` on `STATE.md` and `ARTIFACT_INDEX.md`. |
| **Claude Code** | `CLAUDE.md` guidance, `.claude/skills/graphify/`, and `.claude/settings.json` `PreToolUse` / `SessionStart` advisory hooks (`graphify hook-guard`). | Same CLI queries via Bash, or `Grep` / `Read` targeted to `STATE.md` and `ARTIFACT_INDEX.md`. |

---

## 8. Provenance, Limitations & Verification
- Graphify tags edges with provenance (`EXTRACTED`, `INFERRED`, `AMBIGUOUS`). Treat graph edges—especially `INFERRED` or `AMBIGUOUS`—as navigation leads, never as unverified proof.
- Always open and read the canonical artifact/source file before citing claims in `EVIDENCE_LEDGER.md`, `ISSUES.md`, or Package A/B.
- Git hooks (`graphify hook install`) keep `graphify-out/` refreshed on commits/checkouts/merges; you can also run `graphify update .` manually after major milestones.
