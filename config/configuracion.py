"""
CONFIGURACIÓN GENERAL - PREPARADO PARA AVANCES FUTUROS
-------------------------------------------------------
Contiene constantes y configuraciones globales del sistema.

AVANCE No. 2: Este archivo NO se usa todavía.

PRÓXIMOS AVANCES (3+):
=======================
Este archivo centralizará todas las configuraciones del sistema,
facilitando cambios y mantenimiento.

CONFIGURACIONES A USAR:
-----------------------
"""

# ============================================================================
# RUTAS DE ARCHIVOS DE DATOS
# ============================================================================
# Ubicación del archivo JSON que almacena los productos del inventario
RUTA_ARCHIVO = "base_de_datos/productos.json"

# Ubicación del archivo JSON que almacena el historial de ventas
RUTA_VENTAS = "base_de_datos/ventas.json"

# ============================================================================
# CONFIGURACIONES DE INVENTARIO
# ============================================================================
# Cantidad mínima de stock para generar alerta de inventario bajo
# Cuando un producto tenga esta cantidad o menos, se mostrará advertencia
STOCK_MINIMO = 5

# ============================================================================
# CONFIGURACIONES FUTURAS (Avance 3+)
# ============================================================================
# Estas constantes se activarán en avances futuros:

# FORMATO DE MONEDA
# SIMBOLO_MONEDA = "₡"  # Colones costarricenses
# DECIMALES = 2  # Cantidad de decimales para precios

# CONFIGURACIONES DE REPORTES
# ITEMS_POR_PAGINA = 10  # Productos a mostrar por página
# FORMATO_FECHA = "%d/%m/%Y %H:%M:%S"  # Formato de fecha/hora

# VALIDACIONES
# NOMBRE_MIN_LENGTH = 3  # Longitud mínima para nombre de producto
# NOMBRE_MAX_LENGTH = 50  # Longitud máxima para nombre de producto
# PRECIO_MINIMO = 1  # Precio mínimo permitido
# CANTIDAD_MAXIMA = 10000  # Cantidad máxima en inventario

"""
ESTADO: 💤 Preparado pero no implementado (Avance No. 2)
USADO POR: servicios/, utils/ (en avances futuros)
"""
