# products/forms.py
from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating products.
    """
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    """
    Form for creating and updating categories.
    """
    class Meta:
        model = Category
        fields = ('name', 'description')
