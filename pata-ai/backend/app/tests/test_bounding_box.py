import unittest
from app.agents.validation_agent import validate_coordinates_in_india, self_check, RiskLevel

class TestBoundingBoxValidation(unittest.TestCase):
    """
    Unit tests for geographic territory bounding box validation.
    """
    def test_major_indian_cities_are_valid(self):
        cities = [
            ("Hyderabad", 17.3850, 78.4867),
            ("New Delhi", 28.6139, 77.2090),
            ("Mumbai", 19.0760, 72.8777),
            ("Bengaluru", 12.9716, 77.5946),
            ("Kolkata", 22.5726, 88.3639),
            ("Chennai", 13.0827, 80.2707),
        ]
        for name, lat, lon in cities:
            with self.subTest(city=name):
                self.assertTrue(validate_coordinates_in_india(lat, lon), f"{name} should be inside India bounds")

    def test_out_of_bounds_foreign_coordinates(self):
        foreign_points = [
            ("London", 51.5074, -0.1278),
            ("New York", 40.7128, -74.0060),
            ("Tokyo", 35.6762, 139.6503),
            ("Sydney", -33.8688, 151.2093),
        ]
        for name, lat, lon in foreign_points:
            with self.subTest(place=name):
                self.assertFalse(validate_coordinates_in_india(lat, lon), f"{name} should be outside India bounds")

    def test_none_coordinates(self):
        self.assertFalse(validate_coordinates_in_india(None, None))
        self.assertFalse(validate_coordinates_in_india(17.3850, None))
        self.assertFalse(validate_coordinates_in_india(None, 78.4867))

    def test_self_check_flags_critical_risk_for_out_of_bounds(self):
        candidate = {"name": "London Eye", "latitude": 51.5074, "longitude": -0.1278, "confidence": 95.0}
        logs = []
        result = self_check(candidate, {}, {}, lambda src, desc, score: logs.append(desc))
        self.assertFalse(result["is_safe"])
        self.assertEqual(result["risk_level"], RiskLevel.CRITICAL.value)
        self.assertIn("Critical Risk", result["risk_warning"])

if __name__ == "__main__":
    unittest.main()
