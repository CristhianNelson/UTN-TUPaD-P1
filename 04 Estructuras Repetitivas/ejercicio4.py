"""
Programa que permite al usuario ingresar números enteros y sumarlos en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

suma = 0  # Inicializamos la suma

# Bucle infinito que se rompe cuando se ingresa 0
while True:
    # Solicitamos al usuario que ingrese un número
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    # Si el número es 0, salimos del bucle
    if numero == 0:
        break
    # Sumamos el número a la suma total
    suma += numero

# Imprimimos la suma total
print("La suma total es", suma)
