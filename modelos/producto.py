"""
CLASE PRODUCTO - PREPARADA PARA AVANCES FUTUROS

Este archivo está listo para ser implementado en los siguientes avances del proyecto.
Esta clase es como un molde o plantilla.

Define qué datos tiene cada producto:
- nombre
- cantidad
- precio

AVANCE No. 2:
Este archivo no se usa todavía dentro del sistema principal, pero se deja preparado
para facilitar los avances futuros del proyecto.

PRÓXIMOS AVANCES (3+):
Esta clase representará un producto del inventario y permitirá:
- almacenar datos del producto
- convertir la información a diccionario
- mostrar el producto en formato legible
- actualizar cantidad
- calcular valor total en inventario
"""


class Producto:
    """
    Clase que representa un producto del inventario.

    Atributos:
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible en stock.
        precio (float): Precio unitario del producto.
    """

    def __init__(self, nombre, cantidad, precio=0.0):
        """
        Constructor de la clase Producto.

        Parámetros:
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible.
            precio (float): Precio unitario del producto.
        """
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """
        Convierte el producto a un diccionario.
        Esto será útil para guardar la información en archivos JSON.

        Retorna:
            dict: Diccionario con los datos del producto.
        """
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def convertir_a_texto(self):
        """
        Devuelve una representación legible del producto.

        Retorna:
            str: Texto con la información del producto.
        """
        return f"{self.nombre} (Disponibles: {self.cantidad}) - ₡{self.precio:.2f}"

    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad disponible del producto.

        Parámetros:
            nueva_cantidad (int): Nueva cantidad en inventario.
        """
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """
        Calcula el valor total del producto en inventario.

        Retorna:
            float: Resultado de cantidad * precio.
        """
        return self.cantidad * self.precio