# SKILL_REGISTRY.md — Agent Skill Registry

Maintained by **Agent 12** (`agents/12-skill-research.md`).
Lifecycle: `discovered -> evaluated -> awaiting_approval -> approved -> installed -> assigned -> verified -> monitored` (or `rejected` / `retired`).
**Security rule:** External GitHub skills must **not** be installed or executed without explicit human approval.

---

## 1. Local & Built-In Team Skills (Active)

| ID | Skill Name | Location | Version | Discovered / Updated | Intended Agent(s) | Evaluation Summary | Risks / Permissions | Status |
|---|---|---|---|---|---|---|---|---|
| `SKL-001` | `discovery-orchestrator` | `.agents/skills/discovery-orchestrator/SKILL.md` & `.claude/skills/discovery-orchestrator/SKILL.md` | `1.0.0` | 2026-11-19 | Agent 00 (Orchestrator) | Thin adapter enforcing intake, sequential gates, and state persistence via `WORKFLOW.md`. | Local repo-only; read/write workspace state files. | `verified` |
| `SKL-002` | `stage-qa-audit` | `.agents/skills/stage-qa-audit/SKILL.md` & `.claude/skills/stage-qa-audit/SKILL.md` | `1.0.0` | 2026-11-19 | Agent 10 (QA Auditor) | Structured cross-artifact consistency, citation verification, and `ISSUES.md` routing checklist. | Local repo-only; read artifacts, write `ISSUES.md` / review reports. | `verified` |
| `SKL-003` | `skill-research-eval` | `.agents/skills/skill-research-eval/SKILL.md` & `.claude/skills/skill-research-eval/SKILL.md` | `1.0.0` | 2026-11-19 | Agent 12 (Skill Research) | 8-point GitHub skill evaluation, security inspection, and `SKILL_REGISTRY.md` maintenance runbook. | Read-only web/repo inspection; approval gate before install. | `verified` |
| `SKL-004` | `client-humanizer-synthesis` | `.agents/skills/client-humanizer-synthesis/SKILL.md` & `.claude/skills/client-humanizer-synthesis/SKILL.md` | `1.0.0` | 2026-11-19 | Agent 13 (Client Synthesizer) | Plain-language synthesis wrapper pairing with `SKL-006` (`humanizer`) and claim-to-artifact traceability. | Local repo-only; read approved artifacts, write `artifacts/client-package/`. | `verified` |
| `SKL-005` | `graphify` | `.agents/skills/graphify/SKILL.md` & `.claude/skills/graphify/SKILL.md` | `0.9.111` | 2026-11-19 | All Agents (00–13) | Official Graphify skill installed project-locally via `graphify install --project` for knowledge-graph build and queries. | Local CLI (`graphify`); writes only to `graphify-out/`. | `verified` |

---

## 2. Approved External GitHub Skills (Installed & Pinned)

> Audited in scratch before installation (pure Markdown/template files only; zero external scripts copied or executed) and pinned to verified commit SHAs after explicit user approval (`2026-11-19`).

