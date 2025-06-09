# Ejercicio 4: Convertir un número decimal a binario usando recursividad
def decimal_a_binario(n):
    # Caso base: si n es 0, su binario es cadena vacía
    if n == 0:
        return ""
    else:
        # Paso recursivo: concatenamos el resto de n dividido por 2
        return decimal_a_binario(n // 2) + str(n % 2)

# Probamos la función
numero = int(input("Número decimal para convertir a binario: "))
# Si el número es 0, lo mostramos directamente
if numero == 0:
    print("0")
else:
    print(f"Binario: {decimal_a_binario(numero)}")
