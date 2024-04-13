from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'total_amount', 'payment_status']  

        widgets = {
            'user': forms.HiddenInput(),
            'total_amount': forms.NumberInput(attrs={'readonly': True}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Define OrderItemFormSet using inlineformset_factory
OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, extra=1, can_delete=True
)
