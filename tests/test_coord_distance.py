import unittest
from app.core.coord_distance import euclidean_approx
class TestCoordDistance(unittest.TestCase):
    def test_dist(self):
        self.assertAlmostEqual(euclidean_approx(0.0, 0.0, 3.0, 4.0), 5.0)
