from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('checkout/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('about-us/', include(('about_us.urls', 'about_us'), namespace='about_us')),
    path('contact-us/', include(('contact_us.urls', 'contact_us'), namespace='contact_us')),  # Include Contact Us app
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
