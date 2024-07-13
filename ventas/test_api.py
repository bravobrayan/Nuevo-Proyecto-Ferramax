import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from producto.models import Producto
from ventas.models import CartItem, Orden
from .api import ProductListAPI, CartItemListCreateAPI, CheckoutAPI

@pytest.mark.django_db
def test_product_list_api():
    client = APIClient()
    url = reverse('product-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_cart_item_create_api():
    client = APIClient()
    url = reverse('cart-item-list-create')
    data = {
        'products': [
            {'id': 1, 'quantity': 2},  # Assuming product with ID 1 exists
            {'id': 2, 'quantity': 1}   # Assuming product with ID 2 exists
        ]
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_checkout_api():
    client = APIClient()
    url = reverse('checkout')
    response = client.post(url)
    assert response.status_code == status.HTTP_200_OK
    # Add more assertions based on the response data if needed
