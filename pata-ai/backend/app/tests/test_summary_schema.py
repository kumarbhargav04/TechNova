import unittest
from app.utils.summary_schema import create_batch_summary

class TestSummarySchema(unittest.TestCase):
    def test_rate_calculation(self):
        summary = create_batch_summary(100, 95, 5)
        self.assertEqual(summary["success_rate_pct"], 95.0)

if __name__ == "__main__":
    unittest.main()
