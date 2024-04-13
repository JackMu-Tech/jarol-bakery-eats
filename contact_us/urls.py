from django.urls import path
from . import views

app_name = 'contact_us'

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('success/', views.contact_success, name='contact_success'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/add/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('contact-form/add/', views.ContactFormCreateView.as_view(), name='contact_form_create'),
]
