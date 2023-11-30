import numpy as np
from sklearn import linear_model
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier


#---------------------------------------------------------------------------------------------------------
# Parte del KNN
#---------------------------------------------------------------------------------------------------------

xKNN = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
yKNN = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

data = list(zip(xKNN, yKNN))
knn = KNeighborsClassifier(n_neighbors=1)
# knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, classes)

new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)






#---------------------------------------------------------------------------------------------------------
# Parte de la lineal
#---------------------------------------------------------------------------------------------------------

# pares de puntos utilizados para generar / entrenar el modelo
x_points = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y_points = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

slope, intercept, r, p, std_err = stats.linregress(x_points, y_points)

print("Pendiente (m):......................", slope)
print("Condición inicial (y0):.............", intercept)
print("Tasa de Ajuste promedio (r):........", r)
print("Coeficiente de determinación (r²):..", r ** 2)


# m = (y-y0) / (x-x0)   -->
# (y-y0) = m(x-x0)      -->
# y = m(x-x0) + y0      -->  \x0=0
# f(x) = y = mx + y0

# generamos una función con la ecuación de la recta
def func(x):
    return slope * x + intercept


# array de puntos en X para dibujar la recta (""datos de testing"")
x = np.linspace(x_points.min(), x_points.max(), 100)

# obtenemos la predicción con los ""datos de testing""
modellineal = list(map(func, x))






#---------------------------------------------------------------------------------------------------------
#Parte de la logistica
#---------------------------------------------------------------------------------------------------------


# X represents the size of a tumor in centimeters.
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88])
# Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
X = X.reshape(-1, 1)
# y represents whether the tumor is cancerous (0 for "No", 1 for "Yes").
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(np.array([3.46]).reshape(-1, 1))
print(predicted)

log_odds = logr.coef_
print(log_odds)
print(logr.intercept_)
odds = np.exp(log_odds)
print(odds)

def prob(x):
    w = logr.coef_
    b = logr.intercept_
    z = w * x + b
    return 1 / (1 + np.exp(-z))


def prob1(x):
    log_odds = logr.coef_ * x + logr.intercept_
    odds = np.exp(log_odds)
    probability = odds / (1 + odds)
    return probability


def odd1(x):
    return prob(x) / (1 - prob(x))


def odd2(x):
    w = logr.coef_
    b = logr.intercept_
    z = w * x + b
    return np.exp(z)


X = X.reshape(1, -1)
arr = np.linspace(X.min(), X.max(), 50)

model = prob1(arr)
f_mod = prob(arr)
odds1 = odd1(arr)
odds2 = odd2(arr)

print(model)
print(f_mod)
print(odds1)
print(odds2)

#-------------------------------------------------------
# Grafico de KNN
#-------------------------------------------------------
# Como se separa cada plot
#   2: cantidad de filas
#   1: cantidad de columnas
#   1: posicion en la que se pone
#   Posicion:
#       1
#       2
plt.subplot(2, 1, 1)
plt.scatter(xKNN, yKNN, c=classes)
plt.scatter(xKNN + [new_x], yKNN + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")






#-------------------------------------------------------
# Grafico de Logistica
#-------------------------------------------------------
#   3: cantidad de filas que tiene
#   2: cantidad de columnas
#   5: posicion en la que se pone
#   Posicion:
#       1   2
#       3   4
#       5   6
plt.subplot(3, 2, 5)
plt.scatter(X, y)
plt.plot(arr, model[0])
plt.plot(arr, f_mod[0])
plt.xlabel("Size of tumor")
plt.ylabel("Probability of being malignant")
plt.title('Probability')






#-------------------------------------------------------
# Grafico de lineal
#-------------------------------------------------------
#   3: cantidad de filas que tiene
#   3: cantidad de columnas que tiene
#   9: posicion en la que se pone
#   Posicion:
#       1   2   3
#       4   5   6
#       7   8   9
plt.subplot(3, 3, 9)
# dibujamos por una lado los puntos
plt.scatter(x_points, y_points)

# y por otro lado la recta de previsión
plt.plot(x, modellineal)

# indicamos los ejes y el título del gráfico
plt.title("Linear regression with SciPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# desplegamos el gráfico
plt.show()
