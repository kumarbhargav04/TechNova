import math
from typing import List, Dict, Any, Tuple

class DeliveryRouteOptimizer:
    """Optimizes last-mile delivery waypoints using nearest-neighbor heuristic."""

    def __init__(self, avg_speed_kmh: float = 25.0):
        self.avg_speed_kmh = avg_speed_kmh

    @staticmethod
    def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        r = 6371.0
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (math.sin(delta_phi / 2) ** 2 +
             math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * c

    def estimate_eta_minutes(self, distance_km: float) -> float:
        """Estimates transit time in minutes given distance in kilometers."""
        if distance_km <= 0:
            return 0.0
        hours = distance_km / self.avg_speed_kmh
        return round(hours * 60, 1)

    def plan_sequence(self, origin: Tuple[float, float], waypoints: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Plans greedy nearest neighbor sequence from origin through waypoints."""
        if not waypoints:
            return {"sequence": [], "total_distance_km": 0.0, "estimated_minutes": 0.0}

        unvisited = list(waypoints)
        curr_lat, curr_lon = origin
        sequence = []
        total_dist = 0.0

        while unvisited:
            best_idx = 0
            best_dist = float("inf")
            for i, wp in enumerate(unvisited):
                dist = self.haversine_km(curr_lat, curr_lon, wp["latitude"], wp["longitude"])
                if dist < best_dist:
                    best_dist = dist
                    best_idx = i

            next_wp = unvisited.pop(best_idx)
            total_dist += best_dist
            curr_lat, curr_lon = next_wp["latitude"], next_wp["longitude"]
            sequence.append({**next_wp, "leg_distance_km": round(best_dist, 2)})

        return {
            "sequence": sequence,
            "total_distance_km": round(total_dist, 2),
            "estimated_minutes": self.estimate_eta_minutes(total_dist)
        }
