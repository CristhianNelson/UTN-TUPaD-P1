"""
Programa que tome la lista de numeros aleatorios, calcule su moda, su mediana y su media y las compare
para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

# Solicita una contraseña
contraseña = input("Ingrese una contraseña: ")

# Verifica la longitud
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
