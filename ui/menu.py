"""
INTERFAZ DE USUARIO

Responsabilidades:
- Mostrar un menú principal con opciones CRUD para inventario y ventas.
- Solicitar y validar la opción seleccionada por el usuario.
- Invocar los métodos adecuados de los servicios (inventario y venta) según la elección.
- Manejar la entrada de datos (nombre de producto, cantidad, etc) y mostrar resultados.
- Permitir salir de la aplicación.
"""

# Dependencias y mapeos (sin implementar lógica aún)
import sys

def mostrar_menu(inventario_service, venta_service):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar stock")
        print("4. Listar productos")
        print("5. Vender producto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            cant = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario_service.agregar_producto(nombre, cant, precio)

        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            prod = inventario_service.buscar_producto(nombre)
            if prod:
                print(f"Encontrado: {prod}")
            else:
                print("No existe.")

        elif opcion == '3':
            nombre = input("Nombre: ")
            cant = int(input("Nueva cantidad: "))
            inventario_service.actualizar_stock(nombre, cant)

        elif opcion == '4':
            inventario_service.listar_productos()

        elif opcion == '5':
            nombre = input("Producto: ")
            cant = int(input("Cantidad: "))
            venta_service.realizar_venta(nombre, cant)

        elif opcion == '6':
            print("Adiós!")
            sys.exit()
        
        else:
            print("Opción no válida.")
