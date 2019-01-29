#%%
#기본 테스트
import matplotlib.pyplot as plt
import numpy as np


# x = np.random.randn(1000)
# y= np.random.randn(1000)
# z = np.arange(0.,7.,0.2)


# p1 = (z,z,'bs')
# p2 = (z,z**2,'r--')
# p3 = (z,np.exp(z),'g^')
# p4 = (z,np.log2(z),'y<')


# plt.plot(*p1,*p2,*p3,*p4)
# # plt.plot(x,y,'r^')
# # plt.ylabel('Some random number')
# # plt.xlabel('Some xbar')
# # plt.axis([-5,5,-5,5])
# plt.show()


n = 60
np.random.seed(20190129)
x = np.random.rand(n)
y = np.random.rand(n)

colors = np.random.rand(n)
coloridx = ['#ef9c0d','#fec832','#c25400','#ceceee']
area = (30*np.random.rand(n))**2

plt.scatter(x,y,s=area,c=colors,marker='D',alpha=0.3)
plt.show()

x = np.random.rand(10)
y = np.random.rand(10)
z = np.sqrt(x**2 + y**2)

plt.scatter(x,y,s=80,c=z,marker=(5,0))
plt.show()


#bar chart

import numpy as np
import matplotlib.pyplot as plt

ind = np.arange(4)

x = [4,6,5,8]
plt.bar(ind,x,width=0.3,bottom=5)
plt.show()


n = 5
menmeans = (20,36,30,35,27)
womenmeans = (25,32,34,20,27)

ind = np.arange(n)
width = 0.35
colors = np.random.rand(n)
p1 = plt.bar(ind-width/2,menmeans,width,color='black')
p2 = plt.bar(ind+width/2,womenmeans,width)
plt.ylabel('scores')
plt.title('scores by group and gender')
plt.xticks(ind,('g1','g2','g3','g4','g5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1,p2),('men','women'))
plt.show()

l = [12,3,4]



labels = 'frogs','hogs','dogs','logs'

sizes = [15,30,45,10]
explode = (0,0.2,0.5,0)

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
shadow=True,startangle=90)
plt.axis('equal')
plt.legend()
plt.show()


size = 0.3
vals = np.array([60.,32.],[37.,40.],[29.,10.])
cmpt = plt.get_cmap('tab20c')


#%%
v = np.random.uniform(0.,10.,100)
plt.hist(v)
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
spread = np.random.rand(50)*100
center = np.ones(25)*50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10)*-100
data = np.concatenate((spread,center,flier_high,flier_low),0)
plt.boxplot(data)

#%%


a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c =np.concatenate((a,b),axis=0)
d = np.concatenate((a,b.T),axis=1)
c
d
#%%


spread = np.random.rand(50) * 100
center = np.ones(25)*50
flier_high = np.random.rand(10)*100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread,center,flier_high,flier_low),0)
plt.figure()
plt.boxplot(data,1)

#%%
plt.figure()
data = [np.random.rand(50)*100,np.random.rand(50)*50]
plt.boxplot(data)

#%%
