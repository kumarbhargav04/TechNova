import time
import uuid
from typing import Dict, Any

class RequestTracingContext:
    """Generates unique correlation IDs and measures request turnaround time."""

    def __init__(self, prefix: str = "req"):
        self.prefix = prefix

    def generate_trace_id(self) -> str:
        return f"{self.prefix}_{uuid.uuid4().hex[:12]}"

    def build_timing_headers(self, start_time: float) -> Dict[str, str]:
        elapsed = (time.perf_counter() - start_time) * 1000
        return {
            "X-Response-Time-Ms": f"{elapsed:.2f}",
            "X-Trace-Engine": "pata-pipeline-v2"
        }
