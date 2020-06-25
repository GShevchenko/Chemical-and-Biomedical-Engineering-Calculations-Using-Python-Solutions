# f(x,y) = x^2/1 - y^2/2 
# -1 <= x <= 1 and -1 <= y <= 1

import sympy
x,y = sympy.symbols('x y')
f =0.4+  x**2/1.0 - y**2/2.0
sympy.plotting.plot3d(f,(x,-1.0,1),(y,-1.0,1.0))

df2dx2 = sympy.diff(f,x,x)
df2dy2 = sympy.diff(f,y,y)

Cxy = sympy.Abs(df2dx2) + sympy.Abs(df2dy2)
print(Cxy)