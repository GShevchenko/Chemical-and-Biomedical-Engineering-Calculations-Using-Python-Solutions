import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

Temp = np.array([118.99, 120.76, 122.71, 125.48, 127.31, 130.06, 132.41, 
                 135.89, 139.02, 140.25, 145.61, 153.45, 158.03, 162.72,
                 167.67, 172.86, 177.52, 182.09               
                 ])

Heat_Cap = np.array([10.79, 10.8, 10.86, 10.93, 10.99, 10.96, 10.98, 11.03, 11.08,
                 11.1, 11.19, 11.25, 11.4, 11.61, 11.69, 11.91, 12.07, 12.32])

# Function for fragment equation:
# used in call to curve_fit below

def quad(x,a,b,c,d):
    f = a + b*x + c*(x**2) + d*(x**3)
    return f

params = [10,20,30,40]

fit,_ = curve_fit(quad, Temp, Heat_Cap, p0 = params)

yfit = quad(Temp, fit[0], fit[1], fit[2], fit[3])

plt.plot(Temp,Heat_Cap,'o',Temp,yfit)
plt.xlabel('Temperature ($^oC$)')
plt.ylabel('Heat Capacity (cal/molK)')
plt.show() 
