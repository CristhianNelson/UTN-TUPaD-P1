"""
Programa que suma todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

# Solicitamos al usuario que ingrese dos valores
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0  # Inicializamos la suma

# Iteramos desde valor1 + 1 hasta valor2 - 1
for i in range(valor1 + 1, valor2):
    # Sumamos el número actual a la suma total
    suma += i

# Imprimimos la suma de los números entre los dos valores
print("La suma de los números entre", valor1, "y", valor2, "es", suma)
