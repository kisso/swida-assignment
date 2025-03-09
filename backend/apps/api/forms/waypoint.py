from django.forms import fields
from django_api_forms import Form, EnumField

from apps.core.models import Waypoint


class WaypointForm:
    class Create(Form):
        address = fields.CharField(required=True)
        waypoint_type = EnumField(enum=Waypoint.WaypointType, required=True)
        date = fields.DateTimeField(required=True)
