# Research Team — Development Team Handoff & Request Hub

Canonical cross-team boundary between **Web Development Research Team** (`E:\Codes\WebDevResearchTeam`) and **Web Developer Team** (`E:\Codes\WebDeveloperTeam`).

---

## 1. Organizational Ownership Boundaries

| Organization | Repository | Owns | Must Not |
|---|---|---|---|
| **Research Team** | `E:\Codes\WebDevResearchTeam` | Product research, problem definition, `EVIDENCE_LEDGER.md`, `REQ-NNN`, business rules, personas, user journeys (`UX-NNN`), IA, research-based architecture recommendations (`ARC-NNN`), product decisions (`DEC-NNN`), research limitations, and validation findings. | Begin application source coding, silently modify `E:\Codes\WebDeveloperTeam` implementation files, or treat a handoff package as implementation authorization. |
| **Development Team** | `E:\Codes\WebDeveloperTeam` | Application source code, implementation architecture, DB/frontend/backend/API implementation, automated tests, deployment config, engineering ADRs, and technical implementation docs. | Silently rewrite Research Team-owned artifacts (`ART-001`..`ART-018`) or bypass formal clarification requests. |

---

## 2. Directory Structure

```text
handoff/
├── README.md                          # Cross-team integration guide (this file)
├── HANDOFF_REGISTRY.md                # Outgoing package versions, SHA-256 checksums, delivery & status log
├── developer-packages/
│   ├── outgoing/                      # Prepared release ZIP(s) staged for delivery
│   └── package-history/               # Immutable historical archive of delivered ZIPs
└── developer-requests/
    ├── REQUEST_TEMPLATE.md            # Incoming clarification/research request schema (REQST-NNN)
    ├── RESPONSE_TEMPLATE.md           # Outgoing Research Team response schema
    ├── inbox/                         # Queued requests received from WebDeveloperTeam
    ├── in-progress/                   # Requests actively being researched/routed
    ├── responses/                     # Structured responses ready for Development Team verification
    └── archive/                       # Closed or cancelled request/response pairs
```

---

## 3. Transport & Communication Behavior

- **Primary transport:** Filesystem queue (`handoff/developer-requests/` <-> `E:\Codes\WebDeveloperTeam\ResearchTeamFinalResults\`).
- **Why filesystem queue:** Antigravity / Claude Code sessions run per workspace, and no live cross-repository background agent daemon is verified active between `WebDevResearchTeam` and `WebDeveloperTeam`.
- **Integrity rules:**
  - Never claim an idle Research Team session automatically processes queued requests.
  - Never fabricate acknowledgments, responses, or Development Team package acceptance.
  - Preserve `Request ID` (`REQST-NNN`) and existing `ART-NNN` / `REQ-NNN` / `DEC-NNN` IDs end-to-end.
- **Delivery path for outgoing packages:**
  - Immutable copy kept in `handoff/developer-packages/package-history/` (and `outgoing/`).
  - Delivery copy placed in `E:\Codes\WebDeveloperTeam\ResearchTeamFinalResults\incoming\` (never silently overwrite an existing filename—compare versions/checksums and bump version if needed).

---

## 4. Request Lifecycle

`DRAFT -> SENT -> ACKNOWLEDGED -> IN_PROGRESS -> RESPONSE_READY -> VERIFIED_BY_DEVELOPMENT -> CLOSED`

Exception / terminal states: `NEEDS_CLARIFICATION`, `BLOCKED`, `DECLINED_WITH_REASON`, `CANCELLED`.

See [workflows/developer-requests.md](../workflows/developer-requests.md) for the step-by-step intake, routing, response, and archive runbook.
