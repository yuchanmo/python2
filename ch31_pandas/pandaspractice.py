

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


sales_stats = {'visitors':[43,45,33,43,78,44],
    'revenue':[64,73,62,64,53,66]}

df2 = DataFrame(sales_stats,index=['a','b','c','d','e','f'])
df3 = DataFrame(df2,columns=['visitors','revenue','dept'
])
df3

del df3['dept']

df3.loc['h'] = [200,77]


df2.drop(columns=['visitors'])

import MySQLdb as mysql


db = mysql.connect('localhost','asd','1q2w3e4r5t!','moyu')

c = db.cursor()
c.execute('select * from student limit 10')
datas = c.fetchall()

df4 = DataFrame(datas,columns=['SID','name','major','score'])


for i,r in df2.iterrows():
    print(i,r)


df4 = pd.DataFrame({'A':['foo','bar']*4,'B':['one','two']*4,'C':np.random.randn(8),'D':np.random.randn(8)})
df4 = DataFrame()
grouped = df4.groupby(['A'])
grouped.mean()
grouped.get_group('bar')

import pandas as pd

dd = pd.read_csv('test.csv')


date_str = ['2018.1.1','2018.1.4','2018.1.5','2018.1.6']
idx = pd.to_datetime(date_str)
idx

idx2 = pd.date_range(start='2018-4-1',periods=30)
idx3 = pd.date_range('2018-4-1','2018-4-30',freq='B')
idx4 = pd.date_range('2019-01-01','2019-12-31',freq='W')

rng = pd.date_range('1/1/2011',periods=72,freq='H')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
ts.head()

ts.truncate(before='01/02/2011',after='01/03/2011')