"""
CLASE INVENTARIO
----------------
Funciona como una lista inteligente de productos.
Permite buscar y guardar los productos en memoria mientras el programa corre.
"""


class Inventario:
    def __init__(self):
        # Usamos un diccionario para buscarlos rápido por nombre
        # 'self.productos' pertenece a ESTE inventario específico, no a otros.
        self.productos = {} 

    def agregar_producto(self, producto):
        """Metemos un producto nuevo en la lista."""
        # 'self.productos' nos asegura que guardamos en EL diccionario de ESTE objeto.
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        """Buscamos si un producto existe por su nombre."""
        # Buscamos dentro de LOS productos de ESTA instancia (self.productos).
        return self.productos.get(nombre)

    def listar_productos(self):
        """Devolvemos todos los productos que tenemos."""
        # Sacamos los valores del diccionario de ESTA instancia.
        return list(self.productos.values())
