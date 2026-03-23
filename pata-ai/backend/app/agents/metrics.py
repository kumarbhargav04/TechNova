import time
from typing import Dict, Any, List

class PipelineMetricsCollector:
    """Thread-safe telemetry collector for multi-agent pipeline latency and throughput."""

    def __init__(self):
        self._samples: List[float] = []

    def record_duration(self, duration_ms: float):
        if duration_ms >= 0:
            self._samples.append(duration_ms)

    def get_percentile(self, p: float) -> float:
        if not self._samples:
            return 0.0
        sorted_samples = sorted(self._samples)
        k = (len(sorted_samples) - 1) * (p / 100.0)
        f = int(k)
        c = min(f + 1, len(sorted_samples) - 1)
        d0 = sorted_samples[f] * (c - k)
        d1 = sorted_samples[c] * (k - f)
        return round(d0 + d1, 2)

    def stats(self) -> Dict[str, Any]:
        if not self._samples:
            return {"count": 0, "avg_ms": 0.0, "p50_ms": 0.0, "p95_ms": 0.0, "p99_ms": 0.0}

        avg = sum(self._samples) / len(self._samples)
        return {
            "count": len(self._samples),
            "avg_ms": round(avg, 2),
            "p50_ms": self.get_percentile(50),
            "p95_ms": self.get_percentile(95),
            "p99_ms": self.get_percentile(99)
        }
