from django.forms import ModelForm
from .models import Order,Product,Customer,Tag


# order forms
class OrderForms(ModelForm):
    class Meta:
        model=Order
        fields="__all__"