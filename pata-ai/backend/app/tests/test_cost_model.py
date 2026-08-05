import unittest
from app.utils.cost_model import calculate_resolution_cost
class TestCost(unittest.TestCase):
    def test_cost(self): self.assertGreater(calculate_resolution_cost(100), 0)
