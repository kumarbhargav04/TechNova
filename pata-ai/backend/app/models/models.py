from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional

class AddressResolveRequest(BaseModel):
    address: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Unstructured Indian address string containing landmarks, local spellings, etc."
    )
    user_id: Optional[int] = Field(None, description="The ID of the user submitting the request")
    target_language: Optional[str] = Field(None, max_length=50, description="Selected output translation language (supporting 100+ families)")

    @field_validator("address")
    @classmethod
    def validate_address_content(cls, v: str) -> str:
        cleaned = v.strip()
        if len(cleaned) < 3:
            raise ValueError("Address must contain at least 3 non-whitespace characters")
        return cleaned

    @field_validator("target_language")
    @classmethod
    def sanitize_language(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        cleaned = v.strip()
        return cleaned if cleaned else None


class EvidenceItem(BaseModel):
    source: str = Field(..., description="Agent or data source providing this evidence")
    description: str = Field(..., description="Human-readable explanation of the deduction or verification")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score from 0.0 to 1.0")

    model_config = ConfigDict(from_attributes=True)

class GeocodingCandidateSchema(BaseModel):
    name: str
    latitude: float
    longitude: float
    category: Optional[str] = None
    confidence: float = Field(..., ge=0.0, le=100.0)
    distance_meters: Optional[float] = None

class HealthStatusSchema(BaseModel):
    status: str
    service: str
    version: str
    database_connected: bool
    timestamp: str

class AddressResolveResponse(BaseModel):
    original_address: str
    normalized_address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    confidence: float
    evidence: List[str]
    correction_explanation: str
    risk_warning: Optional[str] = None
    latency_ms: float
    cost_inr: float = 0.05
    cost_usd: float = 0.0006
    model_used: str = "Hybrid Pipeline (Gemini Flash & Classical Solver)"
    parsed_components: Optional[dict] = None
    pois: Optional[List[dict]] = None



class PincodeDetailSchema(BaseModel):
    pincode: str
    office: str
    district: str
    state: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)

class UserSchema(BaseModel):
    id: int
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)

class BulkResolveRequest(BaseModel):
    addresses: List[str]
    user_id: Optional[int] = None

class BulkResolveItem(BaseModel):
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    confidence: float
    status: str
