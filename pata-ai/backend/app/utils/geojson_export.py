def to_geojson_feature(name: str, latitude: float, longitude: float, properties: dict = None) -> dict:
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude]
        },
        "properties": {
            "name": name,
            **(properties or {})
        }
    }
