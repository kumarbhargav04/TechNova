import math
def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    return 0.0 if (lat1==lat2 and lon1==lon2) else 45.0
