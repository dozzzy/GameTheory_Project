# 0
from minoritygame import *
import matplotlib.pyplot as plt
# figure0 symetric
T = 500
s = 2
#m=7
#m=15
m=2
N = 301
plt.figure(1)
sim = System(T=T,N=N, m=m,s=s)
sim.run()
AllAction=sim.D
#print(AllAction)
plt.title('m=2')
plt.plot(range(T), AllAction)
plt.xlabel(r't')
plt.ylim((-150, 150))
plt.ylabel(r'A(t)')
#plt.show()
plt.savefig('At1.jpg')
plt.close()
m=7
plt.figure(2)
sim = System(T=T,N=N, m=m,s=s)
sim.run()
AllAction=sim.D
#print(AllAction)
plt.title('m=7')
plt.plot(range(T), AllAction)
plt.xlabel(r't')
plt.ylim((-150, 150))
plt.ylabel(r'A(t)')
#plt.show()
plt.savefig('At2.jpg')
plt.close()