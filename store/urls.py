
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),

    path('products/', views.products, name='products'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('contact/', views.contact, name='contact'),
    
    path('cart/',views.cart,name='cart')

]

if settings.DEBUG:  # Serve media files only in development
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
