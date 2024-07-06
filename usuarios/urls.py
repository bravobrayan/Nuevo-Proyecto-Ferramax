from django.urls import path
from .views import UsuarioCreateAPI, UsuarioDetailAPI, ChangePasswordAPI

urlpatterns = [
    path('', UsuarioCreateAPI.as_view(), name='crear_usuario'),  # Cambia el nombre de la ruta para crear usuario
    path('<int:pk>/', UsuarioDetailAPI.as_view(), name='editar_usuario'),  # Cambia el nombre de la ruta para editar usuario
    path('change-password/', ChangePasswordAPI.as_view(), name='cambiar_contraseña'),  # Cambia el nombre de la ruta para cambiar contraseña
]