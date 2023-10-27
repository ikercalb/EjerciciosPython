#!/usr/bin/env python3

import numpy as np

# All te dice si hay algun valor que valga 0 en la array

x = np.array([1, 2, 3, 4, 5])

print(np.all(x))

x = np.array([0, 1, 2, 3, 4, 5])


print(np.all(x))