| ID | Skill Name | Repository URL & Source Path | Pinned Commit | Installed Path(s) | Intended Agent(s) | Audit & Usage Notes | Status |
|---|---|---|---|---|---|---|---|
| `SKL-006` | `humanizer` | `https://github.com/blader/humanizer` (`SKILL.md`, `LICENSE`) | `b48c832f0f809c1b5658edbb838c2521b72f2413` | `.agents/skills/humanizer/` & `.claude/skills/humanizer/` | **Agent 13** (Client Synthesizer) | MIT-licensed (`v4.0.0`). Treats input text as untrusted data; removes AI prose tells without altering facts or evading AI detectors. Scripts/CI excluded. | `verified` |
| `SKL-007` | `discovery-process` | `https://github.com/deanpeters/Product-Manager-Skills` (`skills/discovery-process/{SKILL.md,template.md}`) | `476ae12917b8e77609eb956bcc2203a4e4ec857d` | `.agents/skills/discovery-process/` & `.claude/skills/discovery-process/` | **Agent 01, 04, 06** | Pure Markdown discovery framing & validation workflow. Use within `WORKFLOW.md` sequential gates; missing sibling skills in upstream repo are not required. | `verified` |
| `SKL-008a` | `user-research` | `https://github.com/anthropics/knowledge-work-plugins` (`design/skills/user-research/SKILL.md`) | `b4c9a4e1de4b42868b74a6fe30ac766f64e43a3e` | `.agents/skills/user-research/` & `.claude/skills/user-research/` | **Agent 02** (Evidence & User Research) | Pure Markdown methods, interview guide structure, and analysis framework. | `verified` |
| `SKL-008b` | `research-synthesis` | `https://github.com/anthropics/knowledge-work-plugins` (`design/skills/research-synthesis/SKILL.md`) | `b4c9a4e1de4b42868b74a6fe30ac766f64e43a3e` | `.agents/skills/research-synthesis/` & `.claude/skills/research-synthesis/` | **Agent 02** (Evidence & User Research) | Pure Markdown synthesis template separating observations from interpretations. | `verified` |
| `SKL-008c` | `accessibility-review` | `https://github.com/anthropics/knowledge-work-plugins` (`design/skills/accessibility-review/SKILL.md`) | `b4c9a4e1de4b42868b74a6fe30ac766f64e43a3e` | `.agents/skills/accessibility-review/` & `.claude/skills/accessibility-review/` | **Agent 08** (UX & IA) | Pure Markdown WCAG 2.1 AA audit checklist and review matrix. | `verified` |
| `SKL-009` | `web-design-guidelines` | `https://github.com/vercel-labs/agent-skills` (`skills/web-design-guidelines/SKILL.md`) | `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` | `.agents/skills/web-design-guidelines/` & `.claude/skills/web-design-guidelines/` | **Agent 08** (UX & IA) | Pure Markdown (`v1.0.0`); references Vercel Web Interface Guidelines URL on demand for UI/UX checks. | `verified` |
| `SKL-010a` | `writing-plans` | `https://github.com/obra/superpowers` (`skills/writing-plans/SKILL.md`) | `22f0b463e7a5e579904dd6211a520321035526f7` | `.agents/skills/writing-plans/` & `.claude/skills/writing-plans/` | **Agent 09, 11** | Pure Markdown planning decomposition format. **Constraint:** Use only for implementation roadmap planning (`Package A`); `AGENTS.md` discovery-only rule overrides coding triggers. | `verified` |
| `SKL-010b` | `requesting-code-review` | `https://github.com/obra/superpowers` (`skills/requesting-code-review/{SKILL.md,code-reviewer.md}`) | `22f0b463e7a5e579904dd6211a520321035526f7` | `.agents/skills/requesting-code-review/` & `.claude/skills/requesting-code-review/` | **Agent 10** (QA Auditor) | Pure Markdown structured review template and severity calibration (`Critical/Important/Minor`). | `verified` |

---

## 3. Approval & Installation Log

| Date | Skill ID | Decision | Approved By | Pinned Commit / Version | Verification Result | Notes |
|---|---|---|---|---|---|---|
| 2026-11-19 | `SKL-001`..`SKL-004` | `installed` | System Setup | `1.0.0` | Validated locally | Authored inside `.agents/skills/` and mirrored to `.claude/skills/`. |
| 2026-11-19 | `SKL-005` | `installed` | User task spec | `graphify 0.9.111` | CLI & graph tested | Project-scoped install only (`--project`). |
| 2026-11-19 | `SKL-006`..`SKL-010b` | `approved` -> `verified` | User (explicit approval) | Pinned SHAs above | Frontmatter, file integrity & safety audited | Pure Markdown/template copies installed; upstream scripts/CI omitted. |
