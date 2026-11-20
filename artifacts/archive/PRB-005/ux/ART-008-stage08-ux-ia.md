# ART-008 — Stage 08 UX & Information Architecture Specification

| Field | Value |
|---|---|
| **Artifact ID** | `ART-008` |
| **Purpose** | Define provisional user archetypes, end-to-end user journeys (`UX-001`..`UX-005`), information architecture, screen/state inventory, WCAG 2.1 AA accessibility & mobile-browser rules, text wireframes, and full `REQ <-> UX` traceability strictly aligned with `ART-007`. |
| **Status** | `approved` |
| **Owner** | `Agent 08 (UX & Information Architecture Planner)` |
| **Revision** | `v1.0` |
| **Date Created** | `2026-11-19` |
| **Date Updated** | `2026-11-19` |
| **Sources / Input Artifacts** | `ART-002`, `ART-006`, `ART-007` (`REQ-001`..`REQ-011`, `REQ-NFR-001`..`REQ-NFR-007`), `SKL-008c` (`accessibility-review`), `SKL-009` (`web-design-guidelines`) |

---

## Assumptions & Limitations

- **Provisional Personas (`DEC-007`):** Because no live interviews or usability tests were run, all user archetypes below are explicitly labeled **`provisional`** and synthesized from desk-research evidence (`FND-001`–`FND-004`, `FND-010`, `FND-014`).
- **Scope Discipline:** Zero production UI code is written here, and no features outside `ART-007` (`REQ-001`..`REQ-011`) are introduced.

---

## Content

### 1. Provisional User Archetypes

| Archetype | Label | Grounded Evidence Basis | Primary Goal & Emotional Need | Top UX Failure to Prevent |
|---|---|---|---|---|
| **Maya — The Streak-Fatigued Daily Puzzler** | `provisional` | `FND-001`, `FND-010`, `FND-014` (`SRC-006`–`SRC-008`) | Wants a joyful 3–5 min morning brain spark she can share in her family/friend group chat without battery/energy locks or missed-day guilt. | Energy counters, red "broken streak" shamescreens, or forced account signup before playing. |
| **Devon — The Chat-Group Host** | `provisional` | `FND-002`, `FND-003` (`SRC-009`–`SRC-011`, `SRC-018`) | Wants to drop a link in Discord/WhatsApp so 4–25 friends can play a quick trivia or phrase round together on their phones without a 10-player paywall. | Multi-step host setup, account walls for guests, or rooms stalling when one friend's phone drops Wi-Fi. |
| **Sam — The Busy Async Buddy** | `provisional` | `FND-004`, `FND-005` (`SRC-012`–`SRC-014`) | Wants to play the same 5-card challenge as friends on his commute or lunch break within 24 hours without coordinating everyone online at 8 PM. | Seeing peer answers before playing (spoilers) or getting penalized for taking hours to respond. |

---

### 2. End-to-End User Journeys & Recovery Flows (`UX-NNN`)

