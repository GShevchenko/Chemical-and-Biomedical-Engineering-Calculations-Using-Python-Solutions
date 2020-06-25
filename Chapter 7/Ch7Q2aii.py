import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

n = 13

year = np.linspace(1890,2010,13)
temp = np.array([13.8, 13.7, 13.7, 13.6, 13.8, 13.9, 14.0, 14.0, 14.0, 14.0, 14.2, 14.4, 14.6])

def quad(x,a,b,c):
    f = a + b*x + c*(x**2)
    return f

params = [10,20,30]

fit,_ = curve_fit(quad, year, temp, p0 = params)

yfit = quad(year, fit[0], fit[1], fit[2])

plt.plot(year,temp,'o',year,yfit)
plt.xlabel('year')
plt.ylabel('temperature ($^oC$')
plt.show() 
