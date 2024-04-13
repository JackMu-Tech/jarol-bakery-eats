# products/admin.py
from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" width="100" height="auto" />'.format(obj.image.url)
        else:
            return 'No Image'
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for Category model.
    """
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
