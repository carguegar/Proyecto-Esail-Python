import mysql.connector

class conexion:
    
    @staticmethod
    def ConexionBasedeDatos():
        """
        Establece la conexión a la base de datos MySQL y devuelve el objeto de conexión.
        """
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
        """
        Ejecuta una consulta SQL y devuelve los resultados.
        """
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
    
    @staticmethod 
    def ejecutar_query(query):
        """
        Ejecuta una consulta SQL que no devuelve resultados (INSERT, UPDATE, DELETE).
        """
        try:
            conexion_db = conexion.ConexionBasedeDatos()
            if conexion_db:
                cursor = conexion_db.cursor()
                cursor.execute(query)
                conexion_db.commit()
                cursor.close()
                conexion_db.close()
        except mysql.connector.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None


        

