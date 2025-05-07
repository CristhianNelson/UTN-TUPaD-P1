"""
Programa que permite al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

pares = 0  # Inicializamos el contador de números pares
impares = 0  # Inicializamos el contador de números impares
positivos = 0  # Inicializamos el contador de números positivos
negativos = 0  # Inicializamos el contador de números negativos

# Iteramos 100 veces para solicitar números al usuario
for _ in range(100):
    # Solicitamos al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero: "))
    # Si el número es par, incrementamos el contador de pares
    if numero % 2 == 0:
        pares += 1
    # Si no, incrementamos el contador de impares
    else:
        impares += 1
    # Si el número es positivo, incrementamos el contador de positivos
    if numero > 0:
        positivos += 1
    # Si el número es negativo, incrementamos el contador de negativos
    elif numero < 0:
        negativos += 1

# Imprimimos la cantidad de números pares, impares, positivos y negativos
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)

