import unittest
from app.utils.bearing_calc import calculate_bearing
class TestBearing(unittest.TestCase):
    def test_zero(self): self.assertEqual(calculate_bearing(10, 10, 10, 10), 0.0)
