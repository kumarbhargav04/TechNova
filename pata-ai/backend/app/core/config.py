import os
from typing import List
from pydantic import BaseModel, Field

class Settings(BaseModel):
    """
    Application configuration settings loaded from environment variables with safe defaults.
    """
    app_name: str = "PataAI Address Intelligence Engine"
    app_version: str = "1.0.0"
    environment: str = Field(default_factory=lambda: os.getenv("ENVIRONMENT", "development"))
    host: str = Field(default_factory=lambda: os.getenv("HOST", "0.0.0.0"))
    port: int = Field(default_factory=lambda: int(os.getenv("PORT", "8000")))
    log_level: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))

    # Database
    database_url: str = Field(default_factory=lambda: os.getenv("DATABASE_URL", "sqlite:///./pataai.db"))

    # AI & Geocoding Services
    gemini_api_key: str = Field(default_factory=lambda: os.getenv("GEMINI_API_KEY", ""))
    osm_overpass_url: str = Field(default_factory=lambda: os.getenv("OSM_OVERPASS_URL", "http://overpass-api.de/api/interpreter"))
    overpass_timeout_seconds: float = Field(default_factory=lambda: float(os.getenv("OVERPASS_TIMEOUT_SECONDS", "5.0")))

    # Security & CORS
    cors_origins: List[str] = Field(
        default_factory=lambda: [
            origin.strip()
            for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")
            if origin.strip()
        ]
    )

settings = Settings()
