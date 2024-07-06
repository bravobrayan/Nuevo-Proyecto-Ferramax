from django.db import models
from django.apps import apps

class Pago(models.Model):
    carrito_id = models.IntegerField()
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - Total: {self.total_pagado}"

    def get_carrito(self):
        CarritoCompra = apps.get_model('carrito_compra', 'CarritoCompra')
        return CarritoCompra.objects.get(id=self.carrito_id)
