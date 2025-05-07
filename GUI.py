from tkinter import *
import tkinter.messagebox as Messagebox
from SQL.base_datos import *
from clases import *
from proyecto import *

# Crear la ventana principal
ventana = Tk()
ventana.title("CristoMarket")
ventana.geometry("800x600")
ventana.config(bg="lightblue")

# Función genérica para actualizar la ventana
def actualizar_ventana(funcion_actualizacion):
    """
    Limpia la ventana principal y ejecuta una función para definir los nuevos widgets.

    Args:
        funcion_actualizacion (function): Una función que define los nuevos widgets.
    """
    for widget in ventana.winfo_children():
        widget.destroy()
    funcion_actualizacion()
# Función para iniciar sesión
def mostrar_login():
    etiqueta_correo = Label(ventana, text="Correo Electrónico:", font=("Arial", 14), bg="lightblue")
    etiqueta_correo.pack(pady=10)
    entrada_correo = Entry(ventana, font=("Arial", 14))
    entrada_correo.pack(pady=10)
    etiqueta_contrasena = Label(ventana, text="Contraseña:", font=("Arial", 14), bg="lightblue")
    etiqueta_contrasena.pack(pady=10)
    entrada_contrasena = Entry(ventana, show="*", font=("Arial", 14))
    entrada_contrasena.pack(pady=10)
    boton_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), command=lambda: iniciar_sesion(entrada_correo.get(), entrada_contrasena.get()), bg="lightgreen")
    boton_login.pack(pady=10)
#funcion para registrar un usuario
def mostrar_registro_usuario():
    etiqueta_titulo = Label(ventana, text="Registro de Usuario", font=("Arial", 20), bg="lightblue")
    etiqueta_titulo.pack(pady=20)
    etiqueta_aviso = Label(ventana, text="Los campos marcados con * son obligatorios", font=("Arial", 12), bg="lightblue")
    etiqueta_aviso.pack(pady=10)
    etiqueta_nombre = Label(ventana, text="Nombre*:", font=("Arial", 14), bg="lightblue")
    etiqueta_nombre.pack(pady=10)
    entrada_nombre = Entry(ventana, font=("Arial", 14))
    entrada_nombre.pack(pady=10)
    etiqueta_apellido1 = Label(ventana, text="Apellido 1*:", font=("Arial", 14), bg="lightblue")
    etiqueta_apellido1.pack(pady=10)
    entrada_apellido1 = Entry(ventana, font=("Arial", 14))
    entrada_apellido1.pack(pady=10)
    etiqueta_apellido2 = Label(ventana, text="Apellido 2:", font=("Arial", 14), bg="lightblue") 
    etiqueta_apellido2.pack(pady=10)
    entrada_apellido2 = Entry(ventana, font=("Arial", 14))
    entrada_apellido2.pack(pady=10)
    etiqueta_dni = Label(ventana, text="DNI*:", font=("Arial", 14), bg="lightblue")
    etiqueta_dni.pack(pady=10)
    entrada_dni = Entry(ventana, font=("Arial", 14))
    entrada_dni.pack(pady=10)
    etiqueta_numero_tarjeta = Label(ventana, text="Número de Tarjeta:", font=("Arial", 14), bg="lightblue")
    etiqueta_numero_tarjeta.pack(pady=10)
    entrada_numero_tarjeta = Entry(ventana, font=("Arial", 14))
    entrada_numero_tarjeta.pack(pady=10)
    etiqueta_numero_tlf = Label(ventana, text="Número de Teléfono:", font=("Arial", 14), bg="lightblue")
    etiqueta_numero_tlf.pack(pady=10)
    entrada_numero_tlf = Entry(ventana, font=("Arial", 14))
    entrada_numero_tlf.pack(pady=10)
    etiqueta_correo = Label(ventana, text="Correo Electrónico*:", font=("Arial", 14), bg="lightblue")
    etiqueta_correo.pack(pady=10)
    entrada_correo = Entry(ventana, font=("Arial", 14))
    entrada_correo.pack(pady=10)
    etiqueta_fecha_nacimiento = Label(ventana, text="Fecha de Nacimiento*:", font=("Arial", 14), bg="lightblue")
    etiqueta_fecha_nacimiento.pack(pady=10)
    entrada_fecha_nacimiento = Entry(ventana, font=("Arial", 14))
    entrada_fecha_nacimiento.pack(pady=10)
    etiqueta_contrasena = Label(ventana, text="Contraseña*:", font=("Arial", 14), bg="lightblue")
    etiqueta_contrasena.pack(pady=10)
    entrada_contrasena = Entry(ventana, show="*", font=("Arial", 14))
    entrada_contrasena.pack(pady=10)
    boton_registrar = Button(ventana, text="Registrar", font=("Arial", 14), command=lambda: registrar(entrada_nombre.get(), entrada_apellido1.get(), entrada_apellido2.get(), entrada_dni.get(), entrada_numero_tarjeta.get(), entrada_numero_tlf.get(), entrada_correo.get(), entrada_fecha_nacimiento.get(), entrada_contrasena.get()), bg="lightgreen")
    boton_registrar.pack(pady=10)

