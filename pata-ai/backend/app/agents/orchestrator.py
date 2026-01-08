import time
from typing import Dict, Any, List, Optional

class MultiAgentOrchestrator:
    """Coordinates address processing pipeline stages with timing telemetry."""

    def __init__(self):
        self.stage_timings: Dict[str, float] = {}
        self.audit_log: List[str] = []

    def record_stage(self, stage_name: str, duration_sec: float):
        self.stage_timings[stage_name] = round(duration_sec * 1000, 2)
        self.audit_log.append(f"Completed {stage_name} in {self.stage_timings[stage_name]}ms")

    def run_stage(self, stage_name: str, fn, *args, **kwargs) -> Any:
        start = time.perf_counter()
        try:
            result = fn(*args, **kwargs)
            duration = time.perf_counter() - start
            self.record_stage(stage_name, duration)
            return result
        except Exception as err:
            duration = time.perf_counter() - start
            self.record_stage(f"{stage_name}_failure", duration)
            raise RuntimeError(f"Stage '{stage_name}' failed: {err}") from err

    def get_summary(self) -> Dict[str, Any]:
        total_ms = sum(self.stage_timings.values())
        return {
            "total_latency_ms": round(total_ms, 2),
            "stages": dict(self.stage_timings),
            "events_count": len(self.audit_log)
        }
