from minoritygame import *
import matplotlib.pyplot as plt

N = 51
s = 2
T=500
m=11

sim = System(T=T,N=N, m=m,s=s,lp=1)
sim.run()
A=sim.A
x=[]
y1=[]

for i in range(T):
    x.append(i)
    temp=[]
    for j in range(i):
        temp.append(A[j])
    y1.append(var(temp))
plt.plot(x, y1)
plt.xlabel(r't')
plt.ylabel(r'occurrence')
plt.savefig('Var_t.jpg')
plt.show()


