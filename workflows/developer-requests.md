# Workflow: `developer-requests`

Portable Research Team runbook for handling asynchronous clarification and research requests from the Development Team (`E:\Codes\WebDeveloperTeam`).

## Preconditions
- Request file arrives in `handoff/developer-requests/inbox/` (matching `handoff/developer-requests/REQUEST_TEMPLATE.md`) via the filesystem queue or an explicitly verified cross-repo tool.
- Never claim automatic background processing when no Research Team session is running, and never fabricate acknowledgments or Development verification.

## Lifecycle States
`DRAFT -> SENT -> ACKNOWLEDGED -> IN_PROGRESS -> RESPONSE_READY -> VERIFIED_BY_DEVELOPMENT -> CLOSED`

Exception / terminal states: `NEEDS_CLARIFICATION`, `BLOCKED`, `DECLINED_WITH_REASON`, `CANCELLED`.

## Steps
1. **Intake & Acknowledge (`Agent 00` — Orchestrator)**
   - Inspect `handoff/developer-requests/inbox/<REQST-NNN>.md` and verify all required fields (`Request ID`, `Project ID`, `Package ID`, `Question`, `Relevant Artifact IDs`, `Blocks Implementation`, etc.).
   - Move file to `handoff/developer-requests/in-progress/`, update `Status: ACKNOWLEDGED` (if details are missing, set `NEEDS_CLARIFICATION` and emit a clarification note).
2. **Route to Owning Research Specialist (`TEAM.md` Section 4)**
   - Update `Status: IN_PROGRESS` and assign the owning Research agent (`01`–`13` or Human for product/policy/Level-5 choices).
   - Query Graphify (`graphify query "<ART-NNN / REQ-NNN>"`) to assess upstream/downstream impact before editing any artifact.
3. **Execute Research / Revision & QA Check**
   - Preserve all unrelated `ART-NNN` IDs, versions, and citations. If an upstream artifact changes, bump its revision, update `EVIDENCE_LEDGER.md` / `DECISIONS.md` / `ARTIFACT_INDEX.md`, and run an `Agent 10` scoped consistency check.
   - If the request requires unapproved live human research (`DEC-007`) or a product/scope tradeoff, mark `BLOCKED` and escalate to the user.
4. **Emit Structured Response**
   - Write response using `handoff/developer-requests/RESPONSE_TEMPLATE.md` to `handoff/developer-requests/responses/<REQST-NNN>-response.md` (`Status: RESPONSE_READY`).
   - If authorized to deliver directly across repos, copy the response into `E:\Codes\WebDeveloperTeam\ResearchTeamFinalResults\responses-from-research\` (without modifying any other Development Team files); otherwise clearly tell the user the response is staged in `handoff/developer-requests/responses/`.
   - If artifact revisions warrant a formal re-release, cut an incremented package version (e.g., `v1.1`) in `handoff/developer-packages/` and update `HANDOFF_REGISTRY.md`.
5. **Close & Refresh Graph**
   - Only after Development Team confirms `VERIFIED_BY_DEVELOPMENT`, move the request/response record to `handoff/developer-requests/archive/` with `Status: CLOSED`.
   - Refresh Graphify (`graphify update .`) and update `STATE.md` / `CHANGELOG.md`.
