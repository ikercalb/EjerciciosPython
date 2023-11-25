import pandas as pd

ds1 = pd.read_csv("../titanic.csv")
ds2 = pd.read_csv("../titanic.csv")
ds3 = pd.read_csv("../titanic.csv")
ds4 = pd.read_csv("../titanic.csv")
ds5 = pd.read_csv("../titanic_mod.csv")

# los atributos de el dataset es
# PassengerId,Name,Pclass,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked,Survived

# printa las primeras líneas del array y si ponemos un número salen las que se pone
ds1.head()

# dropea las columnas especificadas, axis es para decir lo que quieres borrar en este caso columnas,
# inplace es para cambiar el dataset en vez de crear una 'copia' y modificar esa
ds2.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)


# sirve para separar las variables categoricas como en este caso el sexo
# pondría dos variables female y male en este caso poniendo true o false dependiendo de cada valor
dummies = pd.get_dummies(ds1.Sex)

# esto es para cambiar valores a datos concretos
d = {'male': 0, 'female': 1}
ds3['Sex'] = ds3['Sex'].map(d)

#----huecos vacios----

media = int(ds5['Age'].mean().round())
ds5['Age'] = ds5['Age'].fillna(media)

print(ds5['Age'])
