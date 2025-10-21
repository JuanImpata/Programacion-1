#Realizado por Andrés Felipe Chamorro Pérez y Juan Camilo Impata Aguirre

#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - MANEJO DE EXCEPCIONES
Completa estos ejercicios mientras exploras los conceptos confusos de manejo de excepciones.
"""

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")
print("Esta función tiene un except desnudo. Arréglalo para capturar excepciones específicas.")
print()

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    ARREGLA: Usa manejo de excepciones específico en lugar de except desnudo.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
         print("Error: no se puede dividir entre cero. La lista está vacía.")
    except TypeError:
        print("Error: la lista contiene elementos no numéricos.")
        return None

# Prueba tu arreglo:
# print(calcular_promedio([1, 2, 3, 4, 5]))  # Debería funcionar
# print(calcular_promedio([]))  # Debería manejar lista vacía
# print(calcular_promedio([1, 2, 'a']))  # Debería manejar error de tipo

print("¿Completado? [Sí/No]: __si___")

# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")
print("Este código falla silenciosamente. Añade mensajes apropiados.")
print()

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo.
    ARREGLA: Añade manejo de excepciones Y feedback al usuario.
    """
    # Tu código aquí
    try:
        with open(archivo, 'w') as f:
            f.write(str(datos))
        print(f" Datos guardados correctamente en '{archivo}'.")
        return True
    except FileNotFoundError:
        print(f" Error: no se encontró la ruta o el archivo '{archivo}'.")
        return False
    except PermissionError:
        print(f"Error: no tienes permisos para escribir en '{archivo}'.")
        return False
    except Exception as e:
        print(f" Ocurrió un error inesperado: {e}")
        return False


# Prueba tu arreglo:
# guardar_datos({"usuario": "Ana"}, "datos.txt")  # Debería funcionar
# guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")  # Debería informar error

print("¿Completado? [Sí/No]: _si____")

# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")
print("Implementa un manejo completo de archivos con else y finally.")
print()

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    TODO: Implementa try-except-else-finally:
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    """
    # Tu código aquí

    f = None
    try:
        f = open(nombre_archivo, 'r')
        contenido = f.read()
    except FileNotFoundError:
        print(" El archivo no existe.")
    else:
        print(" Archivo leído correctamente.")
        print(contenido)
    finally:
        if f:
            f.close()
            print(" Archivo cerrado correctamente.")



# Prueba tu implementación:
# procesar_archivo("existente.txt")
# procesar_archivo("faltante.txt")

print("¿Completado? [Sí/No]: _si____")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")
print("Implementa validación con excepciones específicas.")
print()

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    TODO: Lanza excepciones apropiadas si:
    - nombre_usuario tiene menos de 3 caracteres (ValueError)
    - edad no es un entero (TypeError)
    - edad es negativa o mayor a 150 (ValueError)
    - email no contiene '@' (ValueError)
    """
    # Tu código aquí

    if len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150.")
    if "@" not in email:
        raise ValueError("El email debe contener '@'.")
    
    print("Usuario creado correctamente:", nombre_usuario)


# Prueba tu implementación:
# crear_usuario("Ana", 25, "ana@example.com")  # Debería funcionar
# crear_usuario("Ab", 25, "ana@example.com")  # Debería lanzar ValueError
# crear_usuario("Ana", "25", "ana@example.com")  # Debería lanzar TypeError
# crear_usuario("Ana", -5, "ana@example.com")  # Debería lanzar ValueError
# crear_usuario("Ana", 25, "anaexample.com")  # Debería lanzar ValueError

print("¿Completado? [Sí/No]: __si___")

# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")
print("Crea excepciones personalizadas para un sistema bancario.")
print()

# TODO: Crea estas clases de excepción:
# class SaldoInsuficienteError(Exception):
#     def __init__(self, saldo, monto):
#         self.saldo = saldo
#         self.monto = monto
#         super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

