#!/usr/bin/env python3
class Person:
    #esto es lo primero que se ejecuta en la case para definir la clase
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def __str__(self):
    return f"{self.name} {self.age}"

  def mi_fun(self):
    print("mi nombre es "+self.name+" y tengo "+self.age)


nombre = input("nombre")
edad = input("edad")

p1 = Person(nombre, edad)

print(p1.name)
print(p1.age)

print(p1)
p1.mi_fun()