#!/usr/bin/env python3
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
#printea si encientra sino te dice que no encientra la duvisa 
print(monedas.get(moneda.title(), "La divisa no está."))