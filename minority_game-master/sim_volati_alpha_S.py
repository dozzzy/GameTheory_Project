import matplotlib.pyplot as plt
from numpy import *
from minoritygame import *


N = 101
syms = ['ro-','gs-','bd-']
s = [2, 4, 6]
for i in range(len(s)):
    Y = []
    X = []
    for m in range(1,15):
        x = []
        y = []
        for t in range(10):
            sim = System(T=200,N=N, m=m,s=s[i])
            sim.run()
            x.append(float(2**m)/float(N))
            y.append(var(sim.A)/float(N))
        X.append(mean(x))
        Y.append(mean(y))
        print('m='+str(m))
    plt.plot(X,Y,syms[i],label='s='+str(s[i]))
    print('s='+str(s[i]))

plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$2^{m}/N$')
plt.ylabel(r'$\sigma^2/N$')
plt.legend(loc='best')
plt.savefig('Var_alpha_multiS.jpg')