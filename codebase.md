# VANGUARD - Codebase Context for Agents

This document is optimized for AI agents to quickly understand the VANGUARD repository structure, conventions, and architecture.

## Architecture Overview

VANGUARD is a Third-Party Risk Management (TPRM) auditing system built using **Band External Agents**. It operates in three main phases inside a **Band Room**:
1. **Phase A (Parallel Analysis)**: `INTAKE` ingests a PDF and publishes `IngestMessage`. `LEXIS`, `SENTINEL`, and `LEDGER` analyze the document in parallel and publish `Finding` messages.
2. **Phase B (Deliberation)**: `ARBITER` detects contradictions in findings and triggers debates using `@mentions`. `TRUTHLOCK` verifies claims against the ChromaDB RAG and gates the pipeline. `ARBITER` publishes the final `RiskScore`.
3. **Phase C (Delivery)**: `FORGE` generates `Remediation` plans for validated findings. `HERALD` aggregates everything into an `ExecutiveSummary` pushed to Streamlit, PDF, and Telegram.

## Directory Structure

```text
/home/binary/Projects/VANGUARD/
├── core/                  # Core shared logic across all agents
│   ├── schemas/           # Pydantic schemas (Single Source of Truth for communication)
│   ├── rag/               # Retrieval-Augmented Generation (PyMuPDF Extractor, ChromaDB)
│   └── llm/               # LLM clients (BaseLLMClient, FeatherlessClient)
├── tests/                 # Pytest test suite
│   ├── documents/         # Sample PDFs for testing
│   └── fixtures/          # JSON mocks for agent tests
├── agents/                # Implementation of individual Band agents (Phase A, B, C)
├── docs/                  # Architecture, Adr, Prompts and Project planning
├── dashboard/             # Streamlit UI application
└── integrations/          # External integrations (PDF Generator, Telegram/n8n)
```

## Key Modules

### 1. Schemas (`core/schemas/`)
All inter-agent communication must conform strictly to these Pydantic models.
- **messages.py**: `IngestMessage` (Published by INTAKE).
- **findings.py**: `Finding` (Published by Phase A agents), `SeverityEnum`.
- **debate.py**: `DebateMessage`, `DebateResponse`, `RiskScore`, `ValidationResult`.
- **reporting.py**: `Remediation`, `ExecutiveSummary`.

### 2. LLM Client (`core/llm/`)
- Uses `BaseLLMClient` interface.
- Default implementation is `FeatherlessClient` which wraps the OpenAI Python SDK and points to `api.featherless.ai`. 
- Model used: `deepseek-ai/DeepSeek-V4-Flash`.

### 3. RAG Pipeline (`core/rag/`)
- **extractor.py**: `DocumentExtractor` uses `fitz` (PyMuPDF) to read PDF text, compute a SHA-256 hash, and split text into chunks.
- **embeddings.py**: `ChromaManager` interacts with `chromadb`. Uses local default embeddings (`all-MiniLM-L6-v2`). Instantiated with `:memory:` during testing.

## Coding Conventions
1. **Language**: Python 3.12+ managed by `uv`.
2. **Type Hinting**: Strict type hinting is required for all functions and classes.
3. **Docstrings**: English docstrings describing intent, not just restating code. Keep comments minimal and necessary.
4. **Testing**: `pytest` is used for all tests. TDD is encouraged. Avoid external network calls in unit tests; use `unittest.mock`.
5. **Environment**: All secrets and configuration overrides must be sourced from `.env` or passed directly to constructors. Do not commit `.env`.

## Current State
- `Phase 0` and `Day 1` DEV tasks are initialized: Schemas, RAG structure, and LLM Client base implementations are present and tested.
- `uv` is configured with `pydantic`, `chromadb`, `langchain`, `pymupdf`, `pytest`, `openai`.
