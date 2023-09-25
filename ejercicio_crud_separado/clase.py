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

  def cargar_array():
    personas.clear()
    try:
        with open("./ejercicio_crud_separado/personas.json", "r") as archivo:
            diccionario = json.load(archivo)
            for d in diccionario:
                p1 = Persona(d.get("dni"),d.get("nombre"),d.get("edad"))
                personas.append(p1)
            return(personas)
    except:
        print("No hay personas guardadas")
        
  def cargar_json(array_personas):
    personas_dict = [p.to_dict() for p in array_personas]
    text_file = open("./ejercicio_crud_separado/personas.json", "w")
    json_data = json.dumps(personas_dict)
    text_file.write(json_data)
    text_file.close()
        
    