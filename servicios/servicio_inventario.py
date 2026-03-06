"""
SERVICIO DE INVENTARIO - PREPARADO PARA AVANCES FUTUROS
------------------------------------------------------

Este archivo contiene la lógica de negocio para gestionar el inventario.
Aquí estará toda la lógica para manejar los productos.

Es como el "cerebro" que controla el stock.

AVANCE No. 2:
Este archivo NO se usa todavía.
En avances futuros sabrá agregar productos, actualizarlos y guardarlos.

PRÓXIMOS AVANCES (3+):
- Este servicio será el "cerebro" que maneja todas las operaciones
  relacionadas con productos e inventario.

RESPONSABILIDADES:
1. CRUD de productos (crear, leer, actualizar, eliminar).
2. Persistencia de datos (guardar/cargar desde JSON).
3. Validaciones de negocio.
4. Gestión de stock (alertas de bajo inventario).
5. Cálculos y reportes.

MÉTODOS A IMPLEMENTAR:

Gestión de productos:
- agregar_producto(nombre, cantidad, precio)
- buscar_producto(nombre)
- actualizar_stock(nombre, cantidad)
- actualizar_precio(nombre, precio)
- eliminar_producto(nombre)
- listar_productos()

Persistencia:
- cargar_inventario()
- guardar_inventario()

Validaciones:
- validar_stock(nombre, cantidad)
- alertar_stock_bajo()
- validar_nombre_unico(nombre)

Reportes:
- generar_reporte_inventario()
- productos_mas_vendidos()
- valor_total_inventario()

CONEXIONES FUTURAS:
- modelos.inventario.Inventario: estructura de datos
- modelos.producto.Producto: modelo de producto
- utils.archivos: funciones para leer/escribir JSON
- configuracion: rutas y constantes

USADO POR:
- interfaz.menu: opciones del menú principal
- servicios.servicio_ventas: para verificar stock al vender

ARCHIVOS DE DATOS:
- Lee/Escribe: base_de_datos/productos.json

EJEMPLO DE USO FUTURO:
>>> servicio = ServicioInventario()
>>> servicio.agregar_producto("Leche", 50, 1500.00)
✓ Producto 'Leche' agregado correctamente
>>> servicio.actualizar_stock("Leche", 45)
✓ Stock actualizado: Leche ahora tiene 45 unidades
>>> producto = servicio.buscar_producto("Leche")
>>> print(producto.convertir_a_texto())
'Leche (Disponibles: 45) - ₡1500.00'

FLUJO DE DATOS:
1. Usuario selecciona "Incluir producto" en menú.
2. Menú llama a servicio.agregar_producto().
3. Servicio crea objeto Producto.
4. Servicio agrega a Inventario en memoria.
5. Servicio llama a guardar_inventario().
6. Utils.archivos escribe en productos.json.
7. Datos persisten en disco.

VALIDACIONES DE NEGOCIO:
- Stock no puede ser negativo.
- Precio debe ser mayor a cero.
- Nombre de producto no puede estar vacío.
- No permitir productos duplicados.
- Al eliminar, verificar que no tenga ventas pendientes.

ESTADO:
Preparado pero no implementado (Avance No. 2)

PRIORIDAD:
Alta (necesario para Avance 3)
"""


class ServicioInventario:
    """
    Servicio placeholder para futuros avances.

    La implementación completa se agregará cuando se requiera
    en el Avance 3 o posteriores.
    """

    pass