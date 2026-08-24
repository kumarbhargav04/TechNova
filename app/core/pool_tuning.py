"""Database connection pool dynamic tuning helper."""

def compute_optimal_pool_size(cpu_cores: int, max_connections: int, reserve_ratio: float = 0.2) -> int:
    """Calculates optimal database connection pool size based on CPU cores and database limits."""
    if cpu_cores <= 0:
        cpu_cores = 1
    base_pool = (cpu_cores * 2) + 1
    safe_max = int(max_connections * (1.0 - reserve_ratio))
    return max(2, min(base_pool, safe_max))
