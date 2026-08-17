# ADR-003: Composite Database Indexing Strategy for Postal Zones

## Status
Accepted

## Decision
Create composite B-tree indexes on `(state, district, pincode)` and spatial bounding boxes on postal coordinates `(latitude, longitude)`.
