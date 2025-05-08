from tkinter import *
import tkinter.messagebox as Messagebox
from tkinter import ttk
from SQL.base_datos import *
from clases import *
from proyecto import *

# Crear la ventana principal
ventana = Tk()
ventana.title("CristoMarket")
ventana.geometry("1922x1080")
ventana.config(bg="lightblue")

def mostrar_menu_principal(cliente,carrito):
    etiqueta_bienvenida = Label(ventana, text="Bienvenido a CristoMarket", font=("Arial", 20), bg="lightblue")
    etiqueta_bienvenida.pack(pady=20)
    boton_ver_productos = Button(ventana, text="Ver Productos", font=("Arial", 14), command=lambda: actualizar_ventana(lambda: mostrar_productos(1,carrito)), bg="lightgreen")
    boton_ver_productos.pack(pady=10)
    boton_ver_carrito = Button(ventana, text="Ver Carrito", font=("Arial", 14), command=lambda: actualizar_ventana(lambda: mostrar_cesta_compra(carrito,cliente)), bg="lightgreen")
    boton_ver_carrito.pack(pady=10)
    boton_ver_tickets = Button(ventana, text="Ver Tickets", font=("Arial", 14), command=lambda: actualizar_ventana(lambda: mostrar_tickets(cliente)), bg="lightgreen")
    boton_ver_tickets.pack(pady=10)
    boton_modificar_datos = Button(ventana, text="Modificar Datos Del Usuario", font=("Arial", 14), command=lambda:actualizar_ventana(lambda:mostrar_datos_cliente(cliente)), bg="lightgreen")
    boton_modificar_datos.pack(pady=10)
    boton_cerrar_sesion = Button(ventana, text="Cerrar Sesión", font=("Arial", 14), command=cerrar_sesion, bg="lightgreen")
    boton_cerrar_sesion.pack(pady=10)
# Crear un canvas con scrollbar
def crear_ventana_con_scroll():
    """
    Crea una ventana con barra de desplazamiento.
    """
    frame_principal = Frame(ventana, bg="lightblue")
    frame_principal.pack(fill=BOTH, expand=True)

    # Crear un canvas para contener los widgets
    canvas = Canvas(frame_principal, bg="lightblue")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Crear una scrollbar y vincularla al canvas
    scrollbar = ttk.Scrollbar(frame_principal, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Crear un frame dentro del canvas para los widgets
    frame_contenido = Frame(canvas, bg="lightblue")
    canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

    # Configurar el canvas para que se ajuste al tamaño del contenido
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_contenido.bind("<Configure>", ajustar_scroll)

    return frame_contenido

# Crear el frame con scroll
frame_contenido = crear_ventana_con_scroll()

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
def funcion_login(correo, contrasena):
    """
    Comprueba si el usuario existe y si la contraseña es correcta.

    Args:
        correo (str): Correo electrónico del usuario.
        contrasena (str): Contraseña del usuario.
    """
    correo = correo.strip() #eliminar espacios en blanco
    cliente = comprobar_login(correo, contrasena)
    if cliente != False:
        carrito = [[],[]] #lista de productos y lista de cantidades de cada producto
        #Messagebox.showinfo("Inicio de sesión exitoso.", f"Bienvenido {cliente.nombre} {cliente.apellido1}")
        actualizar_ventana(lambda:mostrar_menu_principal(cliente,carrito))
    else:
        Messagebox.showerror("Error", "Correo o contraseña incorrectos.")

 

def mostrar_login():
    etiqueta_correo = Label(ventana, text="Correo Electrónico:", font=("Arial", 14), bg="lightblue")
    etiqueta_correo.pack(pady=10)
    entrada_correo = Entry(ventana, font=("Arial", 14))
    entrada_correo.pack(pady=10)
    etiqueta_contrasena = Label(ventana, text="Contraseña:", font=("Arial", 14), bg="lightblue")
    etiqueta_contrasena.pack(pady=10)
    entrada_contrasena = Entry(ventana, show="*", font=("Arial", 14))
    entrada_contrasena.pack(pady=10)
    boton_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), command=lambda: funcion_login(entrada_correo.get(), entrada_contrasena.get()), bg="lightgreen")
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

    def registrar(nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento, contrasena):
        """
        Registra un nuevo usuario en la base de datos.
        """
        # Eliminar espacios en blanco
        nombre = nombre.strip()  
        apellido1 = apellido1.strip()
        apellido2 = apellido2.strip()
        dni = dni.strip()
        numero_tarjeta = numero_tarjeta.strip()
        numero_tlf = numero_tlf.strip()
        correo = correo.strip()
        fecha_nacimiento = fecha_nacimiento.strip()
        if nombre and apellido1 and dni and correo and fecha_nacimiento and contrasena:
            cliente = Cliente(None,nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento, contrasena)
            insertar_cliente_bd(cliente)
            Messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")
            actualizar_ventana(mostrar_login)
        else:
            Messagebox.showerror("Error", "Por favor completa todos los campos obligatorios.")

