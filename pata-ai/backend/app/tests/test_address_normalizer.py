import unittest
from app.agents.address_normalizer import expand_abbreviations

class TestAddressNormalizer(unittest.TestCase):
    def test_expand_abbreviations(self):
        raw = "Plot 40 Rd 2 Opp Metro St"
        exp = expand_abbreviations(raw)
        self.assertIn("Road", exp)
        self.assertIn("Opposite", exp)
        self.assertIn("Street", exp)

    def test_empty_string(self):
        self.assertEqual(expand_abbreviations(""), "")

if __name__ == "__main__":
    unittest.main()
