"""
Programa que tome la lista de numeros aleatorios, calcule su moda, su mediana y su media y las compare
para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo aparente (distribución simétrica)"


print("Lista generada (primeros 10 elementos):", numeros_aleatorios[:10], "...")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")  # Mostramos con 2 decimales
print("\nAnálisis de sesgo:", sesgo)