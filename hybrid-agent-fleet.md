# The 90-Day Hybrid AI Agent Fleet for a Clinician-Entrepreneur

## The Operating Philosophy

The core insight is simple but counterintuitive: **the clinician-entrepreneur should be the orchestrator, not the executor.** Every repeatable task — from content scheduling to inbox triage to clinical note formatting — should be delegated to a specialised agent within 90 days.

This isn't about replacing human judgment. It's about freeing it. The highest-value activities (clinical decision-making, creative direction, strategic thinking, relationship-building) should get more of your time, not less. Agents handle the scaffolding.

> Design for orchestration, not execution. You are the conductor — the agents are the orchestra.

## The 7-Agent Fleet

Each agent operates in a defined domain with clear inputs, outputs, and escalation triggers. The fleet architecture is deliberately modular — agents can be upgraded, swapped, or retired independently.

| Agent | Domain | Core Loop |
|-------|--------|-----------|
| **Atlas** | Content & Distribution | Draft → Review → Schedule → Analyse |
| **Helix** | Clinical Support | Notes → Summary → Template → Archive |
| **Nexus** | Business Ops | Inbox → Triage → Route → Track |
| **Prism** | Research & Learning | Scan → Filter → Brief → Store |
| **Forge** | Dev & Infrastructure | Build → Test → Deploy → Monitor |
| **Echo** | Personal OS | Capture → Organise → Surface → Review |
| **Groot** | Communications | Receive → Classify → Draft → Send |

## Phase 1 — Foundation (Days 1–30)

### Infrastructure Sprint

The first month is about laying pipe. No agent can function without reliable infrastructure underneath it. This means:

- Domain and DNS consolidation (Cloudflare-native)
- Knowledge base architecture in Obsidian
- API key management and secrets rotation
- Core automation scaffolding (n8n or Make)
- Monitoring and logging baseline

The temptation in Phase 1 is to start building agents immediately. Resist it. An agent built on shaky infrastructure will cost you more time debugging than it saves. Get the plumbing right first.

> You can't automate chaos. First, create order. Then, automate the order.

## Phase 2 — Activation (Days 31–60)

### First Agents Online

With infrastructure solid, activate the highest-ROI agents first. For most clinician-entrepreneurs, that's **Atlas** (content) and **Nexus** (ops), because these two domains consume the most discretionary time.

Each agent starts in "co-pilot" mode: it drafts, you approve. Nothing goes out without human review during this phase. The goal is to build trust in the agent's outputs while tuning its parameters.

> **Activation Checklist:** For each agent — define inputs → set output format → establish review cadence → create escalation rules → document failure modes.

## Phase 3 — Autonomy (Days 61–90)

### Graduated Trust

The final phase is about moving select agents from co-pilot to auto-pilot — but only for well-defined, low-risk tasks. Content scheduling on pre-approved posts? Auto-pilot. Clinical note templates? Co-pilot forever, by design.

The autonomy boundary is determined by two factors:

1. **Reversibility** — Can you undo the action easily? If yes, more autonomy is safe.
2. **Consequence magnitude** — What's the worst-case failure? If low, more autonomy is safe.

By Day 90, the fleet should be saving 15–20 hours per week of execution time, freeing the clinician-entrepreneur to focus on the irreplaceable: patient care, creative vision, and strategic relationships.

## What Comes After Day 90

The fleet is not a destination — it's a living system. Post-90-day priorities include inter-agent communication (letting Prism feed insights to Atlas automatically), performance dashboards, and the gradual introduction of web3 primitives for provenance and token-gated content.

The operating model scales. The human doesn't have to.
