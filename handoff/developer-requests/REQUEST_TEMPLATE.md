# Incoming Developer Request Schema (`REQST-NNN`)

Requests placed into `handoff/developer-requests/inbox/` by the Development Team (`E:\Codes\WebDeveloperTeam`) must preserve all fields below so Research Team agents can process them without reconstructing context.

```text
Request ID: REQST-NNN
Project ID: PRB-005
Package ID: PKG-PRB-005-v1.0
Requester: Agent XX (<Development Team Role>)
Assigned Research Team Agent: <Research Team Agent 01..13 or Orchestrator>
Date: YYYY-MM-DD
Priority: Critical | High | Medium | Low
Status: DRAFT | SENT | ACKNOWLEDGED | IN_PROGRESS | RESPONSE_READY | VERIFIED_BY_DEVELOPMENT | CLOSED | NEEDS_CLARIFICATION | BLOCKED | DECLINED_WITH_REASON | CANCELLED

Question:
<Specific unambiguous question or research/requirement gap>

Reason:
<Why Development cannot safely guess or resolve internally>

Relevant Artifact IDs:
<ART-NNN, REQ-NNN, DEC-NNN>

Relevant Sections:
<Exact section headings or line ranges>

Technical Finding:
<What Development verified or discovered (e.g., provider docs/quota check)>

Implementation Impact:
<Affected milestones, modules, schemas, or quotas>

Requested Outcome:
<Exact decision, citation, or updated artifact revision needed>

Evidence Requirements:
<Official docs, user research, or explicit human product decision>

Blocks Implementation: Yes | No (partial)
Independent Work Can Continue: Yes | No
```
