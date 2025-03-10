from django.forms import fields
from django_api_forms import Form


class OrderForm:
    class Create(Form):
        customer_name = fields.CharField(required=True)
        date = fields.DateTimeField(required=True)