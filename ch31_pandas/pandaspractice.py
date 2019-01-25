

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

s = pd.Series([1,2,3,np.nan,6,7])
s[3]


np_s = np.array([1,3,5,np.nan,6,8])
pd_s = pd.Series(np_s)
pd_s


d = {'a':0,'b':1,'c':2}

pd.Series(d)

from pandas import Series,DataFrame
import pandas as pd

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = Series(sdata)
obj3


states = ['Califonia','Ohio','Oregon','Texas']
obj4 = Series(sdata,index = states)
obj4

obj4['Califonia'] = np.nan
obj4


for i in obj4:
    print(i)


pd.isnull(obj4)

obj4.isnull()
d = dict()
linenum = 0
with open('people.txt','r') as f:
    for line in f:
        datas = line.split(',')
        if linenum ==0:
            for i in datas:
                d[i] = ''


ss = {'day':[1,2,3,4,5,6]
,'visitors':[43,45,33,43,78,44]
,'revenue':[64,73,62,64,53,66]}

df = pd.DataFrame(ss)
df

df.loc[1]

dd = df.set_index('day')

df.loc[5]
dd.loc[5]
df.loc[3:5]


df[df['day']>3]

df[['day','visitors']]
del df['day']