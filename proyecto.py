from clases import Cliente, Producto, Ticket
from SQL.base_datos import *
from SQL.base_datos import conexion
from datetime import datetime


def main():
    
    cliente = None
    sesion = True  
    while sesion:
        cliente = menu_principal()
        if cliente != False:
            menu_cliente(cliente)
        else:
            sesion = False

def imprimir_opciones_menu_principal():
    print("Bienvenido a CristoMarket.")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion     
       
def imprimir_opciones_menu_cliente():
    print("Bienvenido a CristoMarket.")
    print("1. Añadir productos a la cesta")
    print("2. Ver cesta de la compra")
    print("3. Ver tickets")
    print("4. Modificar datos de cliente")
    print("5. Borrar cliente")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def imprimir_opciones_gestion_cesta():
    print("Gestión de la cesta de la compra:")
    print("1. Eliminar un producto de la cesta")
    print("2. Cambiar cantidad de un producto en la cesta")
    print("3. Comprar productos de la cesta")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def imprimir_menu_modificar_cliente(): 
    print("Modificar datos de cliente:")
    print("1. Modificar número de tarjeta")
    print("2. Modificar número de teléfono")
    print("3. Cambiar contraseña")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_principal():
    cliente = None
    bucle = True
    while bucle:
        opcion =imprimir_opciones_menu_principal()
        if opcion == "1":
            bucle = False
            cliente = login()
        elif opcion == "2":
            cliente = registro()
        elif opcion == "3":
            print("Saliendo del programa.")
            cliente = False
            bucle = False
        else:
            print("Opción no válida. Intente de nuevo.")
    return cliente

def menu_cliente(cliente):
    salir = False
    cesta_compra = [[], []] 
    while salir == False:
        opcion = imprimir_opciones_menu_cliente()
        if opcion == "1":
            añadir_producto_cesta(cesta_compra)
        elif opcion == "2":
            gestionar_cesta_compra(cesta_compra,cliente)
        elif opcion == "3":
           mostrar_tickets_cliente(cliente)
        elif opcion == "4":
            menu_modificar_cliente(cliente)
        elif opcion == "5":
            controlador_borrar_cliente(cliente)
            salir = True
        elif opcion == "6":
            print("Saliendo del programa.")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_modificar_cliente(cliente):
    salir = False
    while salir == False:
        opcion = imprimir_menu_modificar_cliente()
        if opcion == "1":
            controlador_modificar_numero_tarjeta_cliente(cliente)
        elif opcion == "2":
            controlador_modificar_numero_telefono_cliente(cliente)
        elif opcion == "3":
            controlador_modificar_contraseña_cliente(cliente)
        elif opcion == "4":
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_cesta_compra(cesta_compra,cliente):
    bucle = True
    while bucle:
        mostrar_cesta_compra(cesta_compra)
        opcion = imprimir_opciones_gestion_cesta()
        if opcion == "1":
            eliminar_producto_cesta(cesta_compra)
        elif opcion == "2":
            controlador_modificar_cantidad_producto(cesta_compra)
        elif opcion == "3":
            comprar_productos_cesta(cesta_compra, cliente)
        elif opcion == "4":
            bucle = False

#############################
### FUNCIONES DE BORRADO ####
#############################

def borrar_tikets(cliente):
    '''
    @brief: 
    '''

    query = f"SELECT * FROM GENERA_TICKET WHERE id_cliente = {cliente.id_cliente}"
    resultados = conexion.obtener_datos(query)
    if resultados:
        for ticket in resultados:
            ticket = Ticket(
                id_ticket=ticket['id_ticket'],
                id_cliente=ticket['id_cliente'],
                id_producto=ticket['id_producto'],
                fecha=ticket['fecha'],
                cantidad=ticket['cantidad']
            )
            borrar_ticket_bd(ticket)  

def borrar_cliente(cliente):
    '''
    @brief: 
    
    '''
    borrar_tikets(cliente)
    borrar_cliente_bd(cliente)
            
