"""
SERVICIO DE VENTAS
------------------
Maneja toda la parte de vender y cobrar.
Se encarga de restar del inventario, calcular el total ($) y guardar el historial.
"""

from utils.archivos import cargar_datos, guardar_datos
import configuracion as config
from datetime import datetime

class ServicioVentas:
    def __init__(self, servicio_inventario):
        # Necesita conectarse con el inventario para saber si hay stock
        self.servicio_inventario = servicio_inventario

    def _cargar_ventas(self):
        """Lee el archivo de ventas del disco."""
        return cargar_datos(config.RUTA_VENTAS)

    def _guardar_ventas(self, ventas):
        """Escribe la lista actualizada de ventas en el disco."""
        guardar_datos(config.RUTA_VENTAS, ventas)

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Registra una venta nueva.
        1. Revisa si el producto existe y si hay stock.
        2. Calcula el precio total.
        3. Resta la cantidad vendida del inventario.
        4. Guarda el registro de la venta.
        """
        producto = self.servicio_inventario.buscar_producto(nombre_producto)
        
        if not producto:
            print("(!) El producto no existe.")
            return

        if cantidad <= 0:
            print("(!) La cantidad debe ser mayor a 0.")
            return

        if cantidad > producto.cantidad:
            print(f"(!) No hay suficiente stock. Solo quedan {producto.cantidad}.")
            return

        # Cargamos las ventas anteriores para saber qué ID toca
        ventas = self._cargar_ventas()
        nuevo_id = 1
        if ventas:
            # Buscamos el ID más alto y le sumamos 1
            nuevo_id = max(v.get("id", 0) for v in ventas) + 1

        total = cantidad * producto.precio
        
        # Creamos el "ticket" de la venta
        nueva_venta = {
            "id": nuevo_id,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "producto": nombre_producto,
            "cantidad": cantidad,
            "total": total
        }

        # Actualizamos el stock real
        producto.cantidad -= cantidad 
        self.servicio_inventario.actualizar_stock(nombre_producto, producto.cantidad)

        # Guardamos la venta
        ventas.append(nueva_venta)
        self._guardar_ventas(ventas)
        print(f"-> Venta #{nuevo_id} exitosa. Total a pagar: ${total}")

    def listar_ventas(self):
        """Muestra todas las ventas que se han hecho."""
        ventas = self._cargar_ventas()
        if not ventas:
            print("No hay ventas registradas todavía.")
        else:
            print("\n--- Historial de Ventas ---")
            for v in ventas:
                print(f"ID: {v.get('id')} | Fecha: {v['fecha']} | Producto: {v['producto']} | Cant: {v['cantidad']} | Total: ${v['total']}")

    def buscar_venta(self, id_venta):
        """Busca un ticket específico por su número ID."""
        ventas = self._cargar_ventas()
        for v in ventas:
            if v.get("id") == id_venta:
                return v
        return None

    def eliminar_venta(self, id_venta):
        """Anula una venta y devuelve los productos al inventario."""
        ventas = self._cargar_ventas()
        venta_a_borrar = None
        
        for v in ventas:
            if v.get("id") == id_venta:
                venta_a_borrar = v
                break
        
        if not venta_a_borrar:
            print("(!) Venta no encontrada.")
            return

        # Devolvemos los productos al inventario
        producto = self.servicio_inventario.buscar_producto(venta_a_borrar["producto"])
        if producto:
            nuevo_stock = producto.cantidad + venta_a_borrar["cantidad"]
            self.servicio_inventario.actualizar_stock(producto.nombre, nuevo_stock)

        ventas.remove(venta_a_borrar)
        self._guardar_ventas(ventas)
        print(f"-> Venta #{id_venta} eliminada. Stock devuelto.")

    def actualizar_venta(self, id_venta, nueva_cantidad):
        """Permite corregir la cantidad de una venta ya hecha (si te equivocaste)."""
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
        producto = self.servicio_inventario.buscar_producto(producto_nombre)

        if not producto:
            print("(!) El producto ya no existe en la base de datos.")
            return

        # Calculamos la diferencia para ajustar el stock
        diferencia = nueva_cantidad - venta_actual["cantidad"]

        if diferencia > 0 and producto.cantidad < diferencia:
            print(f"(!) No hay suficiente stock extra. Disponible: {producto.cantidad}")
            return

        # Actualizamos stock
        producto.cantidad -= diferencia
        self.servicio_inventario.actualizar_stock(producto_nombre, producto.cantidad)

        # Actualizamos la venta
        venta_actual["cantidad"] = nueva_cantidad
        venta_actual["total"] = nueva_cantidad * producto.precio
        
        self._guardar_ventas(ventas)
        print(f"-> Venta #{id_venta} corregida. Nuevo total: ${venta_actual['total']}")
