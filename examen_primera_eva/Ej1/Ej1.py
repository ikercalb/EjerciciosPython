import numpy as np
import matplotlib.pyplot as plt

# IMPORTAR LIBRERÍAS NECESARIAS AQUÍ ######################
from sklearn.metrics import r2_score
###########################################################

X = np.arange(0, 20, 0.2)
y = np.cos(X)

# INSERTAR CÓDIGO AQUÍ ####################################

model1 = np.poly1d(np.polyfit(X, y, 1))  # grado i
score = r2_score(y, model1(X))
i = 1

while score > 0.9:
    model1 = np.poly1d(np.polyfit(X, y, i))  # grado i
    score = r2_score(y, model1(X))
    print(score)
    i = i + 1
    print("hola")
###########################################################

plt.show()
