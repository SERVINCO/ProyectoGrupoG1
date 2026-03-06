"""
PERSISTENCIA JSON

Responsabilidades:
- Leer y escribir datos en un archivo JSON (por ejemplo inventario y/o ventas).
- Proveer métodos genéricos cargar_datos() y guardar_datos(diccionario).
- Manejar el caso en el que el archivo no exista creando uno nuevo o devolviendo estructuras vacías.
- Centralizar el acceso al almacenamiento para que los servicios no manipulen archivos directamente.
"""

# Dependencias y mapeos (sin implementar lógica aún)
import json
import os

# Funciones simples para leer y guardar archivos
def cargar_datos(ruta_archivo):
    # Si el archivo no existe, retornamos una lista vacía
    if not os.path.exists(ruta_archivo):
        return []
    
    try:
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_datos(ruta_archivo, datos):
    # Nos aseguramos que la carpeta exista (por si acaso)
    carpeta = os.path.dirname(ruta_archivo)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)
        
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
