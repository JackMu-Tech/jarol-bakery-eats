from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemFormSet

@login_required
def place_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            formset.instance = order
            formset.save()
            messages.success(request, 'Order placed successfully.')
            return redirect('order_history')
    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()
    return render(request, 'orders/place_order.html', {'order_form': order_form, 'formset': formset})

class OrderHistoryView(ListView):
    model = Order
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_object(self):
        order = super().get_object()
        if order.user != self.request.user:
            raise PermissionDenied("You don't have permission to view this order.")
        return order
