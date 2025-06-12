# Ejercicio 5: Palabras únicas y conteo
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)

repeticiones = {}
for palabra in palabras:
    if palabra in repeticiones:
        repeticiones[palabra] += 1
    else:
        repeticiones[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Repeticiones:", repeticiones)