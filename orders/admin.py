from django.contrib import admin
from .models import Order, OrderItem, OrderStatus

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('id', 'user__username', 'user__email')
    inlines = (OrderItemInline,)

admin.site.register(Order, OrderAdmin)

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order', 'status')
    search_fields = ('order__id',)
    list_filter = ('status',)

admin.site.register(OrderStatus, OrderStatusAdmin)
