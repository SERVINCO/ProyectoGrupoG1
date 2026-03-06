"""
ARCHIVO PRINCIPAL - AVANCE No. 2
---------------------------------
Sistema de Gestión de Inventario
Menú de la solución programada

Integrantes del Grupo G1:
Luis Alexander Rodríguez Zamora
Gabriel Venegas Jarquin
Demian Rendina Binns
NANCY FABIOLA JARA HERNANDEZ
JOSE DANIEL VILLALOBOS CABRERA

Fecha: 6 de marzo de 2026

AVANCE No. 2: Este avance implementa el menú con opciones de Incluir, Consultar,
Modificar, Borrar y Salir. Las funcionalidades completas se desarrollarán en
avances posteriores.
"""

from interfaz.menu import mostrar_menu # Importamos la función del menú principal

def principal():
    """
    Función principal que inicia el programa.
    Muestra el mensaje de bienvenida y ejecuta el menú.
    """
    print("\n" + "="*60)
    print("   SISTEMA DE GESTIÓN DE INVENTARIO")
    print("   Avance No. 2 - Menú de la solución programada")
    print("="*60)
    
    # Ejecutamos el menú principal
    mostrar_menu()
    
    print("\nPrograma finalizado exitosamente.")
    print("="*60)

# Si ejecutamos este archivo directamente...
if __name__ == "__main__":
    principal()
