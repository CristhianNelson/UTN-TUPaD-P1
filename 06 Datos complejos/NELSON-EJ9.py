# Ejercicio 9: Agenda con tuplas como claves
agenda = {}
dia = input("Día del evento: ")
hora = input("Hora del evento: ")
evento = input("Descripción del evento: ")
agenda[(dia, hora)] = evento

consulta_dia = input("Consultar evento - Día: ")
consulta_hora = input("Consultar evento - Hora: ")

print("Evento programado:", agenda.get((consulta_dia, consulta_hora), "No hay actividad"))