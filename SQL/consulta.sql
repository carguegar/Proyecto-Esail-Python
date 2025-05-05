    use tienda;

    SELECT CLIENTE.nombre, CLIENTE.apellido1, CLIENTE.apellido2, genera_ticket.id_ticket, nombre_producto, cantidad 
    FROM genera_ticket
    JOIN CLIENTE ON CLIENTE.id_cliente = genera_ticket.id_cliente
    JOIN PRODUCTO ON PRODUCTO.id_producto = genera_ticket.id_producto;