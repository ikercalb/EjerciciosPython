#!/usr/bin/env python3
import pandas
import matplotlib.pyplot as plt
import numpy

df = pandas.read_csv("data.csv")

x = df['Volume']
y = df['CO2']

print(x)
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(900, 2500, 100)


plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()