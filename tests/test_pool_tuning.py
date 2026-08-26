import unittest
from app.core.pool_tuning import compute_optimal_pool_size

class TestPoolTuning(unittest.TestCase):
    def test_default_quad_core(self):
        size = compute_optimal_pool_size(4, 100)
        self.assertEqual(size, 9)

    def test_low_max_connections_clamped(self):
        size = compute_optimal_pool_size(8, 10)
        self.assertEqual(size, 8)

    def test_minimum_floor(self):
        size = compute_optimal_pool_size(0, 5)
        self.assertGreaterEqual(size, 2)

if __name__ == '__main__':
    unittest.main()
