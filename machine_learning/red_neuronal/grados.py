import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40,-10,0,8,15,22,38], dtype=float)
fahrenheit = np.array([-40,14,32,46,59,72,100], dtype=float)  

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Entrenando")
historial = modelo.fit(celsius, fahrenheit, epochs=10000000, verbose=False)
print("Entrenado")


print("prediccion")
valor = float(input("introduce el valor de grados para pasar a fahrenheid"))
resultado= modelo.predict([valor])
print("el resultado es "+str(resultado)+" fahrenheid")