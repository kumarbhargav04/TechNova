import unittest
from app.agents.parser_agent import extract_pincode_regex, extract_landmark_clue, tokenize_address

class TestParserAgent(unittest.TestCase):
    def test_extract_pincode_valid(self):
        text = "Plot 42, Green Park, Hyderabad 500035, India"
        self.assertEqual(extract_pincode_regex(text), "500035")

    def test_extract_pincode_invalid(self):
        text = "Plot 42, Green Park, Hyderabad 012345"
        self.assertIsNone(extract_pincode_regex(text))

    def test_extract_landmark_clue(self):
        text = "Flat 101, Opp Metro Station, MG Road, 560001"
        clue = extract_landmark_clue(text)
        self.assertIsNotNone(clue)
        self.assertIn("Opp Metro Station", clue)

    def test_tokenize_address_complete(self):
        text = "Plot 10, Near City Hospital, Ameerpet, 500016"
        res = tokenize_address(text)
        self.assertEqual(res["pincode"], "500016")
        self.assertIsNotNone(res["landmark_clue"])
        self.assertIn("Ameerpet", res["tokens"])

    def test_tokenize_empty(self):
        res = tokenize_address("")
        self.assertIsNone(res["pincode"])
        self.assertEqual(res["tokens"], [])

if __name__ == "__main__":
    unittest.main()
