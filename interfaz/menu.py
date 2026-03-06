"""
INTERFAZ DE USUARIO (Menú) - AVANCE No. 2

Este archivo controla el menú principal y los submenús del sistema.
Este archivo controla lo que ves en la pantalla cuando ejecutas el programa.

Implementa las opciones: Incluir, Consultar, Modificar, Borrar y Salir.
Muestra las opciones y recibe lo que escribas para saber qué hacer.

NOTA: Este es el Avance No. 2 del proyecto.
Las funcionalidades completas (guardar datos, validaciones avanzadas, etc.)
se implementarán en avances futuros.

Por ahora, cada opción muestra un mensaje informativo.
"""

import sys


# =============================================================================
# FUNCIONES PARA CADA OPCIÓN DEL MENÚ PRINCIPAL
# =============================================================================

def opcion_incluir():
    """
    Opción 1: INCLUIR
    Permite incluir nuevos datos en el sistema.
    Funcionalidad completa se desarrollará en avances futuros.
    """
    en_submenu = True

    while en_submenu:
        print("\n" + "-" * 50)
        print("   OPCIÓN: INCLUIR DATOS")
        print("-" * 50)
        print("1. Incluir producto")
        print("2. Incluir información del encargado")
        print("3. Incluir cantidad de producción")
        print("4. Volver al menú principal")
        print("-" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n[INCLUIR PRODUCTO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion == '2':
            print("\n[INCLUIR INFORMACIÓN DEL ENCARGADO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion == '3':
            print("\n[INCLUIR CANTIDAD DE PRODUCCIÓN]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion == '4':
            en_submenu = False
            print("\nRegresando al menú principal...")

        else:
            print("\nOpción no válida. Intente nuevamente.")


def opcion_consultar():
    """
    Opción 2: CONSULTAR
    Permite consultar información del sistema.
    Funcionalidad completa se desarrollará en avances futuros.
    """
    continuar_consultando = True

    while continuar_consultando:
        print("\n" + "-" * 50)
        print("   OPCIÓN: CONSULTAR DATOS")
        print("-" * 50)
        print("1. Consultar producto específico")
        print("2. Consultar todos los productos")
        print("3. Consultar producción mensual")
        print("4. Reporte de productos en stock")
        print("5. Volver al menú principal")
        print("-" * 50)

        opcion_consulta = input("Seleccione una opción: ")

        if opcion_consulta == '1':
            print("\n[CONSULTAR PRODUCTO ESPECÍFICO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_consulta == '2':
            print("\n[CONSULTAR TODOS LOS PRODUCTOS]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_consulta == '3':
            print("\n[CONSULTAR PRODUCCIÓN MENSUAL]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_consulta == '4':
            print("\n[REPORTE DE PRODUCTOS EN STOCK]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_consulta == '5':
            continuar_consultando = False
            print("\nRegresando al menú principal...")

        else:
            print("\nOpción no válida. Intente nuevamente.")


def opcion_modificar():
    """
    Opción 3: MODIFICAR
    Permite modificar datos existentes en el sistema.
    Funcionalidad completa se desarrollará en avances futuros.
    """
    en_modificacion = True

    while en_modificacion:
        print("\n" + "-" * 50)
        print("   OPCIÓN: MODIFICAR DATOS")
        print("-" * 50)
        print("1. Modificar información de producto")
        print("2. Modificar cantidad en stock")
        print("3. Modificar precio de producto")
        print("4. Volver al menú principal")
        print("-" * 50)

        opcion_mod = input("Seleccione una opción: ")

        if opcion_mod == '1':
            print("\n[MODIFICAR INFORMACIÓN DE PRODUCTO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_mod == '2':
            print("\n[MODIFICAR CANTIDAD EN STOCK]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_mod == '3':
            print("\n[MODIFICAR PRECIO DE PRODUCTO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_mod == '4':
            en_modificacion = False
            print("\nRegresando al menú principal...")

        else:
            print("\nOpción no válida. Intente nuevamente.")


def opcion_borrar():
    """
    Opción 4: BORRAR
    Permite borrar datos del sistema.
    Funcionalidad completa se desarrollará en avances futuros.
    """
    en_borrado = True

    while en_borrado:
        print("\n" + "-" * 50)
        print("   OPCIÓN: BORRAR DATOS")
        print("-" * 50)
        print("1. Borrar producto")
        print("2. Borrar registro de venta")
        print("3. Borrar todos los datos")
        print("4. Volver al menú principal")
        print("-" * 50)

        opcion_borrar_menu = input("Seleccione una opción: ")

        if opcion_borrar_menu == '1':
            print("\n[BORRAR PRODUCTO]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_borrar_menu == '2':
            print("\n[BORRAR REGISTRO DE VENTA]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_borrar_menu == '3':
            print("\n[BORRAR TODOS LOS DATOS]")
            print("OPCIÓN NO IMPLEMENTADA")
            print("Esta funcionalidad se desarrollará en avances futuros.")

        elif opcion_borrar_menu == '4':
            en_borrado = False
            print("\nRegresando al menú principal...")

        else:
            print("\nOpción no válida. Intente nuevamente.")


# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def mostrar_menu():
    """
    Menú Principal del Sistema.

    Utiliza un ciclo while para ejecutarse las veces que el usuario desee,
    hasta que seleccione la opción 'Salir'.

    CUMPLE CON LA RÚBRICA DEL AVANCE No. 2:
    - Menú con las 5 opciones solicitadas
    - Se ejecuta las veces que el usuario desea sin error
    - Utiliza ciclos en la solución
    - Utiliza estructuras de decisión
    - Uso correcto de variables e identificadores
    """
    continuar_programa = True

    while continuar_programa:
        print("\n" + "=" * 50)
        print("              MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Incluir")
        print("2. Consultar")
        print("3. Modificar")
        print("4. Borrar")
        print("5. Salir")
        print("=" * 50)

        opcion_principal = input("Seleccione una opción (1-5): ")

        if opcion_principal == '1':
            opcion_incluir()

        elif opcion_principal == '2':
            opcion_consultar()

        elif opcion_principal == '3':
            opcion_modificar()

        elif opcion_principal == '4':
            opcion_borrar()

        elif opcion_principal == '5':
            print("\n" + "=" * 50)
            print("   ¡Gracias por usar el sistema!")
            print("   Cerrando el programa...")
            print("=" * 50)
            continuar_programa = False
            sys.exit(0)

        else:
            print("\nOpción no válida.")
            print("Por favor, seleccione una opción entre 1 y 5.")


# =============================================================================
# EJECUCIÓN DEL PROGRAMA
# =============================================================================

mostrar_menu()