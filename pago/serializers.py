from rest_framework import serializers
from .models import Pago
from carrito_compra.models import CarritoCompra  # Asegúrate de importar el modelo CarritoCompra
from carrito_compra.serializers import CarritoCompraSerializer  # Asegúrate de que el serializador esté importado correctamente

class PagoSerializer(serializers.ModelSerializer):
    carrito_details = serializers.SerializerMethodField()  # Método para generar datos personalizados

    class Meta:
        model = Pago
        fields = ['id', 'carrito_id', 'total_pagado', 'carrito_details']

    def get_carrito_details(self, obj):
        """ Este método recupera los detalles del carrito basado en el ID almacenado en Pago. """
        try:
            carrito = CarritoCompra.objects.get(id=obj.carrito_id)  # Recupera el carrito de compra basado en el ID
            return CarritoCompraSerializer(carrito).data  # Devuelve los datos serializados del carrito
        except CarritoCompra.DoesNotExist:
            return None  # Devuelve None si no hay carrito asociado
