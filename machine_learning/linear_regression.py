#!/usr/bin/env python3
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# datos de la regresion
x_array = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y_array = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# devulve los datos de la regresion lineal
slope, intercept, r, p, std_err = stats.linregress(x_array, y_array)

print("Pendiente (m):......................", slope)
print("Condición inicial (y0):.............", intercept)
print("Tasa de Ajuste promedio (r):........", r)
print("Coeficiente de determinación (r²):..", r ** 2)


# generamos una función con la ecuación de la recta
def func(valor_x):
    return slope * valor_x + intercept


# Array de puntos en X para dibujar la recta (""datos de testing"")
# El número 100 es la cantidad de punto que saca en la línea. Normalmente, poner la el doble o el triple
# de la cantidad de valores o sacar muchos en este caso 100
x = np.linspace(x_array.min(), x_array.max(), 100)

# obtenemos la predicción con los""datos de testing""
# ejecuta la funcion con la array de la recta
model = list(map(func, x))

# dibujamos, por un lado, los puntos
plt.scatter(x_array, y_array)

# y, por otro lado, la recta de previsión. La x es la array de puntos de la recta y el modelo es prediccion de datos
plt.plot(x, model)

# indicamos los ejes y el título del gráfico
plt.title("Linear regression with SciPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# obtenemos la predicción con los""datos de testing""
model = list(map(func, x))

# muestra el gráfico
plt.show()
