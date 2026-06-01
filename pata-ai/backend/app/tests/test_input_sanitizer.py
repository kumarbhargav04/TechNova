import unittest
from app.utils.input_sanitizer import sanitize_address_input

class TestInputSanitizer(unittest.TestCase):
    def test_strips_html_tags(self):
        cleaned = sanitize_address_input("<script>alert(1)</script> Near Temple, Hyderabad")
        self.assertNotIn("<script>", cleaned)
        self.assertIn("Near Temple", cleaned)

    def test_collapses_whitespace(self):
        self.assertEqual(sanitize_address_input("Kothapet    SO"), "Kothapet SO")

if __name__ == "__main__":
    unittest.main()
