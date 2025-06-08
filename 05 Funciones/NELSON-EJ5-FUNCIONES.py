def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivalen a {horas:.2f} horas.")
