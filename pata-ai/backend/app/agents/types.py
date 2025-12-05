from typing import TypedDict, Optional, List, Callable, Any

# Type alias for evidence tracking callback: (source: str, description: str, score: float) -> None
EvidenceCallback = Callable[[str, str, float], None]

class ParsedAddress(TypedDict, total=False):
    landmark: Optional[str]
    locality: Optional[str]
    city: Optional[str]
    pincode: Optional[str]
    state: Optional[str]

class PincodeInfo(TypedDict, total=False):
    pincode: Optional[str]
    office: Optional[str]
    district: Optional[str]
    state: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    is_corrected: bool

class LandmarkCandidate(TypedDict, total=False):
    name: str
    category: Optional[str]
    latitude: float
    longitude: float
    resolved_locality: Optional[str]
    source: Optional[str]

class RankedCandidate(TypedDict, total=False):
    name: str
    latitude: float
    longitude: float
    confidence: float
    category: Optional[str]
    source: Optional[str]
    distance_to_centroid: Optional[float]

class SelfCheckResult(TypedDict):
    confidence: float
    risk_warning: Optional[str]
    is_safe: bool
