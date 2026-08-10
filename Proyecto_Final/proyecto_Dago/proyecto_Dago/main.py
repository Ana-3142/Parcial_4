print ('\033c')
import os
from paquete_usuarios.usuarios import *
from paquete_ejercicios.ejercicios import *
from paquete_reportes.reportes import *

ROJO = "\033[91m"
RESET = "\033[0m"

def imprimir_error(mensaje):
    print(f"{ROJO}❌ Error: {mensaje}{RESET}")

def imprimir_centrado(texto, ancho=55):
    print(texto.center(ancho))

def menu():
    ANCHO_MENU = 55
    ejecutando = True
    
    while ejecutando:

        print('\033c', end='')
        
        imprimir_centrado("=" * ANCHO_MENU)
        imprimir_centrado("...::::📐  SISTEMA CÁLCULO DIFERENCIAL  📐::::...")
        imprimir_centrado("=" * ANCHO_MENU)
        print()
        imprimir_centrado("👤 1. Crear usuario        ")
        imprimir_centrado("📋 2. Listar usuarios       ")
        imprimir_centrado("✏️  3. Actualizar usuario    ")
        imprimir_centrado("🗑️  4. Eliminar usuario      ")
        imprimir_centrado("🧮 5. Resolver ejercicio    ")
        imprimir_centrado("📊 6. Ver estadísticas      ")
        imprimir_centrado("📄 7. Generar reporte (.txt)")
        imprimir_centrado("🚪 0. Salir                 ")
        print()
        imprimir_centrado("-" * ANCHO_MENU)
        
        op = input("\n👉 Selecciona una opción: ").strip()
        
        print('\033c', end='')

        try:
            if op == "1":
                crear_usuario()
            elif op == "2":
                listar_usuarios()
            elif op == "3":
                actualizar_usuario()
            elif op == "4":
                eliminar_usuario()
            elif op == "5":
                uid = input("Tu ID de usuario: ")
                if uid.isdigit():
                    resolver_ejercicio(int(uid))
                else:
                    imprimir_error("El ID debe ser un número entero.")
            elif op == "6":
                ver_estadisticas()
            elif op == "7":
                generar_reporte_txt()
            elif op == "0":
                print("👋 ¡Hasta luego!")
                ejecutando = False
            else:
                imprimir_error("Opción inválida. Elige un número del menú.")
        except Exception as e:
            imprimir_error(e)

        if ejecutando:
            input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    menu()

    
