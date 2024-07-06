import os
import django

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremax_api.settings')
django.setup()

from producto.models import Producto
from inventario.models import Inventario  # Asumiendo que hay un modelo de Inventario

def load_productos():
    # Lista de productos a cargar
    productos = [
        {"nombre": "Taladro Inalámbrico", "descripcion": "Taladro de marca Bosch", "precio": 120.0, "disponible": True},
        {"nombre": "Sierra Circular", "descripcion": "Sierra de marca Makita", "precio": 200.0, "disponible": True},
        {"nombre": "Caja de Herramientas", "descripcion": "Caja de herramientas Stanley", "precio": 80.0, "disponible": True},
        {"nombre": "Amoladora Angular", "descripcion": "Amoladora de marca Dewalt", "precio": 150.0, "disponible": True},
        {"nombre": "Lijadora Orbital", "descripcion": "Lijadora de marca Black & Decker", "precio": 60.0, "disponible": True},
    ]

    stocks = [100, 50, 150, 75, 200]

    # Creación de productos en la base de datos
    for idx, prod in enumerate(productos):
        producto, created = Producto.objects.get_or_create(**prod)
        if created:
            Inventario.objects.create(producto=producto, cantidad=stocks[idx])
    print("Productos cargados exitosamente.")

if __name__ == "__main__":
    load_productos()
