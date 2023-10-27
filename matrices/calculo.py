#!/usr/bin/env python3
import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[7, 8], [9, 10], [11, 12]])
f1, c1 = array_a.shape
f2, c2 = array_b.shape
suma= np.zeros((f1,c2))

for i in range(len(array_a)):

    for j in range(len(array_b[0])):

        for k in range(len(array_b)):
            suma[i][j] = array_a[i][k]*array_b[k][j]

print(suma)
