"""
Programa que solicite una nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar el mensaje de "Aprobado".
Caso contrario, deberá mostrar "Desaprobado"
Autor: Nelson, Cristhian
Fecha: 15/04/2025
"""

nota = int(input("Ingrese su nota: "))

if nota >= 6 :
    print("Aprobado")
else : 
    print("Desaprobado")