def controlador_borrar_cliente(cliente):
    '''
    @brief: 
    
    '''
    print("¿Está seguro de que desea borrar su cuenta? (S/N)")
    respuesta = input()
    if respuesta.lower() == "s":
        borrar_cliente(cliente)
        print("Cliente borrado correctamente.")
    else:
        print("Operación cancelada.")   
##########################################
### FUNCIONES DE MODIFICACIÓN CLIENTE ####
##########################################

def modificar_numero_tarjeta_cliente(cliente):
    '''
    @brief: 
    
    '''
    query = f"UPDATE CLIENTE SET numero_tarjeta = '{cliente.numero_tarjeta}' WHERE id_cliente = {cliente.id_cliente}"
    conexion.ejecutar_query(query)

def controlador_modificar_numero_tarjeta_cliente(cliente):
    '''
    @brief: 
    '''
    print("Introduce el nuevo número de tarjeta:")
    cliente.numero_tarjeta = input()
    modificar_numero_tarjeta_cliente(cliente)
    print("Número de tarjeta modificado correctamente.")
    

def modificar_numero_telefono_cliente(cliente):
    '''
    @brief: 
    '''
    query = f"UPDATE CLIENTE SET numero_tlfn = '{cliente.numero_tlf}' WHERE id_cliente = {cliente.id_cliente}"
    conexion.ejecutar_query(query)

def controlador_modificar_numero_telefono_cliente(cliente):
    '''
    @brief: 
    '''
    print("Introduce el nuevo número de teléfono:")
    cliente.numero_tlf = input()
    modificar_numero_telefono_cliente(cliente)
    print("Número de teléfono modificado correctamente.")

def modificar_contraseña_cliente(cliente):
    '''
    @brief: 
    '''
    if cliente.contraseña == "":
        return
    else:
        query = f"UPDATE CLIENTE SET contraseña = '{cliente.contraseña}' WHERE id_cliente = {cliente.id_cliente}"
        conexion.ejecutar_query(query)

def controlador_modificar_contraseña_cliente(cliente):
    '''
    @brief: 
    '''
    print("Introduce la nueva contraseña:")
    cliente.contraseña = input()
    modificar_contraseña_cliente(cliente)
    print("Contraseña modificada correctamente.")
    

def comprobar_login(correo,contraseña):
    '''
    @brief: Comprueba si el cliente existe en la base de datos.
    @pre: Se requiere una conexión a la base de datos y un cliente válido.
    @post: Comprueba si el cliente existe en la base de datos.
    @param conexion: La conexión a la base de datos.
    @param correo: El correo electrónico del cliente que se va a comprobar.
    @param contraseña: La contraseña del cliente que se va a comprobar.
    @return: El cliente que ha iniciado sesión o False si no se encuentra.
    
    '''

    query = f"SELECT * FROM CLIENTE WHERE email = '{correo}' AND contraseña = '{contraseña}'"
    resultados = conexion.obtener_datos(query)
    if resultados:
        cliente = Cliente(
                id_cliente=resultados[0]['id_cliente'],
                nombre=resultados[0]['nombre'],
                apellido1=resultados[0]['apellido1'],
                apellido2=resultados[0]['apellido2'],
                DNI=resultados[0]['DNI'],
                numero_tarjeta=resultados[0]['numero_tarjeta'],
                numero_tlf=resultados[0]['numero_tlfn'],
                correo=resultados[0]['email'],
                fecha_nacimiento=resultados[0]['fecha_nacimiento'],
                contraseña=resultados[0]['contraseña']
            )
        return cliente
    else:
        return False
def login():
    '''
    @brief: Inicia sesión de un cliente en la base de datos.
    @pre: Se requiere una conexión a la base de datos y un cliente válido.
    @post: Inicia sesión del cliente en la base de datos.
    @param conexion: La conexión a la base de datos.
    @return: El cliente que ha iniciado sesión o None si no se encuentra.
    
    '''
    cliente = None
    login = False
    while login == False:
        correo = input("Ingrese su correo electrónico:\n ")
        contrasena = input("Ingrese su contraseña:\n ")
        cliente = comprobar_login(correo, contrasena)
        if cliente == False:
            print("Correo electrónico o contraseña incorrectos.")
        else:
            print(f"Bienvenido {cliente.nombre} {cliente.apellido1}.")
            login = True
    return cliente

