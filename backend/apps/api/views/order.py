from http import HTTPStatus
from uuid import UUID

from django.db import transaction
from django.utils.translation import gettext as _
from django.views import View

from apps.api.errors import ProblemDetailException, ValidationException
from apps.api.filters.order import OrderFilter
from apps.api.forms.order import OrderForm
from apps.api.responses import PaginationResponse, SingleResponse
from apps.api.serializers.order import OrderSerializer
from apps.core.models import Order


class OrderManagement(View):
    @transaction.atomic
    def post(self, request):
        form = OrderForm.Create.create_from_request(request)

        if not form.is_valid():
            raise ValidationException(request, form)

        order = Order()
        form.populate(order)
        order.save()

        return SingleResponse(request, OrderSerializer.Base.model_validate(order), status=HTTPStatus.CREATED)

    def get(self, request):
        orders = OrderFilter(
            request.GET, queryset=Order.objects.all().prefetch_related("waypoints"), request=request
        ).qs

        return PaginationResponse(request, orders, serializer=OrderSerializer.Base)


class OrderDetail(View):
    @staticmethod
    def get_order(request, order_id: UUID) -> Order:
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist as e:
            raise ProblemDetailException(request, _("Order not found"), status=HTTPStatus.NOT_FOUND, previous=e)

        return order

    def get(self, request, order_id: UUID):
        order = self.get_order(request, order_id)

        return SingleResponse(request, OrderSerializer.Base.model_validate(order))

    @transaction.atomic
    def delete(self, request, order_id: UUID):
        order = self.get_order(request, order_id)
        order.delete()

        return SingleResponse(request, status=HTTPStatus.NO_CONTENT)
