"""
PUNTO DE ENTRADA DEL SISTEMA
"""

from services.inventario_service import InventarioService
from services.venta_service import VentaService
from ui.menu import mostrar_menu

def main():
    # Creamos los servicios
    servicio_inventario = InventarioService()
    servicio_venta = VentaService(servicio_inventario)
    
    # Iniciamos el menú
    mostrar_menu(servicio_inventario, servicio_venta)

if __name__ == "__main__":
    main()
