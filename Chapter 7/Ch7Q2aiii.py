import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

n = 13

year = np.linspace(1890,2010,13)
temp = np.array([13.8, 13.7, 13.7, 13.6, 13.8, 13.9, 14.0, 14.0, 14.0, 14.0, 14.2, 14.4, 14.6])

def expen(x,a,b):
    f = a * np.exp(b*x)
    return f

params = [0,0]

fit,_ = curve_fit(expen, year, temp, p0 = params)

yfit = expen(year, fit[0], fit[1])
print(yfit)

plt.plot(year,temp,'o',year,yfit,'--')
plt.xlabel('year')
plt.ylabel('temperature ($^oC$')
