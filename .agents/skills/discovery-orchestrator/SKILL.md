---
name: discovery-orchestrator
description: >-
  Coordinate the sequential AI web-app discovery and planning pipeline
  (start-discovery, resume, review, finalize) using canonical repo state.
  Use when starting, resuming, routing, or finalizing a discovery project.
---

# Discovery Orchestrator Adapter

This skill delegates directly to the canonical repository specifications (do not duplicate rules here).

## Steps
1. Read `AGENTS.md`, `STATE.md`, `TEAM.md`, and `WORKFLOW.md`.
2. Orient with Graphify if `graphify-out/graph.json` is present (`graphify query "<topic>"`).
3. Execute the requested portable runbook:
   - `workflows/start-discovery.md` (only when the user provides a project goal)
   - `workflows/resume.md`
   - `workflows/review.md`
   - `workflows/finalize.md`
4. Follow `agents/orchestrator.md` for task briefs, stage gates, `ARTIFACT_INDEX.md`, and `STATE.md` updates.
