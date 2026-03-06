"""
UTILIDADES PARA MANEJO DE ARCHIVOS - PREPARADO PARA AVANCES FUTUROS
---------------------------------------------------------------------
Este archivo contiene funciones auxiliares para leer y escribir datos en archivos JSON.

AVANCE No. 2: Este archivo NO se usa todavía.

PRÓXIMOS AVANCES (3+):
=======================
Este módulo proporciona funciones reutilizables para persistir datos del
sistema en archivos JSON.

FUNCIONES A IMPLEMENTAR:
------------------------

### cargar_datos(ruta_archivo)
Descripción: Lee un archivo JSON y devuelve los datos como lista/diccionario
Parámetros: 
  - ruta_archivo (str): Ruta al archivo JSON
Retorna: list o dict con los datos, o [] si el archivo no existe
Maneja: FileNotFoundError, JSONDecodeError

Ejemplo futuro:
>>> productos = cargar_datos("base_de_datos/productos.json")
>>> print(productos)
[
    {"nombre": "Leche", "cantidad": 50, "precio": 1500},
    {"nombre": "Pan", "cantidad": 100, "precio": 800}
]

### guardar_datos(ruta_archivo, datos)
Descripción: Escribe datos en un archivo JSON de forma legible
Parámetros:
  - ruta_archivo (str): Ruta donde guardar el archivo
  - datos (list/dict): Datos a guardar
Retorna: None
Opciones: indent=4 para formato legible

Ejemplo futuro:
>>> productos = [
...     {"nombre": "Leche", "cantidad": 50, "precio": 1500}
... ]
>>> guardar_datos("base_de_datos/productos.json", productos)
✓ Datos guardados correctamente

### verificar_archivo_existe(ruta_archivo)
Descripción: Verifica si un archivo existe antes de intentar leerlo
Parámetros:
  - ruta_archivo (str): Ruta al archivo
Retorna: bool (True si existe, False si no)

Ejemplo futuro:
>>> if verificar_archivo_existe("base_de_datos/productos.json"):
...     datos = cargar_datos("base_de_datos/productos.json")
... else:
...     print("Archivo no encontrado, creando uno nuevo...")

### crear_archivo_vacio(ruta_archivo)
Descripción: Crea un archivo JSON vacío con estructura inicial
Parámetros:
  - ruta_archivo (str): Ruta del archivo a crear
Retorna: None

Ejemplo futuro:
>>> crear_archivo_vacio("base_de_datos/productos.json")
✓ Archivo creado con estructura inicial: []

MANEJO DE ERRORES:
-----------------
Las funciones manejarán errores comunes:
- FileNotFoundError: Archivo no existe → Devolver lista vacía o crear archivo
- JSONDecodeError: JSON inválido → Mostrar error y devolver lista vacía
- PermissionError: Sin permisos → Notificar al usuario
- IOError: Error de lectura/escritura → Mostrar mensaje apropiado

CONEXIONES FUTURAS:
------------------
USADO POR:
- servicios.servicio_inventario: Para productos.json
- servicios.servicio_ventas: Para ventas.json

ARCHIVOS DE DATOS:
- base_de_datos/productos.json: Inventario de productos
- base_de_datos/ventas.json: Historial de ventas

FORMATO DE ARCHIVOS JSON:
-------------------------

productos.json:
[
    {
        "nombre": "Leche",
        "cantidad": 50,
        "precio": 1500.00
    },
    {
        "nombre": "Pan",
        "cantidad": 100,
        "precio": 800.00
    }
]

ventas.json:
[
    {
        "id": 1,
        "producto": "Leche",
        "cantidad": 5,
        "precio_unitario": 1500.00,
        "total": 7500.00,
        "fecha": "2026-03-06 14:30:00"
    }
]

FLUJO DE USO:
-------------
1. Servicio necesita cargar datos
2. Llama a cargar_datos(ruta)
3. Función verifica si archivo existe
4. Si existe: lee y parsea JSON
5. Si no existe: devuelve lista vacía []
6. Servicio trabaja con datos en memoria
7. Al hacer cambios, llama a guardar_datos(ruta, datos)
8. Función escribe JSON con formato legible
9. Datos persisten en disco

BUENAS PRÁCTICAS:
-----------------
- Usar indent=4 para JSON legible
- Siempre usar encoding='utf-8' para caracteres especiales
- Manejar excepciones de forma apropiada
- Crear directorios si no existen
- Hacer backup antes de sobrescribir

DEPENDENCIAS:
-------------
- json: Librería estándar de Python para JSON
- os: Para verificar existencia de archivos y crear directorios
- pathlib: Para manejo moderno de rutas

EJEMPLO DE IMPLEMENTACIÓN FUTURA:
---------------------------------
import json
import os

def cargar_datos(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print(f"Error: Archivo {ruta_archivo} tiene formato inválido")
        return []

def guardar_datos(ruta_archivo, datos):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

"""

# Placeholder: La implementación real se agregará en avances futuros
# Por ahora, solo existe la documentación de lo que contendrá

# Las funciones se implementarán cuando se requieran en Avance 3+
