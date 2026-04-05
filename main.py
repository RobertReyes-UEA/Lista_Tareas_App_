# main.py

import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

def main():
    # Crear ventana principal
    root = tk.Tk()

    # Crear instancia del servicio (lógica)
    servicio = TareaServicio()

    # Crear la aplicación (UI)
    app = AppTkinter(root, servicio)

    # Ejecutar la app
    root.mainloop()

# Punto de entrada
if __name__ == "__main__":
    main()
