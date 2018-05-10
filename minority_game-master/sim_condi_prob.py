# 2
from pylab import *
from numpy import *
from minoritygame import *
import matplotlib.pyplot as plt
# figure2-1 symetric
T = 100
s = 2
m = 4
N = 101
figure2=[[0 for i in range(2)]for j in range(2**m)]

for i in range(500):
    sim = System(T=T,N=N, m=m,s=s,lp=1)
    sim.run()
    tempf=sim.figure2
    for j in range(2**m):
        figure2[j][0]=figure2[j][0]+tempf[j][0]
        figure2[j][1]=figure2[j][1]+tempf[j][1]
print(figure2)

figure2_rate=[0 for j in range(2**m)]
for i in range(2**m):
    figure2_rate[i]=figure2[i][1]/(figure2[i][0]+figure2[i][1])
plt.figure(1)
print(figure2_rate)
plt.bar(range(2**m), figure2_rate)
plt.xlabel(r'$\mu$')
plt.ylabel(r'P(1|$\mu$)')
plt.savefig('Condi_win_sym.jpg')
plt.show()
plt.close()

#figure2-2 asymmetric
T = 100
s = 2
m = 11
N = 101
figure2=[[0 for i in range(2)]for j in range(2**m)]
for i in range(500):
    sim = System(T=T,N=N, m=m,s=s,lp=1)
    sim.run()
    tempf=sim.figure2
    for j in range(2**m):
        figure2[j][0]=figure2[j][0]+tempf[j][0]
        figure2[j][1]=figure2[j][1]+tempf[j][1]
print(figure2)

figure2_rate=[0 for j in range(2**m)]
for i in range(2**m):
    figure2_rate[i]=figure2[i][1]/(figure2[i][0]+figure2[i][1])

print(figure2_rate)
plt.bar(range(2**m), figure2_rate)
plt.xlabel(r'$\mu$')
plt.ylabel(r'P(1|$\mu$)')
plt.savefig('Condi_win_assym.jpg')
plt.show()
plt.close()