| UX ID | Journey | Step-by-Step Flow | Error / Edge Recovery Paths | Linked `REQ` |
|---|---|---|---|---|
| **UX-001** | **Solo Daily 5-Card Ritual & Share** | 1. Open root URL -> 2. Tap **"Play Today's 5"** (1 tap, zero signup) -> 3. Answer 5 cards sequentially with instant deterministic feedback + explanation -> 4. View Mastery Warmth update -> 5. Tap **"Copy Share Grid"** (`🟩🟨⬜`). | - *Offline/Network blip:* Daily seed cached locally after first load; practice works offline.<br>- *Clipboard blocked:* Opens selectable text box (`BR-03`) for manual copy.<br>- *Broken card:* Tap subtle **"Flag card"** (`REQ-008`) -> confirms locally and skips/replaces cleanly. | `REQ-001`, `REQ-002`, `REQ-003`, `REQ-008`, `REQ-009` |
| **UX-002** | **Host Creates & Shares Room (`<= 3` clicks)** | 1. Tap **"Play with Friends"** -> 2. Pick Track (*Phrases* / *World Trivia*) & Pacing (*Live Sync* or *24h Async*) -> 3. Tap **"Create Room"** -> 4. Copy invite link/6-char code and enter own display name. | - *Quota ceiling (`>= 85%` free tier):* Clear banner explains rooms paused until `00:00 UTC` and offers immediate **Solo Daily / Local Pass-and-Play** (`REQ-010`). | `REQ-004`, `REQ-005`, `REQ-010` |
| **UX-003** | **Guest Joins Room (`<= 2` taps) & Reconnects** | 1. Open invite URL (or enter 6-char code) -> 2. Type display name (`2–20` chars) & tap **"Join Room"** -> 3. Play rounds (`Live`: shared timer + reveal; `24h Async`: self-paced seeded 5 cards, blind until done) -> 4. View group summary & copy grid. | - *Wi-Fi/LTE drop or refresh:* Auto-reconnect uses signed `playerToken` (`REQ-006`) + non-blocking "Reconnecting..." pill, hydrating exact current round without double-scoring.<br>- *Expired/invalid code:* Friendly recovery card with 1-tap **"Start a Fresh Room"** or **"Play Solo Daily"**. | `REQ-004`, `REQ-005`, `REQ-006`, `REQ-NFR-002`, `REQ-NFR-006` |
| **UX-004** | **Zero-Guilt Mastery Ledger & Portable Backup** | 1. Open **"My Mastery"** tab/drawer -> 2. View Warmth/Mastery tiers (`New`, `Learning`, `Familiar`, `Mastered`) & rolling active days (no broken-streak red badges) -> 3. Tap **"Backup / Transfer"** -> 4. Copy sync code or download JSON; paste/upload on new device to merge. | - *Private browsing blocks `IndexedDB`:* Subtle non-blocking notice ("Session-only mode—export backup before closing") using `localStorage`/memory fallback (`REQ-002`).<br>- *Invalid import string:* Checksum error message; existing local data untouched (`BR-09`). | `REQ-001`, `REQ-002`, `REQ-009` |
| **UX-005** | **Optional Local AI Explanation (`Phase 2` Opt-In)** | 1. During answer feedback, tap **"Explain More"** -> 2. First time on WebGPU-capable device: modal shows exact model size & Wi-Fi recommendation (`REQ-011`) -> 3. On unsupported devices: instant deterministic open-metadata note displays directly with zero error. | - *Low RAM / WebGPU crash:* Silently falls back to deterministic metadata note and disables local-AI toggle for session without interrupting gameplay (`GOAL-005`). | `REQ-011`, `GOAL-005` |

---

### 3. Information Architecture & Screen Inventory

Minimal flat IA (3 primary destinations + 2 focused overlays) so mobile users never get lost:

```text
/ (Play Hub: Solo Daily CTA + Play with Friends + Track Picker)
├── /play/:mode (Solo Daily / Practice Card Runner -> Summary & Share Grid)
├── /room/new (2-Step Room Config: Track + Live/24h Async)
├── /room/:code (Guest Join Gate -> Live Lobby / Active Round -> Blind/Live Reveal -> Group Summary)
├── /mastery (Local Mastery Ledger + Rolling Rhythm + Portable Export/Import)
└── /about (Open Data Credits, CC0 / CC BY-SA 4.0 Attribution & Privacy Zero-PII Statement)
```

#### Screen State Matrix (Every Screen Must Implement All Applicable States)

