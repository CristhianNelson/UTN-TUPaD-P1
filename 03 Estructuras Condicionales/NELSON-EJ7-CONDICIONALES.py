"""
Programa un programa que solicite una frase o palabra al usuario. Si el string termina con vocal, 
colocar signo de exclamación al final e imprimir.  Caso contrario, imprimir en pantalla el string como está
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

# Solicita una frase o palabra
texto = input("Ingrese una frase o palabra: ")

# Verifica si termina en vocal
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)
