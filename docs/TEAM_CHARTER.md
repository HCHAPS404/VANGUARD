# VANGUARD — Team Charter

**Hackathon:** Band of Agents · Lablab.ai  
**Sprint:** 13–19 June 2026  
**Team:** INZERM (DEV · Juliana · HELL)

---

## Mission

Deliver a demo-ready, judge-verifiable multi-agent TPRM platform where Band is the deliberation layer — not a log — and TRUTHLOCK guarantees zero unverified claims in the final report.

---

## Agent ownership (final)

| Agent | Phase | Owner | Branch |
|-------|-------|-------|--------|
| **INTAKE** | A | HELL | `agent/intake` |
| **LEXIS** | A | DEV | `agent/lexis` |
| **SENTINEL** | A | HELL | `agent/sentinel` |
| **LEDGER** | A | DEV | `agent/ledger` |
| **ARBITER** | B | HELL | `agent/arbiter` |
| **TRUTHLOCK** | B | HELL | `agent/truthlock` |
| **FORGE** | C | Juliana | `agent/forge` |
| **HERALD** | C | Juliana | `agent/herald` |

**HELL — 4 agents** (Band integration + security + deliberation stack)  
**DEV — 2 agents** (compliance + financial analysis + platform core)  
**Juliana — 2 agents** (remediation + executive delivery + product surface)

---

## Role definitions

### HELL — Tech Lead & Band Architect

**Agents:** INTAKE, SENTINEL, ARBITER, TRUTHLOCK  
**Owns:** `core/band/`, Band Room lifecycle, WebSocket event bus, debate orchestration, anti-hallucination gate, merge authority on `dev`

| # | Responsibility | Deliverable |
|---|----------------|-------------|
| H1 | Register 8 External Agents on band.ai; maintain `config/agent_config.yaml` | All UUIDs + API keys documented in Notion (redacted) |
| H2 | Implement `core/band/` — REST publish, WebSocket subscribe, @mention parser | Shared client imported by all agents |
| H3 | Create Band Room with structured debate configuration | Room ID in `.env` |
| H4 | Build **INTAKE** — PDF ingest, hash, ChromaDB write, Room publish | `agents/intake/agent.py` + tests |
| H5 | Build **SENTINEL** — security analysis + 50-signal cross-reference | `agents/sentinel/agent.py` + tests |
| H6 | Build **ARBITER** — contradiction detection, debate threads, Risk Score | `agents/arbiter/agent.py` + tests |
| H7 | Build **TRUTHLOCK** — claim verification, invalidation alerts, Phase C gate | `agents/truthlock/agent.py` + tests |
| H8 | Implement `AuditSession` state machine in `core/schemas/session.py` | Session phases enforced in code |
| H9 | @mention response handlers in SENTINEL (own agent) | SENTINEL replies in debate threads |
| H10 | AI/ML API integration for ARBITER + TRUTHLOCK reasoning | `core/llm/aiml_client.py` |
| H11 | Integration lead — Días 3, 7 | E2E green before demo |
| H12 | Architecture Decision Records (ADR) for Band patterns | `docs/adr/001-band-room.md`, `002-truthlock-gate.md` |
| H13 | Code review all PRs to `dev` before merge | Review checklist signed daily |
| H14 | Contingency: simplified ARBITER if active debate blocked | Documented in ADR + Room still shows thread |
| H15 | Demo segment: live Band Room debate + TRUTHLOCK invalidation | 60s in demo video |

---

### DEV — Platform Engineer & Analysis Lead

**Agents:** LEXIS, LEDGER  
**Owns:** `core/rag/`, `core/schemas/`, `core/llm/featherless_client.py`, `scripts/`, pytest infrastructure

| # | Responsibility | Deliverable |
|---|----------------|-------------|
| D1 | Define all Pydantic schemas in `core/schemas/` (blocking Day 1 PM) | `messages.py`, `findings.py`, `session.py` |
| D2 | Implement `core/rag/` — PyMuPDF extract, LangChain chunk, ChromaDB store/query | Unit tests with sample PDF |
| D3 | Implement Featherless AI client with model routing | `core/llm/featherless_client.py` |
| D4 | Build **LEXIS** — GDPR/ISO27001/SOC2 analysis with reference RAG | `agents/lexis/agent.py` + tests |
| D5 | Build **LEDGER** — financial risk analysis | `agents/ledger/agent.py` + tests |
| D6 | Expand reference corpora in `docs/reference/` (full articles, not stubs) | GDPR, ISO, SOC2 enriched |
| D7 | @mention handlers in LEXIS and LEDGER | Agents respond in ARBITER threads |
| D8 | `scripts/run_agent.py` — CLI to start any agent | `uv run python scripts/run_agent.py lexis` |
| D9 | `scripts/run_pipeline.py` — orchestrated local demo | Single command full flow |
| D10 | Pytest fixtures for Room messages in `tests/fixtures/` | JSON mocks per message type |
| D11 | Integration tests — Phase A (ingest → 2 findings) | `tests/test_phase_a.py` |
| D12 | Integration tests — full E2E (Day 5) | `tests/test_e2e.py` |
| D13 | Integration lead — Día 5 | 3/3 document profiles pass |
| D14 | Refactor + type hints + ruff/format pass | Clean `dev` branch Day 6 |
| D15 | Fallback Ollama client stub if Featherless credits low | `core/llm/ollama_client.py` |
| D16 | Schemas `Remediation` + `ExecutiveSummary` (Day 4 support) | Unblocks Juliana |

