from frame.minoritygame import *
import matplotlib.pyplot as plt
N = [51,101,251,501]
syms = ['x','v','s','p','*']
cValue = ['r','y','g','b','r','y','g','b','r']
s = 2
for i in range(len(N)):
    Y = []
    X = []
    for m in range(1,15):
        x = []
        y = []
        for t in range(10):
            sim = System(T=500,N=N[i], m=m,s=s,lp=1)
            sim.run()
            x.append(float(2**m)/float(N[i]))
            y.append(var(sim.A2)/float(N[i]))
        X.append(mean(x))
        Y.append(mean(y))
        print('m='+str(m))
    plt.scatter(X,Y,c=cValue[i],marker=syms[i],label='N='+str(N[i]))
    print('N='+str(N[i]))
plt.hlines(1,1/1001,2**15/51, colors = "c", linestyles = "dashed" , label='random')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$2^{m}/N$')
plt.ylabel(r'$\sigma^2/N$')
plt.legend(loc='best')
plt.savefig('figures/Var_alpha.jpg')
plt.show()