def cerrar_sesion():
    """
    Cierra la sesión del usuario y vuelve a la pantalla de inicio de sesión.
    """
    actualizar_ventana(interfaz_bienvenida)

def boton_regresar_a_menu_cliente():
    actualizar_ventana(lambda: mostrar_menu_principal(cliente,carrito))

def boton_regresar_modificar():
    actualizar_ventana(lambda: mostrar_datos_cliente(cliente))

def mostrar_datos_cliente(cliente):
    """
    Muestra los datos del cliente y agrega botones para modificar ciertos campos.
    """
    etiqueta_datos_cliente = Label(ventana, text="Datos del Cliente", font=("Arial", 20), bg="lightblue")
    etiqueta_datos_cliente.grid(row=0, column=0, columnspan=3, pady=20)

    # Mostrar los datos del cliente
    Label(ventana, text=f"Nombre: {cliente.nombre}", font=("Arial", 14), bg="lightblue").grid(row=1, column=0, padx=10, pady=5)
    Label(ventana, text=f"Apellido 1: {cliente.apellido1}", font=("Arial", 14), bg="lightblue").grid(row=2, column=0, padx=10, pady=5)
    Label(ventana, text=f"Apellido 2: {cliente.apellido2}", font=("Arial", 14), bg="lightblue").grid(row=3, column=0, padx=10, pady=5)
    Label(ventana, text=f"DNI: {cliente.DNI}", font=("Arial", 14), bg="lightblue").grid(row=4, column=0, padx=10, pady=5)

    # Número de tarjeta con botón para modificar
    Label(ventana, text=f"Número de Tarjeta: {cliente.numero_tarjeta}", font=("Arial", 14), bg="lightblue").grid(row=5, column=0, padx=10, pady=5)
    boton_modificar_tarjeta = Button(ventana, text="Modificar", font=("Arial", 12), bg="lightgreen", command=lambda: modificar_numero_tarjeta(cliente))
    boton_modificar_tarjeta.grid(row=5, column=1, padx=10, pady=5)

    # Número de teléfono con botón para modificar
    Label(ventana, text=f"Número de Teléfono: {cliente.numero_tlf}", font=("Arial", 14), bg="lightblue").grid(row=6, column=0, padx=10, pady=5)
    boton_modificar_tlf = Button(ventana, text="Modificar", font=("Arial", 12), bg="lightgreen", command=lambda: modificar_numero_tlf(cliente))
    boton_modificar_tlf.grid(row=6, column=1, padx=10, pady=5)

    # Contraseña con botón para modificar
    boton_modificar_contrasena = Button(ventana, text="Cambiar contraseña", font=("Arial", 12), bg="lightgreen", command=lambda: modificar_contrasena(cliente))
    boton_modificar_contrasena.grid(row=9, column=0, padx=10, pady=5)

    # Botón para eliminar cuenta
    boton_eliminar_cuenta = Button(ventana, text="Eliminar Cuenta", font=("Arial", 12), bg="lightgreen", command=lambda: eliminar_cliente(cliente))
    boton_eliminar_cuenta.grid(row=10, column=0, padx=10, pady=5)

    # Correo electrónico
    Label(ventana, text=f"Correo Electrónico: {cliente.correo}", font=("Arial", 14), bg="lightblue").grid(row=8, column=0, padx=10, pady=5)
    Label(ventana, text=f"Fecha de Nacimiento: {cliente.fecha_nacimiento}", font=("Arial", 14), bg="lightblue").grid(row=7, column=0, padx=10, pady=5)
    # Botón para regresar al menú principal
    Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
           command=boton_regresar_a_menu_cliente).grid(row=11, column=1, columnspan=5, pady=20)

