#!/usr/bin/env python3
numero = int(input("introduce un numero"))


for i in range(numero):
    z = 1
    for b in range(i+1):
        print(z, end="")
        z=z+2
    print("")