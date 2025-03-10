from datetime import datetime
from uuid import UUID

from apps.api.serializers import Serializer
from apps.core.models import Waypoint


class WaypointSerializer:
    class Base(Serializer):
        id: UUID
        address: str
        waypoint_type: Waypoint.WaypointType
        sequence: int
        date: datetime

    class Detail(Base):
        pass
