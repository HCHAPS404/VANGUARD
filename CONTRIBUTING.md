# Contributing to VANGUARD

Internal guide for INZERM team during the hackathon sprint.

---

## Branch strategy

```
main          ← stable, demo-ready (merge Day 6)
dev           ← daily integration branch
agent/<name>  ← one branch per agent owner
feat/<area>   ← shared infrastructure (e.g. feat/schemas, feat/dashboard)
fix/<issue>   ← hotfixes during integration days
```

**Rules:**

1. Never commit directly to `main` or `dev`.
2. Open PR to `dev`; require 1 review (HELL for agent code, DEV for product code).
3. Merge `dev` → `main` only on Day 6 after E2E green.

---

## Pull request template

Every PR must include:

- **Agent / area:** e.g. `agent/intake` or `core/schemas`
- **Phase:** A / B / C / infra
- **Schema changes:** yes/no — if yes, link model names
- **Band Room tested:** yes/no — screenshot if agent publishes messages
- **pytest added:** yes/no
- **Prompt updated:** link to `docs/prompts/<agent>.md` if changed

---

## Commit message format

```
<type>(<scope>): <description>

Types: feat | fix | docs | test | refactor | chore
Scope: intake | lexis | band | schemas | dashboard | etc.

Examples:
feat(intake): publish IngestMessage to Band Room after PDF embed
fix(truthlock): block Phase C when invalidation count > 0
docs(plan): expand Day 3 task breakdown
```

---

## Local development

```powershell
uv sync
.venv\Scripts\activate
copy .env.example .env
copy config\agent_config.yaml.example config\agent_config.yaml

# Run single agent
uv run python scripts/run_agent.py intake

# Run tests
uv run pytest tests/ -v
```

---

## Code standards

- Python 3.11+ type hints on public functions
- Pydantic models for all Room payloads — no raw dicts at publish boundary
- Agent entry point: `agents/<name>/agent.py` with `main()` or `run()`
- Prompts live in `docs/prompts/` — load from file, don't hardcode in agent
- No secrets in code — use `.env` and `agent_config.yaml`

---

## Review checklist (reviewer)

- [ ] Output validates against schema
- [ ] No hardcoded API keys
- [ ] Band publish uses shared `core/band/` client
- [ ] LLM calls use shared `core/llm/` clients
- [ ] At least one test or manual Room screenshot in PR description

---

## Key documents

| Doc | Purpose |
|-----|---------|
| [PROJECT_PLAN.md](docs/PROJECT_PLAN.md) | Sprint timeline & daily tasks |
| [TEAM_CHARTER.md](docs/TEAM_CHARTER.md) | Ownership & RACI |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design |
| [LABLAB_SUBMISSION.md](docs/LABLAB_SUBMISSION.md) | Submission checklist |
| [DEMO_SCRIPT.md](docs/DEMO_SCRIPT.md) | Video script |
