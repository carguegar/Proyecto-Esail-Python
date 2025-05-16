from tkinter import *
import tkinter.messagebox as Messagebox
from tkinter import ttk
from SQL.base_datos import *
from clases import *
from proyecto import *
from PIL import Image, ImageTk
import re #para las expresiones regulares

# Crear la ventana principal
ventana = Tk()
ventana.title("CristoMarket")
ventana.geometry("1600x900")
ventana.config(bg="#E6E6E6") 
ventana.resizable(False, False)

# Interfaz de bienvenida
def interfaz_bienvenida():
    # Cargar la imagen usando Pillow
    imagen_original = Image.open(r"C:\Users\carlo\Desktop\python\Proyecto-Esail-Python\images\portada.png")  # Ruta de la imagen
    imagen = ImageTk.PhotoImage(imagen_original)

    # Mostrar la imagen en un Label
    etiqueta_imagen = Label(ventana, image=imagen)
    etiqueta_imagen.image = imagen  # Mantener una referencia para evitar que se recolecte como basura
    etiqueta_imagen.place(x=0, y=0, relwidth=1, relheight=1)  # Ajustar la imagen al tamaño de la ventana

    # Crear un frame para los botones
    frame_botones = Frame(ventana, bg="white")
    frame_botones.pack(pady=50)  # Aumentar el valor de pady para bajar los botones

    # Botones alineados uno al lado del otro
    boton_login = Button(frame_botones, text="Iniciar Sesión", font=("Arial", 14), command=lambda: actualizar_ventana(mostrar_login), bg="lightblue")
    boton_login.grid(row=0, column=0, padx=10, pady=10)

    boton_registro = Button(frame_botones, text="Registrarse", font=("Arial", 14), command=lambda: actualizar_ventana(lambda: mostrar_registro_usuario(True, True, True, True, True, True, True, True, True,False,False)), bg="lightblue")
    boton_registro.grid(row=0, column=1, padx=10, pady=10)

    boton_salir = Button(frame_botones, text="Salir", font=("Arial", 14), command=cerrar_programa, bg="lightblue")
    boton_salir.grid(row=0, column=2, padx=10, pady=10)

def mostrar_menu_principal(carrito, cliente):
    """
    Muestra el menú principal con opciones para el cliente.
    """
    # Limpiar la ventana antes de agregar nuevos widgets
    limpiar_ventana(ventana)

    # Configurar las columnas para centrar el contenido horizontalmente
    ventana.grid_columnconfigure(0, weight=1)  # Columna izquierda
    ventana.grid_columnconfigure(1, weight=0)  # Columna central (contenido)
    ventana.grid_columnconfigure(2, weight=1)  # Columna derecha

    # Crear un frame para centrar el contenido
    frame_contenido = Frame(ventana, bg="#E6E6E6")
    frame_contenido.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)  # Columna central

    # Etiqueta de bienvenida
    etiqueta_bienvenida = Label(frame_contenido, text="Bienvenido a CristoMarket", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_bienvenida.grid(row=0, column=0, columnspan=2, pady=20)

    # Botón para ver productos
    boton_ver_productos = Button(frame_contenido, text="Ver Productos", font=("Arial", 14),
                                 command=lambda: actualizar_ventana(lambda: mostrar_productos(1, carrito, cliente)),
                                 bg="lightblue")
    boton_ver_productos.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # Botón para ver carrito
    boton_ver_carrito = Button(frame_contenido, text="Ver Carrito", font=("Arial", 14),
                               command=lambda: actualizar_ventana(lambda: mostrar_cesta_compra(carrito, cliente)),
                               bg="lightblue")
    boton_ver_carrito.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    # Botón para ver tickets
    boton_ver_tickets = Button(frame_contenido, text="Ver Tickets", font=("Arial", 14),
                               command=lambda: actualizar_ventana(lambda: mostrar_tickets(carrito, cliente)),
                               bg="lightblue")
    boton_ver_tickets.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    # Botón para modificar datos del usuario
    boton_modificar_datos = Button(frame_contenido, text="Modificar Datos Del Usuario", font=("Arial", 14),
                                   command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(carrito, cliente)),
                                   bg="lightblue")
    boton_modificar_datos.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    # Botón para cerrar sesión
    boton_cerrar_sesion = Button(frame_contenido, text="Cerrar Sesión", font=("Arial", 14),
                                 command=cerrar_sesion, bg="lightblue")
    boton_cerrar_sesion.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# Función genérica para actualizar la ventana
def actualizar_ventana(funcion_actualizacion):
    """
    Limpia la ventana principal y ejecuta una función para definir los nuevos widgets.

    Args:
        funcion_actualizacion (function): Una función que define los nuevos widgets.
    """
    for widget in ventana.winfo_children():
        widget.destroy()
    ventana.geometry("1600x900")
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
        actualizar_ventana(lambda:mostrar_menu_principal(carrito,cliente))
    else:
        Messagebox.showerror("Error", "Correo o contraseña incorrectos.")

 
#

