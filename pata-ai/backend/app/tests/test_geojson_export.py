import unittest
from app.utils.geojson_export import to_geojson_feature

class TestGeoJsonExport(unittest.TestCase):
    def test_feature_structure(self):
        feat = to_geojson_feature("Charminar", 17.3616, 78.4747, {"confidence": 98.0})
        self.assertEqual(feat["type"], "Feature")
        self.assertEqual(feat["geometry"]["coordinates"], [78.4747, 17.3616])
        self.assertEqual(feat["properties"]["name"], "Charminar")

if __name__ == "__main__":
    unittest.main()
