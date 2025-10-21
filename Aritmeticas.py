"""
EXPRESIONES ARITMÉTICAS CONFUSAS - Actividad 1
Este código demuestra errores comunes y confusión con expresiones aritméticas.
Los estudiantes deben identificar los problemas y entender la precedencia de operadores.
"""

print("=" * 60)
print("EXPRESIONES ARITMÉTICAS - Errores Comunes")
print("=" * 60)
print()

# Problema 1: No entender la precedencia de operadores
print("Problema 1: Confusión con Precedencia de Operadores")
print("-" * 40)

# ¿Qué calcula esto?
result1 = 5 + 3 * 2
print(f"5 + 3 * 2 = {result1}")
print("¿Es (5 + 3) * 2 = 16?")
print("¿O es 5 + (3 * 2) = 11?")
print()
## En la jerarquía de operaciones, la **multiplicación** siempre se resuelve antes que la suma. Por lo tanto, el cálculo se realiza como $5 + (3 \times 2)$, que equivale a $5 + 6 = 11$.

# Otro ejemplo confuso
result2 = 10 - 2 + 3
print(f"10 - 2 + 3 = {result2}")
print("¿Es 10 - (2 + 3) = 5?")
print("¿O es (10 - 2) + 3 = 11?")
print()
## Como la suma y la resta comparten el mismo nivel de prioridad, se aplica la regla de **asociatividad izquierda**. La evaluación se realiza secuencialmente de izquierda a derecha: $(10 - 2) + 3$, lo que da $8 + 3 = 11$.

# Problema 2: Confusión con división
print("Problema 2: Tipos de División")
print("-" * 40)

result3 = 7 / 2
result4 = 7 // 2
result5 = 7 % 2

print(f"7 / 2 = {result3}  (¿Qué tipo de división?)")
print(f"7 // 2 = {result4} (¿Qué significa //?)")
print(f"7 % 2 = {result5}  (¿Qué es %?)")
print()
## - **`/` (División Real):** Siempre devuelve el cociente como un número de punto flotante (**float**), produciendo 3.5.
## - **`//` (División de Piso):** Calcula la división y trunca el resultado hacia el número entero inferior, ignorando el resto, lo que resulta en **3**.
## - **`%` (Operador Módulo):** Devuelve el **resto** de la división entera de 7 entre 2, que es **1**.

# Problema 3: Confusión con operador de potencia
print("Problema 3: Operador de Potencia")
print("-" * 40)

result6 = 2 ** 3
result7 = 2 * 3
result8 = 2 ^ 3 # ¡Esto NO es potencia!

print(f"2 ** 3 = {result6} (¿Es esto potencia?)")
print(f"2 * 3 = {result7}  (¿Es esto potencia?)")
print(f"2 ^ 3 = {result8}  (¿Es esto potencia?)")
print("¡Advertencia: ^ NO es potencia en Python!")
print()
## - **`**` (Doble asterisco): Es el símbolo designado para la operación de **exponenciación** ($2^3 = 8$).
## - **`*` (Asterisco simple):** Representa la multiplicación simple ($2 \times 3 = 6$).
## - **`^` (Caret):** Este operador se interpreta como el operador **bitwise XOR** (OR Exclusivo a nivel de bits), no como una potencia matemática, dando 1.

# Problema 4: Expresión compleja sin paréntesis
print("Problema 4: Expresión Compleja")
print("-" * 40)

result9 = 2 + 3 * 4 - 5 / 2
print(f"2 + 3 * 4 - 5 / 2 = {result9}")
print("¿Cómo se evalúa esto?")
print("¿En qué orden ocurren las operaciones?")
print()
## El orden de evaluación sigue PEMDAS/PEDMAS (Paréntesis, Exponentes, Multiplicación/División, Suma/Resta). Primero se resuelven las operaciones de mayor prioridad: $3 \times 4 = 12$ y $5 / 2 = 2.5$. Luego se ejecuta la suma y la resta de izquierda a derecha: $2 + 12 - 2.5 = 11.5$.

