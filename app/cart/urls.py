from django.urls import path
from .views import Cart

urlpatterns = [
    path('cart/add/<int:product_id>/', Cart.add, name='add_to_cart')
]