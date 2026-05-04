def round_coordinates(latitude: float, longitude: float, decimals: int = 5) -> tuple:
    if latitude is None or longitude is None:
        return (None, None)
    return (round(float(latitude), decimals), round(float(longitude), decimals))
