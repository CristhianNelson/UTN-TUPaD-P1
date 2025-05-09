"""
Programa que permita ingresar sólo números pares. Si el número ingresado es par, mostrar mensaje "Ha ingresado un número par".
Caso contrario, mostrar mensaje "Por favor, ingrese un número par"
Autor: Nelson, Cristhian
Fecha:15/04/2024    
"""

# Solicita un número al usuario
numero = int(input("Ingrese un número par: "))

# Verifica si el número es par usando el módulo (%)
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
