# ADR-001: Band Room as System Bus

**Status:** Accepted  
**Date:** 2026-06-13  
**Owner:** HELL

## Context

Agents must collaborate with debate visibility for judges. Direct Python calls between agents would hide deliberation from Band.

## Decision

All inter-agent communication flows through Band Room messages (REST publish + WebSocket subscribe).

## Consequences

- Positive: Judge-verifiable debate history; deep Band integration.
- Negative: Higher latency than in-process calls.
- Mitigation: Shared `core/band/` client; Pydantic schemas at publish boundary.
