# Ejercicio 6: Sumar los dígitos de un número de forma recursiva (sin convertirlo a string)
def suma_digitos(n):
    # Caso base: si el número es menor a 10, lo devolvemos directamente
    if n < 10:
        return n
    else:
        # Paso recursivo: sumamos el último dígito con el resto del número
        return (n % 10) + suma_digitos(n // 10)

# Prueba de la función
numero = int(input("Número para sumar sus dígitos: "))
print(f"Suma de los dígitos: {suma_digitos(numero)}")