def registro():
    '''
    @brief: Registra un nuevo cliente en la base de datos.
    @pre: Se requiere una conexión a la base de datos y un cliente válido.
    @post: Registra el cliente en la base de datos.
    @param conexion: La conexión a la base de datos.
    @return: El cliente registrado.
    
    '''

    bucle_preguntas = True
    print("Registro de nuevo cliente. Si desea dejar alguna opción en blanco, simplemente presione Enter.")
    ###### Nombre ######
    while bucle_preguntas:
        nombre = input("Ingrese su nombre:\n")
        if nombre != "":
            bucle_preguntas = False
        else:
            print("El nombre no puede estar vacío.")
    bucle_preguntas = True
    ###### Apellido1 ######
    while bucle_preguntas:
        apellido1 = input("Ingrese su primer apellido:\n")
        if apellido1 != "":
            bucle_preguntas = False
        else:
            print("El primer apellido no puede estar vacío.")
    ##### Apellido2 ######
    apellido2 = input("Ingrese su segundo apellido:\n")
    if apellido2 == "":
        apellido2 = None
    ##### DNI ######
    bucle_preguntas = True 
    while bucle_preguntas:
        dni = input("Ingrese su DNI:\n")
        if dni != "":
            if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
                query = f"SELECT * FROM CLIENTE WHERE DNI = '{dni}'"
                resultados = conexion.obtener_datos(query)
                if resultados:
                    print("El DNI ya está registrado.")
                else:
                    bucle_preguntas = False
            else:
                print("El DNI no es válido. Debe tener 8 dígitos y una letra al final.")
        else:
            print("El DNI no puede estar vacío.")
    ##### Número de tarjeta ######  
    numero_tarjeta = input("Ingrese su número de tarjeta:\n")
    if numero_tarjeta == "":
        numero_tarjeta = None
    ##### Número de teléfono ######
    bucle_preguntas = True
    while bucle_preguntas:
        numero_tlf = input("Ingrese su número de teléfono:\n")
        if numero_tlf != "":
            bucle_preguntas = None
        elif len(numero_tlf) != 9 & numero_tlf.isdigit():
            print("El número de teléfono no es válido.")
        else:
            bucle_preguntas = False
    ##### Correo electrónico ######
    bucle_preguntas = True
    while bucle_preguntas:
        correo = input("Ingrese su correo electrónico:\n")
        if correo != "":
            query = f"SELECT * FROM CLIENTE WHERE email = '{correo}'"
            resultados = conexion.obtener_datos(query)
            if resultados:
                print("El correo electrónico ya está registrado.")
            else:
               bucle_preguntas = False
        else:
            print("El correo electrónico no puede estar vacío.")
    ##### Contraseña #####
    bucle_preguntas = True 
    while bucle_preguntas:
        contraseña = input("Ingrese su contraseña:\n")
        if contraseña != "":
            if len(contraseña) >= 4:
                bucle_preguntas = False
            else:
                print("La contraseña debe tener al menos 4 caracteres.")
        else:
            print("La contraseña no puede estar vacía.")
    ####fecha de nacimiento#####
    bucle_preguntas = True
    while bucle_preguntas:
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD):\n")
        if fecha_nacimiento == "":
            print("La fecha de nacimiento no puede estar vacía.")
        else:
            try:
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
                bucle_preguntas = False
            except ValueError:
                print("La fecha de nacimiento no es válida. Debe estar en el formato YYYY-MM-DD.")
    id_cliente = None
    nuevo_cliente = Cliente(id_cliente, nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento, contraseña)
    insertar_cliente_bd(nuevo_cliente)  # Llamar a la función para insertar en la base de datos


####################
### Cesta_Compra ###
####################

