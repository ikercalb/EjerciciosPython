#!/usr/bin/env python3
import json

personas = []

class Persona:
    #esto es lo primero que se ejecuta en la case para definir la clase
  def __init__(self, dni , nombre, edad):
    self.dni = dni
    self.nombre = nombre
    self.edad = edad
    
  def to_dict(self):
    return {
      "dni": self.dni,
      "nombre": self.nombre,
      "edad": self.edad
    }

    
  def __str__(self):
    return f"DNI: {self.dni} Nombre: {self.nombre} Edad: {self.edad}"



def cargar_json(array_personas):
    personas_dict = [p.to_dict() for p in array_personas]
    text_file = open("./ejercicio_crud/personas.json", "w")
    json_data = json.dumps(personas_dict)
    text_file.write(json_data)
    text_file.close()

def cargar_array():
    try:
        with open("./ejercicio_crud/personas.json", "r") as archivo:
            diccionario = json.load(archivo)
            for d in diccionario:
                p1 = Persona(d.get("dni"),d.get("nombre"),d.get("edad"))
                personas.append(p1)
    except:
        print("No hay personas guardadas")
    
def crear():
    d = input("Introduce tu DNI: ").lower()
    n = input("Introduce tu nombre: ")
    e = input("Introduce tu edad: ")
    p1 = Persona(d,n,e)
    personas.append(p1)
    
def leer():
    for p in personas:
        print(p)

def actualizar():
    dni_b = input("Introduce el DNI de la persona que quieres borrar: ").lower()
    for p in personas:
        if dni_b == p.dni:
            nom = input("Introduce el nuevo nombre: ")
            ed = input("Introduce la nueva edad: ")
            p1 = Persona(p.dni, nom, ed)
            personas.remove(p)
            personas.append(p1)
            print("Datos de la persona actualizos.")
            break
    else:
        print("Persona no encontrada.")

def borrar():
    dni_b = input("Introduce el DNI de la persona que quieres borrar: ").lower()
    for p in personas:
        if dni_b == p.dni:
            personas.remove(p)
            print("La persona ha sido borrada.")
            break
    else:
        print("Persona no encontrada.")

        
def seleccion():
    while True:
        modo = input("¿Qué modo deseas: crear, leer, actualizar o borrar(c r u d)? o 's' para salir: ")
        
        if modo == "s":
            cargar_json(personas)
            break  
        
        match modo:
            case "c":
                print("Modo 1: Crear")
                crear()
            case "r":
                print("Modo 2: Leer")
                leer()
            case "u":
                print("Modo 3: Actualizar")
                actualizar()
                
            case "d":
                print("Modo 4: Borrar")
                borrar()
            case _:
                print("Modo no válido.")

cargar_array()
seleccion()
