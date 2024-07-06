from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('producto.urls')),
    path('inventario/', include('inventario.urls')),
    path('carrito_compra/', include('carrito_compra.urls')),
    path('pago/', include('pago.urls')),
    path('usuarios/', include('usuarios.urls')),  # Ruta para el componente de usuarios
]
