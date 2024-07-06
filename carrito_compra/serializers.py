from rest_framework import serializers
from .models import CarritoCompra

class CarritoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompra
        fields = ['producto', 'cantidad']