# class MontoInvalidoError(Exception):
#     pass

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    TODO: 
    - Lanza MontoInvalidoError si monto <= 0
    - Lanza SaldoInsuficienteError si monto > saldo
    - Retorna nuevo saldo si exitoso
    """
    # Tu código aquí
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, pero solo tienes ${saldo}")

class MontoInvalidoError(Exception):
    def __init__(self, monto):
        super().__init__(f"Monto inválido: {monto}. Debe ser mayor que 0.")

def retirar(saldo, monto):
    if monto <= 0:
        raise MontoInvalidoError(monto)
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto


# Prueba tu implementación:
# print(retirar(100, 50))  # Debería funcionar
# retirar(100, 150)  # Debería lanzar SaldoInsuficienteError
# retirar(100, -10)  # Debería lanzar MontoInvalidoError

print("¿Completado? [Sí/No]: __si___")

# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")
print("Procesa una lista con manejo de errores.")
print()

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    TODO: 
    - Intenta convertir cada elemento a int
    - Si falla, registra el error pero continúa con los demás
    - Retorna tupla (resultados_exitosos, lista_errores)
    """
    # Tu código aquí

    resultados_exitosos = []
    lista_errores = []

    for elemento in lista_strings:
        try:
            numero = int(elemento)
            resultados_exitosos.append(numero * 2)
        except ValueError as e:
            lista_errores.append((elemento, str(e)))

    return resultados_exitosos, lista_errores


# Prueba tu implementación:
# resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
# print(f"Exitosos: {resultados}")  # [2, 4, 8]
# print(f"Errores: {errores}")  # [('abc', error), ('xyz', error)]

# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")
print("Registra errores pero permite que el llamador los maneje.")
print()

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    TODO:
    - Intenta procesar valor
    - Si falla, registra el error (print)
    - Re-lanza la excepción para que el llamador pueda manejarla
    """
    #try:
        #resultado = 100 / int(valor)
        #return resultado
    #except (ValueError, ZeroDivisionError) as e:
        # Tu código aquí: registra y re-lanza



    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error al procesar valor '{valor}': {e}")
        raise



# Prueba tu implementación:
# print(operacion_critica("10"))  # Debería funcionar
# try:
#     operacion_critica("0")  # Debería registrar y re-lanzar
# except ZeroDivisionError:
#     print("Llamador: Manejo el error")

print("¿Completado? [Sí/No]: __si___")

# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")
print("Maneja diferentes tipos de errores de manera diferente.")
print()

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    TODO: Implementa try con múltiples except:
    - ZeroDivisionError: retorna mensaje específico
    - TypeError: retorna mensaje específico
    - ValueError: retorna mensaje específico
    """
    # Tu código aquí
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación inválida")
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Los operandos deben ser números."
    except ValueError as ve:
        return f"Error: {ve}"

# Prueba tu implementación:
# print(calculadora_segura("suma", 10, 5))  # 15
# print(calculadora_segura("division", 10, 0))  # Maneja división por cero
# print(calculadora_segura("suma", 10, "5"))  # Maneja error de tipo
# print(calculadora_segura("invalida", 10, 5))  # Maneja operación inválida

print("¿Completado? [Sí/No]: __si___")

# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")
print("Preserva el contexto al lanzar nuevas excepciones.")
print()

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON.
    TODO: 
    - Intenta parsear JSON
    - Si falla, lanza ValueError con 'from' para preservar el error original
    """
    import json
    # Tu código aquí
 
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Error al parsear JSON") from e

# Pruebas
print(parsear_configuracion('{"nombre": "Ana"}'))

try:
    parsear_configuracion('json invalido')
except ValueError as e:
    print(f"Error: {e}")
    print(f"Causado por: {e.__cause__}")


# Prueba tu implementación:
# print(parsear_configuracion('{"nombre": "Ana"}'))  # Debería funcionar
# try:
#     parsear_configuracion('json invalido')
# except ValueError as e:
#     print(f"Error: {e}")
#     print(f"Causado por: {e.__cause__}")

print("¿Completado? [Sí/No]: __si___")

# =========================================================================== 
# Ejercicio 10: Proyecto completo 
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")
print("Crea un sistema de gestión de inventario con manejo completo de excepciones.")
print()

# 1️⃣ Excepciones personalizadas
class ErrorInventario(Exception):
    """Excepción base para inventario"""
    pass

class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando un producto no existe en el inventario"""
    pass

