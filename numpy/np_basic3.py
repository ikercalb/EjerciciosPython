#!/usr/bin/env python3

import numpy as np

# con isposinf y isneginf compruebas cada valor del array si es infinuito negativo o positivo

a = np.array([1, 0, np.nan, np.inf])

print(np.isposinf(a))

print(np.isneginf(a))
