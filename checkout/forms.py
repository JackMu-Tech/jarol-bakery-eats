from django import forms
from .models import ShippingAddress, BillingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'phone']


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'phone']