| Screen | Default State | Loading State | Empty State | Error / Degraded State | Unauthorized / Expired State |
|---|---|---|---|---|---|
| **Play Hub (`/`)** | Daily 5-Card hero card, Track selector, "Play with Friends" CTA, rolling consistency badge | Skeleton card `< 300ms` while local `IndexedDB` hydrates | First visit: welcoming 1-line intro ("No signup, no energy bars—5 cards in 3 min") | Offline without cached seed: clear retry + cached Practice pack fallback | N/A (public entry) |
| **Card Runner (`/play/...`)** | Prompt card, 4 large `>=44px` option buttons (`1–4` hotkeys), progress dots (`1/5`), subtle "Flag card" link | Brief card transition (`prefers-reduced-motion` aware) | "All due review cards cleared! Play extra practice or invite friends" | Submit glitch: non-blocking inline retry keeping selection intact | N/A |
| **Room Lobby & Runner (`/room/:code`)** | Live player chip count, Pacing badge (`Live` / `24h Async`), Host controls or Active Round + countdown bar | "Syncing room state..." non-blocking banner | Host alone in lobby: prominent "Copy Invite Link" button + "Solo warm-up while waiting" hint | Socket disconnect: amber "Reconnecting..." pill preserving inputs; Quota cap: friendly Solo fallback | Invalid/48h-expired room -> recovery screen ("Room ended—create new room or play Solo Daily") |
| **My Mastery (`/mastery`)** | Track mastery breakdown bars, "Comeback Ready" review button, Backup/Restore actions | Brief local read indicator | Zero cards played yet -> direct **"Start First 5 Cards"** CTA | Corrupted import -> inline validation error, zero overwrite | Private-mode notice if storage ephemeral |
| **About & Licenses (`/about`)** | Zero-PII pledge, `Tatoeba CC0`, `Wikidata CC0`, `OpenTriviaDB CC BY-SA 4.0`, `Wiktionary CC BY-SA 4.0` credits | Static render | N/A | N/A | N/A |

---

### 4. UX Principles, Mobile-Browser Safety & Accessibility (`SKL-008c`, `SKL-009`)

1. **Mobile Viewport & Touch Isolation (`REQ-NFR-003`):**
   - Full-height play viewports use `min-height: 100dvh` with single-column stacked options so iOS/Android address bars never clip submit buttons.
   - Apply `touch-action: manipulation` on all interactive buttons/cards to eliminate 300ms delay and accidental double-tap zoom.
   - All text inputs (`displayName`, `roomCode`, `syncCode`) use `font-size >= 16px` to prevent iOS Safari auto-zoom (`SRC-009`).
2. **WCAG 2.1 AA Compliance (`REQ-NFR-004`):**
   - **Perceivable:** Text contrast `>= 4.5:1` (normal) and `>= 3:1` (large/UI borders); feedback uses **both** color and explicit icons/text (`✓ Correct` / `↺ Review soon`), never color alone.
   - **Operable:** `100%` keyboard playable (`Tab`, keys `1`–`4` for answers, `Enter`/`Space` to advance, `Esc` to close modals); visible `:focus-visible` ring; touch targets `>= 44x44 CSS px` with `>= 8px` spacing.
   - **Understandable & Robust:** Semantic landmarks (`<header>`, `<main>`, `<nav>`), explicit `<label>` elements, and `aria-live="polite"` announcements for round transitions, reveal outcomes, and connection status (`Reconnecting...` / `Connected`).
   - **Cognitive & Motion Comfort:** Respect `prefers-reduced-motion`; keep each card focused on one question + max 4 choices (low cognitive load); no ticking red anxiety timers in Solo or 24h Async modes.
3. **Privacy & Consent Touchpoints (`REQ-NFR-005`):**
   - Zero cookie banners needed if zero tracking cookies are used; display clear one-line privacy note on `/room/:code` ("Only your display name is shared in this room for up to 48 hours").

---

### 5. Text Wireframes (Key MVP Screens)

#### Wireframe A — Play Hub (`/`) [Mobile 375px]
```text
+---------------------------------------+
| [BrainPlay]    [Mastery] [About]      |
+---------------------------------------+
|  3 active days this week · 42 learned |
|                                       |
|  +---------------------------------+  |
|  | TODAY'S 5-CARD RITUAL           |  |
|  | Track: [Phrases v] [Trivia]     |  |
|  | 5 quick cards · No energy limit |  |
|  |                                 |  |
|  |     [  Play Today's 5  ]        |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  | PLAY WITH FRIENDS (2–30+ FREE)  |  |
|  | Live party or 24h async run     |  |
|  | [ Create Room ]  [ Join Code ]  |  |
|  +---------------------------------+  |
+---------------------------------------+
```

