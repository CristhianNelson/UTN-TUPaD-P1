# Ejercicio 2: Calcular la serie de Fibonacci hasta la posición indicada por el usuario
def fibonacci(pos):
    # Caso base: si es 0 devuelve 0, si es 1 devuelve 1
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        # Paso recursivo: suma de los dos anteriores
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Ingresamos hasta qué posición queremos mostrar la serie
n = int(input("Ingresá hasta qué posición mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(n + 1):
    print(fibonacci(i), end=" ")