def eliminar_cliente(cliente):
    """
    Elimina la cuenta del cliente y cierra la sesión.
    """
    respuesta = Messagebox.askyesno("Eliminar Cuenta", "¿Estás seguro de que deseas eliminar tu cuenta?")
    if respuesta:
        borrar_cliente_bd(cliente)
        actualizar_ventana(mostrar_login)

def guardar_cambio(nuevo_numero,atributo):
        if nuevo_numero:
            setattr(cliente, atributo, nuevo_numero)
            Messagebox.showinfo("Éxito", "Cambio realizado correctamente.")
            actualizar_ventana(lambda: mostrar_datos_cliente(cliente))
        else:
            Messagebox.showerror("Error", "El número de tarjeta no puede estar vacío.")
        if atributo == "numero_tarjeta":
            modificar_numero_tarjeta_cliente(cliente)
        elif atributo == "numero_tlf":
            modificar_numero_telefono_cliente(cliente)

def modificar_numero_tarjeta(cliente):
    """
    Permite modificar el número de tarjeta del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Número de Tarjeta", font=("Arial", 20), bg="lightblue").pack(pady=20)
    entrada_numero_tarjeta = Entry(ventana, font=("Arial", 14))
    entrada_numero_tarjeta.insert(0, cliente.numero_tarjeta)
    entrada_numero_tarjeta.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightgreen", command=lambda: guardar_cambio(entrada_numero_tarjeta.get().strip(),"numero_tarjeta")).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(cliente))).pack(pady=10)
    
def modificar_numero_tlf(cliente):
    """
    Permite modificar el número de teléfono del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Número de Teléfono", font=("Arial", 20), bg="lightblue").pack(pady=20)
    entrada_numero_tlf = Entry(ventana, font=("Arial", 14))
    entrada_numero_tlf.insert(0, cliente.numero_tlf)
    entrada_numero_tlf.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightgreen", command=lambda:guardar_cambio(entrada_numero_tlf.get().strip() ,"numero_tlf")).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(cliente))).pack(pady=10)

def guardar_cambio_contrasena(contrasena, nueva_contrasena, repetir_contrasena, cliente):

    if nueva_contrasena == repetir_contrasena:
        if contrasena == cliente.contraseña:
            if nueva_contrasena:
                cliente.contraseña = nueva_contrasena
                modificar_contraseña_cliente(cliente)
                Messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
                actualizar_ventana(lambda: mostrar_datos_cliente(cliente))
            else:
                Messagebox.showerror("Error", "La nueva contraseña no puede estar vacía.")
        else:
            Messagebox.showerror("Error", "La contraseña antigua no es correcta.")
    else:
        Messagebox.showerror("Error", "Las nuevas contraseñas no coinciden.")

