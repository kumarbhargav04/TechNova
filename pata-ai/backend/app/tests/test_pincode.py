import unittest
from app.agents.pincode_agent import clean_locality_string

class TestPincodeAgent(unittest.TestCase):
    """
    Unit tests for postal code agent text normalization and noise word stripping.
    """
    def test_clean_locality_strips_prepositions(self):
        cases = [
            ("Near Kothapet", "kothapet"),
            ("Opposite Hanuman Temple", "hanuman temple"),
            ("Behind Post Office", "post office"),
            ("Beside Metro Station", "metro station"),
            ("Adjacent to Cyber Towers", "cyber towers"),
            ("Close to Market", "market"),
        ]
        for raw, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(clean_locality_string(raw), expected)

    def test_clean_locality_empty_or_none(self):
        self.assertEqual(clean_locality_string(None), "")
        self.assertEqual(clean_locality_string(""), "")
        self.assertEqual(clean_locality_string("   "), "")

    def test_clean_locality_pure_noise_word(self):
        self.assertEqual(clean_locality_string("Near"), "")
        self.assertEqual(clean_locality_string("Opposite"), "")

if __name__ == "__main__":
    unittest.main()
