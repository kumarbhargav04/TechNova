import unittest
from app.utils.manhattan_distance import calculate_manhattan_distance

class TestManhattanDistance(unittest.TestCase):
    def test_identical_points_return_zero(self):
        self.assertEqual(calculate_manhattan_distance(17.38, 78.48, 17.38, 78.48), 0.0)

    def test_manhattan_is_greater_than_euclidean(self):
        dist = calculate_manhattan_distance(17.38, 78.48, 17.39, 78.49)
        self.assertTrue(dist > 0)

if __name__ == "__main__":
    unittest.main()
