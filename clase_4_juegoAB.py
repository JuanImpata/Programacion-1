palabra = "banana"

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

cadenas_vocal = []
cadenas_consonante = []

for i in range(len(palabra)):
    for j in range(i+1, len(palabra)+1):
        subcadena = palabra[i:j]
        if subcadena[0] in vocales:
            cadenas_vocal.append(subcadena)
        else:
            cadenas_consonante.append(subcadena)

print(f"Palabra usada: {palabra}")
print("\nJugador A (inician con vocal):")
print(cadenas_vocal)

print("\nJugador B (inician con consonante):")
print(cadenas_consonante)

if len(cadenas_vocal) > len(cadenas_consonante):
    print("\n¡Gana el Jugador A!")
elif len(cadenas_vocal) < len(cadenas_consonante):
    print("\n¡Gana el Jugador B!")
else:
    print("\n¡Empate!")
