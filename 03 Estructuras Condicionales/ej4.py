"""
Programa que solicita edad al usuario y determina a qué categoría pertenece
Autor: Nelson, Cristhian
Fecha: 25/04/2025
"""

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es niño/a")
elif 12 <= edad < 18:
    print("Es adolescente")
elif 18 <= edad < 30:
    print("Es adulto/a joven")
elif edad >= 30:
    print("Es adulto/a mayor")