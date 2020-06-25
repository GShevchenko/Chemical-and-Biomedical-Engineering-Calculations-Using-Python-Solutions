import numpy as np
import bobcatSolve as bS
import numpy.linalg as nl

A = np.array([[4.0, -1.0, 1.0],
              [2.0, 5.0, 2.0],
              [1.0, 2.0, 4.0],
              ])

f = np.array([8.0, 3.0, 11.0])
print(nl.solve(A,f))
A,f = bS.bobcatLU(A,f)
x = bS.bobcatBS(A,f)
print(x)