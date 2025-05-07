"""
Programa que calcula la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

# Solicitamos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))
suma = 0  # Inicializamos la suma

# Iteramos desde 0 hasta el número (inclusive)
for i in range(numero + 1):
    # Sumamos el número actual a la suma total
    suma += i

# Imprimimos la suma de los números desde 0 hasta el número dado
print("La suma de los números desde 0 hasta", numero, "es", suma)
