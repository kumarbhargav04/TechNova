import unittest
from app.agents.ranking_agent import haversine_distance

class TestHaversineDistance(unittest.TestCase):
    """
    Unit tests for the geospatial Haversine distance calculation and boundary edge cases.
    """
    def test_identical_coordinates_return_zero(self):
        # Charminar, Hyderabad
        lat, lon = 17.3616, 78.4747
        dist = haversine_distance(lat, lon, lat, lon)
        self.assertEqual(dist, 0.0)

    def test_none_coordinate_returns_infinity(self):
        self.assertEqual(haversine_distance(None, 78.4747, 17.3616, 78.4747), float('inf'))
        self.assertEqual(haversine_distance(17.3616, None, 17.3616, 78.4747), float('inf'))
        self.assertEqual(haversine_distance(17.3616, 78.4747, None, 78.4747), float('inf'))
        self.assertEqual(haversine_distance(17.3616, 78.4747, 17.3616, None), float('inf'))

    def test_distance_symmetry(self):
        # Hyderabad (17.3850, 78.4867) to Secunderabad (17.4399, 78.4983)
        dist_forward = haversine_distance(17.3850, 78.4867, 17.4399, 78.4983)
        dist_backward = haversine_distance(17.4399, 78.4983, 17.3850, 78.4867)
        self.assertAlmostEqual(dist_forward, dist_backward, places=5)
        # Approximate distance should be between 5.5km and 7km
        self.assertTrue(5500.0 < dist_forward < 7000.0)

    def test_small_displacement(self):
        # ~11 meters offset (0.0001 deg lat)
        dist = haversine_distance(17.3850, 78.4867, 17.3851, 78.4867)
        self.assertTrue(10.0 <= dist <= 12.0)

if __name__ == "__main__":
    unittest.main()
