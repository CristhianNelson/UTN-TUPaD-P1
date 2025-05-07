"""
Programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. 
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

suma = 0  # Inicializamos la suma

# Iteramos 100 veces para solicitar números al usuario
for _ in range(100):
    # Solicitamos al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero: "))
    # Sumamos el número a la suma total
    suma += numero

# Calculamos la media de los números
media = suma / 100
# Imprimimos la media de los números
print("La media de los números es", media)
