import unittest
from app.utils.confidence_tier import get_confidence_tier

class TestConfidenceTier(unittest.TestCase):
    def test_tier_mapping(self):
        self.assertEqual(get_confidence_tier(92.5), "HIGH_CONFIDENCE")
        self.assertEqual(get_confidence_tier(72.0), "MEDIUM_CONFIDENCE")
        self.assertEqual(get_confidence_tier(45.0), "LOW_CONFIDENCE_REVIEW_REQUIRED")

if __name__ == "__main__":
    unittest.main()
