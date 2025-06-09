# Ejercicio 1: Calcular el factorial de un número y mostrar los factoriales desde 1 hasta el número ingresado
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Paso recursivo: n * factorial(n - 1)
        return n * factorial(n - 1)

# Pedimos al usuario un número
num = int(input("Ingresá un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")
