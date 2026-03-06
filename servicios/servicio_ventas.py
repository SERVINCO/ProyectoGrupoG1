"""
SERVICIO DE VENTAS - PREPARADO PARA AVANCES FUTUROS
----------------------------------------------------
Este archivo contiene la lógica de negocio para gestionar ventas y transacciones.

AVANCE No. 2: Este archivo NO se usa todavía.

PRÓXIMOS AVANCES (4+):
=======================
Este servicio manejará todas las operaciones relacionadas con ventas,
registro de transacciones y cálculos monetarios.

RESPONSABILIDADES:
-----------------
1. Registrar ventas de productos
2. Actualizar inventario automáticamente al vender
3. Calcular totales y subtotales
4. Mantener historial de ventas
5. Generar reportes de ventas
6. Permitir corrección/eliminación de ventas

MÉTODOS A IMPLEMENTAR:
---------------------
### Gestión de Ventas:
- realizar_venta(nombre_producto, cantidad): Registrar nueva venta
- listar_ventas(): Mostrar historial completo de ventas
- buscar_venta(id): Buscar venta específica por ID
- actualizar_venta(id, cantidad): Corregir cantidad de una venta
- eliminar_venta(id): Anular venta y devolver stock

### Cálculos:
- calcular_total_venta(producto, cantidad): Calcular monto de venta
- total_ventas_dia(): Sumar ventas del día actual
- total_ventas_mes(): Sumar ventas del mes actual
- promedio_ventas(): Calcular promedio de ventas

### Persistencia:
- cargar_ventas(): Leer ventas desde JSON
- guardar_ventas(): Escribir ventas a JSON

### Reportes:
- generar_reporte_ventas(): Resumen de todas las ventas
- productos_mas_vendidos(): Ranking de productos
- ventas_por_periodo(inicio, fin): Ventas en rango de fechas

CONEXIONES FUTURAS:
------------------
IMPORTA:
- servicios.servicio_inventario: Para verificar y actualizar stock
- utils.archivos: Para leer/escribir JSON de ventas
- configuracion: Rutas y constantes
- datetime: Para registrar fecha/hora de ventas

USADO POR:
- interfaz.menu: Opciones de menú de ventas

ARCHIVOS DE DATOS:
- Lee/Escribe: base_de_datos/ventas.json

ESTRUCTURA DE UNA VENTA:
------------------------
{
    "id": 1,
    "producto": "Leche",
    "cantidad": 5,
    "precio_unitario": 1500.00,
    "total": 7500.00,
    "fecha": "2026-03-06 14:30:00"
}

EJEMPLO DE USO FUTURO:
---------------------
>>> servicio_inv = ServicioInventario()
>>> servicio_ventas = ServicioVentas(servicio_inv)
>>> 
>>> # Realizar una venta
>>> servicio_ventas.realizar_venta("Leche", 5)
✓ Venta registrada: 5 unidades de Leche por ₡7,500.00
✓ Stock actualizado: Leche ahora tiene 45 unidades
>>>
>>> # Ver historial
>>> servicio_ventas.listar_ventas()
ID | Producto | Cantidad | Total    | Fecha
1  | Leche    | 5        | ₡7500.00 | 06/03/2026 14:30
>>>
>>> # Corregir venta (si se equivocaron en cantidad)
>>> servicio_ventas.actualizar_venta(1, 3)
✓ Venta actualizada: Nueva cantidad = 3
✓ Stock devuelto: +2 unidades de Leche
>>>
>>> # Eliminar venta (anular transacción)
>>> servicio_ventas.eliminar_venta(1)
✓ Venta eliminada
✓ Stock devuelto: +3 unidades de Leche

FLUJO DE VENTA:
--------------
1. Usuario selecciona "Registrar venta" en menú
2. Ingresa nombre de producto y cantidad
3. Servicio busca producto en inventario
4. Valida que hay suficiente stock
5. Calcula el total (cantidad × precio)
6. Descuenta del inventario
7. Registra la venta con fecha/hora
8. Guarda en ventas.json
9. Actualiza productos.json
10. Muestra confirmación al usuario

VALIDACIONES DE NEGOCIO:
------------------------
- Producto debe existir en inventario
- Cantidad debe ser mayor a 0
- Debe haber suficiente stock disponible
- No permitir ventas con datos incompletos
- Al actualizar venta, devolver diferencia al stock
- Al eliminar venta, devolver todo el stock

INTEGRACIÓN CON INVENTARIO:
---------------------------
Este servicio DEPENDE de ServicioInventario:
- Para verificar existencia de productos
- Para obtener precios actuales
- Para actualizar stock después de vender
- Para validar disponibilidad

REPORTES Y ESTADÍSTICAS:
-----------------------
- Total de ventas por día/semana/mes
- Producto más vendido
- Ingresos totales
- Promedio de venta
- Historial completo de transacciones

ESTADO: 💤 Preparado pero no implementado (Avance No. 2)
PRIORIDAD: ⭐⭐ Media (necesario para Avance 4+)
DEPENDENCIAS: Requiere ServicioInventario funcionando
"""

# Placeholder: La implementación real se agregará en avances futuros
# Por ahora, solo existe la documentación de lo que contendrá

class ServicioVentas:
    """
    Servicio placeholder para futuros avances.
    La implementación completa se agregará cuando se requiera en Avance 4+.
    """
    pass
