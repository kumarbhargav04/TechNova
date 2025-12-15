import unittest
from app.agents.ranking_agent import rank_candidates, DEFAULT_WEIGHTS

class TestRankingAgent(unittest.TestCase):
    """
    Unit tests for candidate ranking agent scoring, penalties, and ordering.
    """
    def setUp(self):
        self.evidence_logs = []
        self.callback = lambda src, desc, score: self.evidence_logs.append((src, desc, score))

    def test_exact_landmark_scores_higher_than_distant(self):
        parsed = {"landmark": "Ganesh Temple", "locality": "Kothapet", "city": "Hyderabad"}
        pincode_info = {"pincode": "500035", "latitude": 17.3732, "longitude": 78.5476}
        landmarks = [
            # Nearby landmark
            {"name": "Ganesh Temple", "latitude": 17.3719, "longitude": 78.5485, "source": "Local", "category": "place_of_worship"},
            # Far landmark (generic name)
            {"name": "Ganesh Temple Far", "latitude": 17.4800, "longitude": 78.6000, "source": "OSM", "category": "place_of_worship"}
        ]
        lang_info = {"language": "English"}

        ranked = rank_candidates(parsed, pincode_info, landmarks, lang_info, self.callback)
        # 2 landmark candidates + 1 pincode centroid fallback
        self.assertEqual(len(ranked), 3)
        # Closer match should have higher confidence
        self.assertGreater(ranked[0]["confidence"], ranked[1]["confidence"])
        self.assertEqual(ranked[0]["name"], "Ganesh Temple")

    def test_generic_category_penalty(self):
        parsed = {"landmark": "Kothapet", "locality": "Kothapet", "city": "Hyderabad"}
        pincode_info = {"pincode": "500035", "latitude": 17.3732, "longitude": 78.5476}
        landmarks = [
            {"name": "Kothapet", "latitude": 17.3732, "longitude": 78.5476, "source": "OSM", "category": "locality"}
        ]
        lang_info = {"language": "English"}

        ranked = rank_candidates(parsed, pincode_info, landmarks, lang_info, self.callback)
        # 1 landmark candidate + 1 pincode centroid fallback
        self.assertEqual(len(ranked), 2)
        # Category penalty limits max score even with exact string match
        self.assertLessEqual(ranked[0]["confidence"], 70.0)

    def test_empty_landmarks_fallback_to_pincode_centroid(self):
        parsed = {"landmark": None, "locality": "Kothapet", "city": "Hyderabad"}
        pincode_info = {"pincode": "500035", "office": "Kothapet SO", "latitude": 17.3732, "longitude": 78.5476}
        lang_info = {"language": "English"}

        ranked = rank_candidates(parsed, pincode_info, [], lang_info, self.callback)
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0]["type"], "Pincode Centroid")
        self.assertEqual(ranked[0]["latitude"], 17.3732)

if __name__ == "__main__":
    unittest.main()
