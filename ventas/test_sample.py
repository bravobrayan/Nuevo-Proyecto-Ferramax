import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ventas.models import CartItem, Orden
from producto.models import Producto

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def producto(db):
    return Producto.objects.create(nombre="Martillo", marca="Stanley", precio=19.99, activo=True)

@pytest.mark.django_db
class CartItemTest(TestCase):

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, api_client, producto):
        self.client = api_client
        self.producto = producto

    def test_agregar_item_al_carrito(self):
        data = {'products': [{'id': self.producto.id, 'quantity': 2}]}
        response = self.client.post('/api/cart/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        cart_items = CartItem.objects.all()
        self.assertEqual(len(cart_items), 1)
        self.assertEqual(cart_items[0].producto, self.producto)
        self.assertEqual(cart_items[0].cantidad, 2)

    def test_obtener_items_del_carrito(self):
        CartItem.objects.create(producto=self.producto, cantidad=3)
        response = self.client.get('/api/cart/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['product']['id'], self.producto.id)
        self.assertEqual(data[0]['quantity'], 3)  # Corrección de la clave del diccionario

@pytest.mark.django_db
class OrderTest(TestCase):

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, api_client, producto):
        self.client = api_client
        self.producto = producto

    def test_crear_orden(self):
        CartItem.objects.create(producto=self.producto, cantidad=1)

        response = self.client.post('/api/checkout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Orden.objects.count(), 1)
        self.assertEqual(CartItem.objects.count(), 0)

        # Verifica los detalles de la orden (productos, total, etc.)
        order = Orden.objects.first()
        self.assertEqual(order.precio_total, 19.99)  # Suponiendo que el precio es 19.99
        self.assertEqual(order.items_carrito.count(), 1)
        self.assertEqual(order.items_carrito.first().producto, self.producto)
