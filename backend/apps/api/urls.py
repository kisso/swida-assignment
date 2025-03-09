from django.urls import path

from apps.api.views import order, waypoint

urlpatterns = [
    # Order
    path("orders", order.OrderManagement.as_view()),
    path("orders/<uuid:order_id>", order.OrderDetail.as_view()),
    # Waypoint
    path("orders/<uuid:order_id>/waypoints", waypoint.WaypointManagement.as_view()),
    path("waypoints/<uuid:waypoint_id>", waypoint.WaypointDetail.as_view()),
]
