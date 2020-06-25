import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

Area = np.array([5.9, 45, 110, 320, 529, 1386, 3324, 4260, 24520])
Species = np.array([370.0, 640.0, 680.0, 640.0, 1060.0, 1200.0, 1400.0, 1450.0, 2525.0])


# Function for fragment equation:
# used in call to curve_fit below

def quad(A,c,z):
    f = c * (A**z)
    return f

params = [10,0.3]

fit,_ = curve_fit(quad, Area, Species, p0 = params)
print(fit)

yfit = quad(Area, fit[0], fit[1])

plt.semilogx(Area,Species,'o',Area,yfit)
plt.xlabel('Area (mi$^2$)')
plt.ylabel('Species')
plt.show() 