# Ejemplo de cómo centrar el contenido en una función
def mostrar_login():
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=0)
    ventana.grid_columnconfigure(2, weight=1)


    # Correo
    etiqueta_correo = Label(ventana, text="Correo Electrónico:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_correo.grid(row=0, column=1, padx=10, pady=(20, 2), sticky="n")
    entrada_correo = Entry(ventana, font=("Arial", 14), width=18)
    entrada_correo.grid(row=1, column=1, padx=10, pady=(2, 10), sticky="n")

    # Contraseña
    etiqueta_contrasena = Label(ventana, text="Contraseña:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_contrasena.grid(row=2, column=1, padx=10, pady=(10, 2), sticky="n")
    entrada_contrasena = Entry(ventana, show="*", font=("Arial", 14), width=18)
    entrada_contrasena.grid(row=3, column=1, padx=10, pady=(2, 10), sticky="n")

    entrada_contrasena.bind("<Return>", lambda event: funcion_login(entrada_correo.get(), entrada_contrasena.get()))

    # Botón login
    boton_login = Button(ventana, text="Iniciar Sesión", font=("Arial", 14),
                         command=lambda: funcion_login(entrada_correo.get(), entrada_contrasena.get()), bg="lightblue")
    boton_login.grid(row=4, column=1, padx=10, pady=10, sticky="n")

    # Botón para registrarse
    etiqueta_registro = Label(ventana, text="¿No tienes cuenta?", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_registro.grid(row=5, column=1, padx=10, pady=(20, 2), sticky="n")
    boton_registro = Button(ventana, text="Registrarse", font=("Arial", 14),
                            command=lambda: actualizar_ventana(lambda:mostrar_registro_usuario(True,True,True,True,True,True,True,True,True,False,False)), bg="lightblue")
    boton_registro.grid(row=6, column=1, padx=10, pady=(2, 10), sticky="n")

#funcion para registrar un usuario
datos_Registro = None

def mostrar_registro_usuario(condicion_fecha, condicion_mail, condicion_contrasena, condicion_DNI, condicion_tlf, condicion_numero_tarjeta, condicion_nombre, condicion_apellido1, condicion_apellido2, unicidad_dni, unicidad_mail):
    global datos_Registro

    # Configura las columnas del grid de la ventana para centrar el frame
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=0)
    ventana.grid_columnconfigure(2, weight=1)

    # Crea un frame centrado
    frame = Frame(ventana, bg="#E6E6E6")
    frame.grid(row=0, column=1, sticky="n", padx=40, pady=20)

    etiqueta_titulo = Label(frame, text="Registro de Usuario", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

    etiqueta_nombre = Label(frame, text="Nombre*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="n")
    entrada_nombre = Entry(frame, font=("Arial", 14), width=20)
    entrada_nombre.grid(row=1, column=1, padx=10, pady=5, sticky="n")
    if condicion_nombre == False:
        etiqueta_error_nombre = Label(frame, text="Nombre inválido", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_nombre.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        entrada_nombre.config(bg="lightcoral")
    else:
        entrada_nombre.config(bg="white")
        if datos_Registro is not None:
            entrada_nombre.insert(0, datos_Registro["nombre"])

    etiqueta_apellido1 = Label(frame, text="Apellido 1*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_apellido1.grid(row=2, column=0, padx=10, pady=5, sticky="n")
    entrada_apellido1 = Entry(frame, font=("Arial", 14), width=20)
    entrada_apellido1.grid(row=2, column=1, padx=10, pady=5, sticky="n")
    if condicion_apellido1 == False:
        etiqueta_error_apellido1 = Label(frame, text="Apellido inválido", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_apellido1.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        entrada_apellido1.config(bg="lightcoral")
    else:
        entrada_apellido1.config(bg="white")
        if datos_Registro is not None:
            entrada_apellido1.insert(0, datos_Registro["apellido1"])

    etiqueta_apellido2 = Label(frame, text="Apellido 2:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_apellido2.grid(row=3, column=0, padx=10, pady=5, sticky="n")
    entrada_apellido2 = Entry(frame, font=("Arial", 14), width=20)
    entrada_apellido2.grid(row=3, column=1, padx=10, pady=5, sticky="n")
    if datos_Registro is not None:
        apellido2 = datos_Registro["apellido2"]
    else:
        apellido2 = ""
    if apellido2 != "":
        if condicion_apellido2 == False:
            etiqueta_error_apellido2 = Label(frame, text="Apellido inválido", font=("Arial", 12), bg="#E6E6E6", fg="red")
            etiqueta_error_apellido2.grid(row=3, column=2, padx=10, pady=5, sticky="w")
            entrada_apellido2.config(bg="lightcoral")
        else:
            entrada_apellido2.config(bg="white")
            if datos_Registro is not None:
                entrada_apellido2.insert(0, datos_Registro["apellido2"])

    etiqueta_dni = Label(frame, text="DNI*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_dni.grid(row=4, column=0, padx=10, pady=5, sticky="n")
    entrada_dni = Entry(frame, font=("Arial", 14), width=20)
    entrada_dni.grid(row=4, column=1, padx=10, pady=5, sticky="n")
    if condicion_DNI == False:
        etiqueta_error_dni = Label(frame, text="DNI inválido", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_dni.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        entrada_dni.config(bg="lightcoral")
    elif unicidad_dni:
        etiqueta_error_dni = Label(frame, text="El DNI introducido ya existe", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_dni.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        entrada_dni.config(bg="lightcoral")
    else:
        entrada_dni.config(bg="white")
        if datos_Registro is not None:
            entrada_dni.insert(0, datos_Registro["dni"])

    etiqueta_numero_tarjeta = Label(frame, text="Número de Tarjeta*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_numero_tarjeta.grid(row=5, column=0, padx=10, pady=5, sticky="n")
    entrada_numero_tarjeta = Entry(frame, font=("Arial", 14), width=20)
    entrada_numero_tarjeta.grid(row=5, column=1, padx=10, pady=5, sticky="n")
    if condicion_numero_tarjeta == False:
        etiqueta_error_numero_tarjeta = Label(frame, text="Número de tarjeta inválido: debe contener 16 dígitos", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_numero_tarjeta.grid(row=5, column=2, padx=10, pady=5, sticky="w")
        entrada_numero_tarjeta.config(bg="lightcoral")  
    else:
        entrada_numero_tarjeta.config(bg="white")
        if datos_Registro is not None:
            entrada_numero_tarjeta.insert(0, datos_Registro["numero_tarjeta"])

    etiqueta_numero_tlf = Label(frame, text="Número de Teléfono*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_numero_tlf.grid(row=6, column=0, padx=10, pady=5, sticky="n")
    entrada_numero_tlf = Entry(frame, font=("Arial", 14), width=20)
    entrada_numero_tlf.grid(row=6, column=1, padx=10, pady=5, sticky="n")
    if condicion_tlf == False:  
        etiqueta_error_numero_tlf = Label(frame, text="Número de teléfono inválido: Debe contener 9 dígitos", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_numero_tlf.grid(row=6, column=2, padx=10, pady=5, sticky="w")
        entrada_numero_tlf.config(bg="lightcoral")
    else:
        entrada_numero_tlf.config(bg="white")
        if datos_Registro is not None:  
            entrada_numero_tlf.insert(0, datos_Registro["numero_tlf"])

    etiqueta_fecha_nacimiento = Label(frame, text="Fecha de Nacimiento*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_fecha_nacimiento.grid(row=7, column=0, padx=10, pady=5, sticky="n")
    entrada_fecha_nacimiento = Entry(frame, font=("Arial", 14), width=20)
    entrada_fecha_nacimiento.grid(row=7, column=1, padx=10, pady=5, sticky="n")
    etiqueta_error_fecha_nacimiento = Label(frame, text="", font=("Arial", 12), bg="#E6E6E6", fg="red")
    if condicion_fecha == False:
        etiqueta_error_fecha_nacimiento = Label(frame, text="Fecha inválida el formato debe ser: yyyy-mm-dd", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_fecha_nacimiento.grid(row=7, column=2, padx=10, pady=5, sticky="w")
        entrada_fecha_nacimiento.config(bg="lightcoral")
    else:
        entrada_fecha_nacimiento.config(bg="white")
        if datos_Registro is not None:
            entrada_fecha_nacimiento.insert(0, datos_Registro["fecha_nacimiento"])

    etiqueta_correo = Label(frame, text="Correo Electrónico*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_correo.grid(row=8, column=0, padx=10, pady=5, sticky="n")
    entrada_correo = Entry(frame, font=("Arial", 14), width=20)
    entrada_correo.grid(row=8, column=1, padx=10, pady=5, sticky="n")
    if condicion_mail == False:
        etiqueta_error_correo = Label(frame, text="Correo inválido", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_correo.grid(row=8, column=2, padx=10, pady=5, sticky="w")
        entrada_correo.config(bg="lightcoral")
    elif unicidad_mail:
        etiqueta_error_correo = Label(frame, text="El correo introducido ya existe", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_correo.grid(row=8, column=2, padx=10, pady=5, sticky="w")
        entrada_correo.config(bg="lightcoral")
    else:
        entrada_correo.config(bg="white")
        if datos_Registro is not None:
            entrada_correo.insert(0, datos_Registro["correo"])

    etiqueta_contrasena = Label(frame, text="Contraseña*:", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_contrasena.grid(row=9, column=0, padx=10, pady=5, sticky="n")
    entrada_contrasena = Entry(frame, show="*", font=("Arial", 14), width=20)
    entrada_contrasena.grid(row=9, column=1, padx=10, pady=5, sticky="n")
    if condicion_contrasena == False:
        etiqueta_error_contrasena = Label(frame, text="Contraseña inválida: Debe contener entre 8 y 16 caracteres,\n al menos una letra mayúscula, una letra minúscula y un dígito. ", font=("Arial", 12), bg="#E6E6E6", fg="red")
        etiqueta_error_contrasena.grid(row=9, column=2, padx=10, pady=5, sticky="w")
        entrada_contrasena.config(bg="lightcoral")
    else:
        entrada_contrasena.config(bg="white")

    # Botón para registrarse
    boton_registro = Button(frame, text="Registrarse", font=("Arial", 14),
                            command=lambda: registrar(entrada_nombre.get(), entrada_apellido1.get(), entrada_apellido2.get(), entrada_dni.get(), entrada_numero_tarjeta.get(), entrada_numero_tlf.get(), entrada_correo.get(), entrada_fecha_nacimiento.get(), entrada_contrasena.get()),
                            bg="lightblue")
    boton_registro.grid(row=10, column=0, columnspan=3, padx=10, pady=15, sticky="n")

    # Etiqueta "¿Ya tienes cuenta?"
    etiqueta_registro = Label(frame, text="¿Ya tienes cuenta?", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_registro.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="n")

    # Botón de login (debajo de la etiqueta)
    boton_regresar = Button(frame, text="Login", font=("Arial", 14),
                            command=lambda: actualizar_ventana(mostrar_login),
                            bg="lightblue")
    boton_regresar.grid(row=12, column=0, columnspan=3, padx=10, pady=10, sticky="n")

def comprobar_correo_bd(correo):
    """
    Comprueba si el correo electrónico ya existe en la base de datos.

    Args:
        correo (str): Correo electrónico a comprobar.

    Returns:
        bool: True si el correo ya existe, False en caso contrario.
    """
    resultados = traer_correos_bd()
    if resultados != False:
        for resultado in resultados:
            if resultado == correo:
                return True
    return False

def comprobar_dni_bd(dni):
    """
    Comprueba si el DNI ya existe en la base de datos.

    Args:
        dni (str): DNI a comprobar.

    Returns:
        bool: True si el DNI ya existe, False en caso contrario.
    """
    resultados = traer_dni_bd()
    if resultados != False:
        for resultado in resultados:
            if resultado    == dni:
                return True
    return False

def comprobar_correo(correo):
    """
    Comprueba si el correo electrónico es válido con una expresión regular.

    Args:
        correo (str): Correo electrónico a comprobar.

    Returns:
        bool: True si el correo es válido, False en caso contrario.
    """
    patron = r'^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
    if re.match(patron, correo):
        return True
    else:
        return False

def comprobar_contrasena(contrasena):
    """
    Comprueba si la contraseña es válida con una expresión regular.

    Args:
        contrasena (str): Contraseña a comprobar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    #regex para comprobar la contraseña Al menos 6 caracteres, al menos una letra mayúscula, una letra minúscula y un número.
    patron = r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$'
    if re.match(patron, contrasena):
        return True
    else:
        return False

def comprobar_dni(dni):
    """
    Comprueba si el DNI es válido con una expresión regular.

    Args:
        dni (str): DNI a comprobar.

    Returns:
        bool: True si el DNI es válido, False en caso contrario.
    """
    #regex para comprobar el dni
    patron = r'^\d{8}[A-Z]$'
    if re.match(patron, dni):
        return True
    else:
        return False

def comprobar_numero_tlf(numero_tlf):
    """
    Comprueba si el número de teléfono es válido con una expresión regular.

    Args:
        numero_tlf (str): Número de teléfono a comprobar.

    Returns:
        bool: True si el número de teléfono es válido, False en caso contrario.
    """
    #regex para comprobar el numero de telefono
    patron = r'^\d{9}$'
    if re.match(patron, numero_tlf):
        return True
    else:
        return False
    
def comprobar_numero_tarjeta(numero_tarjeta):
    """
    Comprueba si el número de tarjeta es válido con una expresión regular.

    Args:
        numero_tarjeta (str): Número de tarjeta a comprobar.

    Returns:
        bool: True si el número de tarjeta es válido, False en caso contrario.
    """
    #regex para comprobar el numero de tarjeta
    patron = r'^\d{16}$'
    if re.match(patron, numero_tarjeta):
        return True
    else:
        return False
def comprobar_cadena(cadena):
    """
    comprueba que una cadena de texto contiene solo letras
     Args:
        cadena (str): Cadena a comprobar.
        Returns:
        bool: True si la cadena es válida, False en caso contrario.
    """
    #regex para comprobar que la cadena contiene solo letras
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$'
    if re.match(patron, cadena):
        return True
    else:
        return False
    
def comprobar_fecha(fecha):
    """
    Comprueba si la fecha es válida con una expresión regular.

    Args:
        fecha (str): Fecha a comprobar.

    Returns:
        bool: True si la fecha es válida, False en caso contrario.
    """
    fecha_correta = True
    #regex para comprobar la fecha
    patron = r'^\d{4}-\d{2}-\d{2}$'
    # Comprobar si la fecha tiene el formato YYYY-MM-DD
    # y si es una fecha válida
    # Puedes usar el módulo datetime para validar la fecha
    if fecha == "":
        fecha_correta = False
    elif not re.match(patron, fecha):
        fecha_correta=False
    else:
        anio, mes, dia = map(int, fecha.split('-'))
        if anio < 1900 or anio > 2023:
            fecha_correta = False
        elif mes < 1 or mes > 12:
            fecha_correta = False
        elif dia < 1 or dia > 31:
            fecha_correta = False
        elif mes == 2 and dia > 29:
            fecha_correta = False
        elif mes in [4, 6, 9, 11] and dia > 30:
            fecha_correta = False
        elif re.match(patron, fecha):
            fecha_correta = True
        else:
            fecha_correta = False
    return fecha_correta
    
def registrar(nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento, contrasena):
    """
    Registra un nuevo usuario en la base de datos.
    """
    global datos_Registro
    # Eliminar espacios en blanco
    nombre = nombre.strip()  
    apellido1 = apellido1.strip()
    apellido2 = apellido2.strip()
    dni = dni.strip()
    numero_tarjeta = numero_tarjeta.strip()
    numero_tlf = numero_tlf.strip()
    correo = correo.strip()
    fecha_nacimiento = fecha_nacimiento.strip()
    datos_Registro = {
        "nombre": nombre,
        "apellido1": apellido1,
        "apellido2": apellido2,
        "dni": dni,
        "numero_tarjeta": numero_tarjeta,
        "numero_tlf": numero_tlf,
        "correo": correo,
        "fecha_nacimiento": fecha_nacimiento
    }
    condicion_fecha = comprobar_fecha(fecha_nacimiento)
    condicion_mail = comprobar_correo(correo)
    unicidad_mail = comprobar_correo_bd(correo)
    condicion_contrasena = comprobar_contrasena(contrasena)
    condicion_DNI = comprobar_dni(dni)
    unicidad_dni = comprobar_dni_bd(dni)
    condicion_tlf = comprobar_numero_tlf(numero_tlf)
    condicion_numero_tarjeta = comprobar_numero_tarjeta(numero_tarjeta)
    condicion_nombre = comprobar_cadena(nombre)
    condicion_apellido1 = comprobar_cadena(apellido1)
    condicion_apellido2 = comprobar_cadena(apellido2)
    if condicion_nombre and condicion_apellido1 and (condicion_apellido2 or apellido2 == "") and condicion_DNI and unicidad_dni == False and condicion_contrasena and condicion_fecha and condicion_tlf and condicion_mail and unicidad_mail == False and condicion_numero_tarjeta: 
        cliente = Cliente(None,nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento, contrasena)
        insertar_cliente_bd(cliente)
        Messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")
        actualizar_ventana(mostrar_login)
        datos_Registro = None
    else:
        Messagebox.showerror("Error", "Por favor comprueba los campos en rojo.")
        actualizar_ventana(lambda:mostrar_registro_usuario(condicion_fecha, condicion_mail, condicion_contrasena, condicion_DNI, condicion_tlf, condicion_numero_tarjeta, condicion_nombre, condicion_apellido1, condicion_apellido2,unicidad_dni,unicidad_mail))

def cerrar_programa():
    """
    Cierra la ventana principal y termina el programa.
    """
    ventana.destroy()

def cerrar_sesion():
    """
    Cierra la sesión del usuario y vuelve a la pantalla de inicio de sesión.
    """
    actualizar_ventana(interfaz_bienvenida)

def boton_regresar_a_menu_cliente(carrito,cliente):
    actualizar_ventana(lambda: mostrar_menu_principal(carrito,cliente))

def boton_regresar_modificar(carrito,cliente):
    actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))

########################
#####  PRODUCTOS  ######
########################

def mostrar_productos(pagina_actual, carrito, cliente):
    """
    Muestra los productos disponibles en la página actual y agrega botones de navegación.
    """
    # Cargar la imagen para el botón de la cesta
    imagen_cesta = Image.open(r"C:\Users\carlo\Desktop\python\Proyecto-Esail-Python\images\carro.png")  # Ruta de la imagen
    imagen_cesta = imagen_cesta.resize((150, 150), Image.Resampling.LANCZOS)  # Redimensionar la imagen
    imagen_cesta_tk = ImageTk.PhotoImage(imagen_cesta)

    # Título de la página
    etiqueta_titulo = Label(ventana, text="Productos Disponibles", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

    # Mostrar los productos
    productos = obtener_productos_paginados(pagina_actual)  # Obtener los productos de la página actual
    for i, producto in enumerate(productos, start=1):
        # Crear un frame para el producto
        frame_producto = Frame(ventana, bg="white", relief=SOLID, borderwidth=1)
        frame_producto.grid(row=i, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Configurar las columnas del grid para alineación
        frame_producto.grid_columnconfigure(0, weight=1, minsize=600)  # Columna para la información del producto
        frame_producto.grid_columnconfigure(1, weight=0, minsize=150)  # Columna para los controles

        # Información del producto
        etiqueta_nombre = Label(frame_producto, text=f"Nombre: {producto.nombre_producto}", font=("Arial", 14), bg="white", anchor="w")
        etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        etiqueta_precio = Label(frame_producto, text=f"Precio: ${producto.precio:.2f}", font=("Arial", 14), bg="white", anchor="w")
        etiqueta_precio.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        etiqueta_descripcion = Label(frame_producto, text=f"Descripción: {producto.descripcion}", font=("Arial", 12), bg="white", wraplength=600, justify=LEFT, anchor="w")
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
                command=lambda i=indice_producto: (incrementar_cantidad_carrito(carrito, cliente, i, -1), actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito, cliente)))
            ).grid(row=0, column=0, padx=5)

            # Cuadro de texto para la cantidad
            entrada_cantidad = Entry(frame_controles, font=("Arial", 12), width=3, justify="center")
            entrada_cantidad.insert(0, str(cantidad_actual))
            entrada_cantidad.grid(row=0, column=1, padx=5)

            # Asociar el evento "Enter" al cuadro de texto
            entrada_cantidad.bind(
                "<Return>",
                lambda event, i=indice_producto, e=entrada_cantidad: actualizar_cantidad_manual_producto(cliente, event, carrito, i, e, pagina_actual)
            )

            # Botón para aumentar la cantidad
            Button(
                frame_controles,
                text="+",
                font=("Arial", 12),
                command=lambda i=indice_producto: (incrementar_cantidad_carrito(carrito, cliente, i, 1), actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito, cliente)))
            ).grid(row=0, column=2, padx=5)
        else:
            # Botón para agregar al carrito
            boton_agregar_carrito = Button(frame_producto, text="Agregar al Carrito", font=("Arial", 12), bg="lightblue",
                                           command=lambda p=producto: agregar_al_carrito(p, carrito, cliente, pagina_actual))
            boton_agregar_carrito.grid(row=0, column=1, rowspan=3, padx=10, pady=5, sticky="e")

    # Botón de la cesta de la compra
    boton_cesta = Button(ventana, image=imagen_cesta_tk, command=lambda: actualizar_ventana(lambda: mostrar_cesta_compra(carrito, cliente)), bg="#E6E6E6", borderwidth=0)
    boton_cesta.image = imagen_cesta_tk  # Mantener una referencia para evitar que se recolecte como basura
    boton_cesta.grid(row=1, column=2, padx=20, pady=10, sticky="n")
    
    # Botón para regresar al menú principal (debajo de la cesta)
    boton_regresar = Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
                            command=lambda: boton_regresar_a_menu_cliente(carrito, cliente))
    boton_regresar.grid(row=2, column=2, padx=20, pady=10, sticky="n")

    # Mostrar el número de página actual centrado debajo de los productos
    etiqueta_pagina = Label(ventana, text=f"Página {pagina_actual}", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_pagina.grid(row=len(productos) + 1, column=0, columnspan=2, pady=10, sticky="n")

    # Botones de navegación centrados debajo del número de página
    frame_navegacion = Frame(ventana, bg="#E6E6E6")
    frame_navegacion.grid(row=len(productos) + 2, column=0, columnspan=2, pady=20, sticky="n")

    if pagina_actual > 1:
        boton_anterior = Button(frame_navegacion, text="Página Anterior", font=("Arial", 14), bg="lightblue",
                                command=lambda: decrementar_pagina(pagina_actual, carrito, cliente))
        boton_anterior.grid(row=0, column=0, padx=10)

    boton_siguiente = Button(frame_navegacion, text="Siguiente Página", font=("Arial", 14), bg="lightblue",
                              command=lambda: incrementar_pagina(pagina_actual, carrito, cliente))
    boton_siguiente.grid(row=0, column=1, padx=10)

# Función para modificar la cantidad de un producto
def incrementar_cantidad_carrito(carrito, cliente, posicion, incremento):
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

def actualizar_cantidad_manual_producto(cliente,event, carrito, posicion, entrada_cantidad,pagina_actual):
    """
    Actualiza la cantidad de un producto en el carrito manualmente. Detecta el evento de teclado (Enter) para realizar la acción.

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
        actualizar_ventana(lambda: mostrar_productos(pagina_actual,carrito,cliente))
    except ValueError:
        Messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo actualizar la cantidad: {e}")

def agregar_al_carrito(producto, carrito, cliente, pagina_actual):

    insertar_producto_cesta(carrito,producto, 1)  # Agregar el producto a la base de datos
    # Actualizar la interfaz para reflejar los cambios
    actualizar_ventana(lambda: mostrar_productos(pagina_actual, carrito,cliente))

def incrementar_pagina(pagina_actual,carrito,cliente):
    """
    Incrementa la página actual y actualiza la vista de productos.
    """
    pagina_actual += 1
    productos = obtener_productos_paginados(pagina_actual)
    if productos:
        actualizar_ventana(lambda:mostrar_productos(pagina_actual,carrito,cliente))
    else:
        Messagebox.showinfo("Información", "No hay más productos para mostrar.")
 
def decrementar_pagina(pagina_actual,carrito,cliente):
    """
    Decrementa la página actual y actualiza la vista de productos.
    """
    pagina_actual -= 1
    actualizar_ventana(lambda:mostrar_productos(pagina_actual,carrito,cliente))

########################
### Cesta de compra ####
########################

def calcular_precio_total(cesta_compra):
    """
    Calcula el precio total de los productos en la cesta de compra.

    Args:
        cesta_compra (list): Lista que contiene los productos y sus cantidades.

    Returns:
        float: Precio total de la cesta de compra.
    """
    total = 0
    for producto, cantidad in zip(cesta_compra[0], cesta_compra[1]):
        total += producto.precio * cantidad
    return total

# Función principal para mostrar la cesta de compra
def mostrar_cesta_compra(cesta_compra, cliente, pagina_actual=1, productos_por_pagina=5):
    """
    Muestra los productos en la cesta de compra con paginación.

    Args:
        cesta_compra (list): Lista que contiene los productos y sus cantidades.
        cliente (Cliente): Cliente actual.
        pagina_actual (int): Página actual que se está mostrando.
        productos_por_pagina (int): Número de productos a mostrar por página.
    """
    limpiar_ventana(ventana)
    mostrar_titulo(ventana)

    total_productos = len(cesta_compra[0])
    total_paginas = (total_productos + productos_por_pagina - 1) // productos_por_pagina
    frame_botones = Frame(ventana, bg="#E6E6E6")
    frame_botones.grid(row=productos_por_pagina + 3, column=0, columnspan=3, pady=20)
    # Obtener los productos de la página actual
    inicio = (pagina_actual - 1) * productos_por_pagina
    fin = inicio + productos_por_pagina
    productos_pagina = cesta_compra[0][inicio:fin]
    cantidades_pagina = cesta_compra[1][inicio:fin]

    if productos_pagina:
        for i, (producto, cantidad) in enumerate(zip(productos_pagina, cantidades_pagina), start=1):
            mostrar_producto_en_carrito(ventana, producto, cantidad, i, cesta_compra, cliente)

        # Botones de navegación
        frame_navegacion = Frame(ventana, bg="#E6E6E6")
        frame_navegacion.grid(row=productos_por_pagina + 2, column=0, columnspan=3, pady=20)

        if pagina_actual > 1:
            boton_anterior = Button(frame_navegacion, text="Página Anterior", font=("Arial", 14), bg="lightblue",
                                    command=lambda: mostrar_cesta_compra(cesta_compra, cliente, pagina_actual - 1, productos_por_pagina))
            boton_anterior.grid(row=0, column=0, padx=10)

        if pagina_actual < total_paginas:
            boton_siguiente = Button(frame_navegacion, text="Siguiente Página", font=("Arial", 14), bg="lightblue",
                                    command=lambda: mostrar_cesta_compra(cesta_compra, cliente, pagina_actual + 1, productos_por_pagina))
            boton_siguiente.grid(row=0, column=1, padx=10)

        # Botón para comprar productos (al lado del botón de regresar)
        boton_comprar = Button(frame_botones, text="Comprar Productos", font=("Arial", 14), bg="lightblue",
                            command=lambda: comprar(cesta_compra, cliente))
        boton_comprar.grid(row=0, column=1, padx=10)

        etiqueta_precio_total = Label(frame_botones, text=f"Precio Total: {calcular_precio_total(cesta_compra):.2f}€", font=("Arial", 14), bg="#E6E6E6")
        etiqueta_precio_total.grid(row=0, column=2, padx=10)
        
    else:   
        Label(
            ventana,
            text="La cesta de compra está vacía.",
            font=("Arial", 16),
            bg="#E6E6E6"
        ).grid(row=1, column=0, columnspan=3, pady=20, sticky="n")


    boton_regresar = Button(frame_botones, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
                            command=lambda: boton_regresar_a_menu_cliente(cesta_compra, cliente))
    boton_regresar.grid(row=0, column=0, padx=10)

# Función para mostrar la cesta de compra
def limpiar_ventana(ventana):
    """
    Limpia todos los widgets de la ventana y restablece las configuraciones del grid.
    """
    for widget in ventana.winfo_children():
        widget.destroy()
    ventana.geometry("1600x900")  # Restablecer el tamaño de la ventana

# Función para mostrar el título
def mostrar_titulo(ventana, texto="Cesta de Compra"):
    titulo = Label(ventana, text=texto, font=("Arial", 24), bg="#E6E6E6")
    titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

# Función para mostrar un producto en la interfaz
def mostrar_producto_en_carrito(ventana, producto, cantidad, indice, cesta_compra, cliente):
    """
    Muestra un producto en el carrito con controles para modificar la cantidad.
    """
    # Crear un frame para el producto
    frame_producto = Frame(ventana, bg="#E6E6E6")
    frame_producto.grid(row=indice + 1, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    # Configurar las columnas del grid para alineación
    frame_producto.grid_columnconfigure(0, weight=1, minsize=800)  # Aumentar el tamaño mínimo de la columna para la información del producto
    frame_producto.grid_columnconfigure(1, weight=0, minsize=150)  # Columna para los controles
    frame_producto.grid_columnconfigure(2, weight=0, minsize=100)  # Columna para el botón eliminar

    # Información del producto
    texto_producto = f"{producto.nombre_producto} - Precio Unitario: {producto.precio}€ - Precio Total: {producto.precio * cantidad}€"
    Label(frame_producto, text=texto_producto, font=("Arial", 14), bg="#E6E6E6", anchor="w", wraplength=800).grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Controles para modificar la cantidad
    frame_controles = Frame(frame_producto, bg="#E6E6E6")
    frame_controles.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    # Botón para disminuir la cantidad
    Button(
        frame_controles,
        text="-",
        font=("Arial", 12),
        width=3,  # Ancho fijo
        command=lambda: disminuir_cantidad_cesta_compra(cesta_compra, cliente, indice-1)
    ).grid(row=0, column=0, padx=5)

    # Cuadro de texto para la cantidad
    entrada_cantidad = Entry(frame_controles, font=("Arial", 14), width=5, justify="center")  # Ancho fijo
    entrada_cantidad.insert(0, str(cantidad))
    entrada_cantidad.grid(row=0, column=1, padx=5)

    # Asociar el evento "Enter" al cuadro de texto
    entrada_cantidad.bind(
        "<Return>",
        lambda event: actualizar_cantidad_manual_cesta(cliente, event, cesta_compra, indice, entrada_cantidad)
    )

    # Botón para aumentar la cantidad
    Button(
        frame_controles,
        text="+",
        font=("Arial", 12),
        width=3,  # Ancho fijo
        command=lambda: aumentar_cantidad_cesta(cesta_compra, cliente, indice-1)
    ).grid(row=0, column=2, padx=5)

    # Botón para eliminar el producto
    Button(
        frame_producto,
        text="Eliminar",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,  # Ancho fijo
        command=lambda: eliminar_producto(cesta_compra, cliente, indice - 1)
    ).grid(row=0, column=2, padx=10, pady=5, sticky="e")
    
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

# Función para eliminar un producto
def eliminar_producto(cesta_compra, cliente, posicion):
    try:
        modificar_cantidad_producto(cesta_compra, posicion + 1, 0)
        mostrar_cesta_compra(cesta_compra, cliente)
    except Exception as e:
        Messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")

# Función para comprar los productos
def comprar(cesta_compra, cliente):
    if len(cesta_compra[0]) == 0: 
        Messagebox.showerror("Error", "La cesta de compra está vacía.")
    else:
        comprar_productos_cesta(cesta_compra, cliente)
        mostrar_cesta_compra(cesta_compra, cliente)

# Función para mostrar el botón de comprar
def mostrar_boton_comprar(ventana, cesta_compra, cliente):
    Button(
        ventana,
        text="Comprar Productos",
        font=("Arial", 14),
        command=lambda: comprar(cesta_compra, cliente)
    ).grid(row=len(cesta_compra[0]) + 1, column=0, columnspan=2, pady=20)

########################
######  TICKETS  #######
########################

def mostrar_tickets(carrito, cliente, pagina_actual=1, tickets_por_pagina=10):
    """
    Muestra los tickets de un cliente en la interfaz gráfica, agrupando los productos por fecha.
    """
    limpiar_ventana(ventana)

    # Obtener los tickets del cliente
    tickets_cliente = obtener_tickets_cliente(cliente)  # Devuelve una lista de productos con sus fechas

    etiqueta_tickets = Label(ventana, text="Tickets de Compra", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_tickets.grid(row=0, column=0, columnspan=5, pady=10, sticky="n")

    # Agrupar los tickets por fecha
    tickets_cliente_por_fecha = {}
    for ticket in tickets_cliente:
        fecha = ticket['fecha']
        if fecha not in tickets_cliente_por_fecha:
            tickets_cliente_por_fecha[fecha] = []
        tickets_cliente_por_fecha[fecha].append(ticket)

    # Convertir el diccionario en una lista de tuplas para paginación
    tickets_agrupados = list(tickets_cliente_por_fecha.items())
    total_paginas = (len(tickets_agrupados) + tickets_por_pagina - 1) // tickets_por_pagina
    row = 1
    # Obtener los tickets de la página actual
    inicio = (pagina_actual - 1) * tickets_por_pagina
    fin = inicio + tickets_por_pagina
    tickets_pagina = tickets_agrupados[inicio:fin]

    # Mostrar los tickets agrupados por fecha
    if tickets_pagina:
        for fecha, tickets in tickets_pagina:
            # Crear un frame para el ticket
            frame_ticket = Frame(ventana, bg="white", relief=SOLID, borderwidth=1)
            frame_ticket.grid(row=row, column=0, columnspan=5, padx=20, pady=10, sticky="n")
            row += 1

            # Información del ticket
            etiqueta_ticket = Label(frame_ticket, text=f"Ticket del: {fecha}", font=("Arial", 14), bg="white")
            etiqueta_ticket.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            # Botón para ver los detalles del ticket
            boton_detalles = Button(frame_ticket, text="Ver Detalles", font=("Arial", 12), bg="lightblue",
                                    command=lambda t=tickets: mostrar_detalles_ticket(t))
            boton_detalles.grid(row=0, column=1, padx=10, pady=5, sticky="e")
    else:
        etiqueta_no_tickets = Label(
            ventana,
            text="No se encontraron tickets para este cliente.",
            font=("Arial", 14),
            bg="#E6E6E6"
        )
        etiqueta_no_tickets.grid(row=1, column=0, columnspan=5, pady=20, sticky="n")

    # Botones de navegación
    frame_navegacion = Frame(ventana, bg="#E6E6E6")
    frame_navegacion.grid(row=row, column=0, columnspan=5, pady=20, sticky="n")

    if pagina_actual > 1:
        boton_anterior = Button(frame_navegacion, text="Página Anterior", font=("Arial", 14), bg="lightblue",
                                command=lambda: mostrar_tickets(carrito, cliente, pagina_actual - 1, tickets_por_pagina))
        boton_anterior.grid(row=0, column=0, padx=10)

    if pagina_actual < total_paginas:
        boton_siguiente = Button(frame_navegacion, text="Siguiente Página", font=("Arial", 14), bg="lightblue",
                                  command=lambda: mostrar_tickets(carrito, cliente, pagina_actual + 1, tickets_por_pagina))
        boton_siguiente.grid(row=0, column=1, padx=10)

    # Botón para regresar al menú principal
    Button(
        ventana,
        text="Regresar al Menú Principal",
        font=("Arial", 14),
        bg="lightblue",
        command=lambda: boton_regresar_a_menu_cliente(carrito, cliente)
    ).grid(row=row + 1, column=0, columnspan=5, pady=20, sticky="n")

def mostrar_detalles_ticket(tickets):
    """
    Muestra los detalles de un grupo de tickets en una nueva ventana con un scrollbar vertical.

    Args:
        tickets (list): Lista de tickets a mostrar.
    """
    # Crear una nueva ventana para mostrar los detalles del ticket
    ventana_detalles = Toplevel(ventana)
    ventana_detalles.title("Detalles del Ticket")
    ventana_detalles.geometry("450x600")
    ventana_detalles.configure(bg="#E6E6E6")
    ventana_detalles.resizable(False, False)

    # Crear un frame principal para contener el canvas y el scrollbar
    frame_principal = Frame(ventana_detalles, bg="#E6E6E6")
    frame_principal.pack(fill=BOTH, expand=True)

    # Crear un canvas dentro del frame principal
    canvas = Canvas(frame_principal, bg="#E6E6E6")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Crear un scrollbar vertical y asociarlo al canvas
    scrollbar = Scrollbar(frame_principal, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configurar el canvas para usar el scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Crear un frame dentro del canvas para contener los widgets
    frame_contenido = Frame(canvas, bg="#E6E6E6")
    canvas.create_window((0, 0), window=frame_contenido, anchor="n")

    # Mostrar los detalles del ticket
    etiqueta_detalles = Label(frame_contenido, text="Detalles del Ticket", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_detalles.pack(pady=10)

    for ticket in tickets:
        # Crear un frame para el producto con tamaño fijo
        frame_producto = Frame(frame_contenido, bg="white", relief=SOLID, borderwidth=1, width=400, height=175)
        frame_producto.pack(padx=20, pady=10)
        frame_producto.pack_propagate(False)  # Evitar que el frame cambie de tamaño según su contenido

        # Información del producto
        etiqueta_nombre = Label(frame_producto, text=f"Nombre: {ticket['nombre_producto']}", font=("Arial", 14), bg="white", wraplength=380, justify="left")
        etiqueta_nombre.pack(pady=5)

        etiqueta_precio = Label(frame_producto, text=f"Precio: ${ticket['precio']:.2f}", font=("Arial", 14), bg="white", wraplength=380, justify="left")
        etiqueta_precio.pack(pady=5)

        etiqueta_cantidad = Label(frame_producto, text=f"Cantidad: {ticket['cantidad']}", font=("Arial", 14), bg="white", wraplength=380, justify="left")
        etiqueta_cantidad.pack(pady=5)

        etiqueta_precio_total = Label(frame_producto, text=f"Precio Total: ${ticket['precio'] * ticket['cantidad']:.2f}", font=("Arial", 14), bg="white", wraplength=380, justify="left")
        etiqueta_precio_total.pack(pady=5)

    # Botón para cerrar la ventana de detalles
    boton_cerrar = Button(ventana_detalles, text="Cerrar", font=("Arial", 12), bg="lightblue", command=ventana_detalles.destroy)
    boton_cerrar.pack(pady=10)
    etiqueta_precio_total = Label(ventana_detalles, text=f"Precio Total: {calcular_precio_total_tickets(tickets):.2f}€", font=("Arial", 14), bg="#E6E6E6")
    etiqueta_precio_total.pack(pady=10)

def calcular_precio_total_tickets(tickets):
    """
    Calcula el precio total de los productos en un ticket.

    Args:
        tickets (list): Lista de tickets a calcular.

    Returns:
        float: Precio total del ticket.
    """
    total = 0
    for ticket in tickets:
        total += ticket['precio'] * ticket['cantidad']
    return total
########################
###  DATOS CLIENTE  ####
########################

def mostrar_datos_cliente(carrito,cliente):
    """
    Muestra los datos del cliente y agrega botones para modificar ciertos campos.
    """
    etiqueta_datos_cliente = Label(ventana, text="Datos del Cliente", font=("Arial", 20), bg="#E6E6E6")
    etiqueta_datos_cliente.grid(row=0, column=0, columnspan=3, pady=20)

    # Mostrar los datos del cliente
    Label(ventana, text=f"Nombre: {cliente.nombre}", font=("Arial", 14), bg="#E6E6E6").grid(row=1, column=0, padx=10, pady=5)
    Label(ventana, text=f"Apellido 1: {cliente.apellido1}", font=("Arial", 14), bg="#E6E6E6").grid(row=2, column=0, padx=10, pady=5)
    Label(ventana, text=f"Apellido 2: {cliente.apellido2}", font=("Arial", 14), bg="#E6E6E6").grid(row=3, column=0, padx=10, pady=5)
    Label(ventana, text=f"DNI: {cliente.DNI}", font=("Arial", 14), bg="#E6E6E6").grid(row=4, column=0, padx=10, pady=5)

    # Número de tarjeta con botón para modificar
    Label(ventana, text=f"Número de Tarjeta: {cliente.numero_tarjeta}", font=("Arial", 14), bg="#E6E6E6").grid(row=5, column=0, padx=10, pady=5)
    boton_modificar_tarjeta = Button(ventana, text="Modificar", font=("Arial", 12), bg="lightblue", command=lambda: modificar_numero_tarjeta(carrito,cliente))
    boton_modificar_tarjeta.grid(row=5, column=1, padx=10, pady=5)

    # Número de teléfono con botón para modificar
    Label(ventana, text=f"Número de Teléfono: {cliente.numero_tlf}", font=("Arial", 14), bg="#E6E6E6").grid(row=6, column=0, padx=10, pady=5)
    boton_modificar_tlf = Button(ventana, text="Modificar", font=("Arial", 12), bg="lightblue", command=lambda: modificar_numero_tlf(carrito,cliente))
    boton_modificar_tlf.grid(row=6, column=1, padx=10, pady=5)

    # Contraseña con botón para modificar
    boton_modificar_contrasena = Button(ventana, text="Cambiar contraseña", font=("Arial", 12), bg="lightblue", command=lambda: modificar_contrasena(carrito,cliente))
    boton_modificar_contrasena.grid(row=9, column=0, padx=10, pady=5)

    # Botón para eliminar cuenta
    boton_eliminar_cuenta = Button(ventana, text="Eliminar Cuenta", font=("Arial", 12), bg="red", command=lambda: eliminar_cliente(cliente))
    boton_eliminar_cuenta.grid(row=10, column=0, padx=10, pady=5)

    # Correo electrónico
    Label(ventana, text=f"Correo Electrónico: {cliente.correo}", font=("Arial", 14), bg="#E6E6E6").grid(row=8, column=0, padx=10, pady=5)
    Label(ventana, text=f"Fecha de Nacimiento: {cliente.fecha_nacimiento}", font=("Arial", 14), bg="#E6E6E6").grid(row=7, column=0, padx=10, pady=5)
    # Botón para regresar al menú principal
    Button(ventana, text="Regresar al Menú Principal", font=("Arial", 14), bg="lightblue",
           command=lambda: boton_regresar_a_menu_cliente(carrito,cliente)).grid(row=11, column=1, columnspan=5, pady=20)

def eliminar_cliente(cliente):
    """
    Elimina la cuenta del cliente y cierra la sesión.
    """
    respuesta = Messagebox.askyesno("Eliminar Cuenta", "¿Estás seguro de que deseas eliminar tu cuenta?")
    if respuesta:
        borrar_tikets(cliente)
        borrar_cliente_bd(cliente)
        actualizar_ventana(lambda: mostrar_login())

def guardar_cambio_tarjeta(carrito,cliente,nuevo_numero):
    """
    Guarda el cambio del número de tarjeta del cliente.
    """
    if comprobar_numero_tarjeta(nuevo_numero):
        cliente.numero_tarjeta = nuevo_numero
        modificar_numero_tarjeta_cliente(cliente)
        Messagebox.showinfo("Éxito", "Número de tarjeta actualizado correctamente.")
        actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))
    else:
        Messagebox.showerror("Error", "Número de tarjeta inválido.")

def guardar_cambio_tlf(carrito,cliente,nuevo_numero):
    """
    Guarda el cambio del número de teléfono del cliente.
    """
    if comprobar_numero_tlf(nuevo_numero):
        cliente.numero_tlf = nuevo_numero
        modificar_numero_telefono_cliente(cliente)
        Messagebox.showinfo("Éxito", "Número de teléfono actualizado correctamente.")
        actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))
    else:
        Messagebox.showerror("Error", "Número de teléfono inválido.")

def modificar_numero_tarjeta(carrito,cliente):
    """
    Permite modificar el número de tarjeta del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Número de Tarjeta", font=("Arial", 20), bg="#E6E6E6").pack(pady=20)
    entrada_numero_tarjeta = Entry(ventana, font=("Arial", 14))
    entrada_numero_tarjeta.insert(0, cliente.numero_tarjeta)
    entrada_numero_tarjeta.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightblue", command=lambda: guardar_cambio_tarjeta(carrito,cliente,entrada_numero_tarjeta.get().strip())).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))).pack(pady=10)
    
def modificar_numero_tlf(carrito,cliente):
    """
    Permite modificar el número de teléfono del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Número de Teléfono", font=("Arial", 20), bg="#E6E6E6").pack(pady=20)
    entrada_numero_tlf = Entry(ventana, font=("Arial", 14))
    entrada_numero_tlf.insert(0, cliente.numero_tlf)
    entrada_numero_tlf.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightblue", command=lambda:guardar_cambio_tlf(carrito,cliente,entrada_numero_tlf.get().strip())).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))).pack(pady=10)

def guardar_cambio_contrasena(contrasena, nueva_contrasena, repetir_contrasena, carrito, cliente):

    if nueva_contrasena == repetir_contrasena:
        if contrasena == cliente.contraseña:
            if comprobar_contrasena(nueva_contrasena):
                cliente.contraseña = nueva_contrasena
                modificar_contraseña_cliente(cliente)
                Messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
                actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))
            else:
                Messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres, una letra mayúscula, una letra minúscula y un número.")
        else:
            Messagebox.showerror("Error", "La contraseña antigua no es correcta.")
    else:
        Messagebox.showerror("Error", "Las nuevas contraseñas no coinciden.")

def modificar_contrasena(carrito, cliente):
    """
    Permite modificar la contraseña del cliente.
    """
    limpiar_ventana(ventana)
    Label(ventana, text="Modificar Contraseña", font=("Arial", 20), bg="#E6E6E6").pack(pady=20)
    Label(ventana, text="Contraseña antigua:", font=("Arial", 14), bg="#E6E6E6").pack(pady=10)
    entrada_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_contrasena.pack(pady=10)
    Label(ventana, text="Nueva contraseña:", font=("Arial", 14), bg="#E6E6E6").pack(pady=10)
    entrada_nueva_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_nueva_contrasena.pack(pady=10)
    Label(ventana, text="Repetir nueva contraseña:", font=("Arial", 14), bg="#E6E6E6").pack(pady=10)
    entrada_repetir_contrasena = Entry(ventana, font=("Arial", 14), show="*")
    entrada_repetir_contrasena.pack(pady=10)
    Button(ventana, text="Guardar", font=("Arial", 14), bg="lightblue", command=lambda: guardar_cambio_contrasena(entrada_contrasena.get(),entrada_nueva_contrasena.get(),entrada_repetir_contrasena.get() ,carrito, cliente)).pack(pady=10)
    # Botón para regresar a los datos del cliente
    Button(ventana, text="Regresar", font=("Arial", 14), bg="lightblue", command=lambda: actualizar_ventana(lambda: mostrar_datos_cliente(carrito,cliente))).pack(pady=10)
    
actualizar_ventana(interfaz_bienvenida)
ventana.mainloop()

