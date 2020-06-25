import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

Female = np.array([49.1, 74.0, 95.1, 109.4, 126.6, 151.2, 159.8, 162.5, 163.1])
Male = np.array([49.8, 75.8, 96.1, 110.0, 127.3, 149.1, 163.2, 172.9, 176.1])
Month = np.array([0, 12, 36, 60, 96, 144, 168, 192, 216])


def FemaleFit(t,a,b,c):
    h = a / (1 + (b*np.exp(-c*t)))
    return h

params = [0,1,1]

fit1,_ = curve_fit(FemaleFit, Month, Female, p0 = params)

yfit1 = FemaleFit(Month, fit1[0], fit1[1], fit1[2])
print(f'Optimal Values: a = {fit1[0]}, b = {fit1[1]}, c = {fit1[2]}')

plt.plot(Month,Female,'o',Month,yfit1)
plt.xlabel('Temperature ($^oC$)')
plt.ylabel('Heat Capacity (cal/molK)')
plt.show() 
