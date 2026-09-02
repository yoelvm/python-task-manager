# Python Task Manager

Gestor de tareas por consola desarrollado en Python.

Este proyecto forma parte de mi portfolio como Desarrollador Junior. El objetivo es practicar lógica de programación, funciones, estructuras de datos, persistencia en JSON, validación de entradas, testing básico y flujo profesional con Git/GitHub.

## Objetivo del proyecto

Crear una aplicación sencilla de terminal que permita gestionar tareas mediante operaciones CRUD básicas, manteniendo los datos guardados en un archivo JSON.

## Tecnologías utilizadas

- Python
- JSON
- unittest
- Git
- GitHub
- Terminal / línea de comandos

## Funcionalidades

- Menú interactivo por consola
- Crear tareas
- Listar tareas guardadas
- Marcar tareas como completadas
- Eliminar tareas
- Gestión de prioridades: baja, media y alta
- Fecha límite opcional para cada tarea
- Validación de formato de fecha YYYY-MM-DD
- Persistencia de datos en tasks.json
- Tests unitarios básicos con unittest

## Estructura del proyecto

    python-task-manager/
    ├── task_manager.py
    ├── tasks.json
    ├── README.md
    ├── .gitignore
    ├── LICENSE
    └── tests/
        ├── __init__.py
        └── test_task_manager.py

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

    git clone https://github.com/yoelvm/python-task-manager.git

2. Entrar en la carpeta del proyecto:

    cd python-task-manager

3. Ejecutar el programa:

    python task_manager.py

En Windows, si python no funciona, usar:

    py task_manager.py

## Demo de uso

Ejemplo de ejecución del programa en terminal:

    === Python Task Manager ===
    1. Ver tareas
    2. Añadir tarea
    3. Marcar tarea como completada
    4. Eliminar tarea
    5. Salir

    Selecciona una opción: 2
    Escribe el nombre de la tarea: Enviar candidatura junior
    Prioridad de la tarea (baja/media/alta): alta
    Fecha límite de la tarea (YYYY-MM-DD, opcional): 2026-07-30
    Tarea añadida correctamente.

    Selecciona una opción: 1

    Lista de tareas:
    1. Enviar candidatura junior - Pendiente - Prioridad: alta - Fecha límite: 2026-07-30

Si el usuario introduce una fecha con formato incorrecto:

    Fecha límite de la tarea (YYYY-MM-DD, opcional): 30/07/2026
    Fecha no válida. Se asignará 'Sin fecha'.

## Cómo ejecutar los tests

El proyecto incluye tests unitarios básicos para validar la lógica principal.

Ejecutar tests:

    python -m unittest discover -s tests

En Windows, si python no funciona, usar:

    py -m unittest discover -s tests

Resultado esperado:

    Ran 6 tests

    OK

## Funciones principales

- load_tasks(): carga las tareas guardadas desde tasks.json.
- save_tasks(): guarda las tareas en formato JSON.
- validate_priority(): valida prioridades permitidas.
- validate_due_date(): valida fechas con formato YYYY-MM-DD.
- create_task(): crea la estructura de una nueva tarea.
- add_task(): solicita datos al usuario y añade una tarea.
- list_tasks(): muestra todas las tareas guardadas.
- complete_task(): marca una tarea como completada.
- delete_task(): elimina una tarea existente.

## Aprendizajes aplicados

- Uso de funciones en Python
- Lectura y escritura de archivos JSON
- Validación de datos introducidos por el usuario
- Validación de valores permitidos mediante listas
- Validación de fechas con datetime.strptime
- Gestión de campos opcionales en estructuras de datos
- Separación de responsabilidades mediante funciones pequeñas
- Tests unitarios básicos con unittest
- Flujo de trabajo con Git y GitHub
- Uso de ramas, commits, Pull Requests y merge a main
- Documentación técnica en README

## Próximas mejoras

- Separar la lógica en varios módulos
- Mejorar el manejo de errores
- Añadir filtros por estado, prioridad o fecha límite
- Añadir edición de tareas existentes
- Crear una versión con interfaz gráfica o web

## Autor

Yoel Velásquez  
Desarrollador Junior Python/Java en Madrid  
GitHub: https://github.com/yoelvm