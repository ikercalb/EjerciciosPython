#!/usr/bin/env python3
from clase import Persona


array_pe = []


def actualizar():
    array_pe = Persona.cargar_array()
    if array_pe != None:
        dni_b = input("Introduce el DNI de la persona que quieres borrar: ").lower()
        for p in array_pe:
            if dni_b == p.dni:
                nom = input("Introduce el nuevo nombre: ")
                ed = input("Introduce la nueva edad: ")
                p1 = Persona(p.dni, nom, ed)
                array_pe.remove(p)
                array_pe.append(p1)
                Persona.cargar_json(array_pe)
                print("Datos de la persona actualizos.")
                break
        else:
            print("Persona no encontrada.")



