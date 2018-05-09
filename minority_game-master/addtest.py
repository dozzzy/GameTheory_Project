from minoritygame import *
import matplotlib.pyplot as plt

N = 51
s = 2
T=500
m=11

sim = System(T=T,N=N, m=m,s=s)
sim.run()
D=sim.D
x=[]
y1=[]
y2=[]
for i in range(T):
    x.append(i)
    temp=[]
    for j in range(i):
        temp.append(D[j])
    #print(temp)
    y1.append(var(temp))
    y2.append(var(temp)/N)
plt.subplot(211)
plt.plot(x, y1)
plt.xlabel(r't')
plt.ylabel(r'var')

plt.subplot(212)
plt.plot(x, y2)
plt.xlabel(r't')
plt.ylabel(r'var/N')
plt.show()