def modificar_contrasena(cliente):
    """
    Permite modificar la contraseña del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Contraseña", font=("Arial", 20), bg="lightblue").pack(pady=20)
    Label(ventana, text="Contraseña antigua:", font=("Arial", 14), bg="lightblue").pack(pady=10)
    entrada_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_contrasena.pack(pady=10)
    Label(ventana, text="Nueva contraseña:", font=("Arial", 14), bg="lightblue").pack(pady=10)
    entrada_nueva_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_nueva_contrasena.pack(pady=10)
    Label(ventana, text="Repetir nueva contraseña:", font=("Arial", 14), bg="lightblue").pack(pady=10)
    entrada_repetir_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_repetir_contrasena.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightgreen", command=lambda: guardar_cambio_contrasena(entrada_contrasena.get(),entrada_nueva_contrasena.get(),entrada_repetir_contrasena.get(), cliente)).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(cliente))).pack(pady=10)
    
def mostrar_tickets(cliente):
    """
    Muestra los tickets de un cliente en la interfaz gráfica con un diseño horizontal.

    Args:
        cliente (Cliente): El cliente cuyos tickets se van a mostrar.
    """
    tickets_cliente = obtener_tickets_cliente(cliente)  # Obtener los tickets del cliente
    print(tickets_cliente)
    etiqueta_tickets = Label(ventana, text="Tickets de Compra", font=("Arial", 20), bg="lightblue")
    etiqueta_tickets.grid(row=0, column=0, columnspan=5, pady=20)
    i = 0

    if tickets_cliente:
        # Encabezados de la tabla
        encabezado_producto = Label(ventana, text="Producto", font=("Arial", 14, "bold"), bg="lightblue")
        encabezado_producto.grid(row=1, column=0, padx=10, pady=5)

        encabezado_cantidad = Label(ventana, text="Cantidad", font=("Arial", 14, "bold"), bg="lightblue")
        encabezado_cantidad.grid(row=1, column=1, padx=10, pady=5)

        encabezado_precio = Label(ventana, text="Precio Unitario", font=("Arial", 14, "bold"), bg="lightblue")
        encabezado_precio.grid(row=1, column=2, padx=10, pady=5)

        encabezado_total = Label(ventana, text="Precio Total", font=("Arial", 14, "bold"), bg="lightblue")
        encabezado_total.grid(row=1, column=3, padx=10, pady=5)

        encabezado_fecha = Label(ventana, text="Fecha", font=("Arial", 14, "bold"), bg="lightblue")
        encabezado_fecha.grid(row=1, column=4, padx=10, pady=5)

        # Mostrar los datos de los tickets
        for i, ticket in enumerate(tickets_cliente, start=2):
            etiqueta_producto = Label(ventana, text=ticket['nombre_producto'], font=("Arial", 12), bg="white")
            etiqueta_producto.grid(row=i, column=0, padx=10, pady=5)

            etiqueta_cantidad = Label(ventana, text=ticket['cantidad'], font=("Arial", 12), bg="white")
            etiqueta_cantidad.grid(row=i, column=1, padx=10, pady=5)

            etiqueta_precio = Label(ventana, text=f"${ticket['precio']:.2f}", font=("Arial", 12), bg="white")
            etiqueta_precio.grid(row=i, column=2, padx=10, pady=5)

            precio_total = ticket['cantidad'] * ticket['precio']
            etiqueta_total = Label(ventana, text=f"${precio_total:.2f}", font=("Arial", 12), bg="white")
            etiqueta_total.grid(row=i, column=3, padx=10, pady=5)

            etiqueta_fecha = Label(ventana, text=ticket['fecha'], font=("Arial", 12), bg="white")
            etiqueta_fecha.grid(row=i, column=4, padx=10, pady=5)
    else:
        etiqueta_no_tickets = Label(ventana, text="No se encontraron tickets para este cliente.", font=("Arial", 14), bg="lightblue")
        etiqueta_no_tickets.grid(row=i+1, column=0, columnspan=5, pady=20)
    # Botón para regresar al menú principal
    Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
           command= boton_regresar_a_menu_cliente).grid(row=i+2, column=0, columnspan=5, pady=20)

    
def actualizar_cantidad_manual_producto(cliente,event, carrito, posicion, entrada_cantidad,pagina_actual):
    """
    Actualiza la cantidad de un producto en el carrito manualmente.

    Args:
        event: Evento de teclado (Enter).
        carrito (list): Lista que contiene los productos y sus cantidades.
        posicion (int): Índice del producto en el carrito.
        entrada_cantidad (Entry): Caja de texto donde se ingresa la cantidad.
    """
    try:
        nueva_cantidad = int(entrada_cantidad.get())
        print(nueva_cantidad)
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        elif nueva_cantidad == 0:
            # Si la cantidad es 0, elimina el producto del carrito
            eliminar_producto(carrito, cliente, posicion)
        else:
            # Actualiza la cantidad del producto
            modificar_cantidad_producto(carrito,posicion+1, nueva_cantidad)  

        # Actualiza la interfaz para reflejar los cambios
        actualizar_ventana(lambda: mostrar_productos(pagina_actual,carrito))
    except ValueError:
        Messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo actualizar la cantidad: {e}")


def actualizar_cantidad_manual_cesta(cliente,event, carrito, posicion, entrada_cantidad):
    """
    Actualiza la cantidad de un producto en el carrito manualmente.

    Args:
        event: Evento de teclado (Enter).
        carrito (list): Lista que contiene los productos y sus cantidades.
        posicion (int): Índice del producto en el carrito.
        entrada_cantidad (Entry): Caja de texto donde se ingresa la cantidad.
    """
    try:
        nueva_cantidad = int(entrada_cantidad.get())
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        elif nueva_cantidad == 0:
            # Si la cantidad es 0, elimina el producto del carrito
            eliminar_producto(carrito, cliente, posicion)
        else:
            # Actualiza la cantidad del producto
            modificar_cantidad_producto(carrito, posicion, nueva_cantidad)  

        # Actualiza la interfaz para reflejar los cambios
        actualizar_ventana(lambda: mostrar_cesta_compra(carrito, cliente))
    except ValueError:
        Messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo actualizar la cantidad: {e}")

# Función para eliminar un producto
def eliminar_producto(cesta_compra, cliente, posicion):
    try:
        modificar_cantidad_producto(cesta_compra, posicion + 1, 0)
        mostrar_cesta_compra(cesta_compra, cliente)
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")

# Función para modificar la cantidad de un producto
def modificar_cantidad(carrito, cliente, posicion, incremento):
    """
    Modifica la cantidad de un producto en el carrito.

    Args:
        carrito (list): Lista que contiene los productos y sus cantidades.
        cliente (Cliente): Cliente actual.
        posicion (int): Índice del producto en el carrito.
        incremento (int): Incremento o decremento de la cantidad.
    """
    try:
        nueva_cantidad = carrito[1][posicion] + incremento
        if nueva_cantidad <= 0:
            # Si la cantidad es 0 o menor, elimina el producto del carrito
            eliminar_producto(carrito, cliente, posicion)
        else:
            # Actualiza la cantidad del producto
            modificar_cantidad_producto(carrito, posicion + 1, nueva_cantidad)

    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo modificar la cantidad: {e}")

# Función para comprar los productos
def comprar(cesta_compra, cliente):
    if len(cesta_compra[0]) == 0: 
        Messagebox.showerror("Error", "La cesta de compra está vacía.")
    else:
        comprar_productos_cesta(cesta_compra, cliente)
        mostrar_cesta_compra(cesta_compra, cliente)


# Función para mostrar la cesta de compra
def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

# Función para mostrar el título
def mostrar_titulo(ventana, texto="Cesta de Compra"):
    titulo = Label(ventana, text=texto, font=("Arial", 24), bg="lightblue")
    titulo.pack(pady=20)

# Función para mostrar un mensaje cuando la cesta está vacía
def mostrar_cesta_vacia(ventana):
    Label(ventana, text="La cesta de compra está vacía.", font=("Arial", 16), bg="lightblue").pack(pady=10)

# Función para mostrar un producto en la interfaz
def mostrar_producto_en_carrito(ventana, producto, cantidad, indice, cesta_compra, cliente):
    """
    Muestra un producto en el carrito con controles para modificar la cantidad.
    """
    frame_producto = Frame(ventana, bg="lightblue")
    frame_producto.pack(pady=5, fill="x")

    # Información del producto
    texto_producto = f"{producto.nombre_producto} - Precio Unitario: {producto.precio}€ - Precio Total: {producto.precio * cantidad}€"
    Label(frame_producto, text=texto_producto, font=("Arial", 14), bg="lightblue").pack(side="left", padx=10)

    # Controles para modificar la cantidad
    frame_controles = Frame(frame_producto, bg="lightblue")
    frame_controles.pack(side="right", padx=10)

    # Botón para disminuir la cantidad
    Button(
        frame_controles,
        text="-",
        font=("Arial", 12),
        command=lambda: disminuir_cantidad_cesta_compra(cesta_compra, cliente, indice)
    ).pack(side="left", padx=5)

    # Cuadro de texto para la cantidad
    entrada_cantidad = Entry(frame_controles, font=("Arial", 14), width=3, justify="center")
    entrada_cantidad.insert(0, str(cantidad))
    entrada_cantidad.pack(side="left", padx=5)

   # Asociar el evento "Enter" al cuadro de texto
    entrada_cantidad.bind(
        "<Return>",
        lambda event: actualizar_cantidad_manual_cesta(cliente,event, cesta_compra, indice+1, entrada_cantidad)
    )

    # Botón para aumentar la cantidad
    Button(
        frame_controles,
        text="+",
        font=("Arial", 12),
        command=lambda: aumentar_cantidad_cesta(cesta_compra, cliente, indice)
    ).pack(side="left", padx=5)

    # Botón para eliminar el producto
    Button(
        frame_producto,
        text="Eliminar",
        font=("Arial", 12),
        command=lambda: eliminar_producto(cesta_compra, cliente, indice)
    ).pack(side="right", padx=10)

def aumentar_cantidad_cesta(cesta_compra, cliente, indice):
    """
    Aumenta la cantidad de un producto en la cesta de compra.
    """
    try:
        cesta_compra[1][indice] += 1
        modificar_cantidad_producto(cesta_compra, indice + 1, cesta_compra[1][indice])
        actualizar_ventana(lambda: mostrar_cesta_compra(cesta_compra, cliente))
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo aumentar la cantidad: {e}")    


def disminuir_cantidad_cesta_compra(cesta_compra, cliente, indice):
    """
    Disminuye la cantidad de un producto en la cesta de compra.
    """
    try:
        if cesta_compra[1][indice] > 1:
            cesta_compra[1][indice] -= 1
            modificar_cantidad_producto(cesta_compra, indice + 1, cesta_compra[1][indice])
            actualizar_ventana(lambda: mostrar_cesta_compra(cesta_compra, cliente))
        else:
            eliminar_producto(cesta_compra, cliente, indice)
        mostrar_cesta_compra(cesta_compra, cliente)
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo disminuir la cantidad: {e}")
        
# Función para mostrar el botón de comprar
def mostrar_boton_comprar(ventana, cesta_compra, cliente):
    Button(
        ventana,
        text="Comprar Productos",
        font=("Arial", 14),
        command=lambda: comprar(cesta_compra, cliente)
    ).pack(pady=20)

# Función principal para mostrar la cesta de compra
def mostrar_cesta_compra(cesta_compra, cliente):
    """
    Muestra los productos en la cesta de compra y permite gestionarlos.
    """
    limpiar_ventana(ventana)
    mostrar_titulo(ventana)

    if len(cesta_compra[0]) == 0:
        mostrar_cesta_vacia(ventana)
    else:
        for i, producto in enumerate(cesta_compra[0]):
            mostrar_producto_en_carrito(ventana, producto, cesta_compra[1][i], i, cesta_compra, cliente)
        mostrar_boton_comprar(ventana, cesta_compra, cliente)
    # Botón para regresar al menú principal
    Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
           command=boton_regresar_a_menu_cliente).pack(pady=20)
    
def incrementar_pagina(pagina_actual,carrito):
    """
    Incrementa la página actual y actualiza la vista de productos.
    """
    pagina_actual += 1
    productos = obtener_productos_paginados(pagina_actual)
    if productos:
        actualizar_ventana(lambda:mostrar_productos(pagina_actual,carrito))
    else:
        Messagebox.showinfo("Información", "No hay más productos para mostrar.")
 
def decrementar_pagina(pagina_actual,carrito):
    """
    Decrementa la página actual y actualiza la vista de productos.
    """
    pagina_actual -= 1
    actualizar_ventana(lambda:mostrar_productos(pagina_actual,carrito))

def mostrar_productos(pagina_actual, carrito):
    """
    Muestra los productos disponibles en la página actual y agrega botones de navegación.
    """
    # Título de la página
    etiqueta_titulo = Label(ventana, text="Productos Disponibles", font=("Arial", 20), bg="lightblue")
    etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20)

    # Mostrar los productos
    productos = obtener_productos_paginados(pagina_actual)  # Obtener los productos de la página actual
    for i, producto in enumerate(productos, start=1):
        frame_producto = Frame(ventana, bg="white", relief=SOLID, borderwidth=1)
        frame_producto.grid(row=i, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        etiqueta_nombre = Label(frame_producto, text=f"Nombre: {producto.nombre_producto}", font=("Arial", 14), bg="white")
        etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        etiqueta_precio = Label(frame_producto, text=f"Precio: ${producto.precio:.2f}", font=("Arial", 14), bg="white")
        etiqueta_precio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        etiqueta_descripcion = Label(frame_producto, text=f"Descripción: {producto.descripcion}", font=("Arial", 12), bg="white", wraplength=600, justify=LEFT)
        etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        if comprobar_producto_en_carrito(carrito, producto):
            # Crear un frame para los controles de cantidad
            frame_controles = Frame(frame_producto, bg="white")
            frame_controles.grid(row=0, column=1, rowspan=3, padx=10, pady=5, sticky="e")

            # Obtener la cantidad actual del producto en el carrito
            indice_producto = carrito[0].index(producto)
            cantidad_actual = carrito[1][indice_producto]
            

           # Botón para disminuir la cantidad
            Button(
                frame_controles,
                text="-",
                font=("Arial", 12),
                command=lambda i=indice_producto: (modificar_cantidad(carrito, cliente, i, -1), actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito)))
            ).grid(row=0, column=0, padx=5)

            # Cuadro de texto para la cantidad
            entrada_cantidad = Entry(frame_controles, font=("Arial", 12), width=3, justify="center")
            entrada_cantidad.insert(0, str(cantidad_actual))
            entrada_cantidad.grid(row=0, column=1, padx=5)

            # Asociar el evento "Enter" al cuadro de texto
            entrada_cantidad.bind(
                "<Return>",
                lambda event, i=indice_producto, e = entrada_cantidad: actualizar_cantidad_manual_producto(cliente,event, carrito, i, e, pagina_actual)
            )

            # Botón para aumentar la cantidad
            Button(
                frame_controles,
                text="+",
                font=("Arial", 12),
                command=lambda i=indice_producto: (modificar_cantidad(carrito, cliente, i, 1), actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito)))
            ).grid(row=0, column=2, padx=5)
        else:
            boton_agregar_carrito = Button(frame_producto, text="Agregar al Carrito", font=("Arial", 12), bg="lightgreen",
                                           command=lambda p=producto: agregar_al_carrito(p, carrito, pagina_actual))
            boton_agregar_carrito.grid(row=0, column=1, rowspan=3, padx=10, pady=5, sticky="e")

    # Mostrar el número de página actual
    etiqueta_pagina = Label(ventana, text=f"Página {pagina_actual}", font=("Arial", 14), bg="lightblue")
    etiqueta_pagina.grid(row=len(productos) + 1, column=0, columnspan=3, pady=10)

    # Botones de navegación
    frame_navegacion = Frame(ventana, bg="lightblue")
    frame_navegacion.grid(row=len(productos) + 2, column=0, columnspan=3, pady=20)

    if pagina_actual > 1:
        boton_anterior = Button(frame_navegacion, text="Página Anterior", font=("Arial", 14), bg="lightgreen",
                                command=lambda: decrementar_pagina(pagina_actual, carrito))
        boton_anterior.pack(side=LEFT, padx=10)

    boton_siguiente = Button(frame_navegacion, text="Siguiente Página", font=("Arial", 14), bg="lightgreen",
                              command=lambda: incrementar_pagina(pagina_actual, carrito))
    boton_siguiente.pack(side=LEFT, padx=10)

    # Botón para regresar al menú principal
    boton_regresar = Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
                            command=boton_regresar_a_menu_cliente)
    boton_regresar.grid(row=len(productos) + 3, column=0, columnspan=3, pady=20)

def agregar_al_carrito(producto, carrito, pagina_actual):

    insertar_producto_cesta(carrito,producto, 1)  # Agregar el producto a la base de datos
    # Actualizar la interfaz para reflejar los cambios
    actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito))

# Interfaz de bienvenida
def interfaz_bienvenida():
    titulo = Label(ventana, text="Bienvenido a CristoMarket", font=("Arial", 20), bg="lightblue")
    titulo.pack(pady=20)

    boton_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), command=lambda: actualizar_ventana(mostrar_login), bg="lightgreen")
    boton_login.pack(pady=10)

    boton_registro = Button(ventana, text="Registrarse", font=("Arial", 14), command=lambda: actualizar_ventana(mostrar_registro_usuario), bg="lightgreen")
    boton_registro.pack(pady=10)

actualizar_ventana(interfaz_bienvenida)
ventana.mainloop()

