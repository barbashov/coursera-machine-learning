from scipy import optimize
import math


def fm(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


res = optimize.differential_evolution(fm, [(1, 30)])

#print(res)

with open('optimization-2.txt', 'w') as f:
    f.write("{:.2f}".format(res.fun))