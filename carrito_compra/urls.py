from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarritoCompraViewSet
from .views import ConfirmacionCarritoCompra

router = DefaultRouter()
router.register(r'', CarritoCompraViewSet, basename='carrito_compra')

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las operaciones CRUD básicas
    path('eliminar/', CarritoCompraViewSet.as_view({
        'delete': 'destroy'  # Asume que el método 'destroy' está configurado para eliminar todo el carrito
    }), name='eliminar-carrito'),
    path('confirmacion/', ConfirmacionCarritoCompra.as_view(), name='confirmacion-carrito'),

]
