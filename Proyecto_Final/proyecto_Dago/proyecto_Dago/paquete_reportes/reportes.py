from data_base.conexion import conectar

def generar_reporte_txt():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT u.nombre, e.funcion, e.tipo, i.respuesta_usuario, i.es_correcto, i.fecha FROM intentos i JOIN usuarios u ON i.usuario_id=u.id JOIN ejercicios e ON i.ejercicio_id=e.id")
    datos = cur.fetchall()
    
    with open("reporte_alumno.txt", "w") as f:
        f.write("REPORTE DE AVANCE - ANALISIS MARGINAL\n")
        f.write("="*40+"\n")
        for d in datos:
            estado = "OK" if d['es_correcto'] else "FAIL"
            f.write(f"{d['fecha']} | {d['nombre']} | {d['tipo']} | {d['funcion']} | Resp: {d['respuesta_usuario']} | {estado}\n")
    print("Reporte generado: reporte_alumno.txt")
    con.close()