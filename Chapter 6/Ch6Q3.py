import numpy as np
import gaussSeidel as gS
np.set_printoptions(precision=4)

A = np.array([[30.0, -20.0, 0.0],
              [10.0, -30.0, 20.0],
              [0.0, 10.0, -30.0],
              ])
f = np.array([200.0, 0.0, 0.0])        
x = np.array([20.0, 20.0, 20.0])
sol = gS.gaussSeidel(A,f,x,omega=1.15)
print(sol)

    