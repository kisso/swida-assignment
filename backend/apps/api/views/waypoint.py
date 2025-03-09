from http import HTTPStatus
from uuid import UUID

from django.db import transaction
from django.utils.translation import gettext as _
from django.views import View

from apps.api.errors import ProblemDetailException, ValidationException
from apps.api.forms.waypoint import WaypointForm
from apps.api.responses import SingleResponse
from apps.api.serializers.waypoint import WaypointSerializer
from apps.api.views.order import OrderDetail
from apps.core.models import Waypoint


class WaypointManagement(View):
    @transaction.atomic
    def post(self, request, order_id: UUID):
        order = OrderDetail.get_order(request, order_id)

        form = WaypointForm.Create.create_from_request(request)
        if not form.is_valid():
            raise ValidationException(request, form)

        waypoint = Waypoint()
        form.populate(waypoint)
        waypoint.order = order
        waypoint.save()

        return SingleResponse(request, WaypointSerializer.Base.model_validate(waypoint), status=HTTPStatus.CREATED)


class WaypointDetail(View):
    @staticmethod
    def get_waypoint(request, waypoint_id: UUID) -> Waypoint:
        try:
            waypoint = Waypoint.objects.get(pk=waypoint_id)
        except Waypoint.DoesNotExist as e:
            raise ProblemDetailException(request, _("Waypoint not found"), status=HTTPStatus.NOT_FOUND, previous=e)

        return waypoint

    def get(self, request, waypoint_id: UUID):
        waypoint = self.get_waypoint(request, waypoint_id)

        return SingleResponse(request, WaypointSerializer.Detail.model_validate(waypoint))

    @transaction.atomic
    def delete(self, request, waypoint_id: UUID):
        waypoint = self.get_waypoint(request, waypoint_id)
        waypoint.delete()

        return SingleResponse(request, status=HTTPStatus.NO_CONTENT)
