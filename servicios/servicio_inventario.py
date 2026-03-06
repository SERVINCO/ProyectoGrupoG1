"""
SERVICIO DE INVENTARIO
----------------------
Aquí está toda la lógica para manejar los productos.
Es como el "cerebro" que controla el stock.
Sabe agregar productos, actualizarlos y guardarlos.
"""

from modelos.inventario import Inventario # Clase contenedora para nuestros productos
from modelos.producto import Producto     # Clase molde para crear nuevos productos
from utils.archivos import cargar_datos, guardar_datos # Funciones para leer/escribir en disco
import configuracion as config            # El archivo donde guardamos rutas y constantes

class ServicioInventario:
    def __init__(self):
        # Creamos una lista vacía en memoria y la guardamos en 'self.inventario'.
        # 'self.inventario' es la base de datos temporal que usará ESTE servicio.
        self.inventario = Inventario()
        # Cargamos los datos del archivo usando NUESTRO propio método 'self.cargar_inventario()'.
        self.cargar_inventario()

    def cargar_inventario(self):
        """Lee el archivo JSON y llena la memoria con los productos."""
        datos = cargar_datos(config.RUTA_ARCHIVO)
        
        for data in datos:
            # Reconvertimos los diccionarios a objetos Producto
            prod = Producto(data["nombre"], data["cantidad"], data["precio"])
            # Usamos 'self.inventario' para agregar el producto a NUESTRA lista interna.
            self.inventario.agregar_producto(prod)

    def guardar_inventario(self):
        """Guarda todo lo que hay en memoria al archivo JSON."""
        # Necesitamos convertir los objetos a diccionarios simples
        # Accedemos a NUESTRA lista ('self.inventario') para leer qué productos tenemos.
        lista_productos = self.inventario.listar_productos()
        datos = [prod.to_dict() for prod in lista_productos]
        guardar_datos(config.RUTA_ARCHIVO, datos)

    def agregar_producto(self, nombre, cantidad, precio):
        """Crea un nuevo producto y lo guarda permanentemente."""
        # Primero revisamos en NUESTRO inventario ('self.inventario') si ya existe.
        if self.inventario.buscar_producto(nombre):
            print("(!) El producto ya existe.")
            return

        nuevo_producto = Producto(nombre, cantidad, precio)
        # Si no existe, lo agregamos a NUESTRA lista 'self.inventario'.
        self.inventario.agregar_producto(nuevo_producto)
        # Y llamamos a NUESTRO método ('self.guardar_inventario') para actualizar el archivo.
        self.guardar_inventario() 
        print("-> Producto agregado correctamente.")

    def buscar_producto(self, nombre):
        # Delegamos la búsqueda a NUESTRO objeto inventario ('self.inventario').
        return self.inventario.buscar_producto(nombre)

    def actualizar_stock(self, nombre, cantidad):
        """Cambia la cantidad de un producto existente."""
        # Buscamos el producto en NUESTRO inventario.
        producto = self.inventario.buscar_producto(nombre)
        if producto:
            producto.cantidad = cantidad
            # Guardamos los cambios usando NUESTRO método.
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