#### Wireframe B — Active Round Runner (`/play/...` & `/room/:code`) [Mobile 375px]
```text
+---------------------------------------+
| ● ● ○ ○ ○   2/5   [Live: 18s] [Conn●] |
+---------------------------------------+
|  Track: Phrases in Context            |
|                                       |
|  "Estoy buscando la estación..."      |
|  Choose the closest meaning:          |
|                                       |
|  [ 1. I am looking for the station ]  |
|  [ 2. I just left the station      ]  |
|  [ 3. The station is closed today  ]  |
|  [ 4. Where is the train ticket?   ]  |
|                                       |
|  [After answer: Feedback + Note]      |
|  [ Next Card -> ]        Flag card    |
+---------------------------------------+
```

#### Wireframe C — Room Summary & Spoiler-Free Share (`/room/:code`)
```text
+---------------------------------------+
|  Round Complete! · 24h Async Room     |
+---------------------------------------+
|  Your Run:  🟩 🟩 🟨 🟩 🟩  (4/5)     |
|  [ Copy Spoiler-Free Grid ]           |
|                                       |
|  Group Results (Unlocked after play): |
|  - Maya      🟩🟩🟨🟩🟩  4/5          |
|  - Devon     🟩🟨🟩🟩🟩  4/5          |
|  - Sam       (Playing today...)       |
|                                       |
|  [ Play Rematch ]   [ Back to Hub ]   |
+---------------------------------------+
```

---

### 6. UX-to-Requirement Traceability (`REQ-NNN <-> UX-NNN`)

| Requirement | Represented In (`UX-NNN` / Screen) | Gate Check |
|---|---|---|
| `REQ-001`, `REQ-002` | `UX-001`, `UX-004` (`/`, `/play/:mode`, `/mastery`) | Zero energy bars; rolling active days; local mastery states |
| `REQ-003` | `UX-001`, `UX-003` (Summary + Share Modal fallback) | Spoiler-free emoji grid + manual copy fallback |
| `REQ-004`, `REQ-005` | `UX-002`, `UX-003` (`/room/new`, `/room/:code`) | `<= 2`-tap guest join; Live & 24h Async pacing states |
| `REQ-006` | `UX-003` (`/room/:code` Reconnecting pill & state hydration) | Reconnect preserves exact round without duplicate scoring |
| `REQ-007`, `REQ-NFR-007` | `/about` + card source credit badge | Clear CC0 / CC BY-SA 4.0 attribution |
| `REQ-008` | `UX-001` (`Flag card` micro-action) | 1-click report + immediate local skip |
| `REQ-009` | `UX-004` (`/mastery` Backup/Restore drawer) | Export JSON/sync string + checksum-validated import |
| `REQ-010` | `UX-002` (`/room/new` Quota-safe notice + Solo fallback) | Graceful degraded UX at edge quota limit |
| `REQ-011` (`Phase 2`) | `UX-005` (Opt-in "Explain More" modal + deterministic fallback) | Explicit opt-in, zero forced AI dependency |
| `REQ-NFR-003`, `REQ-NFR-004` | Section 4 (All screens) | Mobile `100dvh`/`>=16px`/`44px` targets + WCAG 2.1 AA |

---

## Next Steps / Unresolved Issues

- **Stage 08 Gate Check:** Every MVP requirement (`REQ-001`..`REQ-010`, `REQ-NFR-001`..`REQ-NFR-007`) plus Phase 2 `REQ-011` is covered in `UX-001`..`UX-005` and the screen/state matrix; all personas are explicitly labeled `provisional`; zero unapproved features or production code appear.
- **Next Stage:** Hand off to **Agent 09 (Technical Architect)** to design the `$0` system architecture, component boundaries, ERD, WebSocket/HTTP API contracts, security/privacy threat model, and operational/quota plan (`ART-009`).
