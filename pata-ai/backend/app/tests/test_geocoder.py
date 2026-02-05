import unittest
from app.agents.geocoder_agent import is_within_india_bounds, GeocoderFallbackEngine

class TestGeocoderAgent(unittest.TestCase):
    def test_bounds_valid_hyderabad(self):
        self.assertTrue(is_within_india_bounds(17.3850, 78.4867))

    def test_bounds_valid_delhi(self):
        self.assertTrue(is_within_india_bounds(28.6139, 77.2090))

    def test_bounds_invalid_london(self):
        self.assertFalse(is_within_india_bounds(51.5074, -0.1278))

    def test_fallback_engine_primary_success(self):
        engine = GeocoderFallbackEngine(primary_provider=lambda q: {"latitude": 17.4, "longitude": 78.4})
        res = engine.resolve("Test Query")
        self.assertEqual(res["source"], "primary")
        self.assertFalse(res["fallback_used"])

    def test_fallback_engine_cascade_to_centroid(self):
        engine = GeocoderFallbackEngine(primary_provider=lambda q: None, osm_provider=lambda q: None)
        res = engine.resolve("Test Query", centroid_coords=(17.37, 78.54))
        self.assertEqual(res["source"], "centroid_fallback")
        self.assertTrue(res["fallback_used"])

    def test_empty_query_raises(self):
        engine = GeocoderFallbackEngine()
        with self.assertRaises(ValueError):
            engine.resolve("")

if __name__ == "__main__":
    unittest.main()
