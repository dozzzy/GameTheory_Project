from minoritygame import *
import matplotlib.pyplot as plt
# figure2-1 symetric
T = 100
s = 2
m = 4
N = 101

sim = System(T=T,N=N, m=m,s=s)
sim.run()
agentAction=sim.OneUser
print(agentAction)
plt.plot(range(T), agentAction)
plt.xlabel(r'game turn')
plt.ylabel(r'agent action')
plt.show()