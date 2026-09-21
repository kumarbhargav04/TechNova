import unittest
from app.core.geo_calc import compute_bbox_area
class TestGeoCalc(unittest.TestCase):
    def test_area(self):
        self.assertEqual(compute_bbox_area(10.0, 12.0, 70.0, 73.0), 6.0)
