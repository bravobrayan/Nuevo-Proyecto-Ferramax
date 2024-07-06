import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pago
from .serializers import PagoSerializer
from carrito_compra.models import CarritoCompra

# Configurar logger
logger = logging.getLogger(__name__)

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def create(self, request, *args, **kwargs):
        # Recuperar todos los ítems en el carrito de compras
        carrito_items = CarritoCompra.objects.all()
        total = sum(item.producto.precio * item.cantidad for item in carrito_items)

        if total > 0:
            # Crear el pago
            pago = Pago.objects.create(total_pagado=total)
            # Eliminar los ítems del carrito de compras tras realizar el pago
            carrito_items.delete()

            logger.info("Pago realizado correctamente")
            return Response({
                'mensaje': "Pago realizado correctamente",
                'total_pagado': total,
                'detalles': [{'producto': item.producto.nombre, 'cantidad': item.cantidad, 'precio': item.producto.precio} for item in carrito_items]
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'El carrito está vacío'}, status=status.HTTP_400_BAD_REQUEST)