# Problema 5: Confusión con mezcla de tipos
print("Problema 5: Mezcla de Tipos")
print("-" * 40)

result10 = 5 + 3.0
result11 = 10 / 2
result12 = 10 // 2

print(f"5 + 3.0 = {result10}  (tipo: {type(result10).__name__})")
print(f"10 / 2 = {result11}  (tipo: {type(result11).__name__})")
print(f"10 // 2 = {result12} (tipo: {type(result12).__name__})")
print("¿Por qué los tipos son diferentes?")
print()
## - $5 + 3.0$: La operación que involucra un **float** (3.0) y un **int** (5) resulta en una promoción de tipo; el resultado es siempre **float** (8.0).
## - $10 / 2$: El operador de división estándar (`/`) en Python está diseñado para producir un resultado **float** (5.0) por defecto.
## - $10 // 2$: El operador de división de piso (`//`) sobre dos enteros produce un resultado de tipo **int** (5).

# Problema 6: Números negativos y operadores
print("Problema 6: Números Negativos")
print("-" * 40)

result13 = -5 + 3
result14 = 5 + -3
result15 = 5 - -3
result16 = -5 * -3

print(f"-5 + 3 = {result13}")
print(f"5 + -3 = {result14}")
print(f"5 - -3 = {result15}  (¿Por qué es 8?)")
print(f"-5 * -3 = {result16}")
print()
## - $-5 + 3 = -2$: Sumar 3 a un número negativo lo acerca a cero.
## - $5 + -3 = 2$: La adición de un número negativo se simplifica a la resta.
## - $5 - -3 = 8$: La operación de **restar un valor negativo** se convierte en una suma de su valor absoluto, es decir, $5 + 3$.
## - $-5 \times -3 = 15$: En la multiplicación, el producto de dos números con el mismo signo (ambos negativos) es siempre **positivo**.

# Problema 7: Los paréntesis hacen la diferencia
print("Problema 7: Impacto de Paréntesis")
print("-" * 40)

result17 = 2 + 3 * 4
result18 = (2 + 3) * 4
result19 = 2 + (3 * 4)

print(f"2 + 3 * 4 = {result17}")
print(f"(2 + 3) * 4 = {result18}")
print(f"2 + (3 * 4) = {result19}")
print("¡Mismos números, resultados diferentes!")
print()
## - $2 + 3 \times 4 = 14$: Se respeta la precedencia (multiplicación primero).
## - $(2 + 3) \times 4 = 20$: Los **paréntesis** anulan la precedencia estándar, obligando a realizar la suma primero ($5 \times 4$).
## - $2 + (3 \times 4) = 14$: Los paréntesis solo brindan claridad, ya que la multiplicación ya tenía prioridad.

# Problema 8: Múltiples divisiones
print("Problema 8: Múltiples Divisiones")
print("-" * 40)

result20 = 20 / 4 / 2
result21 = 20 / (4 / 2)
result22 = (20 / 4) / 2

print(f"20 / 4 / 2 = {result20}")
print(f"20 / (4 / 2) = {result21}")
print(f"(20 / 4) / 2 = {result22}")
print("¿De qué manera se evalúa?")
print()
## - $20 / 4 / 2 = 2.5$: La división es de **asociatividad izquierda**. Se agrupan los términos de izquierda a derecha: $(20/4)/2$.
## - $20 / (4 / 2) = 10.0$: Los **paréntesis** cambian la agrupación, forzando la división $4/2$ primero, luego $20 / 2$.
## - $(20 / 4) / 2 = 2.5$: Los paréntesis reafirman la regla de asociatividad izquierda para este caso.

# Problema 9: Confusión con operador módulo
print("Problema 9: Operador Módulo")
print("-" * 40)

result23 = 17 % 5
result24 = 17 / 5
result25 = 17 // 5

