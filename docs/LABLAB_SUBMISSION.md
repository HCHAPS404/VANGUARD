# VANGUARD — Lablab.ai Submission Pack

**Event:** Band of Agents Hackathon  
**Deadline:** 19 June 2026  
**Owner:** Juliana (R) · HELL (A)

---

## Project identity

| Field | Value |
|-------|-------|
| **Title** | Vanguard |
| **Tagline** | AI due diligence panel for law firm vendor audits |
| **Short description** (≤140 chars) | Multi-agent AI system that automates third-party vendor compliance audits for law firms using Band's collaborative debate infrastructure |
| **Long description** | See `docs/PROJECT_PLAN.md` + README Problem/Solution sections |
| **Team** | INZERM — DEV, Juliana, HELL |

---

## Technology tags

```
Band, Featherless AI, AI/ML API, Python, RAG, LangChain, ChromaDB, Streamlit, n8n, PyMuPDF
```

---

## Submission checklist

### Code & repository

- [ ] Public GitHub repo: `https://github.com/HCHAPS404/VANGUARD`
- [ ] `main` branch clean — no secrets committed
- [ ] README installable in under 15 minutes
- [ ] All 8 agents have code in `agents/<name>/`
- [ ] Band Room URL in README

### Band integration (judge verification)

- [ ] 8 External Agents registered on band.ai
- [ ] Room history shows debate with @mentions
- [ ] INTAKE → Phase A → ARBITER → TRUTHLOCK visible in Room
- [ ] Room screenshot in slides

### Demo assets

- [ ] Video (3–5 min) — `docs/DEMO_SCRIPT.md`
- [ ] Slides — problem, solution, architecture, screenshots
- [ ] Cover image (1280×720 PNG)
- [ ] Streamlit Cloud URL
- [ ] Telegram screenshot with Risk Score

### Platform form

- [ ] Title, short + long description, tags
- [ ] Cover, video, slides, GitHub link, demo URL
- [ ] Team members listed

---

## Judge criteria mapping

| Criterion | Evidence |
|-----------|----------|
| Technology | Band Room debate, @mentions, WebSocket |
| Originality | TRUTHLOCK real-time invalidation |
| Business value | 40–120h manual → minutes automated |
| Presentation | 8 agents, 3 phases, architecture diagram |

---

## Smoke test (19/06 morning)

```powershell
uv sync
docker compose -f docker/docker-compose.yml up -d
uv run python scripts/run_pipeline.py --pdf tests/documents/sample.pdf
```

Verify: Band Room thread · Telegram message · Streamlit session · PDF output

**Owner:** DEV (run) · HELL (sign-off)
