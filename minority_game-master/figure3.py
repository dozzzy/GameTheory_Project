from pylab import *
from numpy import *
from minoritygame import *
import math
import matplotlib.pyplot as plt
# figure3
T = 100
s = 2
m = 0
N = [51]


for nn in N:

    m=int(math.log2(nn*100))
    x = []
    y = []
    print('N m',N,m)
    for mm in range(1,m+2):

        figure2 = [[0 for i in range(2)] for j in range(2 ** mm)]

        for times in range(100):
            sim = System(T=T,N=nn, m=mm,s=s)
            sim.run()
            tempf=sim.figure2
            for j in range(2**mm):
                figure2[j][0]=figure2[j][0]+tempf[j][0]
                figure2[j][1]=figure2[j][1]+tempf[j][1]
        print('mm',mm)
        print(figure2)

        sum=0
        for j in range(2**mm):
            sum=sum+(figure2[j][0]-figure2[j][1])**2
        y_point=(sum/(2**mm))/nn
        x.append((2**mm)/nn)
        y.append(y_point)
    plt.plot(x, y, color='red', label=str(nn))
plt.show()



