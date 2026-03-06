"""
SERVICIO VENTAS

Responsabilidades:
- Gestionar la creación de ventas asociadas a productos existentes.
- Verificar que el stock disponible sea suficiente antes de registrar una venta.
- Actualizar el inventario al descontar las unidades vendidas.
- Validar datos de entrada y manejar errores como producto no encontrado o stock insuficiente.
- Generar un registro de la venta para su almacenamiento.
"""

from persistence.json_repository import cargar_datos, guardar_datos
import config
from datetime import datetime

"""
SERVICIO DE VENTAS
------------------
Lógica de negocio para las ventas.
Gestiona validaciones, actualización de stock y persistencia de ventas.
"""

class VentaService:
    def __init__(self, inventario_service):
        # Necesitamos el servicio de inventario para consultar y modificar stock
        self.inventario_service = inventario_service

    def _cargar_ventas(self):
        """Método privado para leer el archivo de ventas"""
        return cargar_datos(config.RUTA_VENTAS)

    def _guardar_ventas(self, ventas):
        """Método privado para escribir en el archivo de ventas"""
        guardar_datos(config.RUTA_VENTAS, ventas)


    def realizar_venta(self, nombre_producto, cantidad):
        """
        Registra una venta si el producto existe y hay stock.
        Actualiza el inventario y guarda la transacción.
        """
        producto = self.inventario_service.buscar_producto(nombre_producto)

        
        if not producto:
            print("El producto no existe.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if cantidad > producto.cantidad:
            print(f"No hay suficiente stock. Disponible: {producto.cantidad}")
            return

        # Calcular ID nuevo (Autoincremental: busca el máximo actual y suma 1)
        ventas = self._cargar_ventas()
        nuevo_id = 1
        if ventas:
            nuevo_id = max(v.get("id", 0) for v in ventas) + 1

        # Generar registro de venta
        total = cantidad * producto.precio
        nueva_venta = {
            "id": nuevo_id,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Fecha y hora actual
            "producto": nombre_producto,
            "cantidad": cantidad,
            "total": total
        }

        # Actualizar stock en el inventario real
        producto.cantidad -= cantidad 
        self.inventario_service.actualizar_stock(nombre_producto, producto.cantidad)

        # Guardar venta en el historial
        ventas.append(nueva_venta)
        self._guardar_ventas(ventas)
        print(f"Venta #{nuevo_id} registrada. Total: ${total}")

    def listar_ventas(self):
        """Muestra todas las ventas realizadas."""
        ventas = self._cargar_ventas()
        if not ventas:
            print("No hay ventas registradas.")
        else:
            print("\n--- Historial de Ventas ---")
            for v in ventas:
                print(f"ID: {v.get('id', '?')} | Fecha: {v['fecha']} | Producto: {v['producto']} | Qty: {v['cantidad']} | Total: ${v['total']}")

    def buscar_venta(self, id_venta):
        """Busca una venta específica por su ID."""
        ventas = self._cargar_ventas()
        for v in ventas:
            if v.get("id") == id_venta:
                return v
        return None

    def eliminar_venta(self, id_venta):
        """
        Elimina una venta del historial y DEVUELVE el stock al inventario.
        Útil si hubo un error en la venta.
        """
        ventas = self._cargar_ventas()
        venta_a_borrar = None
        
        # Buscar venta
        for v in ventas:
            if v.get("id") == id_venta:
                venta_a_borrar = v
                break
        
        if not venta_a_borrar:
            print("Venta no encontrada.")
            return

        # Devolver stock al inventario
        producto = self.inventario_service.buscar_producto(venta_a_borrar["producto"])
        if producto:
            nuevo_stock = producto.cantidad + venta_a_borrar["cantidad"]
            self.inventario_service.actualizar_stock(producto.nombre, nuevo_stock)

        # Eliminar de la lista y guardar
        ventas.remove(venta_a_borrar)
        self._guardar_ventas(ventas)
        print(f"Venta #{id_venta} eliminada y stock devuelto.")

    def actualizar_venta(self, id_venta, nueva_cantidad):
        """
        Modifica la cantidad de productos de una venta ya realizada.
        Ajusta el inventario según corresponda (si aumentas venta, baja stock; si bajas venta, sube stock).
        """
        ventas = self._cargar_ventas()
        idx_venta = -1
        
        for i, v in enumerate(ventas):
            if v.get("id") == id_venta:
                idx_venta = i
                break
        
        if idx_venta == -1:
            print("Venta no encontrada.")
            return

        venta_actual = ventas[idx_venta]
        producto_nombre = venta_actual["producto"]
        producto = self.inventario_service.buscar_producto(producto_nombre)

        if not producto:
            print("Producto asociado ya no existe en inventario.")
            return

        # Calcular diferencia de stock necesario
        # Si tenía 5 y ahora quiero 8, necesito 3 más. (diff = 3)
        # Si tenía 5 y ahora quiero 2, sobran 3 (diff = -3)
        diferencia = nueva_cantidad - venta_actual["cantidad"]

        if diferencia > 0 and producto.cantidad < diferencia:
            print(f"No hay stock suficiente para aumentar la venta. Disponible extra: {producto.cantidad}")
            return

        # Actualizar stock
        producto.cantidad -= diferencia
        self.inventario_service.actualizar_stock(producto_nombre, producto.cantidad)

        # Actualizar datos venta
        venta_actual["cantidad"] = nueva_cantidad
        venta_actual["total"] = nueva_cantidad * producto.precio
        
        self._guardar_ventas(ventas)
        print(f"Venta #{id_venta} actualizada. Nuevo total: ${venta_actual['total']}")
