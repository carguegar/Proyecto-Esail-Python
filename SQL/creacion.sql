CREATE SCHEMA IF NOT EXISTS tienda
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
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
    DNI VARCHAR(20) NOT NULL UNIQUE CHECK (DNI REGEXP '^[0-9]{8}[A-Z]$'),
    numero_tarjeta VARCHAR(20) CHECK (numero_tarjeta REGEXP '^[0-9]{16}$'),
    numero_tlfn VARCHAR(15) CHECK (numero_tlfn REGEXP '^[0-9]{9}$'),
    email VARCHAR(100) NOT NULL UNIQUE CHECK (email REGEXP '^[^@]+@[^@]+\.[a-zA-Z]{2,}$'),
    fecha_nacimiento DATE NOT NULL,
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
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);