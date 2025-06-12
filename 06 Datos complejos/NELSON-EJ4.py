# Ejercicio 4: Agenda telefónica
contactos = {}
for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número telefónico: ")
    contactos[nombre] = numero

consulta = input("¿Qué contacto querés consultar? ")
print("Número:", contactos.get(consulta, "No encontrado"))
