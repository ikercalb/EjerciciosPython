#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# pandas lee el CSV y devuelve un dataframe
df = pd.read_csv("data.csv")

# seleccionamos peso y volumen como variables independientes
# y CO2 como variable dependiente de las otras dos.
X = df[['Weight', 'Volume']]
y = df['CO2']

# generamos un objeto generico de regresión lineal
# y le decimos que se ajuste a los datos escogidos
regr = linear_model.LinearRegression()
regr.fit(X, y)

# generamos""datos de testing"" para poder mostrar la recta en 3d
x_line = np.linspace(X.Weight.min(), X.Weight.max(), 100)
y_line = np.linspace(X.Volume.min(), X.Volume.max(), 100)


# juntamos los datos de x e y a pares y se los pasamos al modelo para que genere la predicción
z_vals = regr.predict(np.concatenate((x_line.reshape(-1, 1), y_line.reshape(-1, 1)), axis=1))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X.Weight, X.Volume, y)
ax.plot(x_line, y_line, z_vals)
ax.set(title="Multiple Regression with SciKit Learn", xlabel='Weight', ylabel='Volume', zlabel='CO2')

plt.show()