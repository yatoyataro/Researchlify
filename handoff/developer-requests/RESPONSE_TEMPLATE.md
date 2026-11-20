# Outgoing Research Response Schema (`REQST-NNN`)

Responses placed into `handoff/developer-requests/responses/` (and routed to `E:\Codes\WebDeveloperTeam\ResearchTeamFinalResults\responses-from-research\`) must include every field below.

```text
Request ID: REQST-NNN
Project ID: PRB-005
Package ID: PKG-PRB-005-v1.0
Research Owner: Agent XX (<Research Team Role>)
Response Date: YYYY-MM-DD
Status: RESPONSE_READY

Answer:
<Direct, unambiguous answer preserving existing IDs unless revised>

Rationale:
<Why this answer/decision aligns with evidence, goals, and constraints>

Evidence and Citations:
<SRC-NNN, FND-NNN, DEC-NNN, or explicit [ASSUMPTION / NEEDS HUMAN DECISION] note>

Changed Artifacts:
<None | List of updated ART-NNN>

Artifact Versions:
<ART-NNN: vX.Y (unchanged or bumped)>

Files Added or Updated:
<Relative paths inside E:\Codes\WebDevResearchTeam>

Implementation Impact:
<Effect on milestones, schemas, API/WS contracts, UX, or $0 constraints>

New Risks or Limitations:
<Any newly surfaced caveats or unvalidated hypotheses>

Recommended Downstream Rework:
<None | Specific tasks/specs for Development Team review, or new package version if needed>

Remaining Questions:
<None | Explicit human or follow-up questions>
```
