#%%
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(1000,2000,1)
y = norm.pdf(x=x,loc=1500,scale=100)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('pdf on standard normal dist')
plt.hold(False)
plt.show()

#%%
samples = np.random.normal(size=1000)
bins = np.arange(-4,5)
print(bins)

histogram = np.histogram(samples,bins=bins,normed=True)[0]
bins = 0.5*(bins[1:]+bins[:-1])
print(bins)

#%%


from scipy import stats
samples = np.random.normal(size=1000)
loc,std = stats.norm.fit(samples)
print(loc)
print('-----')
print(std)

#%%

samples = np.random.normal(size=1000)
print(samples)
np.mean(samples)

#%%

from scipy import stats
a = np.random.normal(0,1,size=100)
b = np.random.normal(1,1,size=10)
stats.ttest_ind(a,b)


#%%

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

s1 = np.random.normal(0,size=1000)
s2 = np.random.normal(1,size=1000)

bins = np.linspace(-4,4,30)
h1,bins = np.histogram(s1,bins=bins,normed=True)
h2,bins = np.histogram(s2,bins=bins,normed=True)
plt.figure(figsize=(6,4))
plt.hist(s1,bins=bins,normed=True,label='Sample1')
plt.hist(s2,bins=bins,normed=True,label='Sample2')
plt.legend(loc='best')
plt.show()
stats.ttest_ind(a,b)

#%%
from scipy.stats import binom,norm
import matplotlib.pyplot as plt

k = range(7)
list(k)
y= binom.pmf(k,6,0.5)
y
plt.plot(k,y,'o')
plt.vlines(k,0,y)
plt.show()



plt.subplots(131)
plt.xlim(-3,15)
plt.plot(range(16),binom.pmf(range(16),n=10,p=0.1),marker='o')
plt.subplot(132)
plt.xlim(-3,15)
plt.plot(range(-5,16),norm.pdf(range(-5,16),loc=1,scale=np.sqrt(0.9)),color='black')
plt.subplot(133)
plt.xlim(-3,15)
plt.plot(range(16),binom.pmf(range(16),n=10,p=0.1),marker='o')
plt.plot(range(-5,16),norm.pdf(range(-5,16),loc=1,scale=np.sqrt(0.9)),color='black')

#%%

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

x = np.arange(0,40.1,0.1)


x



#%%
