from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Cambia el related_name aquí
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Cambia el related_name aquí
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='user',
    )
