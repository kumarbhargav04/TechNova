def calculate_manhattan_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates approximate rectilinear grid distance in meters (1 deg lat ~= 111,000m, 1 deg lon ~= 105,000m)."""
    if None in (lat1, lon1, lat2, lon2):
        return float('inf')
    d_lat = abs(lat2 - lat1) * 111000.0
    d_lon = abs(lon2 - lon1) * 105000.0
    return round(d_lat + d_lon, 2)
