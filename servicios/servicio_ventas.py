"""
SERVICIO DE VENTAS
------------------
Maneja toda la parte de vender y cobrar.
Se encarga de restar del inventario, calcular el total ($) y guardar el historial.
"""

from utils.archivos import cargar_datos, guardar_datos # Para manejar los archivos JSON
import configuracion as config # Para obtener la ruta del archivo de ventas
from datetime import datetime # Para registrar la fecha y hora exacta de cada venta

class ServicioVentas:
    def __init__(self, servicio_inventario):
        # Guardamos la conexión con el inventario en 'self.servicio_inventario'.
        # Así, ESTE servicio de ventas siempre sabrá a quién preguntarle por el stock.
        self.servicio_inventario = servicio_inventario

    def _cargar_ventas(self):
        """Lee el archivo de ventas del disco."""
        # Método interno: Lo usa ESTA clase para leer sus propios datos.
        return cargar_datos(config.RUTA_VENTAS)

    def _guardar_ventas(self, ventas):
        """Escribe la lista actualizada de ventas en el disco."""
        # Método interno: Lo usa ESTA clase para guardar sus cambios.
        guardar_datos(config.RUTA_VENTAS, ventas)

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Registra una venta nueva.
        """
        # Usamos 'self.servicio_inventario' para preguntarle al OTRO servicio si hay producto.
        producto = self.servicio_inventario.buscar_producto(nombre_producto)
        
        if not producto:
            print("(!) El producto no existe.")
            return
        
        # ... (validaciones) ...

        if cantidad <= 0:
            print("(!) La cantidad debe ser mayor a 0.")
            return

        if cantidad > producto.cantidad:
            print(f"(!) No hay suficiente stock. Solo quedan {producto.cantidad}.")
            return

        # Usamos NUESTRO método interno ('self._cargar_ventas') para ver qué ID sigue.
        ventas = self._cargar_ventas()
        nuevo_id = 1
        if ventas:
            nuevo_id = max(v.get("id", 0) for v in ventas) + 1

        total = cantidad * producto.precio
        
        # ... (creación venta) ...
        nueva_venta = {
            "id": nuevo_id,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "producto": nombre_producto,
            "cantidad": cantidad,
            "total": total
        }

        # Actualizamos el stock en el inventario usando la conexión que guardamos ('self.servicio_inventario').
        producto.cantidad -= cantidad 
        self.servicio_inventario.actualizar_stock(nombre_producto, producto.cantidad)

        # Guardamos usando NUESTRO método interno.
        ventas.append(nueva_venta)
        self._guardar_ventas(ventas)
        print(f"-> Venta #{nuevo_id} exitosa. Total a pagar: ${total}")

    def listar_ventas(self):
        """Muestra todas las ventas que se han hecho."""
        # Usamos 'self._cargar_ventas' para obtener SOLO las ventas de este sistema.
        ventas = self._cargar_ventas()
        if not ventas:
            print("No hay ventas registradas todavía.")
        else:
            print("\n--- Historial de Ventas ---")
            for v in ventas:
                print(f"ID: {v.get('id')} | Fecha: {v['fecha']} | Producto: {v['producto']} | Cant: {v['cantidad']} | Total: ${v['total']}")

    def buscar_venta(self, id_venta):
        # Buscamos en NUESTRAS ventas.
        ventas = self._cargar_ventas()
        for v in ventas:
            if v.get("id") == id_venta:
                return v
        return None

    def eliminar_venta(self, id_venta):
        ventas = self._cargar_ventas()
        venta_a_borrar = None
        
        for v in ventas:
            if v.get("id") == id_venta:
                venta_a_borrar = v
                break
        
        if not venta_a_borrar:
            print("(!) Venta no encontrada.")
            return

        # Usamos 'self.servicio_inventario' para devolver el stock al inventario.
        producto = self.servicio_inventario.buscar_producto(venta_a_borrar["producto"])
        if producto:
            nuevo_stock = producto.cantidad + venta_a_borrar["cantidad"]
            self.servicio_inventario.actualizar_stock(producto.nombre, nuevo_stock)

        ventas.remove(venta_a_borrar)
        self._guardar_ventas(ventas)
        print(f"-> Venta #{id_venta} eliminada. Stock devuelto.")

    def actualizar_venta(self, id_venta, nueva_cantidad):
        ventas = self._cargar_ventas()
        idx_venta = -1
        
        for i, v in enumerate(ventas):
            if v.get("id") == id_venta:
                idx_venta = i
                break
        
        if idx_venta == -1:
            print("(!) Venta no encontrada.")
            return

        venta_actual = ventas[idx_venta]
        producto_nombre = venta_actual["producto"]
        # Usamos 'self.servicio_inventario' otra vez.
        producto = self.servicio_inventario.buscar_producto(producto_nombre)
        
        # ... (resto del código igual) ...
        if not producto:
            print("(!) El producto ya no existe en la base de datos.")
            return

        diferencia = nueva_cantidad - venta_actual["cantidad"]

        if diferencia > 0 and producto.cantidad < diferencia:
            print(f"(!) No hay suficiente stock extra. Disponible: {producto.cantidad}")
            return

        producto.cantidad -= diferencia
        self.servicio_inventario.actualizar_stock(producto_nombre, producto.cantidad)

        venta_actual["cantidad"] = nueva_cantidad
        venta_actual["total"] = nueva_cantidad * producto.precio
        
        self._guardar_ventas(ventas)
        print(f"-> Venta #{id_venta} corregida. Nuevo total: ${venta_actual['total']}")
