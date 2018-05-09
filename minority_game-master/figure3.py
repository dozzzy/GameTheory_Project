from pylab import *
from numpy import *
from minoritygame import *
import math
import matplotlib.pyplot as plt
# figure3
T = 5000
s = 2
m = 0
N = [51]

for nn in N:

    m=int(math.log2(nn*100))
    x = []
    y = []
    print('N m',nn,m)
    for mm in range(1,m+1):

        figure3 = [[0 for i in range(2)] for j in range(2 ** mm)]

        #for times in range(2**mm):
        sim = System(T=T,N=nn, m=mm,s=s)
        sim.run()
        #tempf=sim.figure3
        figure3=sim.figure3
            #for j in range(2**mm):
             #   figure3[j][0]=figure3[j][0]+tempf[j][0]
              #  figure3[j][1]=figure3[j][1]+tempf[j][1]

        print('mm',mm)
        print(figure3)
        sum=0
        for j in range(2**mm):
            avg=((figure3[j][0]-figure3[j][1])/(50))**2
            sum=sum+avg
        y_point=(sum/(2**mm))/nn
        x.append((2**mm)/nn)
        y.append(y_point)
        print(y_point)
    plt.scatter(x, y)
plt.xscale('log')
plt.show()



