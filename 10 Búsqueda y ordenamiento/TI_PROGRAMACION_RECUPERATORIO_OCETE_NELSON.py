#Este archivo de Python contiene los codigos correspondientes a los algoritmos tanto de busqueda como de ordenamiento.
#Alumnos: Ocete Rocio Milagros y Nelson Cristhian Alejandro
#Comisión 18

import time
import random


#       ALGORITMOS DE BUSQUEDA

#   •LINEAL (secuencial)

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

#   •BINARIA 

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# ////////////////////////////////////////////

#       ALGORITMOS DE ORDENAMIENTO

#   •BURBUJA (BUBBLE SORT)

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#   •INSERCIÓN (INSERTION SORT)

def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

#   •QUICKSORT

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)


# TIEMPOS DE EJECUCIÓN DE LISTAS

# EJECUCIÓN DE TIPOS DE ORDENAMIENTO


# Función para generar listas aleatorias de números
def generar_lista(tamaño):
    return [random.randint(1, 10000) for _ in range(tamaño)]

# Esta función mide cuánto tarda cada algoritmo de ordenamiento
# Se repite varias veces para que el tiempo no dé cero
def medir_tiempo_ordenamiento(algoritmo, lista, repeticiones=100):
    total = 0
    for _ in range(repeticiones):
        copia = lista.copy()  # hacemos copia para no modificar la lista original
        inicio = time.time()
        if algoritmo == quicksort:
            algoritmo(copia)  # quicksort devuelve una nueva lista
        else:
            algoritmo(copia)  # los otros ordenan sobre la misma lista
        fin = time.time()
        total += (fin - inicio)
    return total / repeticiones  # promedio por ejecución

# Comparación de algoritmos de ordenamiento con listas de distintos tamaños
print("\n===== COMPARACIÓN DE TIEMPOS DE ORDENAMIENTO =====")
for tamaño in [10, 100, 1000]:
    lista = generar_lista(tamaño)
    print(f"\n--- Lista de {tamaño} elementos ---")
    for nombre, algoritmo in [("Burbuja", burbuja), ("Inserción", insercion), ("Quicksort", quicksort)]:
        tiempo = medir_tiempo_ordenamiento(algoritmo, lista)
        print(f"{nombre}: {tiempo:.8f} segundos")
        

# EJECUCIÓN DE TIPOS DE BÚSQUEDAS

# Esta función mide cuánto tarda cada algoritmo de búsqueda
# Se repite muchas veces para que el tiempo no dé cero
def medir_tiempo_busqueda(algoritmo, lista, objetivo, repeticiones=10000):
    inicio = time.time()
    for _ in range(repeticiones):
        algoritmo(lista, objetivo)
    fin = time.time()
    return (fin - inicio) / repeticiones  # promedio por ejecución

# Comparación de algoritmos de búsqueda con listas de distintos tamaños
print("\n===== COMPARACIÓN DE TIEMPOS DE BÚSQUEDA =====")
for tamaño in [10, 100, 1000]:
    lista = sorted(generar_lista(tamaño))  # la búsqueda binaria necesita lista ordenada
    objetivo = lista[tamaño // 2]  # elegimos un número que está seguro en la lista

    print(f"\n--- Lista de {tamaño} elementos ---")
    tiempo_lineal = medir_tiempo_busqueda(busqueda_lineal, lista, objetivo)
    tiempo_binaria = medir_tiempo_busqueda(busqueda_binaria, lista, objetivo)

    print(f"Búsqueda Lineal:  {tiempo_lineal:.8f} segundos")
    print(f"Búsqueda Binaria: {tiempo_binaria:.8f} segundos")



