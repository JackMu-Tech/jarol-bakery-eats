from django import forms
from .models import CartItem


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'max': 10, 'step': 1}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return quantity
