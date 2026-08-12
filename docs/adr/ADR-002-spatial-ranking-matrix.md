# ADR-002: Spatial Ranking Scoring Matrix and Distance Weighting

## Status
Accepted

## Decision
We implement a multi-factor ranking scoring matrix combining:
1. Haversine spherical surface distance (40% weight).
2. Postal zone tier multiplier (25% weight).
3. Office category rating (Sub Post Office vs Head Office) (20% weight).
4. Historical delivery completion rate (15% weight).
