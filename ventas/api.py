from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from producto.models import Producto
from .models import CartItem, Orden
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer

class ProductListAPI(ListAPIView):
    queryset = Producto.objects.filter(activo=True)
    serializer_class = ProductSerializer

class CartItemListCreateAPI(ListAPIView, CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get('products', [])
        response_data = []
        total = 0
        try:
            for item in data:
                product_id = item.get('id')
                producto = Producto.objects.get(id=product_id)
                cart_item = CartItem.objects.create(producto=producto, cantidad=item['quantity'])
                response_data.append({
                    'product': {
                        'id': producto.id,
                        'marca': producto.marca,
                        'nombre': producto.nombre,
                        'precio': producto.precio,
                        'cantidad': cart_item.cantidad,
                    }
                })
                total += producto.precio * item['quantity']
            return Response({'message': 'Productos añadidos al carro de compras', 'cart_items': response_data, 'total': total}, status=status.HTTP_201_CREATED)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Solicitud inválida'}, status=status.HTTP_400_BAD_REQUEST)

class CheckoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener los detalles del producto de la base de datos
        cart_items = CartItem.objects.all()
        
        # Serializar los detalles del producto
        serialized_cart_items = []
        for item in cart_items:
            serialized_item = {
                'id': item.producto.id,
                'marca': item.producto.marca,
                'nombre': item.producto.nombre,
                'precio': item.producto.precio,
                'cantidad': item.cantidad
            }
            serialized_cart_items.append(serialized_item)
        
        # Calcular el total de la compra
        total = sum(item.producto.precio * item.cantidad for item in cart_items)
        
        # Eliminar los productos del carrito después de procesar el pago
        CartItem.objects.all().delete()

        # Retornar el detalle de los productos comprados en el mensaje de "Checkout"
        return Response({'message': 'Pago realizado con éxito', 'cart_items': serialized_cart_items, 'total': total}, status=status.HTTP_200_OK)
