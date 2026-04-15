import unittest
from app.agents.geofence import point_in_polygon

class TestGeofence(unittest.TestCase):
    def setUp(self):
        # Square polygon
        self.poly = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]

    def test_point_inside(self):
        self.assertTrue(point_in_polygon((5.0, 5.0), self.poly))

    def test_point_outside(self):
        self.assertFalse(point_in_polygon((15.0, 5.0), self.poly))

    def test_invalid_polygon(self):
        self.assertFalse(point_in_polygon((1.0, 1.0), [(0.0, 0.0), (1.0, 1.0)]))

if __name__ == "__main__":
    unittest.main()
