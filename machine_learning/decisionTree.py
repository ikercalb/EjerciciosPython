import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("datadt.csv")

# todos los datos tienen que ser numéricos.
# generamos una enumeración para la 'Nationality'
# y modificamos los valores del dataframe
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
# Lo mismo con 'Go'
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# seleccionamos las colummnas 'feature' y la 'target'
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[40, 10, 6, 1]]))

tree.plot_tree(dtree, feature_names=features)


plt.figure(figsize=(12,12))

plt.savefig('tree_high_dpi', dpi=100)

plt.show()

