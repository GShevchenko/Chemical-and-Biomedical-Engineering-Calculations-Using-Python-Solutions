import sympy

# v = (deltaP / 4mL) * (R^2 - r^2)
deltaP = 60e3 #kgm-1s-2
m = 1.8e-5 #kg/ms
L = 1 #mm
R = 0.5 #mm

# when r = R, v = 0
#integrate following 

# Q = 2pi int(vr.dr)Rr

v, deltaP, m, L, R, r, pi = sympy.symbols('v deltaP m L R r pi')
v = (deltaP / (4*m*L)) * (R**2 - r**2)
int_prod = v * r

Q = 2 * pi * sympy.integrate(int_prod, (r, 0, R))
print(Q)
