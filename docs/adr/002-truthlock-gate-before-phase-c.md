# ADR-002: TRUTHLOCK Gate Before Phase C

**Status:** Accepted  
**Date:** 2026-06-15  
**Owner:** HELL

## Context

Legal audit outputs with hallucinated claims create juridical liability.

## Decision

`AuditSession` blocks transition to `REMEDIATING` while unsupported ValidationResults exist. FORGE runs only after `session.phase == VERIFIED`.

## Consequences

- Positive: Zero unverified claims in executive report.
- Negative: Pipeline may stall if TRUTHLOCK is too aggressive.
- Mitigation: Tunable similarity threshold for demo tuning.
