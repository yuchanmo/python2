from random import randint

import numpy as np

#1
a = np.zeros(10)

#2
a[4] = 1

#3
b = np.arange(10,50,1)

#4
c = np.arange(0,25).reshape((5,5))

#5
d = np.eye(5)

#6
e = np.random.random((5,5))
e.max()
e.min()

#7
m1 = np.ones((4,3))
m2 = np.random.random((3,2))
m3 = np.dot(m1,m2)
print(m3)

#8
m3transpose = m3.T

#9
m91 = np.arange(0,24).reshape((5,5))
m92 = np.arange(25,49).reshape((5,5))
added_m12 = m91 + m92
substracted_m12 = m91 - m92

#10

a1_1 = np.array([[1,2],[3,4]])
a1_2 = np.array([[1,2],[3,4],[5,6]])

