class PataAIException(Exception):
    """Base domain exception for PataAI services."""
    def __init__(self, message: str, status_code: int = 500, details: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class AddressResolutionError(PataAIException):
    """Raised when address parsing or agent pipeline resolution fails."""
    def __init__(self, message: str, details: dict = None):
        super().__init__(message=message, status_code=422, details=details)

class PincodeNotFoundError(PataAIException):
    """Raised when a postal code cannot be located in master records."""
    def __init__(self, pincode: str, details: dict = None):
        super().__init__(
            message=f"Postal PIN code '{pincode}' was not found in directory master records",
            status_code=404,
            details=details or {"pincode": pincode}
        )

class GeocodingTimeoutError(PataAIException):
    """Raised when external geocoding/OSM providers exceed deadline."""
    def __init__(self, provider: str, timeout_seconds: float):
        super().__init__(
            message=f"Geocoding service provider '{provider}' timed out after {timeout_seconds}s",
            status_code=504,
            details={"provider": provider, "timeout_seconds": timeout_seconds}
        )

class InvalidCoordinatesError(PataAIException):
    """Raised when coordinates fall outside the valid geographic bounds."""
    def __init__(self, latitude: float, longitude: float, bounds_description: str):
        super().__init__(
            message=f"Coordinates ({latitude}, {longitude}) violate geographic bounds: {bounds_description}",
            status_code=422,
            details={"latitude": latitude, "longitude": longitude, "bounds": bounds_description}
        )
