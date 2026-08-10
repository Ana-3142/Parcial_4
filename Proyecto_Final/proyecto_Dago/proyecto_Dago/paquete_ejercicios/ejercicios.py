from data_base.conexion import conectar
import re

def validar_numero(texto):
    return re.match(r'^-?\d+(\.\d+)?$', texto)

def resolver_ejercicio(usuario_id):
    con = conectar()
    if not con:
        print("❌ No se pudo conectar a la base de datos.")
        return

    cur = con.cursor(dictionary=True)
    
    cur.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
    if not cur.fetchone():
        print(f"\n❌ El usuario con ID {usuario_id} no existe. Por favor crea un usuario primero.")
        con.close()
        return

    cur.execute("SELECT * FROM ejercicios ORDER BY RAND() LIMIT 1")
    ej = cur.fetchone()
    
    if not ej:
        print("❌ No hay ejercicios registrados en la base de datos.")
        con.close()
        return

    print(f"\nEjercicio: {ej['tipo']} | Función: {ej['funcion']} | Evalúa en x={ej['x_eval']}")
    print("Calcula la derivada marginal en ese punto:")
    
    resp = input("Tu respuesta: ")
    if not validar_numero(resp):
        print("Solo números válidos")
        con.close()
        return
    
    resp_float = float(resp)
    es_correcto = abs(resp_float - ej['respuesta_correcta']) < 0.01

    cur.execute(
        "INSERT INTO intentos (usuario_id, ejercicio_id, respuesta_usuario, es_correcto) VALUES (%s,%s,%s,%s)",
        (usuario_id, ej['id'], resp_float, es_correcto)
    )
    con.commit()
    print("¡Correcto!" if es_correcto else f"Incorrecto. Respuesta: {ej['respuesta_correcta']}")
    con.close()

def ver_estadisticas():
    con = conectar()
    if not con:
        print("❌ No se pudo conectar a la base de datos.")
        return

    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT u.nombre, COUNT(i.id) as total, SUM(i.es_correcto) as correctos 
        FROM intentos i 
        JOIN usuarios u ON i.usuario_id=u.id 
        GROUP BY u.nombre
    """)
    
    resultados = cur.fetchall()
    
    if not resultados:
        print("No hay registros de intentos aún.")
    else:
        ANCHO_TABLA = 58

        print("┌" + "─" * ANCHO_TABLA + "┐")
        print(f"│ {'Usuario':<22} │ {'Aciertos':<12} │ {'Promedio':<16} │")
        print("├" + "─" * ANCHO_TABLA + "┤")
        
        for r in resultados:
            nombre = str(r['nombre'])
            total = r['total']
            correctos = int(r['correctos'] or 0)
            promedio = (correctos / total * 100) if total > 0 else 0
            
            aciertos_str = f"{correctos}/{total}"
            promedio_str = f"{promedio:.1f}%"
            
            print(f"│ {nombre:<22} │ {aciertos_str:<12} │ {promedio_str:<16} │")
            
        print("└" + "─" * ANCHO_TABLA + "┘")
            
    con.close()