def obtener_productos_paginados(pagina):
    """
    Obtiene productos de la base de datos según la página solicitada y los convierte en objetos Producto.

    @param pagina (int): Número de la página (comenzando desde 1).

    @return list: Lista de objetos Producto de la página solicitada.
    """
    productos_por_pagina = 7
    offset = (pagina - 1) * productos_por_pagina  # Calcular el desplazamiento
    query = f"SELECT * FROM PRODUCTO LIMIT {productos_por_pagina} OFFSET {offset}"
    resultados = conexion.obtener_datos(query)

    # Convertir los resultados en objetos Producto
    productos = []
    if resultados:
        for producto in resultados:
            producto_objeto = Producto(
                id_producto=producto['id_producto'],
                nombre_producto=producto['nombre_producto'],
                descripcion=producto['descripcion'],
                precio=producto['precio'],
                fabricante=producto['fabricante'],
                tipo=producto['tipo']
            )
            productos.append(producto_objeto)
    return productos

def mostrar_cesta_compra(cesta_compra):
    """
    @brief: Muestra la cesta de compra del cliente.
    @param cesta_compra(E): La cesta de compra del cliente.
    @post: Imprime la cesta de compra del cliente.
    """
    if len(cesta_compra[0]) == 0:
        print("La cesta de compra está vacía.")
    else:
        print("Cesta de compra:")
        for i in range(len(cesta_compra[0])):
            print(f"{i+1}.- Producto: {cesta_compra[0][i].nombre_producto}, Cantidad: {cesta_compra[1][i]}, Precio: {cesta_compra[0][i].precio}, Precio Total: {float(cesta_compra[0][i].precio) * int(cesta_compra[1][i])}")

def pedir_usuario_posicion_producto(cesta_compra):
    """
    @brief Pide al usuario la posición del producto en la cesta de compra y valida la entrada.
    @param cesta_compra(E): La cesta de compra del cliente.
    @post: Devuelve una posición válida de un producto en la cesta de compra.
    @return posicion_producto: La posición del producto en la cesta de compra.
    @pre: La posición del producto debe ser un número entero entre 1 y el tamaño de la cesta de compra.
    """
    
    tamaño_cesta = len(cesta_compra[0])
    posicion_producto = 0
    while posicion_producto < 1 or posicion_producto > tamaño_cesta:
        posicion_producto = int(input("Ingrese la posición del producto cuya cantidad desea modificar:\n"))
        if posicion_producto < 1 or posicion_producto > tamaño_cesta:
            print("Posición no válida. Intente de nuevo.")
    return posicion_producto

def imprimir_productos():
    '''
    @brief: Imprime los productos disponibles en la base de datos.
    @pre: Se requiere una conexión a la base de datos.
    @post: Imprime los productos disponibles en la base de datos.
    @param conexion: La conexión a la base de datos.
    @return: None
    
    '''

    query = "SELECT * FROM PRODUCTO"
    resultados = conexion.obtener_datos(query)
    if resultados:
        print("Productos disponibles:")
        for producto in resultados:
            print(f"ID: {producto['id_producto']}, Nombre: {producto['nombre_producto']}, Precio: {producto['precio']}")
    else:
        print("No se encontraron productos.")

def obtener_tickets_cliente(cliente):
    """
    Obtiene los tickets de un cliente desde la base de datos.
    @param cliente: El cliente cuyos tickets se van a obtener.
    @return: Una lista de tickets o None si no se encuentran.
    """
    query = f"""
    SELECT 
        PRODUCTO.nombre_producto,
        PRODUCTO.precio,
        GENERA_TICKET.cantidad,
        GENERA_TICKET.fecha
    FROM 
        GENERA_TICKET
    JOIN 
        CLIENTE ON GENERA_TICKET.id_cliente = CLIENTE.id_cliente
    JOIN 
        PRODUCTO ON GENERA_TICKET.id_producto = PRODUCTO.id_producto
    WHERE 
        CLIENTE.id_cliente = {cliente.id_cliente};
    """
    resultados = conexion.obtener_datos(query)
    return resultados


