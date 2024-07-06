from rest_framework import serializers
from .models import CartItem, Orden
from producto.models import Producto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['producto', 'cantidad']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
