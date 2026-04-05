# Lista de Tareas - Aplicación GUI con Tkinter

## Descripción

Este proyecto consiste en el desarrollo de una aplicación de escritorio tipo **Lista de Tareas (To-Do List)** utilizando Python y la librería Tkinter.

La aplicación permite gestionar tareas diarias de forma interactiva, aplicando una **arquitectura modular por capas**, separando la lógica del sistema, los modelos y la interfaz gráfica.

## Objetivo

Desarrollar una aplicación GUI que permita administrar tareas mediante eventos de teclado y ratón, mejorando la experiencia del usuario y generando un ejecutable utilizando PyInstaller.

## Estructura del Proyecto

```bash
lista_tareas_app/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
└── ui/
    └── app_tkinter.py
```

## Funcionalidades

* Agregar tareas
* Marcar tareas como completadas
* Eliminar tareas
* Visualización dinámica de tareas
* Feedback visual (✔ en tareas completadas)

## Atajos de Teclado

* **Enter:** Añadir tarea
* **C:** Marcar tarea como completada
* **Delete / D:** Eliminar tarea
* **Escape:** Cerrar la aplicación
* **Doble clic:** Completar tarea rápidamente

## Tecnologías Utilizadas

* Python 3
* Tkinter
* PyInstaller

## Autor

**Robert Reyes**
