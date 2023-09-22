#!/usr/bin/env python3
lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobada = []
for asignatura in lista:
    nota = int(input("introduce la nota de "+asignatura+": "))
    if nota >= 5:
        aprobada.append(asignatura)
        


print(aprobada)