"""
SERVICIO VENTAS

Responsabilidades:
- Gestionar la creación de ventas asociadas a productos existentes.
- Verificar que el stock disponible sea suficiente antes de registrar una venta.
- Actualizar el inventario al descontar las unidades vendidas.
- Validar datos de entrada y manejar errores como producto no encontrado o stock insuficiente.
- Generar un registro de la venta para su almacenamiento.
"""

class VentaService:
    def __init__(self, inventario_service):
        self.inventario_service = inventario_service

    def realizar_venta(self, nombre_producto, cantidad):
        producto = self.inventario_service.buscar_producto(nombre_producto)
        
        if not producto:
            print("El producto no existe.")
            return

        if cantidad > producto.cantidad:
            print(f"No hay suficiente stock. Disponible: {producto.cantidad}")
            return

        # Restamos stock
        nuevo_stock = producto.cantidad - cantidad
        self.inventario_service.actualizar_stock(nombre_producto, nuevo_stock)
        
        total = cantidad * producto.precio
        print(f"Venta realizada. Total a pagar: ${total}")
