from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import BaseModel


class Waypoint(BaseModel):
    class Meta:
        app_label = "core"
        db_table = "waypoint"

    class WaypointType(models.TextChoices):
        PICKUP = "pickup", _("Pickup")
        DELIVERY = "delivery", _("Delivery")

    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="waypoints")
    address = models.CharField(max_length=256)
    waypoint_type = models.CharField(max_length=8, choices=WaypointType.choices)
    date = models.DateTimeField()
    sequence = models.IntegerField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self._create_sequence()

        super(Waypoint, self).save(*args, **kwargs)

    def _create_sequence(self):
        last_id = Waypoint.objects.filter(order=self.order).aggregate(last=models.Max("sequence"))["last"]
        self.sequence = 1 if last_id is None else last_id + 1
