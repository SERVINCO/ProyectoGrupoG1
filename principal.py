"""
ARCHIVO PRINCIPAL
-----------------
Este es el punto de inicio. Aquí arranca todo el programa.
Conecta las partes principales (Inventario, Ventas y Menú) y le da 'play'.
"""

from servicios.servicio_inventario import ServicioInventario # Importamos la lógica de productos
from servicios.servicio_ventas import ServicioVentas # Importamos la lógica de ventas
from interfaz.menu import mostrar_menu # Importamos la función para iniciar el menú visual

def principal():
    # 1. Preparamos el servicio de inventario (quien maneja los productos)
    servicio_inventario = ServicioInventario()
    
    # 2. Preparamos el servicio de ventas (quien maneja el dinero), 
    #    que necesita saber del inventario para descontar productos.
    servicio_ventas = ServicioVentas(servicio_inventario)
    
    # 3. Lanzamos el menú para que el usuario pueda usar el programa.
    mostrar_menu(servicio_inventario, servicio_ventas)

# Si ejecutamos este archivo directamentes...
if __name__ == "__main__":
    principal()
