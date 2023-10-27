#!/usr/bin/env python3

import numpy as np

# devuelve si la array tiene valor o no solo con numeros

x = np.array([0, 0, 0, 0])
print(np.any(x))

x = np.array([1, 0, 0, 0])
print(np.any(x))
