def create_batch_summary(total: int, success: int, failed: int) -> dict:
    return {
        "total_requests": total,
        "successful_resolutions": success,
        "failed_resolutions": failed,
        "success_rate_pct": round((success / total) * 100, 2) if total > 0 else 0.0
    }
