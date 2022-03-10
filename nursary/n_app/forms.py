from django.forms import ModelForm
from django import forms
from .models import Nursary, Order


class NursaryForm(ModelForm):
    class Meta:
        model = Nursary
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # exclude = ('nursary_p',)
        fields = "__all__"
        # widgets = {
        #         'nursary_p': forms.TextInput(attrs={'type': 'hidden'}),
        #     }