print(f"17 % 5 = {result23}  (¿Qué significa esto?)")
print(f"17 / 5 = {result24}")
print(f"17 // 5 = {result25}")
print("¿Cómo se relacionan?")
print()
## - **17 % 5 = 2**: El residuo es lo que queda después de repartir 17 en grupos completos de 5 (tres grupos de 5 dejan un sobrante de 2).
## - **17 // 5 = 3**: Este es el número máximo de veces que el divisor (5) cabe en el dividendo (17).
## - **17 / 5 = 3.4**: El cociente exacto, que combina la parte entera (3) y la parte fraccionaria del residuo (0.4, que es $2/5$).

# Problema 10: Cálculo del mundo real que sale mal
print("Problema 10: Ejemplo del Mundo Real")
print("-" * 40)

# Calcular: (100 + 50) * 0.15 impuesto
wrong_tax = 100 + 50 * 0.15
correct_tax = (100 + 50) * 0.15

print("Calculando impuesto del 15% sobre $150:")
print(f"100 + 50 * 0.15 = ${wrong_tax}")
print(f"(100 + 50) * 0.15 = ${correct_tax}")
print("¿Cuál es correcto?")
print()
## - **Cálculo Incorrecto ($107.5$):** Se respeta la prioridad de la multiplicación, aplicando el impuesto solo a $50$ ($50 \times 0.15 = 7.5$), y luego sumando $100$ al resultado, lo que es erróneo.
## - **Cálculo Correcto ($22.5$):** Los **paréntesis** aseguran que la suma total ($150$) se compute antes de aplicarle el multiplicador de $0.15$.

# Problema 11: Confusión con conversión de temperatura
print("Problema 11: Conversión de Temperatura")
print("-" * 40)

celsius = 25
# Convertir a Fahrenheit: F = C * 9/5 + 32
wrong_fahrenheit = celsius * 9 / 5 + 32
also_wrong = celsius * 9 / (5 + 32)
correct_fahrenheit = (celsius * 9 / 5) + 32

print(f"25°C a Fahrenheit:")
print(f"celsius * 9 / 5 + 32 = {wrong_fahrenheit}")
print(f"celsius * 9 / (5 + 32) = {also_wrong}")
print(f"(celsius * 9 / 5) + 32 = {correct_fahrenheit}")
print("¿Qué fórmula es correcta?")
print()
## - **$celsius \times 9 / 5 + 32$ ($77.0$):** Esta es correcta, ya que las multiplicaciones y divisiones se evalúan primero de izquierda a derecha, respetando la fórmula.
## - **$celsius \times 9 / (5 + 32)$ ($\approx 6.08$):** Incorrecta. Los paréntesis agrupan erróneamente el divisor y la constante de ajuste, violando la estructura de la fórmula.
## - **$(celsius \times 9 / 5) + 32$ ($77.0$):** Correcta. Los paréntesis añaden claridad, aunque la precedencia natural de los operadores ya garantizaba el orden correcto.

# Problema 12: Cálculo de promedio
print("Problema 12: Cálculo de Promedio")
print("-" * 40)

a, b, c = 10, 20, 30
wrong_average = a + b + c / 3
correct_average = (a + b + c) / 3

print(f"Promedio de 10, 20, 30:")
print(f"a + b + c / 3 = {wrong_average}")
print(f"(a + b + c) / 3 = {correct_average}")
print("¿Por qué son diferentes?")
print()
## - **Cálculo Incorrecto ($40.0$):** Debido a la alta precedencia de la división, solo el último número ($c=30$) se divide por 3, y luego se suma al resto: $10 + 20 + (30 / 3)$.
## - **Cálculo Correcto ($20.0$):** Los **paréntesis** son indispensables para garantizar que la **suma total** de todos los valores se complete antes de ser dividida por el número de elementos.

print("=" * 60)
print("¿Puedes identificar todos los problemas?")
print("¿Entiendes por qué cada resultado es lo que es?")
print("=" * 60)