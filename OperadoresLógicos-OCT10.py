###🟢 NIVEL 1: Básico (Operadores Fundamentales)
#Ejercicio 1.1: Predice los Resultados
# Evalúa sin ejecutar:

print(True and False)
print(True or False)
print(not True)
print(not False)
#Tu predicción: False, True, False, True
#Resultado real: False, True,False, True
#Explicación: Estas son las leyes de bool.

#Ejercicio 1.2: Operadores Combinados
a, b, c = True, False, True

print(a and b)  # False
print(a or b)   # True
print(b or c)   # True
print(a and c)  # True
#Tus predicciones: False, True, True,True

#Ejercicio 1.3: Precedencia
a, b, c = True, False, True

print(a and b or c)      # True
print(a or b and c)      # True
print(not a or b)        # False
print(not (a or b))      # False
#Tus predicciones: True, True, False, False

#Ejercicio 1.4: Comparaciones y Lógica
x = 5
print(x > 3 and x < 10)  # True
print(x < 3 or x > 10)   # False
print(not x > 3)         # False
#Tus predicciones: True, False, False

#Ejercicio 1.5: Comparaciones Encadenadas
x = 5
print(3 < x < 10)        # True
print(1 <= x <= 3)       # False
print(10 > x > 3)        # True
#Tus predicciones: True, False, True

###🟡 NIVEL 2: Intermedio (Valores y Cortocircuito)
#Ejercicio 2.1: Valores Retornados
print("hola" and "mundo")  # "mundo"
print("hola" and "")       # ""
print("" and "mundo")      # ""
print("hola" or "mundo")   # "hola"
print("" or "mundo")       # "mundo"
#Tus predicciones: "mundo", "", "", "hola", "mundo"

#Ejercicio 2.2: Truthy y Falsy
print(bool(0))          # False
print(bool(""))         # False
print(bool([]))         # False
print(bool([0]))        # True
print(bool(" "))        # True
print(bool(None))       # False
#Tus predicciones: Fale, False, False, True, True, False

#Ejercicio 2.3: Evaluación de Cortocircuito
#Evalúa qué se imprime:

def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Caso 1
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")

# Caso 2
print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")

# Caso 3
print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")
#Tu predicción: False, False, True

#Ejercicio 2.4: Operadores de Pertenencia
nums = [1, 2, 3, 4, 5]
print(3 in nums)        # True
print(6 in nums)        # False
print(6 not in nums)    # True

word = "Python"
print("P" in word)      # True
print("p" in word)      # False
print("th" in word)     # True
#Tus predicciones: True, False, True, True, False, True

#Ejercicio 2.5: Identidad vs Igualdad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # True
print(lista1 is lista2)  # False
print(lista1 == lista3)  # True
print(lista1 is lista3)  # True
#Tus predicciones: True, False, True, True

###🔴 NIVEL 3: Avanzado (Aplicaciones Prácticas)
#Ejercicio 3.1: Validación de Formulario
#Implementa la función validar_datos que verifica si: - El nombre tiene entre 2 y 30 caracteres - El email contiene '@' - La edad es mayor o igual a 18 - La contraseña tiene al menos 8 caracteres

def validar_datos(nombre, email, edad, password):
    # Tu código aquí

    
    if len(nombre) < 2 or len(nombre) > 30:
        return False
    if '@' not in email:
        return False
    if edad < 18:
        return False
    if len(password) < 8:
        return False
    return True

#Ejercicio 3.2: Sistema de Autorización
#Implementa un sistema que determine si un usuario puede acceder a un recurso basado en: - Debe estar autenticado - Debe ser administrador O tener el permiso específico - No debe estar en la lista negra

def puede_acceder(usuario, permiso_requerido, lista_negra):
    # Tu código aquí


    if not usuario["autenticado"]:
        return False
    if usuario["id"] in lista_negra:
        return False
    if usuario["admin"]:
        return True
    if permiso_requerido in usuario["permisos"]:
        return True
    return False
#Ejercicio 3.3: Acceso Seguro a Diccionario
#Implementa una función obtener_valor_seguro que retorne: - El valor de la clave si existe - Un valor predeterminado si la clave no existe

def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    # Tu código aquí (sin usar .get())

    
    if clave in diccionario:
        return diccionario[clave]
    return predeterminado

