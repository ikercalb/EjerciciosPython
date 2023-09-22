#!/usr/bin/env python3
altura = input("introduce estatura en metros")
peso = input("introduce peso en kilos")
 
imc = round(float(peso)/float(altura)**2,2)
print(imc)