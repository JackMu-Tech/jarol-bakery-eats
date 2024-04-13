from django import forms
from .models import ContactMessage, Department, ContactForm

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'email', 'phone', 'description']

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'department', 'options']
