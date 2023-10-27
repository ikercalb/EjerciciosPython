#!/usr/bin/env python3
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pandas.read_csv("data.csv")

x = df[['Weight']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)

plt.scatter(x, y)

plt.show()
