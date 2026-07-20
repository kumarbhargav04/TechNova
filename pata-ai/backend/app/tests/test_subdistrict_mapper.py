import unittest
from app.utils.subdistrict_mapper import get_subdistrict
class TestSubdistrict(unittest.TestCase):
    def test_mandal(self): self.assertIn('Mandal', get_subdistrict('Uppal'))
