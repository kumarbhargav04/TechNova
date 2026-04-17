import unittest
from app.agents.cluster_agent import compute_centroid

class TestClusterAgent(unittest.TestCase):
    def test_compute_centroid(self):
        points = [(10.0, 20.0), (20.0, 40.0)]
        c = compute_centroid(points)
        self.assertEqual(c, (15.0, 30.0))

    def test_empty_points(self):
        self.assertEqual(compute_centroid([]), (0.0, 0.0))

if __name__ == "__main__":
    unittest.main()
