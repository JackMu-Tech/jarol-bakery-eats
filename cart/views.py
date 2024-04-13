from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem
from .forms import AddToCartForm
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Attempt to retrieve the user's cart
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            # If the cart doesn't exist for the user, create a new one
            cart = Cart.objects.create(user=request.user)
    else:
        # If the user is not authenticated, redirect them to the login page
        messages.info(request, 'Please log in to view your cart.')
        return redirect('login')

    # Render the cart template with the cart object
    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_create_cart(request.user)
    product = get_object_or_404(Product, id=product_id)  # Retrieve the product object
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Check if the product is already in the cart
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.save()
            messages.success(request, f'{product.name} added to your cart.')
            return redirect('cart:view_cart')
    else:
        form = AddToCartForm()
    context = {
        'form': form,
        'product': product,  # Pass the product object to the context
    }
    return render(request, 'cart/add_to_cart.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    messages.success(request, 'Item removed from your cart.')
    return redirect('cart:view_cart')