def mostrar_menu_principal():
    etiqueta_bienvenida = Label(ventana, text="Bienvenido a CristoMarket", font=("Arial", 20), bg="lightblue")
    etiqueta_bienvenida.pack(pady=20)
    boton_ver_productos = Button(ventana, text="Ver Productos", font=("Arial", 14), command=lambda: mostrar_productos, bg="lightgreen")
    boton_ver_productos.pack(pady=10)
    boton_ver_carrito = Button(ventana, text="Ver Carrito", font=("Arial", 14), command=lambda: mostrar_carrito, bg="lightgreen")
    boton_ver_carrito.pack(pady=10)
    boton_ver_tickets = Button(ventana, text="Ver Tickets", font=("Arial", 14), command=lambda: mostrar_tickets, bg="lightgreen")
    boton_ver_tickets.pack(pady=10)
    boton_modificar_datos = Button(ventana, text="Modificar Datos Del Usuario", font=("Arial", 14), command=lambda: modificar_datos, bg="lightgreen")
    boton_modificar_datos.pack(pady=10)
    boton_eliminar_cuenta = Button(ventana, text="Eliminar Cuenta", font=("Arial", 14), command=lambda: eliminar_cuenta, bg="lightgreen")
    boton_eliminar_cuenta.pack(pady=10)
    boton_cerrar_sesion = Button(ventana, text="Cerrar Sesión", font=("Arial", 14), command=lambda: cerrar_sesion, bg="lightgreen")
    boton_cerrar_sesion.pack(pady=10)
def incrementar_pagina(pagina_actual):
    """
    Incrementa la página actual y actualiza la vista de productos.
    """
    pagina_actual += 1
    productos = obtener_productos_paginados(pagina_actual)
    if productos:
        actualizar_ventana(lambda:mostrar_productos(pagina_actual, productos))
    else:
        Messagebox.showinfo("Información", "No hay más productos para mostrar.")
 
def decrementar_pagina(pagina_actual):
    """
    Decrementa la página actual y actualiza la vista de productos.
    """
    if pagina_actual > 1:
        pagina_actual -= 1
        productos = obtener_productos_paginados(pagina_actual)
        actualizar_ventana(lambda:mostrar_productos(pagina_actual, productos))
    else:
        Messagebox.showinfo("Información", "Ya estás en la primera página.")

def mostrar_productos(pagina_actual, productos):

    etiqueta_titulo = Label(ventana, text="Productos Disponibles", font=("Arial", 20), bg="lightblue")
    etiqueta_titulo.pack(pady=20)

    for producto in productos:
        frame_producto = Frame(ventana, bg="white", relief=SOLID, borderwidth=1)
        frame_producto.pack(pady=10, padx=20, fill=X)

        # Acceder a los atributos del objeto Producto usando la notación de puntos
        etiqueta_nombre = Label(frame_producto, text=f"Nombre: {producto.nombre_producto}", font=("Arial", 14), bg="white")
        etiqueta_nombre.pack(anchor=W, padx=10, pady=5)

        etiqueta_precio = Label(frame_producto, text=f"Precio: ${producto.precio:.2f}", font=("Arial", 14), bg="white")
        etiqueta_precio.pack(anchor=W, padx=10, pady=5)

        etiqueta_descripcion = Label(frame_producto, text=f"Descripción: {producto.descripcion}", font=("Arial", 12), bg="white", wraplength=600, justify=LEFT)
        etiqueta_descripcion.pack(anchor=W, padx=10, pady=5)

        boton_agregar_carrito = Button(frame_producto, text="Agregar al Carrito", font=("Arial", 12), bg="lightgreen", command=lambda p=producto: agregar_al_carrito(p))
        boton_agregar_carrito.pack(anchor=E, padx=10, pady=5)
    # Botones de navegación
    frame_navegacion = Frame(ventana, bg="lightblue")
    frame_navegacion.pack(pady=20)
    # Botón de página anterior (solo si no es la primera página)
    if pagina_actual > 1:
        boton_anterior = Button(frame_navegacion, text="Página Anterior", font=("Arial", 14), bg="lightgreen", command=lambda: decrementar_pagina(pagina_actual))
        boton_anterior.pack(side=LEFT, padx=10)

    # Botón de siguiente página (si hay más productos para mostrar)
    boton_siguiente = Button(frame_navegacion, text="Siguiente Página", font=("Arial", 14), bg="lightgreen", command=lambda: incrementar_pagina(pagina_actual))
    boton_siguiente.pack(side=LEFT, padx=10)

# Interfaz de bienvenida
def interfaz_bienvenida():
    titulo = Label(ventana, text="Bienvenido a CristoMarket", font=("Arial", 20), bg="lightblue")
    titulo.pack(pady=20)

    boton_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), command=lambda: actualizar_ventana(mostrar_login), bg="lightgreen")
    boton_login.pack(pady=10)

    boton_registro = Button(ventana, text="Registrarse", font=("Arial", 14), command=lambda: actualizar_ventana(mostrar_registro_usuario), bg="lightgreen")
    boton_registro.pack(pady=10)

productos = obtener_productos_paginados(1)  # Obtener los productos de la primera página
actualizar_ventana(lambda: mostrar_productos(1, productos))
ventana.mainloop()

