from django import forms
from .models import TeamMember, CompanyInfo, Testimonial

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'bio', 'image']

class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = ['name', 'description', 'address', 'phone', 'email', 'logo']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author_name', 'content']
