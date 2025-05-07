"""
Juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
Autor: Nelson, Cristhian
Fecha: 07/05/2025
"""

import random  # Importamos el módulo random para generar números aleatorios

# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
intentos = 0  # Inicializamos el contador de intentos

# Bucle infinito que se rompe cuando se adivina el número
while True:
    # Solicitamos al usuario que adivine el número
    intento = int(input("Adivine el número (entre 0 y 9): "))
    # Incrementamos el contador de intentos
    intentos += 1
    # Si el intento es igual al número aleatorio, salimos del bucle
    if intento == numero_aleatorio:
        # Imprimimos el número de intentos necesarios para adivinar el número
        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
        break

