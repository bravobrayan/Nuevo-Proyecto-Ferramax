from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from producto.models import Producto  # Ajusta la importación según la ubicación real de tus modelos

class ProductoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.producto1 = Producto.objects.create(nombre='Producto 1', descripcion='Descripción del producto 1', precio=10.0)
        self.producto2 = Producto.objects.create(nombre='Producto 2', descripcion='Descripción del producto 2', precio=20.0)

    def test_list_productos(self):
        url = reverse('producto-list')  # Nombre de la URL configurado en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verifica que se devuelvan todos los productos

    def test_detalle_producto(self):
        url = reverse('producto-detail', kwargs={'pk': self.producto1.id})  # Nombre de la URL configurado en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Producto 1')  # Verifica que se devuelva el producto correcto