---

### Juliana — Product Lead & Delivery

**Agents:** FORGE, HERALD  
**Owns:** `dashboard/`, `integrations/`, `docs/prompts/`, demo assets, Notion workspace, Lablab visual deliverables

| # | Responsibility | Deliverable |
|---|----------------|-------------|
| J1 | Notion workspace — 5 sections live before Day 1 | APIs, Prompts, ADR log, Prompt Log, Daily bitácora |
| J2 | Collect 5+ test PDFs (Google, AWS, Azure + 2 synthetic contracts) | `tests/documents/` |
| J3 | Complete `.env` + `agent_config.yaml` from team credentials | Working local config (gitignored) |
| J4 | Polish all 8 prompts in `docs/prompts/` with final system instructions | Reviewed by team Day 2 AM |
| J5 | Build **FORGE** — remediation generator for Critical/High findings | `agents/forge/agent.py` + tests |
| J6 | Build **HERALD** — executive summary composer | `agents/herald/agent.py` + tests |
| J7 | PDF report template — reportlab with traffic-light layout | `integrations/pdf_generator.py` |
| J8 | n8n Docker compose + Telegram webhook flow | `docker/docker-compose.yml` |
| J9 | Streamlit dashboard — session list, score, semáforo, Room link | `dashboard/app.py` |
| J10 | Streamlit Cloud deployment | Public demo URL |
| J11 | `@mention` handler in FORGE (if invoked post-debate) | Optional response in Room |
| J12 | Integration lead — Día 6 | README, docs, assets complete |
| J13 | Demo script + slide deck (5 acts) | `docs/DEMO_SCRIPT.md` + slides |
| J14 | Lablab cover image + technology tags | PNG 1280×720 |
| J15 | Prompt Log in Notion — every adjustment Day 5 documented | Linked from README |
| J16 | HERALD Telegram 5-line template tested live | Screenshot for submission |
| J17 | Contingency: weasyprint PDF if reportlab fails | `integrations/pdf_weasyprint.py` |

---

## RACI matrix (key activities)

| Activity | HELL | DEV | Juliana |
|----------|:----:|:---:|:-------:|
| Band Room setup | **R/A** | C | I |
| Pydantic schemas | C | **R/A** | I |
| INTAKE agent | **R/A** | C | I |
| LEXIS / LEDGER agents | C | **R/A** | I |
| SENTINEL agent | **R/A** | C | I |
| ARBITER / TRUTHLOCK | **R/A** | C | I |
| FORGE / HERALD | I | C | **R/A** |
| Streamlit dashboard | I | C | **R/A** |
| n8n / Telegram | I | I | **R/A** |
| E2E testing | C | **R** (D5) | C |
| README / docs | C | C | **R** (D6) |
| Lablab submission | **A** | C | **R** |
| Video recording | R | C | **R** |

*R = Responsible · A = Accountable · C = Consulted · I = Informed*

---

## Daily capacity model

Assumption: **~8 h/person/day** · 3 people · 7 days = **168 person-hours**

| Person | Agent coding | Core/platform | Product/demo | Total |
|--------|-------------|---------------|--------------|-------|
| HELL | ~40h (4 agents) | ~12h (band) | ~4h (review/demo) | ~56h |
| DEV | ~24h (2 agents) | ~24h (rag/schemas/tests) | ~4h | ~52h |
| Juliana | ~20h (2 agents) | ~4h | ~28h (UI/demo/docs) | ~52h |

---

## Communication

| Channel | Purpose |
|---------|---------|
| Band Room (prod) | Agent messages — demo evidence |
| Band Room (dev) | Optional second room for testing |
| Notion | Prompt log, ADR, daily bitácora |
| GitHub PRs | All code changes via review |
| Telegram (team) | Human alerts during hackathon |

---

## Definition of Ready (DoR) — before starting an agent

- [ ] Schema for agent output merged in `core/schemas/`
- [ ] Prompt approved in `docs/prompts/<agent>.md`
- [ ] Band API key in `agent_config.yaml`
- [ ] Branch `agent/<name>` created from latest `dev`

## Definition of Done (DoD) — before merging an agent

- [ ] Agent listens and publishes to Band Room
- [ ] Output validates against Pydantic schema
- [ ] At least 1 pytest covering happy path
- [ ] Prompt version noted in Notion Prompt Log
- [ ] PR reviewed by HELL (or DEV for Juliana PRs on product code)
