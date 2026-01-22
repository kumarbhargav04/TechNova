from typing import Optional, Dict, Any, Tuple

INDIA_LAT_RANGE = (6.0, 38.0)
INDIA_LNG_RANGE = (68.0, 98.0)

def is_within_india_bounds(latitude: float, longitude: float) -> bool:
    """Verifies whether GPS coordinates fall within geographical bounds of India."""
    return (INDIA_LAT_RANGE[0] <= latitude <= INDIA_LAT_RANGE[1] and
            INDIA_LNG_RANGE[0] <= longitude <= INDIA_LNG_RANGE[1])

class GeocoderFallbackEngine:
    """Encapsulates geocoding cascade with primary, secondary, and centroid fallbacks."""

    def __init__(self, primary_provider=None, osm_provider=None):
        self.primary = primary_provider
        self.osm = osm_provider

    def resolve(self, query: str, centroid_coords: Optional[Tuple[float, float]] = None) -> Dict[str, Any]:
        if not query or not query.strip():
            raise ValueError("Query string cannot be empty")

        if self.primary:
            res = self.primary(query)
            if res and is_within_india_bounds(res.get("latitude", 0), res.get("longitude", 0)):
                return {**res, "source": "primary", "fallback_used": False}

        if self.osm:
            res = self.osm(query)
            if res and is_within_india_bounds(res.get("latitude", 0), res.get("longitude", 0)):
                return {**res, "source": "osm", "fallback_used": True}

        if centroid_coords and is_within_india_bounds(centroid_coords[0], centroid_coords[1]):
            return {
                "latitude": centroid_coords[0],
                "longitude": centroid_coords[1],
                "source": "centroid_fallback",
                "fallback_used": True
            }

        return {"error": "Geocoding failed across all providers", "fallback_used": True}
