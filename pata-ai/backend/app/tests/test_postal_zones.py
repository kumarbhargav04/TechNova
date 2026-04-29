import unittest
from app.utils.postal_zones import get_postal_zone_name

class TestPostalZones(unittest.TestCase):
    def test_southern_zone_prefix(self):
        self.assertIn("Telangana", get_postal_zone_name("500035"))

    def test_delhi_northern_prefix(self):
        self.assertIn("Delhi", get_postal_zone_name("110001"))

    def test_invalid_pincode_returns_unknown(self):
        self.assertEqual(get_postal_zone_name("invalid"), "Unknown Postal Zone")
        self.assertEqual(get_postal_zone_name(""), "Unknown Postal Zone")

if __name__ == "__main__":
    unittest.main()
