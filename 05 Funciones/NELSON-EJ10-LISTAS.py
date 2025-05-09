"""
Se solicita un programa que genere una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Autor: Cristhian Alejandro Nelson
Fecha: 09/05/2025
"""

# Creamos la lista anidada
lista_anidada = [
    15,                     # índice 0
    True,                   # índice 1
    [25.5, 57.9, 30.6],     # índice 2 (sublista)
    False                   # índice 3
]
print(lista_anidada)
