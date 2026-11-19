---
name: client-humanizer-synthesis
description: >-
  Run Agent 13 plain-language client synthesis and traceability verification
  for Package B deliverables. Use when generating Client Research Overview,
  Presentation Outline, Executive Summary, FAQ, and Traceability Report.
---

# Client Synthesis & Humanizer Adapter

Follow the canonical client synthesizer spec:
1. Check `SKILL_REGISTRY.md` for any approved external humanizer skill; otherwise use this built-in process and note skill status transparently.
2. Read `agents/13-client-synthesizer.md` and only `approved` (or explicitly labeled provisional) upstream artifacts.
3. Produce all 6 Package B deliverables in `artifacts/client-package/`.
4. Remove unnecessary jargon and stiff phrasing while preserving factual accuracy, limitations, expected-vs-proven distinction, honest AI authorship, and full claim traceability.
