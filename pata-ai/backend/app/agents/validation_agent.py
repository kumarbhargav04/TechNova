from enum import Enum
from typing import Dict, Any, Optional
from app.agents.ranking_agent import haversine_distance
from app.agents.types import EvidenceCallback, SelfCheckResult

class RiskLevel(str, Enum):
    NONE = "NONE"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class DistanceThresholds:
    HIGH_RISK_METERS: float = 5000.0
    MODERATE_RISK_METERS: float = 2500.0
    CONFIDENCE_PASS_THRESHOLD: float = 70.0
    HIGH_RISK_PENALTY: float = 25.0
    MODERATE_RISK_PENALTY: float = 10.0
    CITY_MISMATCH_PENALTY: float = 15.0

    # Indian subcontinent geographic bounding box
    INDIA_LAT_MIN: float = 6.0
    INDIA_LAT_MAX: float = 38.0
    INDIA_LON_MIN: float = 68.0
    INDIA_LON_MAX: float = 98.0

def validate_coordinates_in_india(latitude: Optional[float], longitude: Optional[float]) -> bool:
    """
    Validates whether the given coordinate pair falls within the geographic bounding box of India.
    """
    if latitude is None or longitude is None:
        return False
    return (
        DistanceThresholds.INDIA_LAT_MIN <= latitude <= DistanceThresholds.INDIA_LAT_MAX and
        DistanceThresholds.INDIA_LON_MIN <= longitude <= DistanceThresholds.INDIA_LON_MAX
    )

def self_check(
    candidate: Optional[Dict[str, Any]], 
    parsed_address: Dict[str, Any], 
    pincode_info: Dict[str, Any], 
    evidence_callback: EvidenceCallback
) -> Dict[str, Any]:
    """
    Self-Check Agent (Agent 7).
    Validates logical consistency and generates warnings if confidence is low or coordinates are suspect.
    """
    risk_level = RiskLevel.NONE
    risk_warning = None
    confidence = candidate.get("confidence", 0.0) if candidate else 0.0
    
    # 0. Validate coordinates fall within Indian geographic bounds
    if candidate and candidate.get("latitude") is not None and candidate.get("longitude") is not None:
        if not validate_coordinates_in_india(candidate["latitude"], candidate["longitude"]):
            confidence = 10.0
            risk_level = RiskLevel.CRITICAL
            risk_warning = f"Critical Risk: Coordinates ({candidate['latitude']}, {candidate['longitude']}) fall outside Indian geographic territory."
            evidence_callback("Self Check Agent", "Coordinates fall outside Indian bounding box boundaries", 0.0)
            return {
                "confidence": confidence,
                "risk_warning": risk_warning,
                "risk_level": risk_level.value,
                "is_safe": False
            }

    # 1. Check distance between top candidate and pincode centroid
    if candidate and pincode_info.get("latitude"):
        dist = haversine_distance(
            candidate["latitude"], 
            candidate["longitude"], 
            pincode_info["latitude"], 
            pincode_info["longitude"]
        )
        
        # If the landmark is more than 5km from the pincode centroid, it's highly suspicious!
        if dist > DistanceThresholds.HIGH_RISK_METERS:
            confidence = max(confidence - DistanceThresholds.HIGH_RISK_PENALTY, 30.0)
            risk_level = RiskLevel.HIGH
            risk_warning = f"High Risk: Resolved landmark is {int(dist/1000)}km away from the verified pincode centroid. The delivery address might be incorrect."
            evidence_callback("Self Check Agent", f"Detected distance mismatch: landmark is {int(dist)}m away from pincode centroid", 0.3)
        elif dist > DistanceThresholds.MODERATE_RISK_METERS:
            confidence = max(confidence - DistanceThresholds.MODERATE_RISK_PENALTY, 50.0)
            risk_level = RiskLevel.MODERATE
            risk_warning = f"Moderate Risk: Landmark is {int(dist)}m away from the pincode centroid."
            evidence_callback("Self Check Agent", "Landmark distance slightly high compared to pincode centroid", 0.7)
        else:
            evidence_callback("Self Check Agent", "Geospatial logical check passed: Landmark is close to pincode center", 1.0)
            
    # 2. Check for city mismatch
    if parsed_address.get("city") and pincode_info.get("district"):
        city = str(parsed_address["city"]).lower()
        district = str(pincode_info["district"]).lower()
        if city not in district and district not in city:
            confidence = max(confidence - DistanceThresholds.CITY_MISMATCH_PENALTY, 40.0)
            risk_level = RiskLevel.HIGH
            risk_warning = f"High Risk: City mismatch. Address mentions '{parsed_address['city']}' but pincode resolves to '{pincode_info['district']}'."
            evidence_callback("Self Check Agent", f"City/District mismatch detected: {city} vs {district}", 0.2)

    # 3. Check for low confidence threshold
    if confidence < DistanceThresholds.CONFIDENCE_PASS_THRESHOLD:
        if not risk_warning:
            risk_warning = "Low Confidence: Could not verify a matching physical landmark close to the pincode centroid. Human confirmation recommended."
        evidence_callback("Self Check Agent", "Confidence fell below threshold. Flagging as Need Confirmation.", 0.5)

    return {
        "confidence": confidence,
        "risk_warning": risk_warning,
        "risk_level": risk_level.value,
        "is_safe": confidence >= DistanceThresholds.CONFIDENCE_PASS_THRESHOLD
    }
