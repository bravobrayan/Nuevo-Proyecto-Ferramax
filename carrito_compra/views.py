from rest_framework import viewsets
from .models import CarritoCompra
from .serializers import CarritoCompraSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from pago.models import Pago
import threading
from django.db import transaction


class CarritoCompraViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompra.objects.all()
    serializer_class = CarritoCompraSerializer

    def get_queryset(self):
        """
        Este método se puede personalizar para filtrar el queryset basado en parámetros de la consulta,
        por ejemplo, un usuario específico en una aplicación multiusuario.
        """
        # Filtrar por usuario si tu modelo tiene un campo de usuario asociado
        # user = self.request.user
        # return CarritoCompra.objects.filter(usuario=user)
        
        return super().get_queryset()  # Devuelve el queryset sin filtrar si no hay más lógica específica

    def destroy(self, request, *args, **kwargs):
        """
        Elimina todos los ítems del carrito de compras.
        """
        self.queryset.delete()
        return Response({"Productos del Carrito Eliminados Correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
    # Lock para manejar accesos concurrentes para el incremento de carrito_id
lock = threading.Lock()

class ConfirmacionCarritoCompra(APIView):
    def post(self, request, *args, **kwargs):
        carrito_items = CarritoCompra.objects.all()
        if not carrito_items.exists():
            return Response({"mensaje": "El carrito está vacío"}, status=status.HTTP_400_BAD_REQUEST)

        total = sum(item.precio * item.cantidad for item in carrito_items)
        productos = [{'id': item.producto.id, 'nombre': item.producto.nombre, 'cantidad': item.cantidad, 'precio': item.precio} for item in carrito_items]

        return Response({
            'total': total,
            'productos': productos,
            'mensaje': 'Confirmación del carrito exitosa'
        }, status=status.HTTP_200_OK)