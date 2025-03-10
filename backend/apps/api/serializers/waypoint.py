from uuid import UUID

from apps.api.serializers import Serializer
from apps.core.models import Waypoint


class WaypointSerializer:
    class Base(Serializer):
        id: UUID
        address: str
        waypoint_type: Waypoint.WaypointType
        sequence: int

    class Detail(Base):
        pass
