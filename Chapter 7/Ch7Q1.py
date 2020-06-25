import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

n = 12
month = np.linspace(0,12,num=n) # month
temp = np.array([10.9, 13.4, 16.8, 18.1, 18, 15.8, 12.8, 8.8, 7, 5.9, 6.4, 8.6])

def breakup(x,a,b,p):
    f = a * np.sin( (np.pi * x) / p) + b
    return f

params = [0, 10, 20]

fit,_ = curve_fit(breakup, month, temp, p0 = params)

print(fit)

# plot data as points and fit line

fitYield = breakup(month,fit[0], fit[1], fit[2])

bar_width = 0.2
index = np.arange(len(temp))
plt.bar(index,temp,bar_width)
plt.bar(index+bar_width,fitYield,bar_width, color='r')
plt.xlabel('Month Index')
plt.ylabel('Temperature')

 