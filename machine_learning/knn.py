import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()

x = iris.data[:, [2]].flatten()
y = iris.data[:, [3]].flatten()
classes = iris.target

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(data, classes)

new_x = 2.5
new_y = 0.8
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)

result = np.append(x,new_x)
plt.scatter(np.append(x,new_x), np.append(y,new_y), c=np.append(classes,prediction[0]))

plt.show()


#parte del indio aplicado a w3schools
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(len(X_train))
print(len(X_test))

knn_p = KNeighborsClassifier(n_neighbors=5)
knn_p.fit(X_train.reshape(-1,1), y_train.reshape(-1,1))
knn_p.score(X_test, y_test)
