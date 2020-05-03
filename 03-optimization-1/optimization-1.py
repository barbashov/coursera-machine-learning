from scipy import optimize
import math


def fm(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


res2 = optimize.minimize(fm, [2], method='BFGS')
res30 = optimize.minimize(fm, [30], method='BFGS')

#print(res30)

with open('optimization-1.txt', 'w') as f:
    f.write("{:.2f} {:.2f}".format(res2.fun, res30.fun))