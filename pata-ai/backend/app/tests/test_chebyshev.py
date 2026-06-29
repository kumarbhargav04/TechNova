import unittest
from app.utils.chebyshev import chebyshev_distance

class TestChebyshev(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(chebyshev_distance(0, 0, 3, 5), 5.0)

if __name__ == "__main__":
    unittest.main()
