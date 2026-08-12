# ADR-001: Modular Monolith vs Microservices Architecture

## Status
Accepted

## Context
TechNova Pata requires low-latency spatial queries and geospatial routing across Indian postal codes and coordinates. A distributed microservices setup introduces network serialization overhead.

## Decision
We adopt a Modular Monolith architecture within a unified FastAPI codebase. Domain boundaries are strictly enforced through decoupled modules (`app.api`, `app.core`, `app.models`, `app.services`).

## Consequences
- Single container deployment with sub-millisecond in-process function calls.
- Simplified operational observability and centralized logging.
