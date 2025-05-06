import mysql.connector

class conexion:
    
    @staticmethod
    def ConexionBasedeDatos():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='josegras',
                host='localhost',
                database='tienda',
                port='3306'
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    @staticmethod
    def obtener_datos(query):
        try:
            conexion_db = conexion.ConexionBasedeDatos()  # Cambiar el nombre de la variable local
            if conexion_db:
                cursor = conexion_db.cursor(dictionary=True)  # Devuelve los resultados como diccionarios
                cursor.execute(query)
                resultados = cursor.fetchall()
                cursor.close()
                conexion_db.close()
                return resultados
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

