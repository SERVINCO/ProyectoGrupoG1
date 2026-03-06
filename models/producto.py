"""
MODELO PRODUCTO

Responsabilidades:
- Modelo de datos para un producto del inventario.
- Contiene atributos como nombre y cantidad.
- Construir la instancia con __init__, convertir a diccionario (to_dict) y generar
  una instancia a partir de dict (from_dict) para facilitar la serialización.
- Proveer representación en texto (__str__) para mostrar al usuario.
"""

class Producto:
    def __init__(self, nombre, cantidad, precio=0.0):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        # Convertimos el objeto a un diccionario para poder guardarlo en JSON
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        return f"{self.nombre} (Cantidad: {self.cantidad}) - ${self.precio}"
