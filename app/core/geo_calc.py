def compute_bbox_area(min_lat: float, max_lat: float, min_lon: float, max_lon: float) -> float:
    return max(0.0, (max_lat - min_lat) * (max_lon - min_lon))
