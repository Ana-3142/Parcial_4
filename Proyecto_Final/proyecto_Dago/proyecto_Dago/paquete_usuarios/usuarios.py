from data_base.conexion import conectar
import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email)

def crear_usuario():
    nombre = input("Nombre: ")
    matricula = input("Matrícula: ")
    email = input("Email: ")
    if not validar_email(email):
        print("Email no válido")
        return
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios (nombre, matricula, email) VALUES (%s,%s,%s)", (nombre, matricula, email))
    con.commit()
    print("Usuario creado")
    con.close()

def listar_usuarios():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()

    ANCHO_TABLA = 65
    print("┌" + "─" * ANCHO_TABLA + "┐")
    print(f"│ {'ID':<4} │ {'Nombre':<20} │ {'Matrícula':<12} │ {'Email':<20} │")
    print("├" + "─" * ANCHO_TABLA + "┤")
    
    for u in usuarios:
        id_u = str(u['id'])
        nombre = str(u['nombre'])
        matricula = str(u['matricula'])
        email = str(u['email'])
        print(f"│ {id_u:<4} │ {nombre:<20} │ {matricula:<12} │ {email:<20} │")
        
    print("└" + "─" * ANCHO_TABLA + "┘")

def actualizar_usuario():
    id_u = input("ID a actualizar: ")
    nuevo_email = input("Nuevo email: ")
    con = conectar()
    cur = con.cursor()
    cur.execute("UPDATE usuarios SET email=%s WHERE id=%s", (nuevo_email, id_u))
    con.commit()
    print("Actualizado")
    con.close()

def eliminar_usuario():
    id_u = input("ID a eliminar: ")
    con = conectar()
    if not con:
        return
    
    cur = con.cursor()
    
    cur.execute("SELECT id FROM usuarios WHERE id=%s", (id_u,))
    if not cur.fetchone():
        print(f"No existe ningún usuario con el ID {id_u}")
        con.close()
        return

    cur.execute("DELETE FROM intentos WHERE usuario_id=%s", (id_u,))
    cur.execute("DELETE FROM usuarios WHERE id=%s", (id_u,))
    
    con.commit()
    print("Usuario y sus registros asociados fueron eliminados correctamente.")
    con.close()