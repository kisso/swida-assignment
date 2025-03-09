import django_filters

from apps.core.models import Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = []

    customer_name = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="date")
