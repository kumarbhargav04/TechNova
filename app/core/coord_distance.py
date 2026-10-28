import math
def euclidean_approx(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
