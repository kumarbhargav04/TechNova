import unittest
from app.agents.verification_agent import LandmarkVerificationEngine

class TestLandmarkVerificationEngine(unittest.TestCase):
    def test_exact_proximity_score(self):
        res = LandmarkVerificationEngine.calculate_confidence(100.0, has_pincode_match=True)
        self.assertEqual(res["tier"], "High")
        self.assertGreater(res["score"], 80.0)

    def test_neighborhood_proximity_score(self):
        res = LandmarkVerificationEngine.calculate_confidence(600.0, has_pincode_match=False)
        self.assertEqual(res["tier"], "Medium")
        self.assertTrue(50.0 <= res["score"] <= 70.0)

    def test_far_proximity_score(self):
        res = LandmarkVerificationEngine.calculate_confidence(3000.0, has_pincode_match=False)
        self.assertEqual(res["tier"], "Low")
        self.assertLess(res["score"], 50.0)

    def test_negative_distance_raises(self):
        with self.assertRaises(ValueError):
            LandmarkVerificationEngine.calculate_confidence(-10.0, False)

if __name__ == "__main__":
    unittest.main()
