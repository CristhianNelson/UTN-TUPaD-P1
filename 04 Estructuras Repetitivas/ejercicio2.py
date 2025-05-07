"""
Programa que solicita al usuario ingresar un número entero y determinar su cantidad de dígitos
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))
contador = 0  # Inicializamos un contador para los dígitos

# Mientras el número sea diferente de 0
while numero != 0:
    # Eliminamos el último dígito del número
    numero //= 10
    # Incrementamos el contador de dígitos
    contador += 1

# Imprimimos la cantidad de dígitos
print("El número tiene", contador, "dígitos.")
