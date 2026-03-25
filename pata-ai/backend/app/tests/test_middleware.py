import time
import unittest
from app.api.middleware import RequestTracingContext

class TestRequestTracingContext(unittest.TestCase):
    def setUp(self):
        self.ctx = RequestTracingContext(prefix="pata")

    def test_trace_id_format(self):
        tid = self.ctx.generate_trace_id()
        self.assertTrue(tid.startswith("pata_"))
        self.assertEqual(len(tid), 5 + 12)

    def test_timing_headers(self):
        start = time.perf_counter()
        time.sleep(0.01)
        headers = self.ctx.build_timing_headers(start)
        self.assertIn("X-Response-Time-Ms", headers)
        self.assertEqual(headers["X-Trace-Engine"], "pata-pipeline-v2")
        self.assertGreater(float(headers["X-Response-Time-Ms"]), 0.0)

if __name__ == "__main__":
    unittest.main()
