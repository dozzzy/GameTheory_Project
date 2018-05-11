from frame.minoritygame import *
import math
import matplotlib.pyplot as plt
# figure3
T = 500
s = 2
m = 0
N = [51]
syms = ['x','v','s','p','*']
cValue = ['r','y','g','b','r','y','g','b','r']
count=0

miu_count=[0 for i in range(2**10)]

plt.figure(1)
for nn in N:
    m=int(math.log2(nn*100))
    x = []
    y = []
    print('N m',nn,m)
    for mm in range(1,m):
        #sum=0
        yy=0
        for t in range(10):
            #sum=0
            sim = System(T=T,N=nn, m=mm,s=s,lp=1)
            sim.run()
            figure4=sim.figure4
            count_eff=0
            print('mm',mm)
            print(figure4)
            sum=0
            for j in range(2**mm):
                if figure4[j][0]!=0:
                    avg=((figure4[j][1])/(figure4[j][0]))
                    #avg = ((figure4[j][1]) / (T))
                    sum=sum+avg**2
                    count_eff=count_eff+1
            sum=(sum/2**mm)/nn
            yy=yy+sum
            if t==0 and mm==10:
                for j in range(2**mm):
                    miu_count[j]=figure4[j][0]
                print('miu_cout',miu_count)
        #sum=sum/10
        y_point=yy/10
        x.append((2**mm)/nn)
        y.append(y_point)
        print(y_point)
    #plt.scatter(x, y)
    plt.scatter(x, y, c=cValue[count], marker=syms[count], label='N=' + str(N[count]))
    count=count+1
plt.xscale('log')
plt.xlabel(r'$2^{m}/N$')
plt.ylabel('H/N')
plt.legend(loc='best')
plt.savefig('figures/Predict_eff.jpg')
plt.show()
plt.close()

plt.figure(2)
plt.bar(range(2**10), miu_count)
tcount=0
for j in range(2**10):
    if miu_count[j]!=0:
        tcount=tcount+1
print('eff_rate',tcount/2**10)
plt.xlabel(r'$\mu$')
plt.ylabel('accurance_count')
plt.savefig('figures/Predict_eff_cnt.jpg')
plt.show()
plt.close()