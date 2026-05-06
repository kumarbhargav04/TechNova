import unittest
from app.utils.coord_precision import round_coordinates

class TestCoordPrecision(unittest.TestCase):
    def test_rounds_to_five_decimals(self):
        lat, lon = round_coordinates(17.385044234, 78.486671239, 5)
        self.assertEqual(lat, 17.38504)
        self.assertEqual(lon, 78.48667)

    def test_none_coordinates(self):
        self.assertEqual(round_coordinates(None, None), (None, None))

if __name__ == "__main__":
    unittest.main()
