import unittest
from app.agents.llm_client import calculate_backoff_delay, validate_json_response

class TestLLMClientUtils(unittest.TestCase):
    def test_backoff_initial_attempt(self):
        delay = calculate_backoff_delay(0, base_delay=0.5, max_delay=4.0)
        self.assertEqual(delay, 0.5)

    def test_backoff_growth(self):
        d1 = calculate_backoff_delay(1, base_delay=0.5, max_delay=4.0)
        d2 = calculate_backoff_delay(2, base_delay=0.5, max_delay=4.0)
        self.assertEqual(d1, 1.0)
        self.assertEqual(d2, 2.0)

    def test_backoff_max_delay_cap(self):
        delay = calculate_backoff_delay(10, base_delay=0.5, max_delay=4.0)
        self.assertEqual(delay, 4.0)

    def test_validate_valid_json(self):
        payload = '{"status": "ok", "confidence": 0.95}'
        parsed = validate_json_response(payload)
        self.assertEqual(parsed["status"], "ok")
        self.assertEqual(parsed["confidence"], 0.95)

    def test_validate_empty_string_raises(self):
        with self.assertRaises(ValueError):
            validate_json_response("")

    def test_validate_malformed_json_raises(self):
        with self.assertRaises(ValueError):
            validate_json_response("{invalid_json:")

if __name__ == "__main__":
    unittest.main()
