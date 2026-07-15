import unittest
from app.utils.phonetic_matcher import phonetic_similarity
class TestPhonetic(unittest.TestCase):
    def test_sim(self): self.assertGreater(phonetic_similarity('kothapet', 'kotapet'), 0.8)
