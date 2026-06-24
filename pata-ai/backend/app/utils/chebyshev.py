def chebyshev_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return max(abs(x2 - x1), abs(y2 - y1))
