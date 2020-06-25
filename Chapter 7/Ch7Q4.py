import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


Strain = np.array([1.5, 2.0, 3.2, 6.5, 11.5, 16.0, 25.0, 50.0, 100.0])
Shear = np.array([12.5, 16.0, 25.2, 40.0, 62.0, 80.5, 120.0, 240.0, 475.0])

# Function for fragment equation:
# used in call to curve_fit below

def Newtonian(x, a):
    f = a * x
    return f

params1 = [1.0]
    
fit1,_ = curve_fit(Newtonian, Strain, Shear, p0 = params1)
print(f'For the Newtonian fit, the optimal value for m is: {fit1[0]}')

yfit1 = Newtonian(Strain, fit1[0])

def PowerLaw(x,a,n):
    P = a*(x**n)
    return P

params2 = [1.0,1.0]

fit2,_ = curve_fit(PowerLaw, Strain, Shear, p0 = params2)
print(f'For the Power Law fit, the optimal values for k and n respectively are: {fit2[0]} and {fit2[1]}')

yfit2 = PowerLaw(Strain, fit2[0], fit2[1])

plt.subplot(121)
plt.plot(Strain, Shear, 'o', Strain, yfit1)
plt.xlabel('Strain Rate (1/s)')
plt.ylabel('Shear Stress (dynes/cm$^2$)')
plt.subplot(122)
plt.plot(Strain, Shear, 'o', Strain, yfit2)
plt.xlabel('Strain Rate (1/s)')
plt.ylabel('Shear Stress (dynes/cm$^2$)')