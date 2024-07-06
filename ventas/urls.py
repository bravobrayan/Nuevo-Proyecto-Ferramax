from django.urls import path
from .api import ProductListAPI, CartItemListCreateAPI, CheckoutAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name='product-list'),
    path('cart/', CartItemListCreateAPI.as_view(), name='cart-item-list-create'),
    path('checkout/', CheckoutAPI.as_view(), name='checkout'),
]
