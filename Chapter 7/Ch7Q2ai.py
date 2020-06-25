import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy.linalg as nl

n = 13

year = np.linspace(1890,2010,13)
temp = np.array([13.8, 13.7, 13.7, 13.6, 13.8, 13.9, 14.0, 14.0, 14.0, 14.0, 14.2, 14.4, 14.6])

sumYear = np.sum(year)
sumTemp = np.sum(temp)
YearTemp = np.sum(np.dot(temp,year))
YearYear = np.sum(np.dot(year,year))

A = np.array([[n, sumYear], [sumYear, YearYear]])
f = np.array([sumTemp, YearTemp])
c = nl.solve(A,f)

yLR = c[0] + c[1]*year

plt.plot(year,temp,'o',year,yLR)
plt.xlabel('year')
plt.ylabel('temp')

