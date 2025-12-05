import json
import logging
import sys
from datetime import datetime, timezone
from app.core.config import settings

class JSONFormatter(logging.Formatter):
    """
    Formats log records into machine-readable JSON strings for production observability.
    """
    def format(self, record: logging.LogRecord) -> str:
        log_obj = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno,
        }
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_obj)

def setup_logging(level_name: str = None) -> None:
    """
    Configures the root logger with the JSON formatter and the desired log level.
    """
    level = getattr(logging, (level_name or settings.log_level).upper(), logging.INFO)
    root = logging.getLogger()
    root.setLevel(level)

    # Clear existing handlers
    while root.handlers:
        root.handlers.pop()

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(JSONFormatter())
    root.addHandler(handler)

def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance for the given module name.
    """
    return logging.getLogger(name)
