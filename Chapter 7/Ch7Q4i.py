import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy.linalg as nl

Temp = np.array([118.99, 120.76, 122.71, 125.48, 127.31, 130.06, 132.41, 
                 135.89, 139.02, 140.25, 145.61, 153.45, 158.03, 162.72,
                 167.67, 172.86, 177.52, 182.09               
                 ])

Heat_Cap = np.array([10.79, 10.8, 10.86, 10.93, 10.99, 10.96, 10.98, 11.03, 11.08,
                 11.1, 11.19, 11.25, 11.4, 11.61, 11.69, 11.91, 12.07, 12.32])

n = np.size(Temp)

sumTemp = np.sum(Temp)
sumHeat_Cap = np.sum(Heat_Cap)
TempHeat_Cap = np.sum(np.dot(Heat_Cap,Temp))
TempTemp = np.sum(np.dot(Temp,Temp))

A = np.array([[n, sumTemp], [sumTemp, TempTemp]])
f = np.array([sumHeat_Cap, TempHeat_Cap])
c = nl.solve(A,f)

yLR = c[0] + c[1]*Temp

plt.plot(Temp,Heat_Cap,'o',Temp,yLR)
plt.xlabel('Temp')
plt.ylabel('Heat_Cap')


#'Temp should be Heat_Cap and Heat_Cap should be he'

