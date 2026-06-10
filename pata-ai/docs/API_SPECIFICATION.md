# REST API Specification (v1.0.0)

### POST `/api/v1/resolve`
Resolves unstructured Indian address string into geocordinates with audit trail.

**Request:**
```json
{
  "address": "Ganesh temple daggara, Kothapet 500035",
  "target_language": "en"
}
```
