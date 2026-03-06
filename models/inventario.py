

"""
MODELO INVENTARIO
-----------------
Gestión de colecciones de productos en memoria.
"""



# Dependencias
from models.producto import Producto

class Inventario:

    def __init__(self):
        self.productos = {} # Almacén (nombre -> Producto)

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto



    def buscar_producto(self, nombre):
        # Retorna el producto o None
        return self.productos.get(nombre)

    def listar_productos(self):
        # Retorna lista de productos
        return list(self.productos.values())

