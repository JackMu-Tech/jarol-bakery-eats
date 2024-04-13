from django.contrib import admin
from .models import ContactMessage, Department, ContactOption, ContactForm

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'description')
    list_filter = ('created_at',)

@admin.register(ContactOption)
class ContactOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'created_at')
    search_fields = ('name', 'email', 'department__name')
    list_filter = ('created_at',)
    filter_horizontal = ('options',)
