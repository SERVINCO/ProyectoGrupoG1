"""
MODELO PRODUCTO

Responsabilidades:
- Modelo de datos para un producto del inventario.
- Contiene atributos como nombre y cantidad.
- Construir la instancia con __init__, convertir a diccionario (to_dict) y generar
  una instancia a partir de dict (from_dict) para facilitar la serialización.
- Proveer representación en texto (__str__) para mostrar al usuario.
"""

"""
MODELO PRODUCTO
---------------
Clase que representa un producto en el sistema.
Almacena nombre, cantidad y precio.
"""


class Producto:

    def __init__(self, nombre, cantidad, precio=0.0):
        """
        Inicializa un nuevo objeto Producto.
        
        Args:
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible.
            precio (float): Precio unitario.
        """
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio



    def to_dict(self):
        """
        Retorna el producto como un diccionario.
        Útil para serialización a JSON.
        """
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }



    def __str__(self):
        """
        Retorna una representación en cadena del producto.
        """
        """
        return f"{self.nombre} (Cantidad: {self.cantidad}) - ${self.precio}"
