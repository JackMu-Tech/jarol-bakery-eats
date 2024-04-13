from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm, BillingAddressForm
from .models import ShippingAddress, BillingAddress, Order
from cart.models import CartTotal
from orders.models import OrderItem
from checkout.payment_gateway import StripePaymentGateway  # Assuming you have a payment gateway integration module


@login_required
def checkout(request):
    if request.method == 'POST':
        shipping_form = ShippingAddressForm(request.POST, prefix='shipping')
        billing_form = BillingAddressForm(request.POST, prefix='billing')
        if shipping_form.is_valid() and billing_form.is_valid():
            # Save shipping and billing addresses
            shipping_address = shipping_form.save(commit=False)
            billing_address = billing_form.save(commit=False)
            shipping_address.user = request.user
            billing_address.user = request.user
            shipping_address.save()
            billing_address.save()

            # Calculate total amount from the cart
            cart_total = CartTotal.objects.get(cart=request.user.cart)
            total_amount = cart_total.total_amount

            # Create an order
            order = Order.objects.create(
                user=request.user,
                shipping_address=shipping_address,
                billing_address=billing_address,
                total_amount=total_amount
            )

            # Transfer items from cart to order
            cart_items = request.user.cart.items.all()
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )

            # Process payment
            payment_gateway = StripePaymentGateway()
            payment_status, transaction_id = payment_gateway.process_payment(total_amount)
            if payment_status == 'Success':
                # Update order payment status
                order.payment_status = 'Paid'
                order.save()
                # Clear the cart
                request.user.cart.items.all().delete()
                # Redirect to order confirmation page
                return redirect('order_confirmation', order_id=order.id)
            else:
                messages.error(request, 'Payment processing failed. Please try again.')
                return redirect('checkout')
    else:
        shipping_form = ShippingAddressForm(prefix='shipping')
        billing_form = BillingAddressForm(prefix='billing')

    return render(request, 'checkout/checkout.html', {'shipping_form': shipping_form, 'billing_form': billing_form})


@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order': order})