class StockInsuficiente(ErrorInventario):
    """Se lanza cuando no hay suficiente stock para retirar"""
    pass

# 2️⃣ Clase Inventario
class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, codigo, nombre, cantidad):
        """Añade producto al inventario."""
        if cantidad <= 0:
            raise ValueError(f"La cantidad debe ser positiva, no {cantidad}.")
        if codigo in self.productos:
            raise KeyError(f"El producto con código {codigo} ya existe.")
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}

    def retirar_stock(self, codigo, cantidad): 
        """Retira cantidad de un producto."""
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código {codigo} no encontrado.")
        if cantidad > self.productos[codigo]["cantidad"]:
            raise StockInsuficiente(f"Stock insuficiente para el producto {codigo}.")
        self.productos[codigo]["cantidad"] -= cantidad

    def obtener_producto(self, codigo):
        """Obtiene información de un producto."""
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto con código {codigo} no encontrado.")
        return self.productos[codigo]

# 3️⃣ Prueba de la implementación
inventario = Inventario()

# Agregar productos
try:
    inventario.agregar_producto("001", "Laptop", 10)
    inventario.agregar_producto("002", "Teclado", 5)
    print("Productos agregados correctamente.")
except (ValueError, KeyError) as e:
    print("Error al agregar producto:", e)

# Obtener producto
try:
    print(inventario.obtener_producto("001"))
except ProductoNoEncontrado as e:
    print(e)

# Retirar stock
try:
    inventario.retirar_stock("001", 5)
    print("Stock retirado correctamente.")
except (ProductoNoEncontrado, StockInsuficiente) as e:
    print(e)

# Probar errores
try:
    inventario.retirar_stock("003", 1)  # Producto no existe
except ErrorInventario as e:
    print("Error:", e)

try:
    inventario.retirar_stock("002", 10)  # Stock insuficiente
except ErrorInventario as e:
    print("Error:", e)

print("\nEstado final del inventario:", inventario.productos)

print("¿Completado? [Sí/No]:__Sí__")

# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN")
print("=" * 70 + "\n")

print("Después de completar estos ejercicios, reflexiona:Al hacer estos ejercicios entendí la importancia de manejar errores de manera clara y específica. " \
"Usé frecuentemente ValueError, TypeError y KeyError, y creé excepciones personalizadas como SaldoInsuficienteError y ProductoNoEncontrado para situaciones particulares." \
"El patrón try-except-else-finally me resultó muy útil para procesar datos de forma segura y asegurar el cierre de recursos. El manejo de excepciones mejora la experiencia del usuario al mostrar mensajes claros y evitar fallos inesperados, como divisiones por cero o retiros de stock inexistente.")
print()
print("1. ¿Qué tipos de excepciones usaste más frecuentemente?:""ValueError, TypeError, KeyError, y excepciones personalizadas como SaldoInsuficienteError o ProductoNoEncontrado")
print("2. ¿Cuándo decidiste crear excepciones personalizadas?:""Cuando querías comunicar errores específicos del dominio, como problemas con inventario o saldo bancario, que no encajan en excepciones estándar")
print("3. ¿Qué patrón de manejo de excepciones te pareció más útil?:""try-except-else-finally para asegurarse de que ciertas operaciones críticas se ejecuten sin importar errores, o try-except con relanzamiento (raise) para registrar y pasar errores")
print("4. ¿Cómo ayuda el manejo de excepciones a la experiencia del usuario?:""Permite que el programa informe claramente qué salió mal y cómo solucionarlo, en lugar de fallar silenciosamente o con un traceback confuso")
print("5. ¿Qué errores comunes evitaste con el manejo apropiado?:""División por cero, acceso a productos inexistentes, retiros de saldo insuficiente, escritura en rutas no válidas, y conversión de tipos incorrectos")
print()
print("Discute tus respuestas con un compañero o con el profesor.")
print()

print("=" * 70)
print(" ¡EJERCICIOS COMPLETADOS!")
print("=" * 70)



