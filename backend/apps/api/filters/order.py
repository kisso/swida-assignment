import django_filters
from django.db.models import Q

from apps.core.models import Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = []

    text_query = django_filters.CharFilter(method="filter_by_order_and_name")
    date = django_filters.DateFilter(field_name="date", lookup_expr="date")

    def filter_by_order_and_name(self, queryset, name, value):
        return queryset.filter(Q(customer_name__icontains=value) | Q(order_number__icontains=value))
