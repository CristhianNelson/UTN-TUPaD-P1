"""
Programa un programa que solicite una frase o palabra al usuario. Si el string termina con vocal, 
colocar signo de exclamación al final e imprimir.  Caso contrario, imprimir en pantalla el string como está
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

entrada = input("Ingrese una frase o palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if entrada and entrada[-1] in vocales:
    print(entrada + "!")
else:
    print(entrada)
