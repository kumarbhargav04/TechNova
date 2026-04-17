from typing import List, Dict, Any, Tuple

def compute_centroid(coordinates: List[Tuple[float, float]]) -> Tuple[float, float]:
    """Computes arithmetic centroid latitude and longitude from list of points."""
    if not coordinates:
        return (0.0, 0.0)
    avg_lat = sum(p[0] for p in coordinates) / len(coordinates)
    avg_lng = sum(p[1] for p in coordinates) / len(coordinates)
    return (round(avg_lat, 5), round(avg_lng, 5))
