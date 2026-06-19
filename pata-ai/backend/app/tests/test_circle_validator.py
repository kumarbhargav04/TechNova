import unittest
from app.utils.circle_validator import is_valid_postal_circle

class TestCircleValidator(unittest.TestCase):
    def test_valid_digits(self):
        self.assertTrue(is_valid_postal_circle("5"))
        self.assertTrue(is_valid_postal_circle("1"))

    def test_invalid_digits(self):
        self.assertFalse(is_valid_postal_circle("0"))
        self.assertFalse(is_valid_postal_circle("x"))

if __name__ == "__main__":
    unittest.main()
