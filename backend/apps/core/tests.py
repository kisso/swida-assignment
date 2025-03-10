from django.test import TestCase

from apps.core.models import Order, Waypoint


class ModelTest(TestCase):
    def test_create_order_and_waypoint(self):
        """Test creating an order and linking a waypoint to it."""

        # Create Order
        order = Order.objects.create(customer_name="swida innovative", date="2025-03-10T12:00:00Z")

        self.assertEqual(order.customer_name, "swida innovative")

        # Create Waypoint linked to the Order
        waypoint = Waypoint.objects.create(order=order, address="Bratislava, Slovakia", waypoint_type="pickup")

        self.assertEqual(waypoint.address, "Bratislava, Slovakia")
        self.assertEqual(waypoint.waypoint_type, "pickup")
        self.assertEqual(waypoint.order, order)
