#!/usr/bin/env python3
loteria = []
for i in range(6):
    loteria.append(int(input("Introduce un número ganador: ")))
loteria.sort()
print(loteria)