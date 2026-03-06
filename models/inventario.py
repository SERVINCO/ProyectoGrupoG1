"""
MODELO INVENTARIO

Responsabilidades:
- Representar la colección interna de productos.
- Mantener la lista de objetos Producto.
- Proveer métodos para agregar un producto (verificando duplicados), buscar por nombre,
  actualizar el stock de un producto existente, obtener productos con bajo stock y
  listar todos los productos.
- Esta clase funciona como un contenedor lógico que puede ser usado por el servicio
  de inventario o por persistencia.
"""

# Dependencias y mapeos (sin implementar lógica aún)
from __future__ import annotations
from models.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {} # Diccionario para guardar productos: nombre -> objeto Producto

    def agregar_producto(self, producto):
        # Guardamos el producto usando su nombre como clave
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        # Devuelve el producto si existe, o None si no existe
        return self.productos.get(nombre)

    def listar_productos(self):
        # Devuelve una lista con todos los objetos Producto
        return list(self.productos.values())
