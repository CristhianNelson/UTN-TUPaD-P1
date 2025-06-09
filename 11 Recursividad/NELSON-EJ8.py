# Ejercicio 8: Contar cuántas veces aparece un dígito en un número (sin convertir a string)
def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos
    if numero == 0:
        return 0
    else:
        # Comprobamos si el último dígito coincide y sumamos 1 si es así
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Prueba de la función
num = int(input("Número: "))
d = int(input("Dígito a contar: "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")
