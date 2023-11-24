from sklearn import datasets
import keras as kr
import numpy as np

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
Y = iris.target
# Asignar nuevos valores a las clases
Y[Y == 0] = -1
Y[Y == 1] = 0
Y[Y == 2] = 1


lr = 0.01           # learning rate
nn = [2, 16, 16, 1]  # número de neuronas por capa.

# Creamos el objeto que contendrá a nuestra red neuronal, como
# secuencia de capas.
model = kr.Sequential()

# Añadimos la capa 1 fully connected
l1 = model.add(kr.layers.Dense(nn[1], activation='tanh'))

# Añadimos la capa 2
l2 = model.add(kr.layers.Dense(nn[2], activation='tanh'))

# Añadimos la capa 3
l3 = model.add(kr.layers.Dense(nn[3], activation='tanh'))

# Compilamos el modelo, definiendo la función de coste y el optimizador.
model.compile(loss='mse', optimizer=kr.optimizers.SGD(lr=0.05), metrics=['acc'])

# Y entrenamos al modelo. Los callbacks
model.fit(X, Y, epochs=100)


nuevos_datos = np.array([[1.4, 0.2],
                         [4.3, 1.3],
                         [6.0, 2.5]])


# Realiza la predicción
predicciones = model.predict(nuevos_datos)

# Las predicciones son un array con las salidas para cada conjunto de datos de entrada
print("Predicciones:")
print(predicciones)

for preds in predicciones:
    if -1.0 <= preds <= -0.333:
       print("Tu planta es setosa con el valor de: " + str(preds))
    elif -0.333 <= preds <= 0.333:
       print("Tu planta es versicolor con el valor de: " + str(preds))
    elif 0.333 <= preds <= 1.0:
       print("Tu planta es virginica con el valor de: " + str(preds))