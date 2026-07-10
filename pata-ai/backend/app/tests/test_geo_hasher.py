import unittest
from app.utils.geo_hasher import encode_geohash
class TestGeohash(unittest.TestCase):
    def test_encode(self): self.assertTrue(len(encode_geohash(17.38, 78.48)) > 0)
