import unittest
from app.agents.metrics import PipelineMetricsCollector

class TestPipelineMetricsCollector(unittest.TestCase):
    def setUp(self):
        self.collector = PipelineMetricsCollector()

    def test_empty_stats(self):
        stats = self.collector.stats()
        self.assertEqual(stats["count"], 0)
        self.assertEqual(stats["avg_ms"], 0.0)

    def test_recorded_stats(self):
        for val in [10.0, 20.0, 30.0, 40.0, 50.0]:
            self.collector.record_duration(val)
        stats = self.collector.stats()
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["avg_ms"], 30.0)
        self.assertEqual(stats["p50_ms"], 30.0)
        self.assertGreaterEqual(stats["p95_ms"], 40.0)

    def test_negative_duration_ignored(self):
        self.collector.record_duration(-5.0)
        self.assertEqual(self.collector.stats()["count"], 0)

if __name__ == "__main__":
    unittest.main()
