from clases import Cliente, Producto, Ticket
from SQL.base_datos import *
from SQL.base_datos import conexion
from datetime import datetime

def main():
    cliente = None
    cliente = menu_principal()
    menu_cliente(cliente)
#FRONTEND
# MENÚS
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
    print("2. Comprar productos de la cesta")
    print("3. Ver tickets")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_principal():
     cliente = None
     error = True
     while error:
        opcion =imprimir_opciones_menu_principal()
        if opcion == "1":
            error = False
            cliente = login()
        elif opcion == "2":
            cliente = registro()
        else:
            print("Opción no válida. Intente de nuevo.")
        return cliente

def menu_cliente(cliente):
    salir = False
    cesta_compra = [[], []] 
    while salir == False:
        opcion = imprimir_opciones_menu_cliente()
        if opcion == "1":
            error = False
            añadir_producto_cesta(cesta_compra)
        elif opcion == "2":
            error = False
            comprar_productos_cesta(cesta_compra, cliente)
        elif opcion == "3":
            error = False
            ver_tickets(cliente)
        elif opcion == "4":
            print("Saliendo del programa.")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

def login():
    login = False
    while login == False:
        correo = input("Ingrese su correo electrónico:\n ")
        contrasena = input("Ingrese su contraseña:\n ")
        query = f"SELECT * FROM CLIENTE WHERE email = '{correo}' AND contraseña = '{contrasena}'"
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
            print(f"Bienvenido {cliente.nombre} {cliente.apellido1}.")
            login = True
        else:
            print("Correo electrónico o contraseña incorrectos.")
    return cliente
            
def registro(lista_clientes):
    bucle_preguntas = True
    print("Registro de nuevo cliente. Si desea dejar alguna opción en blanco, simplemente presione Enter.")
    while bucle_preguntas:
        nombre = input("Ingrese su nombre:\n")
        if nombre != "":
            bucle_preguntas = False
        else:
            print("El nombre no puede estar vacío.")
    bucle_preguntas = True
    while bucle_preguntas:
        apellido1 = input("Ingrese su primer apellido:\n")
        if apellido1 != "":
            bucle_preguntas = False
        else:
            print("El primer apellido no puede estar vacío.")
    apellido2 = input("Ingrese su segundo apellido:\n")
    if apellido2 == "":
        apellido2 = None
    bucle_preguntas = True 
    while bucle_preguntas:
        dni = input("Ingrese su DNI:\n")
        if dni != "":
            bucle_preguntas = False
        else:
            print("El DNI no puede estar vacío.")  
    numero_tarjeta = input("Ingrese su número de tarjeta:\n")
    if numero_tarjeta == "":
        numero_tarjeta = None
    bucle_preguntas = True
    while bucle_preguntas:
        numero_tlf = input("Ingrese su número de teléfono:\n")
        if numero_tlf != "":
            bucle_preguntas = None
        elif len(numero_tlf) != 9 & numero_tlf.isdigit():
            print("El número de teléfono no es válido.")
        else:
            bucle_preguntas = False
    bucle_preguntas = True
    while bucle_preguntas:
        correo = input("Ingrese su correo electrónico:\n")
        if correo != "":
            bucle_preguntas = False
        else:
            print("El correo electrónico no puede estar vacío.")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD):\n")
    if fecha_nacimiento == "":
        fecha_nacimiento = None
    id_cliente = None
    nuevo_cliente = Cliente(id_cliente, nombre, apellido1, apellido2, dni, numero_tarjeta, numero_tlf, correo, fecha_nacimiento)
    insertar_cliente_bd(nuevo_cliente)  # Llamar a la función para insertar en la base de datos
#BACKEND
##################
#### TICKETS #####
##################

####################
#### PRODUCTOS #####
####################

