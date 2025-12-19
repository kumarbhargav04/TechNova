# PataAI System Architecture & Multi-Agent Dataflow

PataAI is an address intelligence engine designed to parse, normalize, and geocode unstructured, colloquial Indian delivery addresses.

---

## 1. Multi-Agent Pipeline Overview

Colloquial Indian addresses typically lack clean hierarchical numbering and instead rely on landmarks, colloquial phonetics, and local transliterations. PataAI resolves these through a staged 7-agent pipeline:

```
[Raw Address Input]
         │
         ▼
 1. Language Agent (Script detection & phonetic transliteration)
         │
         ▼
 2. Parser Agent (Regex & LLM entity extraction)
         │
         ▼
 3. Pincode Agent (Directory verification & centroid lookup)
         │
         ▼
 4. Landmark Agent (OSM Overpass live query & local cache fallback)
         │
         ▼
 5. Routing Agent (Road network distance & path feasibility)
         │
         ▼
 6. Ranking Agent (Multi-criteria weighted scoring formula)
         │
         ▼
 7. Self-Check Agent (Geospatial sanity bounds & risk warnings)
         │
         ▼
[Normalized Geocode + Audit Trail]
```

---

## 2. Agent Responsibilities & Algorithms

### Agent 1: Language Agent
- **Unicode Script Analysis**: Uses regular expression Unicode range scans covering all 22 Eighth-Schedule Indian languages (Telugu, Devanagari, Tamil, Kannada, Bengali, etc.).
- **Colloquial Normalization**: Translates common transliterated prepositions (`daggara` → near, `samne` → opposite, `pakhare` → near) into standard English spatial tokens.

### Agent 2: Parser Agent
- Extracts structural address components: building/flat number, landmark phrase, street/lane name, locality, city, and 6-digit postal PIN code.

### Agent 3: Pincode Agent
- Resolves PIN codes against the `pincode_master` directory.
- If a PIN code is missing or mismatched against the parsed city, it performs a phonetic locality search to suggest the correct delivery post office centroid.

### Agent 4: Landmark Agent
- Queries OpenStreetMap (OSM) Overpass API within a 2.5km radial bounding circle around the PIN code centroid.
- Falls back to pre-seeded local landmark cache (`landmark_cache`) when OSM is offline or times out.

### Agent 5: Routing Agent
- Validates road network accessibility and estimated last-mile transit feasibility between landmark and postal centroid.

### Agent 6: Ranking Agent
- Scores candidate coordinates using a deterministic weighted formula:
  $$\text{Score} = S_{\text{landmark}} (40\%) + S_{\text{pincode}} (25\%) + S_{\text{locality}} (20\%) + S_{\text{language}} (15\%)$$
- Penalizes generic administrative boundary centroids (e.g., matching a whole district name instead of a specific physical landmark).

### Agent 7: Self-Check Agent
- **Geographic Bounds**: Validates that all candidate coordinates fall strictly inside Indian territory (Lat: 6.0° to 38.0° N, Lon: 68.0° to 98.0° E).
- **Proximity Sanity Check**: Calculates the Haversine distance between the top landmark and the postal centroid. Distances exceeding 5.0 km trigger a `High Risk` flag to protect against misplaced deliveries.

---

## 3. Operational Reliability & Resilience

- **Fail-Safe Fallback**: If external AI or map APIs fail, the pipeline falls back gracefully to deterministic rule-based algorithms and verified postal centroids.
- **Connection Health**: Database connection pool configured with `pool_pre_ping=True` and operational probes at `/api/v1/healthz`.
- **Structured Telemetry**: Standardized JSON log events with correlation identifiers for all geocoding requests.
