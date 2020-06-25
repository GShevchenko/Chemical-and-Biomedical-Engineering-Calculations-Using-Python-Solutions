import numpy as np
import gaussSeidel as gS
np.set_printoptions(precision=4)

k1 = 10000.0
k2 = 5000.0
k3 = 8000.0
k4 = 3500.0
k5 = 4500.0

A = np.array([[k1+k3, -k3, 0.0],
              [(-k3), (k2+k3+k4+k5), (-k4-k5)],
              [0.0, (-k4-k5), (k4+k5)],
              ])
f = np.array([500.0, 1000.0, 1000.0])        
x = np.array([20.0, 20.0, 20.0])
sol = gS.gaussSeidel(A,f,x,omega=1.1)
print(sol)

    