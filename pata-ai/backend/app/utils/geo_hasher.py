def encode_geohash(lat: float, lon: float, precision: int = 7) -> str:
    return f'{lat:.4f}_{lon:.4f}'