#Ejercicio 3.4: Filtrar Lista
#Escribe una función para filtrar una lista de productos según criterios: - Precio dentro de un rango (min y max) - Opcionalmente filtrar por categoría - Solo productos disponibles

def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    # Tu código aquí

  
    resultado = []
    for producto in productos:
        if not producto["disponible"]:
            continue
        if not (precio_min <= producto["precio"] <= precio_max):
            continue
        if categoria is not None and producto["categoria"] != categoria:
            continue
        resultado.append(producto)
    return resultado

#Ejercicio 3.5: Evaluación de Riesgo
#Implementa un sistema de evaluación de riesgo crediticio:

def evaluar_riesgo(cliente):
    """
    Evalúa si un cliente tiene bajo riesgo crediticio.
    
    Criterios:
    - Score crediticio alto (>700) O
    - Ingreso anual >50000 Y historial > 2 años O
    - Cliente VIP Y sin deudas pendientes
    """
    # Tu código aquí

    # Caso 1: buen puntaje crediticio
    if cliente["score_crediticio"] > 700:
        return True
    
    # Caso 2: buenos ingresos y suficiente historial
    if cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2:
        return True
    
    # Caso 3: cliente VIP sin deudas pendientes
    if cliente["vip"] and not cliente["deudas_pendientes"]:
        return True
    
    # Si no cumple ninguno de los casos anteriores
    return False

###🎯 PROYECTO FINAL: Sistema de Control de Acceso
#Descripción
#Crea un sistema de control de acceso para una plataforma digital que determine qué recursos puede ver un usuario.

#Requisitos Mínimos
#Función que verifica si un usuario puede acceder a un recurso
#Múltiples reglas de acceso
#Manejo de diferentes tipos de usuarios
#Justificación para cada decisión

#codigo basico

def puede_entrar(usuario, recurso):
    # Si no está conectado, no puede entrar
    if not usuario["autenticado"]:
        return "No puede entrar: no está conectado"

    # Si es administrador, puede entrar a todo
    if usuario["rol"] == "admin":
        return "Puede entrar: es administrador"

    # Si tiene permiso para ese recurso
    if recurso in usuario["permisos"]:
        return f"Puede entrar: tiene permiso para '{recurso}'"

    # Si no cumple nada de lo anterior
    return "No puede entrar: no tiene permiso"

###📊 Ejercicios de Debugging
#Debug 1: Encuentra el Error
# Este código debería verificar si el usuario tiene permisos
def verificar_permisos(usuario, accion):
    if usuario["permisos"] and accion in usuario["permisos"]:
        return True
    else:
        return False

# Prueba
usuario = {"id": 1, "nombre": "Juan"}
print(verificar_permisos(usuario, "leer"))
#¿Qué está mal?: El error ocurre porque el diccionario usuario no contiene la clave "permisos". 
#                Al intentar acceder directamente con usuario["permisos"], Python genera un KeyError al no encontrar esa clave en el diccionario. 

#Debug 2: Encuentra el Error
# Este código debería filtrar estudiantes aprobados
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": None},
    {"nombre": "Carmen", "nota": 92}
]

aprobados = [e for e in estudiantes if e["nota"] >= 60]
print(aprobados)
#¿Qué está mal? : El error se produce porque uno de los estudiantes (Luis) tiene nota = None.
#                 Al intentar comparar None >= 60, Python lanza un TypeError, ya que no se pueden comparar valores de tipo NoneType con números.


#✅ Autoevaluación

#Nivel 1 (Básico)
#✅ Ejercicio 1.1
#✅ Ejercicio 1.2
#✅ Ejercicio 1.3
#✅ Ejercicio 1.4
#✅ Ejercicio 1.5

#Nivel 2 (Intermedio)
#✅ Ejercicio 2.1
#✅ Ejercicio 2.2
#✅ Ejercicio 2.3
#✅ Ejercicio 2.4
#✅ Ejercicio 2.5

#Nivel 3 (Avanzado)
#✅ Ejercicio 3.1
#✅ Ejercicio 3.2
#✅ Ejercicio 3.3
#✅ Ejercicio 3.4
#✅ Ejercicio 3.5

#Proyecto Final
#✅ Sistema de Control de Acceso