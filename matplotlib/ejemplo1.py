#!/usr/bin/env python3
import pandas
import matplotlib.pyplot as plt
from scipy import stats

df = pandas.read_csv("data.csv")

x = df['Volume']
y = df['CO2']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
print(r)
plt.show()

