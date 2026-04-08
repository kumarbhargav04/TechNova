# Pata AI REST & WebSocket API Specification

## 1. Geocode Address

**Endpoint:** `POST /api/geocode`

### Request Body
```json
{
  "address": "Plot 42, Near Ganesh Temple, Kothapet, Hyderabad, 500035",
  "enable_multi_agent": true
}
```

### Response
```json
{
  "status": "success",
  "data": {
    "query": "Plot 42, Near Ganesh Temple, Kothapet, Hyderabad, 500035",
    "pincode": "500035",
    "top_candidate": {
      "name": "Ganesh Temple",
      "latitude": 17.3719,
      "longitude": 78.5485,
      "confidence": 100.0,
      "type": "Landmark-Based Geocode",
      "source": "Local"
    },
    "risk_level": "Low",
    "latency_ms": 42.1
  }
}
```

## 2. Health & Readiness

**Endpoint:** `GET /health`

Returns HTTP 200 with service heartbeat and agent status.
