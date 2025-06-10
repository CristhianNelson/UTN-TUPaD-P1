# =========================
# Algoritmos de BÚSQUEDA
# =========================

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busqueda_binaria(lista, valor):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# =========================
# Algoritmos de ORDENAMIENTO
# =========================

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# =========================
# Ejemplo de uso directo
# =========================

datos = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", datos)

# Ordenamiento
print("\nOrdenamientos:")
print("Bubble Sort:", bubble_sort(datos.copy()))
print("Insertion Sort:", insertion_sort(datos.copy()))
print("Quick Sort:", quick_sort(datos.copy()))

# Búsquedas
valor_a_buscar = 25
print(f"\nBuscando el valor {valor_a_buscar}...")

pos_lineal = busqueda_lineal(datos, valor_a_buscar)
print("Búsqueda Lineal: Posición", pos_lineal)

datos_ordenados = quick_sort(datos)
pos_binaria = busqueda_binaria(datos_ordenados, valor_a_buscar)
print("Búsqueda Binaria (sobre lista ordenada): Posición", pos_binaria)
