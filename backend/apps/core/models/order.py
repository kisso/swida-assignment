from django.db import models
from django.db.models.functions import Cast

from apps.core.models.base import BaseModel


class Order(BaseModel):
    class Meta:
        app_label = "core"
        db_table = "order"

    order_number = models.CharField(max_length=6, unique=True)
    customer_name = models.CharField(max_length=256)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self._create_order_number()

        super(Order, self).save(*args, **kwargs)

    def _create_order_number(self):
        last_id = (
            Order.all_objects.select_for_update()
            .annotate(order_number_int=Cast("order_number", output_field=models.IntegerField()))
            .aggregate(last=models.Max("order_number_int"))["last"]
        )

        if last_id is not None:
            self.order_number = str(last_id + 1).zfill(6)
        else:
            self.order_number = str(1).zfill(6)
