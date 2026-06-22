import unittest
from app.utils.poi_cache import SimplePoiCache

class TestPoiCache(unittest.TestCase):
    def test_eviction(self):
        cache = SimplePoiCache(max_size=2)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("c"), 3)

if __name__ == "__main__":
    unittest.main()
