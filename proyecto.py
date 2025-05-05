from class_cliente import Cliente, Producto, ticket

a = Cliente("1", "Juan", "Pérez", "Gómez", "12345678A", "1234-5678-9012-3456", "612345678", "correo@ejemplo.com", "1990-01-01")
d = Cliente("2", "Ana", "López", "Martínez", "87654321B", "9876-5432-1098-7654", "698765432", "correo2@ejemplo.com", "1995-05-05")
b = Producto("1", "Producto1", "Descripción del producto 1", 10.99, "Fabricante1", "Tipo1")
c = ticket("1", a.id_cliente, b.id_producto, "2023-10-01", 2)


def main():
    lista_clientes = []
    lista_productos = []
    lista_tickets = []
    lista_clientes.append(a)
    lista_clientes.append(d)
    lista_productos.append(b)
    lista_tickets.append(c)
    a.nombre = "Carlos"
    a.apellido1 = "García"
    a.apellido2 = "Fernández"
    print(a.nombre)
    b.nombre_producto = "Producto2"
    print(b.nombre_producto)

main()