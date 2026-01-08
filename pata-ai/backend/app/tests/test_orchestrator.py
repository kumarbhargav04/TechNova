import unittest
from app.agents.orchestrator import MultiAgentOrchestrator

class TestMultiAgentOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orch = MultiAgentOrchestrator()

    def test_run_stage_success(self):
        res = self.orch.run_stage("parse", lambda x: x.strip().upper(), "  hyderabad  ")
        self.assertEqual(res, "HYDERABAD")
        self.assertIn("parse", self.orch.stage_timings)
        self.assertGreater(len(self.orch.audit_log), 0)

    def test_run_stage_failure_propagates(self):
        def buggy():
            raise ValueError("Invalid address token")
        with self.assertRaises(RuntimeError):
            self.orch.run_stage("invalid_op", buggy)
        self.assertIn("invalid_op_failure", self.orch.stage_timings)

    def test_summary_aggregation(self):
        self.orch.record_stage("s1", 0.05)
        self.orch.record_stage("s2", 0.02)
        summary = self.orch.get_summary()
        self.assertEqual(summary["events_count"], 2)
        self.assertAlmostEqual(summary["total_latency_ms"], 70.0, places=1)

if __name__ == "__main__":
    unittest.main()
