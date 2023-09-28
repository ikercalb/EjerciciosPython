#!/usr/bin/env python3
from clase import Persona


array_pe = []


def crear():
    array_pe = Persona.cargar_array()
    d = input("Introduce tu DNI: ")
    while True:
        if len(d) == 9 and d[0:8].isnumeric() == True:
            n = input("Introduce tu nombre: ")
            break
        else:
            print
            d = input("Introduce DNI correcto: ").lower()
    
    e = input("Introduce tu edad: ")
    while True:
        if e.isnumeric():
            break
        else:
            e = input("Introduce edad correcta: ")
   
    p1 = Persona(d,n,e)
    if array_pe != None:
        array_pe.append(p1)
    else:
        array_pe=[p1]
        
    Persona.cargar_json(array_pe)


