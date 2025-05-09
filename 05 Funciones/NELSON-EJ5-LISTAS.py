"""
Se solicita analizar el funcionamiento de un programa dado
Autor: Cristhian Alejandro Nelson
Fecha: 09/05/2025
"""

# Creamos una lista de números
numeros = [8, 15, 3, 22, 7]

# Usamos max(numeros) para obtener el valor máximo de la lista
# Luego usamos remove() para eliminar ese valor de la lista
numeros.remove(max(numeros))  # Elimina el número 22, que es el mayor

# Imprimimos la lista resultante sin el valor máximo
print(numeros)  # Salida: [8, 15, 3, 7]
