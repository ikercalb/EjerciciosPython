#!/usr/bin/env python3
from clase import Persona


array_pe = []


def crear():
    array_pe = Persona.cargar_array()
    d = input("Introduce tu DNI: ").lower()
    n = input("Introduce tu nombre: ")
    e = input("Introduce tu edad: ")
    p1 = Persona(d,n,e)
    if array_pe != None:
        array_pe.append(p1)
    else:
        array_pe=[p1]
        
    Persona.cargar_json(array_pe)



