# ADR-004: Caching Policy and Redis TTL Hierarchy

## Status
Accepted

## Decision
Adopt a hierarchical TTL strategy:
- Master Pincode Metadata: 86,400s (24 hours).
- Spatial Bounding Boxes: 3,600s (1 hour).
- Live Agent Dispatch Status: 60s.
