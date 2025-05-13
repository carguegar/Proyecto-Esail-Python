class Cliente():
    def __init__(self, id_cliente, nombre, apellido1, apellido2, DNI, numero_tarjeta, numero_tlf, correo, fecha_nacimiento,contraseña):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__DNI = DNI
        self.__numero_tarjeta = numero_tarjeta
        self.__numero_tlf = numero_tlf
        self.__correo = correo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__contraseña = contraseña
        
    def __str__(self):
        return f"Datos del cliente:\nID: {self.id_cliente}\nNombre: {self.nombre}\nApellido1: {self.apellido1}\nApellido2: {self.apellido2}\nDNI: {self.DNI}\nNumero de tarjeta: {self.numero_tarjeta}\nNumero de telefono: {self.numero_tlf}\nCorreo: {self.correo}\nFecha de nacimiento: {self.fecha_nacimiento}\n"
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido1(self):
        return self.__apellido1
    @property
    def apellido2(self):
        return self.__apellido2
    @property
    def DNI(self):
        return self.__DNI
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    @property
    def numero_tlf(self):
        return self.__numero_tlf
    @property
    def correo(self):
        return self.__correo
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    @property
    def id_cliente(self):
        return self.__id_cliente
    @property
    def contraseña(self):
        return self.__contraseña
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @apellido1.setter
    def apellido1(self, apellido1):
        self.__apellido1 = apellido1
    @apellido2.setter
    def apellido2(self, apellido2):
        self.__apellido2 = apellido2
    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI
    @numero_tarjeta.setter
    def numero_tarjeta(self, numero_tarjeta):
        self.__numero_tarjeta = numero_tarjeta
    @numero_tlf.setter
    def numero_tlf(self, numero_tlf):
        self.__numero_tlf = numero_tlf
    @correo.setter
    def correo(self, correo):
        self.__correo = correo
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    @contraseña.setter
    def contraseña(self, contraseña):
        self.__contraseña = contraseña
    def comprobar_login(self, correo, contrasena):
        if self.correo == correo and self.__contraseña == contrasena:
            return True
        else:
            return False
    

class Producto():
    def __init__(self, id_producto, nombre_producto, descripcion, precio, fabricante, tipo):
        self.__id_producto = id_producto
        self.__nombre_producto = nombre_producto
        self.__descripcion = descripcion
        self.__precio = precio
        self.__fabricante = fabricante
        self.__tipo = tipo
    def __str__(self):
        return f"Datos del producto:\nID: {self.id_producto}\nNombre: {self.nombre_producto}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nFabricante: {self.fabricante}\nTipo: {self.tipo}\n"
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.id_producto == other.id_producto
        return False
    @property
    def id_producto(self):
        return self.__id_producto
    @property
    def nombre_producto(self):
        return self.__nombre_producto
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def precio(self):
        return self.__precio
    @property
    def fabricante(self):
        return self.__fabricante
    @property
    def tipo(self):
        return self.__tipo
    @id_producto.setter
    def id_producto(self, id_producto):
        self.__id_producto = id_producto
    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    @fabricante.setter 
    def fabricante(self, fabricante):
        self.__fabricante = fabricante
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

class Ticket(Producto, Cliente):
    def __init__(self, id_ticket, id_cliente, id_producto, fecha, cantidad):
        self.__id_ticket = id_ticket
        self.__id_cliente = id_cliente
        self.__id_producto = id_producto
        self.__fecha = fecha
        self.__cantidad = cantidad
        
    def __str__(self):
        return f"Datos del ticket:\nID: {self.id_ticket}\nID Cliente: {self.id_cliente}\nID Producto: {self.id_producto}\nFecha de compra: {self.fecha}\nCantidad: {self.cantidad}\n"
    
    @property
    def id_ticket(self):
        return self.__id_ticket
    @property
    def id_cliente(self):
        return self.__id_cliente
    @property
    def id_producto(self):
        return self.__id_producto
    @property
    def fecha(self):
        return self.__fecha
    @property
    def cantidad(self):
        return self.__cantidad
    @id_ticket.setter
    def id_ticket(self, id_ticket):
        self.__id_ticket = id_ticket
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    @id_producto.setter
    def id_producto(self, id_producto):
        self.__id_producto = id_producto
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
    