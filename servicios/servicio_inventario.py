"""
SERVICIO DE INVENTARIO
----------------------
Aquí está toda la lógica para manejar los productos.
Es como el "cerebro" que controla el stock.
Sabe agregar productos, actualizarlos y guardarlos.
"""

from modelos.inventario import Inventario
from modelos.producto import Producto
from utils.archivos import cargar_datos, guardar_datos
import configuracion as config

class ServicioInventario:
    def __init__(self):
        # Creamos una lista vacía en memoria
        self.inventario = Inventario()
        # Cargamos los datos del archivo al iniciar
        self.cargar_inventario()

    def cargar_inventario(self):
        """Lee el archivo JSON y llena la memoria con los productos."""
        datos = cargar_datos(config.RUTA_ARCHIVO)
        
        for data in datos:
            # Reconvertimos los diccionarios a objetos Producto
            prod = Producto(data["nombre"], data["cantidad"], data["precio"])
            self.inventario.agregar_producto(prod)

    def guardar_inventario(self):
        """Guarda todo lo que hay en memoria al archivo JSON."""
        # Necesitamos convertir los objetos a diccionarios simples
        lista_productos = self.inventario.listar_productos()
        datos = [prod.to_dict() for prod in lista_productos]
        guardar_datos(config.RUTA_ARCHIVO, datos)

    def agregar_producto(self, nombre, cantidad, precio):
        """Crea un nuevo producto y lo guarda permanentemente."""
        if self.inventario.buscar_producto(nombre):
            print("(!) El producto ya existe.")
            return

        nuevo_producto = Producto(nombre, cantidad, precio)
        self.inventario.agregar_producto(nuevo_producto)
        self.guardar_inventario() # Importante: guardar en disco
        print("-> Producto agregado correctamente.")

    def buscar_producto(self, nombre):
        return self.inventario.buscar_producto(nombre)

    def actualizar_stock(self, nombre, cantidad):
        """Cambia la cantidad de un producto existente."""
        producto = self.inventario.buscar_producto(nombre)
        if producto:
            producto.cantidad = cantidad
            self.guardar_inventario()
            print("-> Stock actualizado.")
        else:
            print("(!) Producto no encontrado.")

    def listar_productos(self):
        lista = self.inventario.listar_productos()
        if not lista:
            print("El inventario está vacío.")
        else:
            print("\n--- Lista de Productos ---")
            for prod in lista:
                print(prod.convertir_a_texto())
