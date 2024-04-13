from django.urls import path
from . import views

app_name = 'about_us'

urlpatterns = [
    path('team-members/', views.team_member_list, name='team_member_list'),
    path('team-members/add/', views.add_team_member, name='add_team_member'),
    path('team-members/<int:pk>/', views.team_member_detail, name='team_member_detail'),
    path('team-members/<int:pk>/edit/', views.edit_team_member, name='edit_team_member'),
    path('team-members/<int:pk>/delete/', views.delete_team_member, name='delete_team_member'),
    
    path('company-info/', views.company_info_detail, name='company_info_detail'),
    path('company-info/edit/', views.edit_company_info, name='edit_company_info'),
    
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/<int:pk>/edit/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/<int:pk>/delete/', views.delete_testimonial, name='delete_testimonial'),
]