def mostrar_tickets_cliente(cliente):
    """
    Muestra los tickets de un cliente en la interfaz.
    @param cliente: El cliente cuyos tickets se van a mostrar.
    """
    resultados = obtener_tickets_cliente(cliente)
    if resultados:
        print("Tickets del cliente:")
        for ticket in resultados:
            precio_total = ticket['cantidad'] * ticket['precio']
            print(f"Producto: {ticket['nombre_producto']}, Precio: {ticket['precio']}, Cantidad: {ticket['cantidad']}, Precio Total: {precio_total}, Fecha: {ticket['fecha']}")
    else:
        print("No se encontraron tickets para este cliente.")

def buscar_producto_por_id(id_producto):
    '''
    @brief: Busca un producto por su ID en la base de datos.
    @pre: Se requiere una conexión a la base de datos y un ID de producto válido.
    @post: Busca el producto en la base de datos.
    @param conexion: La conexión a la base de datos.
    @param id_producto: El ID del producto que se va a buscar.
    @return: El producto encontrado o False si no se encuentra.
    
    '''

    query = f"SELECT * FROM PRODUCTO WHERE id_producto = {id_producto}"
    resultados = conexion.obtener_datos(query)
    if not resultados:
        return False
    else:
        producto = Producto(
            id_producto=resultados[0]['id_producto'],
            nombre_producto=resultados[0]['nombre_producto'],
            descripcion=resultados[0]['descripcion'],
            precio=resultados[0]['precio'],
            fabricante=resultados[0]['fabricante'],
            tipo=resultados[0]['tipo']
        )
        return producto

def añadir_producto_cesta(cesta_compra):
    """
    @brief: Añade un producto a la cesta de compra del cliente.
    @param cesta_compra(E/S): La cesta de compra del cliente.
    @post: Añade el producto a la cesta de compra del cliente con una cantidad asignada.
    """
    no_existe_producto = True
    cantidad = "0"
    imprimir_productos()

    while no_existe_producto:
        id_producto = input("Ingrese el ID del producto que desea añadir a la cesta:\n")
        producto = buscar_producto_por_id(id_producto)
        if producto == False:
            print("No existe un producto con ese ID.")
            no_existe_producto == True
        else:
            no_existe_producto = False
            while cantidad.isdigit() == False or int(cantidad) <= 0:
                if cantidad.isdigit() == False or int(cantidad) <= 0:
                    print("La cantidad debe ser un número entero positivo.")
                cantidad = input("Ingrese la cantidad que desea comprar:\n")
                insertar_producto_cesta(cesta_compra, producto, cantidad)
    return cesta_compra

def insertar_producto_cesta(cesta_compra, producto, cantidad):
    """
    @brief: Inserta un producto en la cesta de compra del cliente.
    @param cesta_compra(E/S): La cesta de compra del cliente.
    @param producto(E): El producto que se va a insertar en la cesta de compra.
    @param cantidad(E): La cantidad del producto que se va a insertar en la cesta de compra.
    @post: Inserta el producto en la cesta de compra del cliente con una cantidad asignada.
    """
    cesta_compra[0].append(producto)
    cesta_compra[1].append(cantidad)


def comprar_productos_cesta(cesta_compra, cliente):
    """
    @brief: Realiza la compra de los productos en la cesta de compra, (realiza la creación de los tickets).
    @param cesta_compra(E): La cesta de compra del cliente.
    @param cliente(E): El cliente que realiza la compra.
    @post: Los productos de la cesta de compra se compran y se insertan en la base de datos.
    @post: Se crea un ticket por cada producto comprado.
    """
    crear_ticket(cesta_compra, cliente)
    cesta_compra[0].clear()
    cesta_compra[1].clear()

def crear_ticket(cesta_compra, cliente):
    fecha = datetime.now()
    fecha = fecha.strftime("%Y-%m-%d")
    for i in range(len(cesta_compra[0])):
        ticket = Ticket(
            id_ticket=None,
            id_cliente=cliente.id_cliente,
            id_producto=cesta_compra[0][i].id_producto,
            fecha=fecha,
            cantidad=cesta_compra[1][i]
         )
        insertar_ticket_bd(ticket)


