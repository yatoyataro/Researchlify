# CHANGELOG.md — System & Project Changelog

Tracks major changes to the portable team architecture, skill registry, Graphify configuration, and project deliverables.

---

## [1.6.0] - 2026-11-20

### Added / Changed
- Recorded `PRB-005` live deployment (`https://prb005-brainplay.pages.dev`, `https://github.com/yatoyataro/brainplay`) in `handoff/HANDOFF_REGISTRY.md` (`DEC-011`).
- Moved `PRB-005` deliverables (`ART-001`..`ART-018`) cleanly into `artifacts/archive/PRB-005/` with zero history deleted, updated `ARTIFACT_INDEX.md` links, reset `STATE.md` to `IDLE` (`READY_FOR_INTAKE`), and refreshed Graphify.

## [1.5.0] - 2026-11-19

### Added
- Established cross-team integration with `E:\Codes\WebDeveloperTeam` (`DEC-010`): `handoff/` package & request/response directory structure, `handoff/README.md`, `handoff/HANDOFF_REGISTRY.md`, `REQUEST_TEMPLATE.md`, `RESPONSE_TEMPLATE.md`, `workflows/developer-requests.md`, and cross-links in `AGENTS.md`, `TEAM.md`, `ARTIFACT_INDEX.md`, `README.md`, and `STATE.md`.
- Built, SHA-256 verified, archived, and delivered `PRB-005_Zero-Cost-Social-Casual-Learning_Developer-Handoff_v1.0.zip` (`PKG-PRB-005-v1.0`, `33` entries, `135,746` bytes) into `E:\Codes\WebDeveloperTeam\ResearchTeamFinalResults\incoming\` while keeping `Implementation Authorization: PENDING USER APPROVAL`.

## [1.4.0] - 2026-11-19

### Added
- Completed Stage 07 (`ART-007` Requirements & `TEST-001`..`010`), Stage 08 (`ART-008` UX/IA & WCAG 2.1 AA), and Stage 09 (`ART-009` `v1.1` `$0` Cloudflare + local-first architecture).
- Executed Stage 10 Cross-Artifact QA Audit (`ART-010`) and closed `ISS-001` (medium) & `ISS-002` (low) in `ISSUES.md` via owning-agent revision loop (`APPROVED_WITH_LIMITATIONS`).
- Assembled **Package A** (`ART-011`, 23-section developer handoff), **Package B** (`ART-012`..`ART-017`, 6 plain-language humanized client deliverables), and passed Stage 10F Final Package Audit (`ART-018`, `workflow: completed`).

## [1.3.0] - 2026-11-19

### Added
- Recorded Stage 05 human selection of `PRB-005` (`DEC-008`) and mandatory zero-money-cost constraint across development, production, and deployment (`DEC-009`).
- Added open-dataset licensing (`SRC-029`, `FND-015`), Cloudflare free-tier limit (`SRC-030`, `FND-016`), and Duolingo Energy detail (`FND-014`) to `EVIDENCE_LEDGER.md`.
- Completed Stage 06 Product Definition (`ART-006`) with `GOAL-001`..`GOAL-005`, build-vs-adopt rationale, MVP scope, explicit non-goals, phased roadmap, and risks.

## [1.2.0] - 2026-11-19

### Added
- Started discovery project (`DEC-006`, `DEC-007`): mainstream fun & delight web app problems matched to a solo backend/real-time/data-reliability/optional-local-AI developer, executed via desk research only and paused after Stage 05.
- Completed Stages 01–05 deliverables: `ART-001` (Discovery & Context), `ART-002` + `EVIDENCE_LEDGER.md` (`SRC-001`..`SRC-028`, `FND-001`..`FND-013`), `ART-003` (Existing Solutions & Gaps), `ART-004` (`RCA-001`..`RCA-009`, `PRB-001`..`PRB-006`), and `ART-005` (Stage 05 Prioritization & Top-3 Ranking).

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
