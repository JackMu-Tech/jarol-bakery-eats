from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

class CartManager(models.Manager):
    def get_or_create_cart(self, user):
        try:
            # Attempt to retrieve the user's cart
            cart = self.get(user=user)
        except Cart.DoesNotExist:
            # If the cart doesn't exist for the user, create a new one
            cart = self.create(user=user)
        return cart


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CartManager()

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product} (Quantity: {self.quantity})"



class CartTotal(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="total")
    total_items = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("Cart Total")
        verbose_name_plural = _("Cart Totals")

    def __str__(self):
        return f"Total for {self.cart}"


@receiver(post_save, sender=CartItem)
def update_cart_total(sender, instance, created, **kwargs):
    cart = instance.cart
    total_items = cart.items.aggregate(total=models.Sum('quantity'))['total'] or 0
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
    cart_total, _ = CartTotal.objects.get_or_create(cart=cart)
    cart_total.total_items = total_items
    cart_total.total_amount = total_amount
    cart_total.save()
