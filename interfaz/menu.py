"""
INTERFAZ DE USUARIO (Menú)
--------------------------
Este archivo controla lo que ves en la pantalla cuando ejecutas el programa.
Muestra las opciones y recibe lo que escribas para saber qué hacer.
"""

import sys  # Importamos la librería 'sys' para poder cerrar el programa limpiamente (sys.exit)

# --- Funciones para el Menú de Inventario ---

def opcion_agregar_producto(servicio):
    """Pide datos al usuario y llama al servicio para agregar un producto."""
    nombre = input("Nombre del producto: ")
    try:
        cantidad = int(input("Cantidad inicial: "))
        precio = float(input("Precio unitario: "))
        servicio.agregar_producto(nombre, cantidad, precio)
    except ValueError:
        print("¡Error! Debes ingresar números válidos para cantidad y precio.")

def opcion_buscar_producto(servicio):
    """Pide un nombre y busca si el producto existe."""
    nombre = input("Nombre a buscar: ")
    producto = servicio.buscar_producto(nombre)
    if producto:
        print(f"-> Encontrado: {producto.convertir_a_texto()}")
    else:
        print("-> El producto no está en el inventario.")

def opcion_actualizar_stock(servicio):
    """Pide un nombre y una nueva cantidad para actualizar el stock."""
    nombre = input("Nombre del producto: ")
    try:
        cantidad = int(input("Nueva cantidad total: "))
        servicio.actualizar_stock(nombre, cantidad)
    except ValueError:
        print("¡Error! La cantidad debe ser un número entero.")

def opcion_listar_productos(servicio):
    """Muestra todos los productos."""
    servicio.listar_productos()

# --- Funciones para el Menú de Ventas ---

def opcion_nueva_venta(servicio):
    """Registra una venta pidiendo producto y cantidad."""
    nombre = input("Nombre del producto a vender: ")
    try:
        cantidad = int(input("Cantidad a vender: "))
        servicio.realizar_venta(nombre, cantidad)
    except ValueError:
        print("¡Error! La cantidad debe ser un número entero.")

def opcion_listar_ventas(servicio):
    """Muestra el historial."""
    servicio.listar_ventas()

def opcion_editar_venta(servicio):
    """Permite corregir una venta anterior."""
    try:
        id_venta = int(input("ID de la venta a editar: "))
        nueva_cant = int(input("Nueva cantidad real: "))
        servicio.actualizar_venta(id_venta, nueva_cant)
    except ValueError:
        print("¡Error! Debes ingresar números enteros.")

def opcion_eliminar_venta(servicio):
    """Borra una venta del historial."""
    try:
        id_venta = int(input("ID de la venta a eliminar: "))
        servicio.eliminar_venta(id_venta)
    except ValueError:
        print("¡Error! El ID debe ser un número.")

# --- Estructura de los Menús ---



def mostrar_menu_inventario(servicio_inventario):
    """
    Función que maneja las opciones de inventario.
    """
    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar stock")
        print("4. Listar productos")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            opcion_agregar_producto(servicio_inventario)
        elif opcion == '2':
            opcion_buscar_producto(servicio_inventario)
        elif opcion == '3':
            opcion_actualizar_stock(servicio_inventario)

        elif opcion == '4':
            opcion_listar_productos(servicio_inventario)
        elif opcion == '5':
            # "break" sale de la función actual y el programa continúa donde se llamó
            break
        else:
            print("Opción no válida, intenta de nuevo.")



def mostrar_menu_ventas(servicio_ventas):
    """
    Función que maneja las opciones de ventas.
    """
    while True:
        print("\n--- GESTIÓN DE VENTAS ---")
        print("1. Registrar nueva venta")
        print("2. Listar historial de ventas")
        print("3. Editar venta")
        print("4. Eliminar venta")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            opcion_nueva_venta(servicio_ventas)
        elif opcion == '2':
            opcion_listar_ventas(servicio_ventas)
        elif opcion == '3':
            opcion_editar_venta(servicio_ventas)

        elif opcion == '4':
            opcion_eliminar_venta(servicio_ventas)
        elif opcion == '5':
            # "break" sale de la función actual y el programa vuelve al menú principal
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def mostrar_menu(servicio_inventario, servicio_ventas):
    """
    Menú Principal.
    """
    while True:
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Inventario (Productos)")
        print("2. Ventas (Caja)")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_menu_inventario(servicio_inventario)
        elif opcion == '2':
            mostrar_menu_ventas(servicio_ventas)
        elif opcion == '3':
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida.")
