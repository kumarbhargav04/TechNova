import unittest
from datetime import datetime, timezone

try:
    from app.models.models import HealthStatusSchema
    from app.core.config import settings
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False

class TestHealthAndOperationalModels(unittest.TestCase):
    """
    Unit tests for operational health check response models and schemas.
    """
    @unittest.skipUnless(HAS_DEPS, "Pydantic required for schema tests")
    def test_health_status_schema_healthy(self):
        now_str = datetime.now(timezone.utc).isoformat()
        schema = HealthStatusSchema(
            status="healthy",
            service=settings.app_name,
            version=settings.app_version,
            database_connected=True,
            timestamp=now_str
        )
        self.assertEqual(schema.status, "healthy")
        self.assertTrue(schema.database_connected)
        self.assertEqual(schema.service, settings.app_name)

    @unittest.skipUnless(HAS_DEPS, "Pydantic required for schema tests")
    def test_health_status_schema_degraded(self):
        now_str = datetime.now(timezone.utc).isoformat()
        schema = HealthStatusSchema(
            status="degraded",
            service=settings.app_name,
            version=settings.app_version,
            database_connected=False,
            timestamp=now_str
        )
        self.assertEqual(schema.status, "degraded")
        self.assertFalse(schema.database_connected)

    @unittest.skipUnless(HAS_DEPS, "Settings required")
    def test_settings_default_values(self):
        self.assertEqual(settings.port, 8000)
        self.assertTrue(len(settings.cors_origins) >= 1)
        self.assertIn("PataAI", settings.app_name)

if __name__ == "__main__":
    unittest.main()
