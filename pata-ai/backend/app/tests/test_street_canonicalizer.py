import unittest
from app.utils.street_canonicalizer import canonicalize_street_suffix

class TestStreetCanonicalizer(unittest.TestCase):
    def test_expands_abbreviations(self):
        self.assertEqual(canonicalize_street_suffix("MG Rd"), "MG Road")
        self.assertEqual(canonicalize_street_suffix("Tilak Marg"), "Tilak Marg")

    def test_handles_empty(self):
        self.assertEqual(canonicalize_street_suffix(""), "")

if __name__ == "__main__":
    unittest.main()
