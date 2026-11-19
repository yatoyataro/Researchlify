"""Validate portable WebDevResearchTeam structure, links, adapters, and Graphify outputs."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_FILES = [
    "AGENTS.md",
    "TEAM.md",
    "WORKFLOW.md",
    "STATE.md",
    "DECISIONS.md",
    "ARTIFACT_INDEX.md",
    "SKILL_REGISTRY.md",
    "EVIDENCE_LEDGER.md",
    "ISSUES.md",
    "CHANGELOG.md",
    "README.md",
    "CLAUDE.md",
    ".graphifyignore",
    "docs/GRAPHIFY.md",
    "artifacts/_TEMPLATE.md",
]

AGENT_FILES = [
    "agents/orchestrator.md",
    "agents/01-discovery-context.md",
    "agents/02-evidence-user-research.md",
    "agents/03-existing-solutions.md",
    "agents/04-root-cause.md",
    "agents/05-prioritization.md",
    "agents/06-product-definition.md",
    "agents/07-business-analysis.md",
    "agents/08-ux-planning.md",
    "agents/09-technical-architecture.md",
    "agents/10-qa-auditor.md",
    "agents/11-documentation-handoff.md",
    "agents/12-skill-research.md",
    "agents/13-client-synthesizer.md",
]

WORKFLOWS = ["start-discovery.md", "resume.md", "review.md", "finalize.md"]

ARTIFACT_DIRS = [
    "research",
    "problem-analysis",
    "product",
    "requirements",
    "ux",
    "architecture",
    "reviews",
    "client-package",
]

LOCAL_SKILLS = [
    "discovery-orchestrator",
    "stage-qa-audit",
    "skill-research-eval",
    "client-humanizer-synthesis",
    "graphify",
    "humanizer",
    "discovery-process",
    "user-research",
    "research-synthesis",
    "accessibility-review",
    "web-design-guidelines",
    "writing-plans",
    "requesting-code-review",
]

MD_LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)#\s]+)(?:#[^)\s]*)?\)")


def check_links(md_path: Path, errors: list[str]) -> None:
    text = md_path.read_text(encoding="utf-8")
    for match in MD_LINK_RE.finditer(text):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (md_path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"Broken link in {md_path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []

    for rel in CANONICAL_FILES + AGENT_FILES:
        p = ROOT / rel
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"Missing or empty file: {rel}")

    agents_md = ROOT / "AGENTS.md"
    if agents_md.is_file() and agents_md.stat().st_size > 24000:
        errors.append(f"AGENTS.md exceeds 24,000-byte rule limit: {agents_md.stat().st_size}")

    for wf in WORKFLOWS:
        for base in ("workflows", ".agents/workflows", ".claude/commands"):
            p = ROOT / base / wf
            if not p.is_file() or p.stat().st_size == 0:
                errors.append(f"Missing workflow/adapter: {base}/{wf}")

    for adir in ARTIFACT_DIRS:
        if not (ROOT / "artifacts" / adir).is_dir():
            errors.append(f"Missing artifact directory: artifacts/{adir}")

    for skill in LOCAL_SKILLS:
        for root_dir in (".agents", ".claude"):
            sfile = ROOT / root_dir / "skills" / skill / "SKILL.md"
            if not sfile.is_file():
                errors.append(f"Missing skill: {sfile.relative_to(ROOT)}")
                continue
            head = sfile.read_text(encoding="utf-8")[:400]
            if not head.startswith("---\n") or "name:" not in head or "description:" not in head:
                errors.append(f"Missing YAML frontmatter in {sfile.relative_to(ROOT)}")

    for req in (".agents/rules/graphify.md", ".agents/workflows/graphify.md", ".claude/skills/graphify/SKILL.md"):
        if not (ROOT / req).is_file():
            errors.append(f"Missing Graphify adapter file: {req}")

    claude_settings = ROOT / ".claude" / "settings.json"
    if not claude_settings.is_file():
        errors.append("Missing .claude/settings.json")
    else:
        try:
            data = json.loads(claude_settings.read_text(encoding="utf-8"))
            if "PreToolUse" not in data.get("hooks", {}):
                errors.append(".claude/settings.json missing PreToolUse hooks")
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in .claude/settings.json: {exc}")

    state_text = (ROOT / "STATE.md").read_text(encoding="utf-8")
    if "IDLE" not in state_text or "READY_FOR_INTAKE" not in state_text:
        errors.append("STATE.md does not indicate IDLE / READY_FOR_INTAKE")

    for md in list(ROOT.glob("*.md")) + list((ROOT / "workflows").glob("*.md")) + list((ROOT / ".agents/workflows").glob("*.md")):
        check_links(md, errors)

    graph_json = ROOT / "graphify-out" / "graph.json"
    graph_report = ROOT / "graphify-out" / "GRAPH_REPORT.md"
    if not graph_json.is_file() or not graph_report.is_file():
        errors.append("Missing graphify-out/graph.json or graphify-out/GRAPH_REPORT.md")
    else:
        gdata = json.loads(graph_json.read_text(encoding="utf-8"))
        nodes = len(gdata.get("nodes", []))
        links = len(gdata.get("links", []))
        if nodes == 0:
            errors.append("graphify-out/graph.json contains 0 nodes")
        print(f"Graphify check: {nodes} nodes, {links} edges")

    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED: all canonical files, agents (00-13), workflows, adapters, links, and Graphify outputs verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
