from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from cart.models import Cart
from checkout.models import ShippingAddress,BillingAddress

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_orders')
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE)
    billing_address = models.OneToOneField(BillingAddress, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id}'

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_item_total(self):
        return self.quantity * self.product.price

class OrderStatus(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status_choices = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return f'Status of Order #{self.order.id}'
