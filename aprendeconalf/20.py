#!/usr/bin/env python3
nombre = input("nombre ")
edad = input("edad ")
direccion = input("direccion ")
telefono = input("telefono ")

persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])    