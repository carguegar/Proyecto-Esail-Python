CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

DROP TABLE IF EXISTS genera_ticket;
DROP TABLE IF EXISTS PRODUCTO;
DROP TABLE IF EXISTS CLIENTE;

-- Creación de la tabla CLIENTE
CREATE TABLE CLIENTE (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido1 VARCHAR(50) NOT NULL,
    apellido2 VARCHAR(50),
    DNI VARCHAR(20) NOT NULL UNIQUE,
    numero_tarjeta VARCHAR(20),
    numero_tlfn VARCHAR(15),
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    contraseña VARCHAR(255) NOT NULL
);

-- Creación de la tabla PRODUCTO
CREATE TABLE PRODUCTO (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    fabricante VARCHAR(100),
    tipo VARCHAR(50) NOT NULL
);

-- Creación de la tabla genera_ticket
CREATE TABLE genera_ticket (
    id_ticket INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);
