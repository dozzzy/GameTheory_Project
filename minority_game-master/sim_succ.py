from pylab import *
from numpy import *
from minoritygame import *

fig = figure(1,figsize=(6,4))

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

plot(X,Y,'o-')
xscale('log')
xlabel(r'$2^{m}/N$')
ylabel(r'$success\ rate$')
savefig('Success_rate.jpg')
close(fig)
