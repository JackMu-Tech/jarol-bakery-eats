from django.urls import path
from .views import place_order, OrderHistoryView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_history/', OrderHistoryView.as_view(), name='order_history'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
