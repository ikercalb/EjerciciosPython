#!/usr/bin/env python3
from clase import Persona


array_pe = []


def borrar():
    array_pe = Persona.cargar_array()
    if array_pe != None:
        dni_b = input("Introduce el DNI de la persona que quieres borrar: ").lower()
        for p in array_pe:
            if dni_b == p.dni:
                array_pe.remove(p)
                print("La persona ha sido borrada.")
                break
        else:
            print("Persona no encontrada.")
            
        Persona.cargar_json(array_pe)



