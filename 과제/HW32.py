
# coding: utf-8

# ## 이후에 해당 데이터로 기계 학습 알고리즘으로 학습한다고 가정하고, 시각화
# ## 작업이 기계 학습에 어떤 도움을 줄 수 있는지 파악하는 데 중점

# ### 1.데이터 로드작업

# In[71]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#1. read csv
dforiginal = pd.read_csv('d:/programming/python/viz.csv')
df = dforiginal.set_index('Time')


# ### 2.데이터 셋 탐색 
# #### - 행수 : 284807 행,Nan값 없음
# #### - 열수 : 총30개 column <float64(29), int64(1)>

# In[5]:


#2 데이터 셋 탐색
#attribute 특징
print(df.info())


# ### 2-1. Column별 통계치 확인
# #### - describe 명령으로 확인,한눈에 통계치와 분산,분포 알아보기 어려움, Boxplot으로 전체 파악 필요

# ### Class의 경우 값의 범위가 적어보여, unique로 파악시 0,1값으로 나뉘어져있음

# In[16]:


df['Class'].unique()


# In[58]:


#통계치 확인
print(df.describe(include='all').unstack())


# In[59]:


print(dforiginal.groupby('Class').describe(include='all').unstack())
#grouped = dforiginal.groupby('Class')

#cols = dforiginal.columns
#for c in cols:
#    print('column : ',c)
#    print(grouped[c].describe(include='all'))

    


# ### 2.Chart 확인
# #### (1)Boxplot 
# #### - boxplot으로 각 column별 데이터 분포 확인 시, Vx colunn은 1Q-3Q까지는 비슷하나 그외의 바깥 구간의 값의 range차이가 큰 것으로 확인됨. Time 축을 x축으로 놓고, 추가 데이터의 시계열적 영향성 확인 필요해보임
# #### - class에 따른 분류로 box plot 확인 시 일부 column(V3,7,10,12,14,16,17 등)에서 Class 0/1간 평균차이가 큰 경향 확인됨. 

# In[28]:


#boxplot으로 확인
import math
ncols = 3
nrows = int(math.ceil(colcnt/3))
boxfig,boxax = plt.subplots(nrows,ncols,figsize=(20,60))
for i,c in enumerate(cols[:-1]):
    grouped = df[[c,'Class']].groupby('Class')
    pairs = [[k,np.array(v[c])] for k,v in grouped]
    vals = list(map(lambda x:x[1],pairs))
    keys = list(map(lambda x:x[0],pairs))
    boxax[i//ncols][i%ncols].title.set_text(c)
    boxax[i//ncols][i%ncols].boxplot(vals,positions=keys)    
    if i <28:
        boxax[i//ncols][i%ncols].set_ylim([-20,20])
    if i==28:
        boxax[i//ncols][i%ncols].set_ylim([-3,10000])
    
plt.show()


# #### (2) Scatter plot
# #### - 시계열(Time column)관점 Class별 값 영향성 확인 위해 scatter plot(X : Time, Y :Value)확인
# #### - 결론 : 특이시점에 Class 1/2간 이중 트렌드를 보이진 않는것으로 보이며, 특정 column(V4,14,16,17,18...)이 전반적으로 class1/2간 이중트렌드 경향성 보임

# In[66]:


#scatter plot으로 확인
import matplotlib.colors as colors
cm = colors.ListedColormap(['#FF0000','#00FF00'])
cols = df.columns    
colcnt = len(cols)
ncols = 2
nrows = int(math.ceil(colcnt/2))
scatterfig,scatterax = plt.subplots(nrows,ncols,figsize=(20,60))
scatterfig.tight_layout()
for i,c in enumerate(cols[:-1]):    
    sax = scatterax[i//ncols][i%ncols]
    sax.scatter(df.index, df[c],c=df['Class'],cmap=cm,alpha=0.3,s=100)
    sax.set_xlim([-2,172800])
    sax.title.set_text(c)
plt.show()


# #### (3) Histogram
# #### - column별 전체 분포 확인 위해 histogram 확인, groupby 를 통해서 class별 나눠서 확인 ,대부분은 종모양을 띄고 있으나 일부 종모양 아닌 경향 띔

# In[79]:


#3.시각화
#histograph 로 확인
from scipy.stats import scoreatpercentile as sp
cols = df.columns    
colcnt = len(cols)
ncols = 2
nrows = int(math.ceil(colcnt/2))
histfig,histax = plt.subplots(nrows,ncols,figsize=(20,60))
histfig.tight_layout()
for i,c in enumerate(cols):    
    hax = histax[i//ncols][i%ncols]
    gr = df.groupby('Class')
    vals=[np.array(v[c]) for k,v in gr]
    c0 = vals[0]
    c1 = vals[1]
    hax.hist(c0, bins=100,range =[sp(df[c],10),sp(df[c],90)], label='0')
    hax.hist(c1, bins=100,range =[sp(df[c],10),sp(df[c],90)],label='1')
    hax.legend(loc='best')
    hax.title.set_text(c)
plt.show()


# #### (4) Scatter plot 
# #### - X축 : V column, Y축 : Amount Column
# #### - V축을 제외하면 Amount/Class/Time Column 이 남는데, V column 과 Amount Column 간의 관계에 따른 Class분류 경향성이 보이는지 확인 위해 plotting, 
# #### - 결론 : 가격과 V개별 Column과의 관계에선 Class 의 구분이 보이지 않음, 선형성 or Clustering 관계성 보이지 않음

# In[96]:


cols = df.columns    
colcnt = len(cols)
ncols = 3
nrows = int(math.ceil(colcnt/3))
corrfig,corrax = plt.subplots(nrows,ncols,figsize=(20,60))
corrfig.tight_layout()
for i,c in enumerate(cols):    
    cax = corrax[i//ncols][i%ncols]
    gr  = df.groupby('Class')
    vals=[[np.array(v[c]),np.array(v['Amount'])] for k,v in gr]    
    cax.scatter(x=vals[0][0],y=vals[0][1], c='blue', s= 100, label='0',alpha=0.3)
    cax.scatter(x=vals[1][0],y=vals[1][1], c='red',  s= 100, label='1',alpha=0.3)
    cax.legend(loc='best')
    cax.title.set_text(c)
plt.show()


# In[ ]:


sns.pairplot(df,hue='Class')


# In[86]:


gr  = df.groupby('Class')
vals=[[np.array(v['V1']),np.array(v['Amount'])] for k,v in gr]    


# In[93]:


print(len(vals[0][0]))
print(len(vals[0][1]))

