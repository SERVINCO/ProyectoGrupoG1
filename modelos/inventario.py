"""
CLASE INVENTARIO
----------------
Funciona como una lista inteligente de productos.
Permite buscar y guardar los productos en memoria mientras el programa corre.
"""

# Importamos la clase Producto
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        # Usamos un diccionario para buscarlos rápido por nombre
        self.productos = {} 

    def agregar_producto(self, producto):
        """Metemos un producto nuevo en la lista."""
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        """Buscamos si un producto existe por su nombre."""
        return self.productos.get(nombre)

    def listar_productos(self):
        """Devolvemos todos los productos que tenemos."""
        return list(self.productos.values())
