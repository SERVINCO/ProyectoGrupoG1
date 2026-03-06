"""
SERVICIO INVENTARIO

Responsabilidades:
- Encapsular la lógica de negocio relacionada con el inventario de productos.
- Proveer métodos para crear, leer, actualizar y borrar productos en el inventario.
- Validar datos de entrada (por ejemplo, que la cantidad sea un número no negativo).
- Detectar y lanzar excepciones cuando se intenten operaciones inválidas.
- Colaborar con el repositorio para persistir cambios.
"""

# Dependencias y mapeos (sin implementar lógica aún)
from models.inventario import Inventario
from models.producto import Producto
from persistence.json_repository import cargar_datos, guardar_datos
import config

class InventarioService:
    def __init__(self):
        self.inventario = Inventario()
        self.cargar_inventario()

    def cargar_inventario(self):
        # Carga datos desde JSON y reconstruye objetos Producto
        datos = cargar_datos(config.RUTA_ARCHIVO)
        
        for data in datos:
            prod = Producto(data["nombre"], data["cantidad"], data["precio"])
            self.inventario.agregar_producto(prod)

    def guardar_inventario(self):
        # Serializa objetos a dict y guarda en JSON
        lista_productos = self.inventario.listar_productos()
        datos = []
        for prod in lista_productos:
            datos.append(prod.to_dict())
            
        guardar_datos(config.RUTA_ARCHIVO, datos)



    def agregar_producto(self, nombre, cantidad, precio):
        # Valida existencia, crea el objeto y persiste cambios
        if self.inventario.buscar_producto(nombre):
            print("El producto ya existe.")
            return

        nuevo_producto = Producto(nombre, cantidad, precio)
        self.inventario.agregar_producto(nuevo_producto)
        self.guardar_inventario()
        print("Producto agregado.")


    def buscar_producto(self, nombre):
        return self.inventario.buscar_producto(nombre)

    def actualizar_stock(self, nombre, cantidad):
        producto = self.inventario.buscar_producto(nombre)
        if producto:
            producto.cantidad = cantidad
            self.guardar_inventario()
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    def listar_productos(self):
        lista = self.inventario.listar_productos()
        if not lista:
            print("El inventario está vacío.")
        else:
            print("\n--- Productos ---")
            for prod in lista:
                print(prod.convertir_a_texto())