###################
#### CLIENTES #####
###################
def ver_tickets(cliente):
    query = f"""SELECT 
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
    if resultados:
        print("Tickets del cliente:")
        for ticket in resultados:
            precio_total = ticket['cantidad'] * ticket['precio']
            print(f"Producto: {ticket['nombre_producto']}, Precio: {ticket['precio']}, Cantidad: {ticket['cantidad']}, Precio Total: {precio_total}, Fecha: {ticket['fecha']}")
    else:
        print("No se encontraron tickets para este cliente.")

def imprimir_productos():
    query = "SELECT * FROM PRODUCTO"
    resultados = conexion.obtener_datos(query)
    if resultados:
        print("Productos disponibles:")
        for producto in resultados:
            print(f"ID: {producto['id_producto']}, Nombre: {producto['nombre_producto']}, Precio: {producto['precio']}")
    else:
        print("No se encontraron productos.")

def buscar_producto_por_id(id_producto):
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
            cesta_compra[0].append(producto)
            while cantidad.isdigit() == False or int(cantidad) <= 0:
                if cantidad.isdigit() == False or int(cantidad) <= 0:
                    print("La cantidad debe ser un número entero positivo.")
                cantidad = input("Ingrese la cantidad que desea comprar:\n")
                cesta_compra[1].append(int(cantidad))
    return cesta_compra


def comprar_productos_cesta(cesta_compra, cliente):
    error_cesta_vacia = False
    if len(cesta_compra[0]) == 0:
        print("No hay productos en la cesta.")
        error_cesta_vacia = True
    else:
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
        print("Productos comprados correctamente.")
        cesta_compra[0].clear()
        cesta_compra[1].clear()

def insertar_cliente_bd(cliente):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO CLIENTE (nombre, apellido1, apellido2, DNI, numero_tarjeta, numero_tlfn, email, fecha_nacimiento, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
            values = (
                cliente.nombre,
                cliente.apellido1,
                cliente.apellido2,
                cliente.DNI,
                cliente.numero_tarjeta,
                cliente.numero_tlf,
                cliente.correo,
                cliente.fecha_nacimiento,
                cliente._Cliente__contraseña  # Acceso al atributo privado
            )

            cursor.execute(query, values)
            conn.commit()
            print("Cliente insertado correctamente.")
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            cursor.close()
            conn.close()

def borrar_cliente_bd(cliente):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM CLIENTE WHERE id_cliente = %s"
    
            values = (cliente.id_cliente,)

            cursor.execute(query, values)
            conn.commit()
            print("Cliente borrado correctamente.")
        except Exception as e:
            print(f"Error al borrar cliente: {e}")
        finally:
            cursor.close()
            conn.close()

def insertar_producto_bd(producto):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO PRODUCTO (nombre_producto, descripcion, precio, fabricante, tipo) VALUES (%s, %s, %s, %s, %s)"
    
            values = (
                producto.nombre_producto,
                producto.descripcion,
                producto.precio,
                producto.fabricante,
                producto.tipo
            )

            cursor.execute(query, values)
            conn.commit()
            print("Producto insertado correctamente.")
        except Exception as e:
            print(f"Error al insertar producto: {e}")
        finally:
            cursor.close()
            conn.close()

def borrar_producto_bd(producto):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM PRODUCTO WHERE id_producto = %s"
    
            values = (producto.id_producto,)

            cursor.execute(query, values)
            conn.commit()
            print("Producto borrado correctamente.")
        except Exception as e:
            print(f"Error al borrar producto: {e}")
        finally:
            cursor.close()
            conn.close()            

def insertar_ticket_bd(ticket):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO GENERA_TICKET (id_cliente, id_producto, fecha, cantidad) VALUES (%s, %s, %s, %s)"
    
            values = (
                ticket.id_cliente,
                ticket.id_producto,
                ticket.fecha,
                ticket.cantidad
            )

            cursor.execute(query, values)
            conn.commit()
            print("Ticket insertado correctamente.")
        except Exception as e:
            print(f"Error al insertar ticket: {e}")
        finally:
            cursor.close()
            conn.close()

def borrar_ticket_bd(ticket):
    conn = conexion.ConexionBasedeDatos()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM GENERA_TICKET WHERE id_ticket = %s"
    
            values = (ticket.id_ticket,)

            cursor.execute(query, values)
            conn.commit()
            print("Ticket borrado correctamente.")
        except Exception as e:
            print(f"Error al borrar ticket: {e}")
        finally:
            cursor.close()
            conn.close()

main()