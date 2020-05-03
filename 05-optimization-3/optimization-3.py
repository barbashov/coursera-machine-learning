from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import math


def fm(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


def h(x):
    return int(fm(x))


def plotf(f, start, end):
    x = np.arange(start, end, 0.1)
    y = np.array([f(x) for x in x])
    plt.plot(x, y)


plotf(h, 1, 30)
plotf(fm, 1, 30)

res_bfgs = optimize.minimize(h, [30], method='BFGS')
res_de = optimize.differential_evolution(h, [(1, 30)])

print(res_bfgs)
print(res_de)

plt.annotate('bfgs_min', xy=(res_bfgs.x, res_bfgs.fun),
             xytext=(res_bfgs.x-5, res_bfgs.fun+2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('de_min', xy=(res_de.x, res_de.fun),
             xytext=(res_de.x, res_de.fun+2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()

with open('optimization-3.txt', 'w') as f:
    f.write("{:.2f} {:.2f}".format(res_bfgs.fun, res_de.fun))