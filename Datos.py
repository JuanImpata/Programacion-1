#!/usr/bin/env python3
"""
EJERCICIOS RESUELTOS - ESTRUCTURAS DE CONTROL Y CONDICIONALES
"""
import os
import sys

# ===========================================================================
# UTILIDADES GENERALES
# ===========================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")
    print() # Añade una línea extra para mejor separación

# ===========================================================================
# EJERCICIOS DE ESTRUCTURAS DE CONTROL (BUCLES) - SOLUCIONES ORIGINALES
# (Se mantienen los nombres y el contenido original)
# ===========================================================================

def ejercicio_control_1():
    """
    Problema: Corregir la modificación de una lista mientras se itera.
    """
    print("--- 1. Corregir iteración y modificación de lista ---")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista original: {numeros}")

    # Solución: Usar una comprensión de lista para crear la nueva lista de impares
    impares = [num for num in numeros if num % 2 != 0]
    print(f"Resultado corregido (Solo impares): {impares}")
    print("Corrección: Se evita modificar la lista original usando una comprensión de lista.")

def ejercicio_control_2():
    """
    Problema: Generar una tabla de multiplicar con bucles anidados.
    """
    print("--- 2. Tabla de multiplicar del 1 al 10 ---")
    for i in range(1, 11):
        linea = ""
        for j in range(1, 11):
            producto = i * j
            # Formatear la salida para la tabla
            linea += f"{producto:4}" # :4 asegura 4 espacios para cada número
        print(f"Tabla del {i:2}: {linea}")

def ejercicio_control_3():
    """
    Problema: Corregir un bucle while infinito.
    """
    print("--- 3. Corregir bucle while infinito ---")
    print("Resultado esperado: Números del 1 al 5")

    contador = 1
    while contador <= 5:
        print(f"Número: {contador}")
        # Corrección: Incrementar la variable de control
        contador += 1

    print("Corrección: Se añadió 'contador += 1' para salir del bucle.")

def ejercicio_control_4():
    """
    Problema: Uso de break y continue.
    """
    print("--- 4. Uso de break y continue ---")
    numeros = [5, -2, 10, 8, -3, 0, 7, 9]
    print(f"Lista: {numeros}")

    for num in numeros:
        if num == 0:
            print(f"¡Cero encontrado! Deteniendo el proceso (usando break).")
            break

        if num < 0:
            print(f"Saltando número negativo: {num} (usando continue).")
            continue

        print(f"Procesando número positivo: {num}")

def ejercicio_control_5():
    """
    Problema: Reescribir un bucle tradicional con una comprensión de lista.
    """
    print("--- 5. Convertir bucle a comprensión de lista ---")

    # Versión con bucle tradicional para referencia
    cuadrados_pares_tradicional = []
    for numero in range(1, 11):
        if numero % 2 == 0:
            cuadrados_pares_tradicional.append(numero ** 2)
    print(f"Bucle tradicional: {cuadrados_pares_tradicional}")

    # Solución con comprensión de lista
    cuadrados_pares_comprension = [numero ** 2 for numero in range(1, 11) if numero % 2 == 0]
    print(f"Comprensión de lista: {cuadrados_pares_comprension}")

def ejercicio_control_6():
    """
    Problema: Combinaciones con bucles anidados y comprensión de listas.
    """
    print("--- 6. Combinaciones con bucles anidados y comprensión ---")
    colores = ["rojo", "azul", "verde"]
    tamaños = ["pequeño", "mediano", "grande"]

    # 1. Solución con bucles anidados
    combinaciones_bucle = []
    for color in colores:
        for tamaño in tamaños:
            combinaciones_bucle.append((color, tamaño))
    print(f"1. Bucles anidados: {combinaciones_bucle}")

    # 2. Solución con comprensión de listas
    combinaciones_comprension = [(color, tamaño) for color in colores for tamaño in tamaños]
    print(f"2. Comprensión de listas: {combinaciones_comprension}")

# ===========================================================================
# EJERCICIOS DE ESTRUCTURAS CONDICIONALES - SOLUCIONES MODIFICADAS
# (Se usan nuevos nombres y lógica para evitar la duplicación)
# ===========================================================================