def modificar_cantidad_producto(cesta_compra, posicion_producto, cantidad):
    """
    @brief: Modifica la cantidad de un producto en la cesta de compra.
    @param cesta_compra(E/S): La cesta de compra del cliente.
    @param posicion_producto(E): La posición del producto en la cesta de compra.
    @param cantidad(E): La nueva cantidad del producto.
    @post: La cantidad del producto en la cesta de compra será igual a la cantidad.
    """
    posicion_producto = posicion_producto - 1
    if int(cantidad) <= 0:
        del cesta_compra[0][posicion_producto]
        del cesta_compra[1][posicion_producto]
    else:
        cesta_compra[1][posicion_producto] = cantidad

def controlador_modificar_cantidad_producto(cesta_compra):
    """
    @brief: Controla la modificación de la cantidad de un producto en la cesta de compra.
    @param cesta_compra(E/S): La cesta de compra del cliente.
    @post: Modifica la cantidad del producto en la cesta de compra.
    """
    if len(cesta_compra[0]) == 0:
        print("No hay productos en la cesta.")
    else:
        posicion_producto = pedir_usuario_posicion_producto(cesta_compra)
        cantidad = input("Ingrese la nueva cantidad:\n")
        modificar_cantidad_producto(cesta_compra,posicion_producto,cantidad)

def eliminar_producto_cesta(cesta_compra):
    """
    @brief: Elimina un producto de la cesta de compra.
    @param cesta_compra(E/S): La cesta de compra del cliente.
    @post: Elimina el producto de la cesta de compra.
    """
    if len(cesta_compra[0]) == 0:
        print("No hay productos en la cesta.")
    else:
        posicion_producto = pedir_usuario_posicion_producto(cesta_compra)
        modificar_cantidad_producto(cesta_compra,posicion_producto,0)

def comprobar_producto_en_carrito(carrito,producto):
    """
    Comprueba si un producto ya está en el carrito.

    Args:
        producto (Producto): El producto a comprobar.
        carrito (list): La lista del carrito de compras.

    Returns:
        bool: True si el producto está en el carrito, False en caso contrario.
    """
    hay_producto = False
    for i in range(len(carrito[0])):
        if carrito[0][i].id_producto == producto.id_producto:
            hay_producto = True
    return hay_producto
  
####### BD ########

def insertar_cliente_bd(cliente):
    query = f"INSERT INTO CLIENTE (nombre, apellido1, apellido2, DNI, numero_tarjeta, numero_tlfn, email, fecha_nacimiento, contraseña) VALUES ( '{cliente.nombre}', '{cliente.apellido1}', '{cliente.apellido2}', '{cliente.DNI}', '{cliente.numero_tarjeta}', '{cliente.numero_tlf}', '{cliente.correo}', '{cliente.fecha_nacimiento}', '{cliente.contraseña}')"
    conexion.ejecutar_query(query)

def borrar_cliente_bd(cliente):
    query = f"DELETE FROM CLIENTE WHERE id_cliente = {cliente.id_cliente}"
    conexion.ejecutar_query(query)

def insertar_producto_bd(producto):
    query = f"INSERT INTO PRODUCTO (nombre_producto, descripcion, precio, fabricante, tipo) VALUES ('{producto.nombre_producto}', '{producto.descripcion}', {producto.precio}, '{producto.fabricante}', '{producto.tipo}')"
    conexion.ejecutar_query(query)

def borrar_producto_bd(producto):
    query = f"DELETE FROM PRODUCTO WHERE id_producto = {producto.id_producto}"
    conexion.ejecutar_query(query)

def insertar_ticket_bd(ticket):
    query = f"INSERT INTO GENERA_TICKET (id_cliente, id_producto, fecha, cantidad) VALUES ({ticket.id_cliente}, {ticket.id_producto}, '{ticket.fecha}', {ticket.cantidad})"
    conexion.ejecutar_query(query)

def borrar_ticket_bd(ticket):
    query = f"DELETE FROM GENERA_TICKET WHERE id_ticket = {ticket.id_ticket}"
    conexion.ejecutar_query(query)
