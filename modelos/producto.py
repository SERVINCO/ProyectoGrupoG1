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
        
        IMAGINA QUE ESTA CLASE ES UN MOLDE PARA HACER GALLETAS.
        Cuando usas este molde para crear una galleta específica (un objeto),
        esa galleta necesita saber cuáles son SUS propios ingredientes.
        
        'self' es esa galleta específica que estamos creando AHORA MISMO.
        No es el molde, ni la galleta de al lado, es ESTA.
        """
        self.nombre = nombre      # La galleta dice: "MI nombre (self.nombre) es el que me diste"
        self.cantidad = cantidad  # La galleta dice: "MI cantidad (self.cantidad) es la que me diste"
        self.precio = precio      # La galleta dice: "MI precio (self.precio) es el que me diste"

    def to_dict(self):
        """
        Convierte el producto a diccionario para poder guardarlo en el archivo.
        
        Aquí 'self' le dice al programa: "Usa MIS datos, los de ESTA galleta".
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
