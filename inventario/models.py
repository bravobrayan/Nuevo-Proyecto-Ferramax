from django.db import models
from producto.models import Producto

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
