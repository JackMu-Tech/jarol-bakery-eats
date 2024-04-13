from django.contrib import admin
from .models import ShippingAddress, BillingAddress, Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_shipping_address', 'get_billing_address', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('id', 'user__username', 'shipping_address__address_line_1', 'billing_address__address_line_1')
    inlines = [OrderItemInline]
    readonly_fields = ['user', 'total_amount', 'payment_status', 'created_at']

    def get_shipping_address(self, obj):
        return obj.cart.shipping_address.address_line_1  

    def get_billing_address(self, obj):
        return obj.cart.billing_address.address_line_1  

    get_shipping_address.short_description = 'Shipping Address'
    get_billing_address.short_description = 'Billing Address'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'transaction_id', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_date')
    search_fields = ('order__id', 'payment_method', 'transaction_id')
    readonly_fields = ['order', 'amount', 'payment_method', 'transaction_id', 'payment_status', 'payment_date']
