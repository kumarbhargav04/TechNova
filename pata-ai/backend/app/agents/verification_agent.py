from typing import Dict, Any, List

class LandmarkVerificationEngine:
    """Calculates landmark proximity confidence score based on physical distance threshold."""

    EXACT_THRESHOLD_METERS = 250.0
    NEIGHBORHOOD_THRESHOLD_METERS = 1000.0

    @classmethod
    def calculate_confidence(cls, distance_meters: float, has_pincode_match: bool) -> Dict[str, Any]:
        if distance_meters < 0:
            raise ValueError("Distance cannot be negative")

        score = 0.0
        if distance_meters <= cls.EXACT_THRESHOLD_METERS:
            score = 90.0 - (distance_meters / cls.EXACT_THRESHOLD_METERS) * 15.0
            tier = "High"
        elif distance_meters <= cls.NEIGHBORHOOD_THRESHOLD_METERS:
            score = 70.0 - (distance_meters / cls.NEIGHBORHOOD_THRESHOLD_METERS) * 20.0
            tier = "Medium"
        else:
            score = max(20.0, 50.0 - (distance_meters / 5000.0) * 30.0)
            tier = "Low"

        if has_pincode_match:
            score = min(100.0, score + 10.0)

        return {
            "score": round(score, 1),
            "tier": tier,
            "distance_meters": distance_meters,
            "pincode_matched": has_pincode_match
        }
