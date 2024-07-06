from django.db import models
from producto.models import Producto

class CarritoCompra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        if not self.id:  # Si es una nueva instancia, asignar el precio actual del producto
            self.precio = self.producto.precio
        super().save(*args, **kwargs)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)