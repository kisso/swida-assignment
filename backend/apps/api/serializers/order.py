from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import field_validator, Field
from pydantic_core.core_schema import ValidationInfo

from apps.api.serializers import Serializer
from apps.api.serializers.waypoint import WaypointSerializer


class OrderSerializer:
    class Base(Serializer):
        id: UUID
        order_number: str
        customer_name: str
        created_at: datetime

    class Detail(Base):
        waypoints: List[WaypointSerializer.Base] = Field(default=[], validate_default=True)

        @field_validator("waypoints", mode="before")
        def generate_waypoints(cls, waypoints, info: ValidationInfo):
            return waypoints.all().order_by("sequence")
