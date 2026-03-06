# Sistema de Gestión de Inventario - Proyecto Grupo G1

## ⚠️ AVANCE No. 2 - Menú de la solución programada

**Estado actual:** Este proyecto se encuentra en la fase de **Avance No. 2**.

### 📋 Sobre este Avance

Este avance implementa el **menú principal** del sistema con las siguientes características:

**✅ Opciones implementadas:**
1. **Incluir** - Para agregar nuevos datos
2. **Consultar** - Para ver información
3. **Modificar** - Para actualizar datos
4. **Borrar** - Para eliminar información
5. **Salir** - Para cerrar el programa

**🎯 Cumplimiento de la rúbrica (10 puntos):**
- ✅ Menú con las 5 opciones solicitadas (1 punto)
- ✅ Ejecución múltiple hasta seleccionar "Salir" (3 puntos)
- ✅ Uso de ciclos `while` (2 puntos)
- ✅ Uso de estructuras de decisión `if-elif-else` (2 puntos)
- ✅ Variables e identificadores correctos (2 puntos)

**📝 Nota importante:** Las funcionalidades completas (guardar datos, validaciones, etc.) se implementarán en avances posteriores. Actualmente, cada opción muestra mensajes informativos indicando que están "En desarrollo".

---

## 🚀 ¿Cómo ejecutar el programa?

### Requisitos
- Python 3.x instalado

### Pasos

1. Abrir una terminal en la carpeta del proyecto

2. Ejecutar:
   ```bash
   python3 principal.py
   ```

3. Interactuar con el menú seleccionando opciones (1-5)

4. Para salir, seleccionar la opción **5. Salir**

---

## 📁 Estructura del Proyecto

```
ProyectoGrupoG1/
├── principal.py              # Punto de entrada del programa
├── configuracion.py          # Configuraciones (para avances futuros)
├── README.md                 # Este archivo
├── base_de_datos/            # Almacenamiento (para avances futuros)
│   ├── productos.json
│   └── ventas.json
├── interfaz/                 # Interfaz de usuario
│   ├── menu.py              # Menú principal ⭐ (AVANCE 2)
│   └── menu_completo_backup.py  # Backup del menú completo original
├── modelos/                  # Clases de datos (para avances futuros)
│   ├── producto.py
│   └── inventario.py
├── servicios/                # Lógica de negocio (para avances futuros)
│   ├── servicio_inventario.py
│   └── servicio_ventas.py
└── utils/                    # Utilidades (para avances futuros)
    └── archivos.py
```

**Archivos clave para el Avance No. 2:**
- `principal.py` - Inicia el programa
- `interfaz/menu.py` - Contiene el menú con las 5 opciones

---

## 👥 Integrantes del Grupo

**IMPORTANTE:** Antes de entregar, editar el archivo `principal.py` y agregar los nombres de los integrantes en las líneas 7-9.

---

## 🔄 Próximos Avances

En futuros avances se implementará:

### Avance 3 (esperado)
- Implementación real de la opción "Incluir"
- Guardado de datos en archivos JSON
- Validación de entradas

### Avance 4 (esperado)
- Implementación de "Consultar"
- Lectura de datos guardados
- Búsqueda de información

### Proyecto Final
- Todas las funcionalidades completas
- Sistema completo de inventario y ventas
- Reportes y estadísticas

---

## 🎓 Contexto Académico

**Curso:** Lógica de Programación  
**Actividad:** Avance No. 2 de la solución programada  
**Fecha:** 6 de marzo de 2026  
**Puntuación:** 10 puntos

---

## 📝 Notas Técnicas

### Conceptos aplicados en este avance:

1. **Ciclos (while)**
   - Ciclo principal en el menú
   - Ciclos en cada submenú
   - Variables de control booleanas

2. **Estructuras de decisión (if-elif-else)**
   - Manejo de opciones del menú
   - Validación de entradas
   - Navegación entre menús

3. **Variables**
   - Booleanas: `continuar_programa`, `en_submenu`, `continuar_consultando`, etc.
   - String: `opcion_principal`, `opcion`, `opcion_consulta`, etc.
   - Nombres descriptivos y significativos

4. **Funciones**
   - `mostrar_menu()`: Menú principal
   - `opcion_incluir()`: Submenú de inclusión
   - `opcion_consultar()`: Submenú de consultas
   - `opcion_modificar()`: Submenú de modificaciones
   - `opcion_borrar()`: Submenú de borrado

---

## 🔧 Resolución de Problemas

### Si aparece "ModuleNotFoundError"
Es normal en este avance. Los módulos de `servicios`, `modelos` y `utils` se utilizarán en avances futuros.

### Si el programa no inicia
```bash
# Verificar que estás en la carpeta correcta
cd /Users/admin/Documents/Personal/ProyectoGrupoG1

# Verificar versión de Python
python3 --version

# Ejecutar el programa
python3 principal.py
```

---

## 📚 Recursos

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- Apuntes del curso de Lógica de Programación
- Guía de buenas prácticas en identificadores

---

**⚠️ Recordatorio:** Este es un proyecto en desarrollo. La versión actual cumple con los requisitos del **Avance No. 2**. Las funcionalidades completas se agregarán progresivamente en los siguientes avances.


