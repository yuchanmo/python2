import matplotlib as plt
import numpy as np
from matplotlib.pyplot import scatter
from numpy import random
from numpy.core.numeric import dtype

a = np.array([1,4,5,8],float)

a
type(a)

a2 = np.array([[1,2,3],[4,5,6]],float)
a2


s = 'hello world'
s2 = np.array(s,str)


aaaa = np.arange(10,30,1)


x = np.array([1,2,3])
x.dtype

x = np.array([1.0,2.0,3])
x.dtype

x = np.array([1,2,3],dtype='f')
x.dtype

x[0]+x[1]


x = np.array([1,2,3],dtype='U')
x.dtype

x[0]+x[1]

np.array([0,1,-1,0])
np.log(0)

np.exp(-np.inf)

np.zeros((3,3))


np.ones((3,3))

np.zeros(5)

np.full((3,3),7)


a = np.eye(3)

np.zeros((2,3))

c = np.zeros((5,2),dtype='i')



d = np.zeros(5,dtype='U4')

g = np.empty((4,3))

np.eye(3)

np.arange(10)


help(np.linspace)




np.random.random((3,3))

np.random.rand(3,3)

np.random.randint(5,size=10)

2.5*np.random.randn(2,4)+3


a= np.array([[1,2,3],[4,5,6],[7,8,9]],float)

aa = np.array(range(6),float).reshape((2,3))


a = np.array([[1,2,3],[4,5,6]],float)
a
a.flatten()


a = np.array([1,2],float)
b= np.array([3,4,5,6],float)
np.concatenate((a,b))

a = np.arange(14)
b = a.reshape(3,-1)


a = np.arange(10)
a.reshape(2,-1)
np.ones(30)


x = np.arange(5)
x.reshape(5,1)


#x.reshape(1,5)
x[:np.newaxis]


a1 = np.ones((2,3))
a2 = np.zeros((10,3))

np.vstack([a1,a2])




c1 = np.ones((3,4))

c2 = np.zeros((4,4))

np.dstack([c1,c2])


x = np.arange(3)
y = np.arange(5)

x,y = np.meshgrid(x,y)


plt.scatter

plt.title('hellot')
plt.scatter(x,y,linewidth=10)
plt.show()


a = np.array(range(100),float).reshape(4,25)
b= np.array([5,2,6],float)

a + b
b**a


for i in a:
    print(i)



bb = np.loadtxt('foo.txt',delimiter=',')


a = np.array([2,4,3],float)
a.var()

a=  np.array([[1,2,1,3],[5,3,1,8]],float)
c = np.corrcoef(a)
c

a = np.array([1,2,3])
b= np.array([0,1,1])
np.dot(a,b)

np.inner(a,b)


r = np.array([[29,25,15],[9,10,7],[162,125,205]])
p = np.array([[0.02,0.6,0.02],[0.02,0.55,0.01],[0.01,0.42,0.02]])

np.dot(r,p)



aa = np.mat('4 3; 2 1')
bb = np.mat('1 2; 3 4')
print(aa)