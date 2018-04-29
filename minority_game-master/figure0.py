from minoritygame import *
import matplotlib.pyplot as plt
# figure0 symetric
T = 500
s = 2
#m = 2
#m=7
#m=15
m=1
N = 301

sim = System(T=T,N=N, m=m,s=s)
sim.run()
AllAction=sim.D
print(AllAction)
plt.plot(range(T), AllAction)
plt.xlabel(r't')
#plt.ylim((-150, 150))
plt.ylabel(r'A(t)')
plt.show()