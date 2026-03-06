"""
MANEJO DE ARCHIVOS (UTILIDADES)
-------------------------------
Funciones para leer y escribir en los archivos JSON donde se guardan los datos.
"""

import json # Librería estándar de Python para manejar el formato JSON
import os   # Librería para interactuar con el sistema operativo (archivos, carpetas)


def cargar_datos(ruta_archivo):
    """
    Intenta leer un archivo JSON y devuelve la lista de datos.
    Si el archivo no existe o hay error, devuelve una lista vacía.
    """
    if not os.path.exists(ruta_archivo):
        return []
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_datos(ruta_archivo, datos):
    """
    Guarda una lista de datos en un archivo JSON.
    Si la carpeta que contiene el archivo no existe, la crea.
    """
    # Verificamos si la carpeta existe, si no, la creamos
    carpeta = os.path.dirname(ruta_archivo)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)
        
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        # indent=4 hace que el archivo se vea bonito y ordenado
        json.dump(datos, archivo, indent=4)
