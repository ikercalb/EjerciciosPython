#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#la libreria sklearn necesita el reshape por que opera con matrices
x = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#creamos un objeto generico de regresion logistica y lo ajustamos a los valores de x e y
logr = linear_model.LogisticRegression().fit(x, y)

#crea un arreglo de numero entre el maximo de x y el minimo
x_line = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)

#crea el modelo predictivo usando el arreglo de numeros del linspace
y_prob = logr.predict_proba(x_line)[:, 1]

#para sacar la linea necesita el linspace y el modelo predictivo
plt.plot(x_line, y_prob)

plt.scatter(x, y)

plt.show()
