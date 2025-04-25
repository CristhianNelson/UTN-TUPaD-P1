"""
Programa que solicita edad al usuario y determina a qué categoría pertenece
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

contraseña = input("Ingrese una contraseña que contenga de 8 a 14 caracteres: ")

if  (8 <= len(contraseña) and len(contraseña) >= 14): 
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    