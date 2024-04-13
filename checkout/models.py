from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Cart, CartItem
from django.utils import timezone


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True


class ShippingAddress(Address):
    class Meta:
        verbose_name_plural = 'Shipping Addresses'


class BillingAddress(Address):
    class Meta:
        verbose_name_plural = 'Billing Addresses'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkout_orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='checkout_order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='checkout_order_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_item_total(self):
        return self.quantity * self.product.price


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f'Payment for Order #{self.order.id}'
