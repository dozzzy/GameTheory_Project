
from numpy import *
from frame.minoritygame import *
import matplotlib.pyplot as plt



N = [51,101,251,501]
syms = ['ro-','gs-','bd-','cx-']
for i in range(len(N)):
    X = []
    Y = []
    for m in range(1,10):
        x = []
        y = []
        for t in range(10):
            sim = System(T=200,N=N[i], m=m,lp=1)
            sim.run()
            x.append(float(2**m)/float(N[i]))
            y.append(mean(sim.SuccessRates))
        X.append(mean(x))
        Y.append(mean(y))
        print('m='+str(m))
    plt.plot(X, Y, syms[i], label='N=' + str(N[i]))
plt.xscale('log')
plt.xlabel(r'$2^{m}/N$')
plt.ylabel(r'$success\ rate$')
plt.legend(loc='best')
plt.savefig('figures/Success_rate.jpg')
plt.close()
