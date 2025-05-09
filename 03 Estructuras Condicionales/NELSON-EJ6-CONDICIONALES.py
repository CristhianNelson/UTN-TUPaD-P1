"""
Programa que tome la lista de numeros aleatorios, calcule su moda, su mediana y su media y las compare
para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

import random
from statistics import mode, median, mean

# Genera lista aleatoria de 50 números entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcula parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Evalúa el sesgo de la distribución
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución sin patrón claro")
