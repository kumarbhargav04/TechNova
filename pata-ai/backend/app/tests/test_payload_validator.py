import unittest
from app.utils.payload_validator import is_valid_delivery_request
class TestPayload(unittest.TestCase):
    def test_short(self): self.assertFalse(is_valid_delivery_request('abc'))
