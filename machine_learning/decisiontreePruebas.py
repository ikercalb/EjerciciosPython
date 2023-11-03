import pandas

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
data = pandas.read_csv('diabetes.csv')

print(data)

features = ['Glucose','Insulin','BMI','DiabetesPedigreeFunction','Age']

X = data[features]
y = data['Outcome']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features,fontsize=6)

plt.show()
