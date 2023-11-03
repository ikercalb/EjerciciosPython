#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# pares de puntos utilizados para generar / entrenar el modelo
x = [1, 2, 5, 3, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 60, 80, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# generamos una función polinómica que se ajuste con un polinomio de grado dado
# a la distribución de datos de entrenamiento
model1 = numpy.poly1d(numpy.polyfit(x, y, 1))  # grado 1 (recta)
model3 = numpy.poly1d(numpy.polyfit(x, y, 3))  # grado 3
model7 = numpy.poly1d(numpy.polyfit(x, y, 7))  # grado 7

# array de puntos en X para dibujar la recta (""datos de testing"")
line = numpy.linspace(0, 25, num=1000)

# r2_score nos proporciona el coeficiente de determinación.
# indicio de cuanto se adecua el polinomio a la distribución
# de datos de test.
print("R² (x):  ", r2_score(y, model1(x)))
print("R² (x³): ", r2_score(y, model3(x)))
print("R² (x⁷): ", r2_score(y, model7(x)))

# Subplot funciona dividiendo el plot en una matriz
# los dos primeros parámetros son las dimensiones y
# el tercero el índice del subplot

plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.plot(line, model1(line), label="1st degree (x)")
plt.plot(line, model3(line), label="3rd degree (x³)")
plt.plot(line, model7(line), label="7th degree (x⁷)")
plt.legend(loc="lower right")
plt.title("Polinomial regression with NumPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")


#para decir que posicion coge en el "grid"
plt.subplot(2, 3, 4)
plt.scatter(x, y)
plt.plot(line, model1(line))
plt.title("1st degree (Linear Regression)")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 5)
plt.scatter(x, y)
plt.plot(line, model3(line))
plt.title("3rd degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 6)
plt.scatter(x, y)
plt.plot(line, model7(line))
plt.title("7th degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()