def solucion_condicional_1():
    """
    Solución 7: Evaluar si un número es positivo, negativo o cero.
    """
    print("--- 7. Evaluar Signo Numérico ---")
    try:
        valor = int(input("Introduce un número entero: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if valor > 0:
        print(f"El número {valor} es un valor Positivo.")
    elif valor < 0:
        print(f"El número {valor} es un valor Negativo.")
    else:
        print(f"El número {valor} es exactamente CERO, el neutro aditivo.")

def solucion_condicional_2():
    """
    Solución 8: Corregir errores de sintaxis en condiciones (== y :).
    """
    print("--- 8. Corregir errores de comparación y sintaxis ---")
    try:
        puntuaje = int(input("Introduce tu puntuación de 0 a 10: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if puntuaje == 10: # Se usa el operador de igualdad '=='
        print("¡Puntuación perfecta!")
    elif puntuaje < 5: # Se asegura la presencia de los dos puntos ':'
        print("Necesitas mejorar, puntuación baja.")
    else:
        print("Puntuación satisfactoria.")

def solucion_condicional_3():
    """
    Solución 9: Simplificar condicionales anidados con operadores lógicos.
    (Basado en Soleado/Caluroso)
    """
    print("--- 9. Simplificar condicionales anidados ---")
    soleado = input("¿El clima está soleado? (s/n): ").lower() == "s"
    caluroso = input("¿Hace calor? (s/n): ").lower() == "s"

    if soleado and caluroso:
        print("Lleva gafas de sol y ropa ligera.")
    elif soleado: # Esto implica que NO está caluroso.
        print("Lleva gafas de sol.")
    elif caluroso: # Esto implica que NO está soleado.
        print("Vístete cómodamente (clima cálido pero nublado).")
    else: # Ni soleado ni caluroso
        print("Lleva algo ligero para protegerte del viento.")

def solucion_condicional_4():
    """
    Solución 10: Corregir el orden de las condiciones (utilizando encadenamiento).
    (Basado en rangos de edad)
    """
    print("--- 10. Corregir orden de condiciones ---")
    try:
        edad = int(input("Introduce la edad: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # Solución alternativa: El encadenamiento de comparadores simplifica la lectura de rangos.
    if 0 <= edad <= 5:
        print("Nivel: Preescolar")
    elif 6 <= edad <= 11:
        print("Nivel: Primaria")
    elif 12 <= edad <= 17:
        print("Nivel: Adolescente")
    else: # Cubre 18+ y edades negativas
        print("Nivel: Adulto o edad inválida.")

def solucion_condicional_5():
    """
    Solución 11: Simplificar if-else con el operador ternario.
    (Basado en valor de compra >= 100)
    """
    print("--- 11. Usar operador ternario ---")
    try:
        valor_compra = float(input("Introduce el valor de la compra: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # Sintaxis: [Resultado si Verdadero] if [Condición] else [Resultado si Falso]
    envio_gratis = "¡Envío gratuito aplicado!" if valor_compra >= 100 else "El envío tiene costo adicional."
    print(f"Mensaje de oferta (Ternario): {envio_gratis}")

def solucion_condicional_6():
    """
    Solución 12: Determinar si un año es bisiesto (lógica desglosada).
    """
    print("--- 12. Determinar si un año es bisiesto ---")
    try:
        year = int(input("Introduce un año: "))
    except ValueError:
        print("Entrada inválida.")
        return

    def es_bisiesto_detallado(year):
        # Desglose de las tres reglas en el orden de prioridad:
        if year % 400 == 0:
            return True  # 1. Divisible por 400
        elif year % 100 == 0:
            return False # 2. Divisible por 100 pero no por 400
        elif year % 4 == 0:
            return True  # 3. Divisible por 4
        else:
            return False

    if es_bisiesto_detallado(year):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


# ===========================================================================
# MENÚ PRINCIPAL
# ===========================================================================

# Mapeo de opciones a las funciones de SOLUCIÓN
MENU_OPS = {
    # BUCLES / ESTRUCTURAS DE CONTROL
    1: ("Control", ejercicio_control_1),
    2: ("Control", ejercicio_control_2),
    3: ("Control", ejercicio_control_3),
    4: ("Control", ejercicio_control_4),
    5: ("Control", ejercicio_control_5),
    6: ("Control", ejercicio_control_6),
    # CONDICIONALES
    7: ("Condicional", solucion_condicional_1),
    8: ("Condicional", solucion_condicional_2),
    9: ("Condicional", solucion_condicional_3),
    10: ("Condicional", solucion_condicional_4),
    11: ("Condicional", solucion_condicional_5),
    12: ("Condicional", solucion_condicional_6),
    0: ("Salir", lambda: sys.exit(0))
}

def menu():
    """Muestra el menú y obtiene la selección del usuario."""
    limpiar_pantalla()
    print("=" * 60)
    print("EJERCICIOS RESUELTOS - ESTRUCTURAS DE CONTROL Y CONDICIONALES".center(60))
    print("=" * 60)

    print("\n--- ESTRUCTURAS DE CONTROL (BUCLES) ---")
    print("1. Corregir iteración y modificación de lista")
    print("2. Tabla de multiplicar con bucles anidados")
    print("3. Corregir bucle while infinito")
    print("4. Uso de break y continue")
    print("5. Convertir bucle a comprensión de lista")
    print("6. Combinaciones con bucles anidados")

    print("\n--- ESTRUCTURAS CONDICIONALES (Modificadas) ---")
    print("7. Evaluar positivo, negativo o cero")
    print("8. Corregir errores de sintaxis en condiciones")
    print("9. Simplificar condicionales anidados")
    print("10. Corregir orden de condiciones (Rangos)")
    print("11. Usar operador ternario")
    print("12. Determinar si un año es bisiesto")

    print("\n0. Salir")

    try:
        opcion = int(input("\nIngresa el número del ejercicio (0-12): "))
        return opcion
    except ValueError:
        print("Entrada inválida. Ingresa un número del 0 al 12.")
        return -1

def main():
    """Función principal para ejecutar los ejercicios."""
    while True:
        opcion = menu()

        if opcion in MENU_OPS:
            _, func = MENU_OPS[opcion]
            if opcion != 0:
                print(f"\nEJECUTANDO EJERCICIO {opcion}...")
                func()
                esperar_enter()
            else:
                # La función de salida ya está definida en MENU_OPS[0]
                func()
        elif opcion != -1:
            print("Opción inválida. Intenta de nuevo.")
            esperar_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
        sys.exit(0)