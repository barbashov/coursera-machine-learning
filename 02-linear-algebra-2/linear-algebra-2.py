import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

def eq(point, pow):
    ret = []
    for p in range(0, pow + 1):
        ret.append(point ** p)
    return ret

def solve_eqsys(points, pow):
    A = np.array([eq(p, pow) for p in points])
    B = f(points)
    return linalg.solve(A, B)

def get_y(coeffs, x):
    retval = 0
    for i in range(len(coeffs)):
        retval += coeffs[i] * (x**i)
    return coeffs, retval

def near(points, pow):
    C = solve_eqsys(points, pow)
    return lambda x: get_y(C, x)

x = np.arange(1, 15.1, 0.1)
y = f(x)

C1, Y1 = near(np.array([1, 15]), 1)(x)
C2, Y2 = near(np.array([1, 8, 15]), 2)(x)
C3, Y3 = near(np.array([1, 4, 10, 15]), 3)(x)

with open('submission-2.txt', 'w') as f:
    f.write(" ".join([str(c) for c in C3]))

plt.plot(x, y)
plt.plot(x, Y1)
plt.plot(x, Y2)
plt.plot(x, Y3)
plt.show()