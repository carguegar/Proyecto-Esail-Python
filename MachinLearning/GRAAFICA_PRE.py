from tkinter import Tk, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from regresion_por_años import *  # Importar datos procesados

# Crear la ventana principal de Tkinter
ventana = Tk()
ventana.title("Predicciones 2025")
ventana.geometry("800x600")

def actualizar_ventana(funcion_actualizacion):
    """
    Limpia la ventana principal y ejecuta una función para definir los nuevos widgets.

    Args:
        funcion_actualizacion (function): Una función que define los nuevos widgets.
    """
    for widget in ventana.winfo_children():
        widget.destroy()
    funcion_actualizacion()

# Función para mostrar el gráfico de productos más vendidos
def mostrar_grafico_productos():
    boton_agentes = Button(ventana, text="Regresar", command=lambda: actualizar_ventana(mostrar_menu))
    boton_agentes.pack(pady=10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(ventas_futuras_por_producto['producto'], ventas_futuras_por_producto['ventas'], color='orange')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas Predichas')
    ax.set_title('Predicción de Productos Más Vendidos (2025)')

    # Integrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

def mostrar_grafico_agentes():
    boton_agentes = Button(ventana, text="Regresar", command=lambda: actualizar_ventana(mostrar_menu))
    boton_agentes.pack(pady=10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(ventas_futuras_por_agente['agente'], ventas_futuras_por_agente['ventas'], color='blue')
    ax.set_xlabel('Agente')
    ax.set_ylabel('Ventas Predichas')
    ax.set_title('Predicción de Agentes que Más Compran (2025)')

    # Integrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

def mostrar_grafico_comisiones():
    # Botón para regresar al menú principal
    boton_regresar = Button(ventana, text="Regresar", command=lambda: actualizar_ventana(mostrar_menu))
    boton_regresar.pack(pady=10)

    # Crear el gráfico de barras para las comisiones predichas
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(comisiones_por_agente['agente'], comisiones_por_agente['comision_predicha'], color='green')
    ax.set_xlabel('Agente')
    ax.set_ylabel('Comisiones Predichas')
    ax.set_title('Predicción de Comisiones por Agente (2025)')

    # Integrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

def mostrar_menu():
    # Botones para mostrar los gráficos
    boton_productos = Button(ventana, text="Mostrar Productos Más Vendidos", command=lambda: actualizar_ventana(mostrar_grafico_productos))
    boton_productos.pack(pady=10)

    boton_agentes = Button(ventana, text="Mostrar Agentes que Más Compran", command=lambda: actualizar_ventana(mostrar_grafico_agentes))
    boton_agentes.pack(pady=10)

    boton_comisiones = Button(ventana, text="Mostrar Comisiones por Agente", command=lambda: actualizar_ventana(mostrar_grafico_comisiones))
    boton_comisiones.pack(pady=10)


mostrar_menu()
# Iniciar el bucle principal de la ventana
ventana.mainloop()