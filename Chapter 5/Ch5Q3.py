import sympy 

Cd = 2.0
Fd = 2.0
A = 2.0
p = 2.0
V = sympy.symbols('V')

#Cd, A, p, Fd, V = sympy.symbols('Cd A p Fd V')
f = sympy.sqrt( (2.0 * Fd) / (Cd * A * p) ) - V

print(sympy.solve(f,V))