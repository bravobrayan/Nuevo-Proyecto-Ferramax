from django.db import models
from producto.models import Producto

class CartItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"

class Orden(models.Model):
    items_carrito = models.ManyToManyField(CartItem)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Orden {self.id}"
