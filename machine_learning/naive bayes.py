import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

df = pd.read_csv("titanic.csv")
# quitamos los datos irrelevantes
df.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)

# aqui esta separando los datos de los que van a sobrevivir
inputs = df.drop('Survived', axis='columns')
target = df.Survived

# Ddummies hace que se combiertan en numeros variables que no lo son y los esta devolviendo a la array
dummies = pd.get_dummies(inputs.Sex)
dummies.head(3)
inputs = pd.concat([inputs, dummies], axis='columns')

# quitamos la de hombre porque al ser hombre o mujer con una columna vale ya que con dummies se han generado 2
inputs.drop(['Sex', 'male'], axis='columns', inplace=True)

#rellena los datos que estan vacios Nan con la media de los datos de age
inputs.Age = inputs.Age.fillna(inputs.Age.mean())

#una vez tengamos el dataset bien puesto empezamos con el naive bayes
#esto sirve para separar los datos en test y en train
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.25)

model = GaussianNB()

model.fit(X_train,y_train)


print(model.score(X_test,y_test))

print(model.predict(X_test))

# saca la probabilidad de 0 o 1. a veces saca por ejemplo 6.59257575e-01 3.40742425e-01 el -01 es elevado a la menos 1 seria 0.659257575e-01 0.340742425e-01
print(model.predict_proba(X_test))