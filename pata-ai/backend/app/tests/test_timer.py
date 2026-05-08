import unittest
import time
from app.utils.timer import ExecutionTimer

class TestExecutionTimer(unittest.TestCase):
    def test_measures_elapsed_duration(self):
        timer = ExecutionTimer()
        time.sleep(0.01)
        elapsed = timer.elapsed_ms()
        self.assertTrue(elapsed >= 8.0)

if __name__ == "__main__":
    unittest.main()
