# F(s) = s + 1 / s^2 (s+2)
import sympy

s = sympy.symbols('s')
f = (s+1) / ( (s**2)*(s+2) )

print(sympy.apart(f))