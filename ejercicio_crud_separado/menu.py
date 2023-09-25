#!/usr/bin/env python3  
import leer
import crear
import actualizar
import borrar

while True:
    modo = input("¿Qué modo deseas: crear, leer, actualizar o borrar(c r u d)? o 's' para salir: ")
        
    if modo == "s":
        break  
        
    match modo:
        case "c":
            print("Modo 1: Crear")
            crear.crear()
        case "r":
            print("Modo 2: Leer")
            leer.leer()
        case "u":
            print("Modo 3: Actualizar")
            actualizar.actualizar()
        case "d":
            print("Modo 4: Borrar")
            borrar.borrar()
                
        case _:
            print("Modo no válido.")
                

