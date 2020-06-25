import sympy
import numpy as np

# v = (deltaP / 4mL) * (R^2 - r^2)
deltaP = 60e3 #kgm-1s-2
m = 1.8e-5 #kg/ms
L = 1e-3 #mm
R = 0.5e-3 #mm

# when r = R, v = 0
#integrate following 

# Q = 2pi int(vr.dr)Rr
v, r = sympy.symbols('v r')

v = (deltaP / (4*m*L)) * (R**2 - r**2)
int_prod = v * r

Q = (2 * np.pi * sympy.integrate(int_prod, (r, 0, R))).evalf(5)
print(Q, 'm3/s')

print((Q*3600), 'm3/h')