#!/usr/bin/env python3

import numpy as np

# con greater, greater equal, less y less equal  se comparan las arrays y se dice si es mayor, mayor o igual, menor y menor o igual

a = np.array([1, 2, 5, 5])
b = np.array([2, 3, 5, 6])

print(np.greater(b, a))
print(np.greater_equal(a, b))
print(np.less(a, b))
print(np.less_equal(a, b))
