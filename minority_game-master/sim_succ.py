
from numpy import *
from minoritygame import *
import matplotlib.pyplot as plt


X = []
Y = []
N = 101
for m in range(1,10):
    x = []
    y = []
    for t in range(10):
        sim = System(T=200,N=N, m=m)
        sim.run()
        x.append(float(2**m)/float(N))
        y.append(mean(sim.SuccessRates))
    X.append(mean(x))
    Y.append(mean(y))
    print('m='+str(m))

plt.plot(X,Y,'o-')
plt.xscale('log')
plt.xlabel(r'$2^{m}/N$')
plt.ylabel(r'$success\ rate$')
plt.savefig('Success_rate.jpg')
plt.close()
