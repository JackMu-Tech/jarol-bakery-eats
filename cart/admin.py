from django.contrib import admin
from .models import Cart, CartItem, CartTotal


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username',)
    inlines = [CartItemInline]


class CartTotalAdmin(admin.ModelAdmin):
    list_display = ('cart', 'total_items', 'total_amount')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartTotal, CartTotalAdmin)
