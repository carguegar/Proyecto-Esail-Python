class Cliente():
    def __init__(self, id_cliente:str, nombre:str, apellido1:str, apellido2:str, DNI:str, numero_tarjeta:str, numero_tlf:str, correo:str, fecha_nacimiento):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.DNI = DNI
        self.numero_tarjeta = numero_tarjeta
        self.numero_tlf = numero_tlf
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        
    def __str__(self):
        return f"Datos del cliente:\nID: {self.id_cliente}\nNombre: {self.nombre}\nApellido1: {self.apellido1}\nApellido2: {self.apellido2}\nDNI: {self.DNI}\nNumero de tarjeta: {self.numero_tarjeta}\nNumero de telefono: {self.numero_tlf}\nCorreo: {self.correo}\nFecha de nacimiento: {self.fecha_nacimiento}\n"
    
a = Cliente("1", "Juan", "Pérez", "Gómez", "12345678A", "1234-5678-9012-3456", "612345678", "ejemplo@mail.com", "1990-01-01")
print(a)