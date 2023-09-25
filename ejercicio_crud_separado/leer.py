#!/usr/bin/env python3
from clase import Persona


array_pe = []


def leer():
        array_pe = Persona.cargar_array()
        if array_pe != None:
            for p in array_pe:
                print(p)
    
