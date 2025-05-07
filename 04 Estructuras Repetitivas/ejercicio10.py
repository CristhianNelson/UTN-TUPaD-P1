"""
Programa que invierte el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))
numero_invertido = 0  # Inicializamos el número invertido

# Mientras el número sea mayor que 0
while numero > 0:
    # Obtenemos el último dígito del número
    digito = numero % 10
    # Agregamos el dígito al número invertido
    numero_invertido = numero_invertido * 10 + digito
    # Eliminamos el último dígito del número
    numero //= 10

# Imprimimos el número invertido
print("El número invertido es", numero_invertido)
