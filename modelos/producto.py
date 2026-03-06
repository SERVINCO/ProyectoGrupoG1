"""
CLASE PRODUCTO
--------------
Esta clase es como un molde o plantilla.
Define qué datos tiene cada producto (nombre, cantidad, precio).
"""

class Producto:
    def __init__(self, nombre, cantidad, precio=0.0):
        """
        Constructor: Crea un nuevo producto.
        """
        self.nombre = nombre      
        self.cantidad = cantidad  
        self.precio = precio      

    def to_dict(self):
        """
        Convierte el producto a diccionario para poder guardarlo en el archivo.
        """
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def convertir_a_texto(self):
        """
        Devuelve una frase bonita para mostrar el producto en pantalla.
        """
        return f"{self.nombre} (Disponibles: {self.cantidad}) - ${self.precio}"
