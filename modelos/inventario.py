"""
CLASE INVENTARIO - PREPARADA PARA AVANCES FUTUROS

Este archivo está listo para ser implementado en los siguientes avances del proyecto.
Funciona como una lista inteligente de productos.

Permite guardar, buscar, eliminar y listar productos en memoria mientras
el programa se está ejecutando.

AVANCE No. 2:
Este archivo no se usa todavía dentro del sistema principal, pero se deja
preparado para facilitar los avances futuros del proyecto.

PRÓXIMOS AVANCES (3+):
Esta clase gestionará la colección de productos usando una estructura de
datos eficiente.
"""


class Inventario:
    """
    Clase que representa el inventario del sistema.

    Atributo:
        productos (dict): Diccionario de productos, usando el nombre
        como clave para facilitar la búsqueda rápida.
    """

    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar productos.
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.

        Parámetros:
            producto: Objeto de tipo Producto.
        """
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre.

        Parámetros:
            nombre (str): Nombre del producto a buscar.

        Retorna:
            Producto o None: El producto si existe, o None si no se encuentra.
        """
        return self.productos.get(nombre)

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario por su nombre.

        Parámetros:
            nombre (str): Nombre del producto a eliminar.
        """
        if nombre in self.productos:
            del self.productos[nombre]

    def listar_productos(self):
        """
        Devuelve una lista con todos los productos del inventario.

        Retorna:
            list: Lista de productos.
        """
        return list(self.productos.values())

    def productos_bajo_stock(self, limite):
        """
        Devuelve una lista de productos cuyo stock está por debajo
        o igual al límite indicado.

        Parámetros:
            limite (int): Cantidad límite para considerar stock bajo.

        Retorna:
            list: Lista de productos con stock bajo.
        """
        return [
            producto for producto in self.productos.values()
            if producto.cantidad <= limite
        ]

    def valor_total_inventario(self):
        """
        Calcula el valor total de todos los productos en inventario.

        Retorna:
            float: Suma total del valor de todos los productos.
        """
        total = 0
        for producto in self.productos.values():
            total += producto.calcular_valor_total()
        return total