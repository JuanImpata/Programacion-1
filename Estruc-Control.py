#!/usr/bin/env python3
"""
ESTRUCTURAS DE CONTROL
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

def mostrar_titulo(texto):
    """Muestra un título formateado (Función Auxiliar Corregida)"""
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")

# ===========================================================================
# EJERCICIOS PARA COMPLETAR (ESTUDIANTE) - Lógica Modificada (Se mantienen)
# ===========================================================================

def ejercicio_1_mod():
    """
    Problema: Reemplaza el bucle por una **comprensión de lista**.
    """
    numeros = [1, 2, 3, 4, 5]

    # Código original a reemplazar (Bucle tradicional)
    print("Código original (Bucle tradicional):")
    dobles_tradicional = []
    for n in numeros:
        dobles_tradicional.append(n * 2)
    print(f"Resultado tradicional: {dobles_tradicional}")

    # Tu corrección: Usar una comprensión de lista
    print("\nTu solución (Comprensión de lista):")
    dobles_comprension = [n * 2 for n in numeros]
    print(dobles_comprension)

    return "¡Ejercicio 1 completado (Comprensión de lista)!"

# --------------------------------------------------

def ejercicio_2_mod():
    """
    Problema: Usa bucles anidados para dibujar un **triángulo rectángulo**
    con asteriscos (*).
    """
    altura = 5
    print(f"Dibujando un triángulo de {altura} filas:")

    # Bucle externo: controla las filas (i)
    for i in range(1, altura + 1):
        # Bucle interno: controla los caracteres en cada fila (j)
        print("*" * i)

    return "¡Ejercicio 2 completado (Bucles anidados)! 📐"

# --------------------------------------------------

def ejercicio_3_mod():
    """
    Problema: Corregir un bucle while que debe contar hacia atrás desde 10 hasta 1.
    """
    print("Bucle while para contar hacia atrás (10 a 1):")

    # Tu corrección
    print("\nTu solución corregida:")
    contador = 10
    while contador >= 1: # La condición debe incluir el 1
        print(f"Cuenta: {contador}")
        contador -= 1 # Corrección: Decrementar la variable de control

    return "¡Ejercicio 3 completado (Bucle `while`)! 🔢"

# --------------------------------------------------

def ejercicio_4_mod():
    """
    Problema: Busca el primer número par en la lista usando **`break` y `for/else`**.
    """
    numeros = [1, 3, 5, 7, 9, 2, 4, 6]

    print(f"Lista de números: {numeros}")

    print("\nResultado:")
    for num in numeros:
        if num % 2 == 0:
            print(f"¡Par encontrado! El número es {num} (usando break).")
            break
    else: # Este `else` se ejecuta SÓLO si el bucle termina SIN ejecutar el `break`.
        print("No se encontró ningún par en la lista completa (usando for...else).")

    return "¡Ejercicio 4 completado (for/else)! 🔍"

# --------------------------------------------------

def ejercicio_5_mod():
    """
    Problema: Usar comprensión de lista para filtrar palabras > 4 letras y convertirlas
    a **mayúsculas**.
    """
    palabras = ["sol", "luna", "mar", "estrellas", "rio", "planeta"]

    # Tu solución con comprensión de lista y condición
    print(f"Lista original: {palabras}")
    print("\nTu solución (filtrado y transformación):")
    palabras_largas_mayus = [
        palabra.upper() for palabra in palabras if len(palabra) > 4
    ]
    print(palabras_largas_mayus)

    return "¡Ejercicio 5 completado (Comprensión avanzada)! 🅰️"

# --------------------------------------------------

def ejercicio_6_mod():
    """
    Problema: Generar combinaciones condicionales con comprensión de lista anidada:
    elementos de B deben ser **menores o iguales** a elementos de A.
    """
    lista_a = [1, 2, 3]
    lista_b = [1, 2, 3]

    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")

    # Solución con comprensión de listas y condición anidada
    print("\nTu solución con comprensión de listas y condición:")
    combinaciones_condicionales = [
        (a, b) for a in lista_a for b in lista_b if b <= a
    ]
    print(combinaciones_condicionales)

    return "¡Ejercicio 6 completado (Comprensión condicional)! 🔗"

# --------------------------------------------------
# ===========================================================================
# PARTE 2: SOLUCIONES INTERACTIVAS Y DEMOSTRACIONES (NUEVA LÓGICA Y CORRECCIÓN)
# ===========================================================================

def ejecutar_solucion(num):
    """Ejecuta la solución correspondiente (Mapeo corregido)."""
    soluciones = {
        1: demostracion_control_1,
        2: demostracion_control_2,
        3: demostracion_control_3,
        4: demostracion_control_4,
        5: demostracion_control_5,
        6: demostracion_control_6,
    }
    limpiar_pantalla()
    print(f"\nEJECUTANDO SOLUCIÓN {num}...")
    soluciones.get(num, lambda: print("Solución no encontrada"))()
    esperar_enter()


def demostracion_control_1():
    """Demostración 1: Comprensión de lista (Transformación)."""
    mostrar_titulo("DEMOSTRACIÓN 1: COMPRENSIÓN DE LISTA (FILTRO Y TRANSFORMACIÓN)")

    precios = [100.50, 20.99, 330.00, 4.25]
    TASA_IMPUESTO = 0.15 # 15%

    print(f"Precios originales: {precios}")
    print(f"Objetivo: Aplicar impuesto del {TASA_IMPUESTO*100}% SÓLO a precios > 100.")

    precios_con_impuesto = [
        round(p * (1 + TASA_IMPUESTO), 2)
        if p > 100
        else p
        for p in precios
    ]

    print(f"\nResultado (Comprensión con condicional ternario): {precios_con_impuesto}")
    print("\nReflexión: Se usa un operador ternario dentro de la comprensión para la transformación.")

def demostracion_control_2():
    """Demostración 2: Bucles Anidados (Patrón de forma cuadrada)."""
    mostrar_titulo("DEMOSTRACIÓN 2: BUCLES ANIDADOS (PATRÓN CUADRADO CON NÚMEROS)")

    lado = 4
    print(f"Dibujando un patrón cuadrado de {lado}x{lado} con números:")

    # Bucle externo: filas
    for i in range(1, lado + 1):
        linea = ""
        # Bucle interno: columnas
        for j in range(1, lado + 1):
            linea += f"{j} "
        print(linea)

    print("\nReflexión: Ambos bucles son independientes, resultando en una estructura rectangular o cuadrada.")

def demostracion_control_3():
    """Demostración 3: Bucle `while` (Esperar una condición)."""
    mostrar_titulo("DEMOSTRACIÓN 3: BUCLE WHILE (ESPERAR ENTRADA VÁLIDA)")

    print("Problema: Solicitar una contraseña hasta que sea correcta ('python').")
    contraseña_correcta = "python"
    intento = ""

    while intento != contraseña_correcta:
        intento = input("\nIntroduce la contraseña: ")
        if intento != contraseña_correcta:
            print("Contraseña incorrecta. Inténtalo de nuevo.")

    print("\n✅ ¡Contraseña aceptada! (El bucle `while` se completó).")
    print("Reflexión: Los bucles `while` son ideales para la validación continua.")

def demostracion_control_4():
    """Demostración 4: `break` y `continue` con índices."""
    mostrar_titulo("DEMOSTRACIÓN 4: CONTROL DE FLUJO CON ÍNDICES")

    elementos = ['A', 'B', 'SKIP', 'D', 'STOP', 'F']
    print(f"Lista de elementos: {elementos}")

    print("\nReglas:")
    print(" - Saltar si es 'SKIP' (continue).")
    print(" - Detener si es 'STOP' (break).")

    for indice, valor in enumerate(elementos):
        if valor == 'STOP':
            print(f"[{indice}] Valor 'STOP' encontrado. Deteniendo el bucle.")
            break
        if valor == 'SKIP':
            print(f"[{indice}] Valor 'SKIP' encontrado. Saltando iteración.")
            continue
        print(f"[{indice}] Procesando elemento: {valor}")

    print("\nReflexión: `enumerate` da el índice, y el control de flujo sigue siendo eficiente.")

def demostracion_control_5():
    """Demostración 5: Comprensión de diccionario."""
    mostrar_titulo("DEMOSTRACIÓN 5: COMPRENSIÓN DE DICCIONARIO")

    nombres = ["Ana", "Pedro", "Luisa", "Carlos"]
    print(f"Lista de nombres: {nombres}")
    print("Objetivo: Crear un diccionario donde la clave es el nombre y el valor es la longitud.")

    # Sintaxis: {clave: valor for elemento in iterable}
    longitudes_dict = {nombre: len(nombre) for nombre in nombres}

    print(f"\nResultado (Comprensión de diccionario): {longitudes_dict}")
    print("\nReflexión: Una forma concisa de mapear un iterable a un diccionario.")

def demostracion_control_6():
    """Demostración 6: Uso de `zip` con `for` (Alternativa a anidados simples)."""
    mostrar_titulo("DEMOSTRACIÓN 6: ITERACIÓN PARALELA CON `ZIP`")

    claves = ["nombre", "edad", "ciudad"]
    valores = ["Elena", 30, "Madrid"]
    print(f"Claves: {claves}")
    print(f"Valores: {valores}")

    print("\nObjetivo: Combinar las listas en un diccionario usando `zip`.")
    nuevo_diccionario = {}

    # Usando for con zip
    for clave, valor in zip(claves, valores):
        nuevo_diccionario[clave] = valor
        print(f"Agregando: {clave}: {valor}")

    print(f"\nResultado final del diccionario: {nuevo_diccionario}")
    print("\nReflexión: `zip` permite iterar sobre múltiples iterables en paralelo de forma segura.")


# ===========================================================================
# MENÚ PRINCIPAL
# ===========================================================================

# Se mantiene el menú principal y la función main original
def menu_principal():
    """Muestra el menú y obtiene la selección del usuario."""
    limpiar_pantalla()
    print("=" * 60)
    print("ESTRUCTURAS DE CONTROL: EJERCICIOS Y SOLUCIONES".center(60))
    print("=" * 60)

    print("\nSelecciona un ejercicio/solución a ejecutar:")
    print("1. Transformación con Comprensión de Lista")
    print("2. Bucles Anidados (Patrón Triangular)")
    print("3. Bucle While Decreciente (Corregido)")
    print("4. Control de Flujo (Break y Continue)")
    print("5. Comprensión de Lista (Filtrado y Fórmula)")
    print("6. Comprensión Anidada (Combinaciones Condicionales)")

    print("\n0. Salir")

    try:
        opcion = int(input("\nIngresa el número (0-6): "))
        return opcion
    except ValueError:
        return -1

def main():
    """Función principal para ejecutar las soluciones."""
    while True:
        opcion = menu_principal()

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif 1 <= opcion <= 6:
            ejecutar_solucion(opcion)
        else:
            print("Opción inválida. Intenta de nuevo.")
            esperar_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n¡Programa terminado por el usuario!")
        sys.exit(0)