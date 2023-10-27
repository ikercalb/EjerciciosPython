#!/usr/bin/env python3

import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt



df = pandas.read_csv("data.csv")

x = df[['Weight','Volume']]
y = df['CO2']


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x.Weight,x.Volume, y )


ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')

plt.show()