# ARTIFACT_INDEX.md — Artifact Registry

Central registry of all project deliverables and system artifacts.
Allowed statuses: `proposed`, `in_progress`, `blocked`, `under_review`, `approved`, `completed`, `archived`.

---

## 1. Active Project Deliverables (Current Run)

| Artifact ID | Title | Path | Stage | Owner | Status | Revision | Dependencies | Last Updated |
|---|---|---|---|---|---|---|---|---|
| *(None yet — ready for next discovery project intake)* | — | — | — | — | — | — | — | — |

---

## 2. Archived Project Deliverables — `PRB-005` (Zero-Cost Social Casual Learning)

> **Status:** Completed (`APPROVED_WITH_LIMITATIONS`), delivered (`PKG-PRB-005-v1.0`), deployed (`https://prb005-brainplay.pages.dev` / `https://github.com/yatoyataro/brainplay`), and archived on `2026-11-20` (`DEC-011`). All IDs, versions, and history preserved intact.

| Artifact ID | Title | Archived Path | Stage | Owner | Final Status | Revision | Dependencies | Last Updated |
|---|---|---|---|---|---|---|---|---|
| `ART-001` | Stage 01 Discovery & Context Package | [artifacts/archive/PRB-005/research/ART-001-stage01-discovery-context.md](artifacts/archive/PRB-005/research/ART-001-stage01-discovery-context.md) | Stage 01 | Agent 01 | `approved` | `v1.0` | `DEC-006`, `DEC-007` | 2026-11-19 |
| `ART-002` | Stage 02 Evidence & User Research Synthesis | [artifacts/archive/PRB-005/research/ART-002-stage02-evidence-synthesis.md](artifacts/archive/PRB-005/research/ART-002-stage02-evidence-synthesis.md) | Stage 02 | Agent 02 | `approved` | `v1.0` | `ART-001`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-003` | Stage 03 Existing Solutions & Gap Analysis | [artifacts/archive/PRB-005/research/ART-003-stage03-existing-solutions.md](artifacts/archive/PRB-005/research/ART-003-stage03-existing-solutions.md) | Stage 03 | Agent 03 | `approved` | `v1.0` | `ART-001`, `ART-002`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-004` | Stage 04 Root Cause & Problem Analysis | [artifacts/archive/PRB-005/problem-analysis/ART-004-stage04-root-cause-problems.md](artifacts/archive/PRB-005/problem-analysis/ART-004-stage04-root-cause-problems.md) | Stage 04 | Agent 04 | `approved` | `v1.1` | `ART-001`..`ART-003`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-005` | Stage 05 Problem Prioritization & Top-3 Recommendation | [artifacts/archive/PRB-005/problem-analysis/ART-005-stage05-prioritization.md](artifacts/archive/PRB-005/problem-analysis/ART-005-stage05-prioritization.md) | Stage 05 | Agent 05 | `approved` | `v1.0` | `ART-003`, `ART-004`, `DEC-006`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-006` | Stage 06 Product Definition (`PRB-005` Zero-Cost Social Casual Learning) | [artifacts/archive/PRB-005/product/ART-006-stage06-product-definition.md](artifacts/archive/PRB-005/product/ART-006-stage06-product-definition.md) | Stage 06 | Agent 06 | `approved` | `v1.0` | `ART-002`..`ART-005`, `DEC-008`, `DEC-009`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-007` | Stage 07 Business Analysis & Requirements Specification | [artifacts/archive/PRB-005/requirements/ART-007-stage07-requirements.md](artifacts/archive/PRB-005/requirements/ART-007-stage07-requirements.md) | Stage 07 | Agent 07 | `approved` | `v1.0` | `ART-004`, `ART-006`, `DEC-007`..`DEC-009`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-008` | Stage 08 UX & Information Architecture Specification | [artifacts/archive/PRB-005/ux/ART-008-stage08-ux-ia.md](artifacts/archive/PRB-005/ux/ART-008-stage08-ux-ia.md) | Stage 08 | Agent 08 | `approved` | `v1.0` | `ART-002`, `ART-006`, `ART-007` | 2026-11-19 |
| `ART-009` | Stage 09 Technical Architecture Specification | [artifacts/archive/PRB-005/architecture/ART-009-stage09-technical-architecture.md](artifacts/archive/PRB-005/architecture/ART-009-stage09-technical-architecture.md) | Stage 09 | Agent 09 | `approved` | `v1.1` | `ART-006`..`ART-008`, `DEC-008`, `DEC-009`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-010` | Stage 10 Cross-Artifact QA Audit Report | [artifacts/archive/PRB-005/reviews/ART-010-stage10-qa-audit.md](artifacts/archive/PRB-005/reviews/ART-010-stage10-qa-audit.md) | Stage 10 | Agent 10 | `approved` | `v1.0` | `ART-001`..`ART-009`, `ISSUES.md` | 2026-11-19 |
| `ART-011` | Package A: Developer-Ready Technical Handoff (23 Sections) | [artifacts/archive/PRB-005/product/ART-011-package-a-technical-handoff.md](artifacts/archive/PRB-005/product/ART-011-package-a-technical-handoff.md) | Stage 11 | Agent 11 | `completed` | `v1.0` | `ART-001`..`ART-010`, `DECISIONS.md`, `EVIDENCE_LEDGER.md` | 2026-11-19 |
| `ART-012` | Package B: Client Research Overview (13 Sections) | [artifacts/archive/PRB-005/client-package/ART-012-client-research-overview.md](artifacts/archive/PRB-005/client-package/ART-012-client-research-overview.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-001`..`ART-011`, `SKL-004`, `SKL-006` | 2026-11-19 |
| `ART-013` | Package B: Client Presentation Outline (17 Sections) | [artifacts/archive/PRB-005/client-package/ART-013-client-presentation-outline.md](artifacts/archive/PRB-005/client-package/ART-013-client-presentation-outline.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-001`..`ART-011`, `SKL-004`, `SKL-006` | 2026-11-19 |
| `ART-014` | Package B: Executive Summary | [artifacts/archive/PRB-005/client-package/ART-014-client-executive-summary.md](artifacts/archive/PRB-005/client-package/ART-014-client-executive-summary.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-001`..`ART-011`, `SKL-004`, `SKL-006` | 2026-11-19 |
| `ART-015` | Package B: Client FAQ | [artifacts/archive/PRB-005/client-package/ART-015-client-faq.md](artifacts/archive/PRB-005/client-package/ART-015-client-faq.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-001`..`ART-011`, `SKL-004`, `SKL-006` | 2026-11-19 |
| `ART-016` | Package B: Communication Quality Review | [artifacts/archive/PRB-005/client-package/ART-016-communication-quality-review.md](artifacts/archive/PRB-005/client-package/ART-016-communication-quality-review.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-012`..`ART-015`, `SKL-004`, `SKL-006` | 2026-11-19 |
| `ART-017` | Package B: Client Claim Traceability Report | [artifacts/archive/PRB-005/client-package/ART-017-client-traceability-report.md](artifacts/archive/PRB-005/client-package/ART-017-client-traceability-report.md) | Stage 13 | Agent 13 | `completed` | `v1.0` | `ART-012`..`ART-015`, `ART-001`..`ART-011` | 2026-11-19 |
| `ART-018` | Stage 10F Final Package Audit Report | [artifacts/archive/PRB-005/reviews/ART-018-final-package-audit.md](artifacts/archive/PRB-005/reviews/ART-018-final-package-audit.md) | Stage 10F | Agent 10 | `completed` | `v1.0` | `ART-001`..`ART-017`, `ISSUES.md` | 2026-11-19 |

---

## 3. Canonical System & Reference Files

| Path | Role | Owner | Status | Revision |
|---|---|---|---|---|
| [AGENTS.md](AGENTS.md) | Cross-IDE root instructions | Orchestrator | `approved` | `v1.0` |
| [TEAM.md](TEAM.md) | Roster, pipeline & routing | Orchestrator | `approved` | `v1.0` |
| [WORKFLOW.md](WORKFLOW.md) | Lifecycle, gates & standards | Orchestrator | `approved` | `v1.0` |
| [STATE.md](STATE.md) | Live session & stage state | Orchestrator | `approved` | `v1.0` |
| [DECISIONS.md](DECISIONS.md) | Decision log | Orchestrator | `approved` | `v1.0` |
| [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) | Sources & findings ledger | Agent 02 | `approved` | `v1.0` |
| [ISSUES.md](ISSUES.md) | QA findings & rework tickets | Agent 10 | `approved` | `v1.0` |
| [SKILL_REGISTRY.md](SKILL_REGISTRY.md) | Local & evaluated skills | Agent 12 | `approved` | `v1.0` |
| [artifacts/_TEMPLATE.md](artifacts/_TEMPLATE.md) | Standard artifact header template | Orchestrator | `approved` | `v1.0` |
| [handoff/README.md](handoff/README.md) | Cross-team handoff & developer-request guide | Orchestrator | `approved` | `v1.0` |
| [handoff/HANDOFF_REGISTRY.md](handoff/HANDOFF_REGISTRY.md) | Delivered developer package registry & checksums | Orchestrator / Agent 11 | `approved` | `v1.0` |
| [workflows/developer-requests.md](workflows/developer-requests.md) | Developer clarification request/response runbook | Orchestrator | `approved` | `v1.0` |
| [docs/GRAPHIFY.md](docs/GRAPHIFY.md) | Graphify operations & verification guide | Orchestrator | `approved` | `v1.0` |
