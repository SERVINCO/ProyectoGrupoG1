# Sistema de Gestión de Inventario - Proyecto Grupo G1

¡Bienvenido! Este es un sistema sencillo para controlar el inventario y las ventas de un negocio (como una pulpería o tienda pequeña).

## ¿Qué hace el sistema?

Permite administrar productos y realizar ventas, guardando toda la información automáticamente para que no se pierda.

### Funcionalidades principales

1. **Inventario**
   - Agregar productos nuevos.
   - Buscar productos por nombre.
   - Actualizar la cantidad de stock disponible.
   - Ver la lista completa de productos.

2. **Ventas**
   - Registrar ventas (se descuenta el stock automáticamente).
   - Ver historial de todas las ventas realizadas.
   - Editar ventas (si te equivocaste en la cantidad).
   - Eliminar ventas (devuelve los productos al inventario).

## Estructura del Proyecto

El código está organizado en carpetas para que sea ordenado y fácil de entender:

- **`base_de_datos/`**: Aquí se guardan los archivos `.json` con la información de productos y ventas.
- **`interfaz/`**: Contiene el menú principal que ves en la pantalla.
- **`modelos/`**: Define qué es un "Producto" y cómo funciona el "Inventario".
- **`servicios/`**: Contiene la lógica del negocio (reglas de cómo agregar, vender, validar, etc.).
- **`utils/`**: Herramientas para guardar y leer archivos.
- **`principal.py`**: El archivo que inicia el programa.
- **`configuracion.py`**: Configuraciones generales (rutas de archivos).

## Requisitos

- Tener instalado **Python 3**.

## ¿Cómo ejecutarlo?

Abre una terminal en la carpeta del proyecto y escribe:

```bash
python3 principal.py
```

## Integrantes del Grupo


