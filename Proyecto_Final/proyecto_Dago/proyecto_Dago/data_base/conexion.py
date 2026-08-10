import mysql.connector
def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # pon tu pass de MySQL
            database="calculo_db"
        )
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None