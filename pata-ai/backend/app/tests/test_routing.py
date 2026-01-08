import unittest
from app.agents.routing_agent import DeliveryRouteOptimizer

class TestDeliveryRouteOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = DeliveryRouteOptimizer(avg_speed_kmh=30.0)

    def test_haversine_zero_distance(self):
        dist = self.optimizer.haversine_km(17.3850, 78.4867, 17.3850, 78.4867)
        self.assertEqual(dist, 0.0)

    def test_haversine_known_distance(self):
        # Hyderabad to Secunderabad ~ 8-9 km
        dist = self.optimizer.haversine_km(17.3850, 78.4867, 17.4399, 78.4983)
        self.assertTrue(6.0 < dist < 12.0)

    def test_estimate_eta(self):
        eta = self.optimizer.estimate_eta_minutes(15.0)
        self.assertEqual(eta, 30.0)  # 15km at 30km/h = 30 mins

    def test_plan_empty_waypoints(self):
        res = self.optimizer.plan_sequence((17.38, 78.48), [])
        self.assertEqual(res["total_distance_km"], 0.0)
        self.assertEqual(len(res["sequence"]), 0)

    def test_plan_sequence_ordering(self):
        origin = (17.3800, 78.4800)
        wps = [
            {"id": "far", "latitude": 17.4500, "longitude": 78.5500},
            {"id": "near", "latitude": 17.3850, "longitude": 78.4850},
        ]
        res = self.optimizer.plan_sequence(origin, wps)
        self.assertEqual(len(res["sequence"]), 2)
        self.assertEqual(res["sequence"][0]["id"], "near")
        self.assertEqual(res["sequence"][1]["id"], "far")

if __name__ == "__main__":
    unittest.main()
