#%%
#1. numpy 및 scipy 라이브러리를사용하여아래의코드를 작성하시오 
import numpy as np

#a (a) 정규분포를따르는랜덤샘플을총 500개생성하시오

samples = np.random.normal(size=500)
print('generated random sample from normal distribution : ', samples)
#b (b) 위랜덤샘플의중앙값을계산하시오

med = np.median(samples)
print('median value of samples above : ',med)

#c (c) 위랜덤샘플의표준편차를계산하시오

std = np.std(samples)
print('stdev of samples above : ',std)

#d (d) 위랜덤샘플의상위 20% 값이무엇인지계산하시오

upper_20percentile = np.percentile(samples,q=0.8)
print('upper 20% :', upper_20percentile)

#e (e) 위랜덤샘플이어떤분포로부터생성되었는지를모른다고가 정하자. 해당샘플이정규분포로부터생성되었다고추측하고, parameter 2개(평균,표준편차)를계산하시오

n = samples.size
mean = np.sum(samples) / n
calculated_variance = np.sum((samples - mean)**2) / n
calculated_std = calculated_variance ** 0.5
print('calcualted mean value : ',mean)
print('calcuated variance value : ',calculated_variance)
print('calculated std value : ', calculated_std)
print('Is it Same between calculated value manually and np.mean :', np.allclose(mean,np.mean(samples)))
print('Is it Same between calculated value manually and np.std :',np.allclose(calculated_std,np.std(samples)))


#2. 주어진행렬 arr에대하여아래의행렬연산을 numpy 혹 은 scipy를활용하여구하시오

from scipy import linalg
import numpy as np  

arr = np.array([[1,3,5],
                [2,4,6],
                [6,5,8]])

# (a) 위행렬의 determinant를구하시오
determinant = linalg.det(arr)
print('determinat of array above : ', determinant)

# (b) 위행렬의역행렬을구하시오
inversematrix = linalg.inv(arr)
print("inverse matrix of array above : ",inversematrix)


#3. 주어진행렬 arr2의 determinant를구하시오. 만약오류 가발생한다면, 그원인을서술하시오.
arr2 = np.array([[1,2,3,4],
                [3,8,5,2],
                [4,3,6,2]])

print(linalg.det(arr2))
#error : ValueError: expected square matrix
#determinant 를 구하위해서는 행수 = 열수 (정방행렬) 이어야함


#%%
#4. 다음의행렬에대해 scipy를사용하지말고, numpy 및 Gaussian 소거법을사용하여 LU Decomposition을구하시오 (각과정단계및 E 값들을모두보이시오 )
import numpy as np
A = np.array([[2,2,2],[4,7,7],[6,18,22]])
U = np.identity(3)
np.copyto(U,A)
print('u = \n' + str(U))

U[1] = U[1] + (-2)*U[0]
E_21 = np.identity(3)
E_21[1,0] = -2
print('U = \n'+ str(U))
print('E_21 = \n'+str(E_21))

U[2]  = U[2] + (-3)*U[0]
E_31 = np.identity(3)
E_31[2,0] = -3
print('U = \n'+ str(U))
print('E_31 = \n'+str(E_31))

U[2] = U[2] + (-4)*U[1]
E_32 = np.identity(3)
E_32[2,1] = -4
print('U = \n'+ str(U))
print('E_32 = \n'+str(E_32))

E = np.matmul(np.matmul(E_32,E_31),E_21)
print('E= \n ' + str(E))

L = np.linalg.inv(E)
print('L = \n' + str(L))
#%%

#5 아래는 4번문제에서사용한행렬이다. Scipy를사용하여 LU 분해를하는코드를작성하고, 각값들을구하시오
import numpy as np
A = np.array([[2,2,2],[4,7,7],[6,18,22]])
U = np.identity(3)
np.copyto(U,A)
print('u = \n' + str(U))

_,L,U = linalg.lu(A)
print(_)
print('L = \n' + str(L))
print('U = \n' + str(U))
print('LU = \n' + str(np.matmul(L,U)))

#%%


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,num=50,endpoint=True)
y = 4*np.cos(2*x) + np.random.normal(size=50)
plt.xlim(-5,5)
plt.scatter(x,y)
plt.show()


#%%
from scipy.optimize import curve_fit

def sinfunc(x,a,b):
    return a*np.sin(b*x)

def cosfunc(x,a,b):
    return a*np.cos(b*x)

funclist = {'AssumeSinFunc' : sinfunc,
            'AssumeCosFunc' : cosfunc}


for i in funclist:    
    print(i)
    params,params_covariance = curve_fit(funclist[i],x,y,p0=[2,2])
    print(params)
    plt.plot(x,funclist[i](x,params[0],params[1]),c='red')
    plt.scatter(x,y)
    plt.title(i)
    plt.show()

#%%
#8 A중학교 1학년 1반과 1학년 2반학생들의몸무게를측정 한결과가아래와같다. 두반의몸무게분포의기댓값이 동일한지를검정하시오. ‒ 단, 두반학생들의몸무게는독립적이다. 
# 결론 : 5% 유의수준내에서는 같다고 볼수 없음
import numpy as np
from scipy.stats import t,f,norm
import matplotlib.pyplot as plt
import scipy.stats as st

xrange = np.arange(0,5.1,0.1)
alpha = 0.05 #5%유의수준내에서 검증(F검정)
class1 = [65.9,53.6,57.3,59.3,63.8,59.2,64.2,75.0,62.9]
class2 = [76.3,82.1,73.3,69.3,59.9,72.1,59.1,86.8,78.1]

c1 = np.array(class1)
c2 = np.array(class2)

n_c1 = c1.size
n_c2 = c2.size
var_c1 = c1.var()*n_c1/(n_c1-1)
var_c2 = c2.var()*n_c2/(n_c2-1)

#분산비
var_ratio = var_c1/var_c2
c_i = (f.ppf(0.025,n_c1-1,n_c2-1),f.ppf(0.975,n_c1-1,n_c2-1))
c_p = f.cdf(var_ratio,n_c1-1,n_c2-1)

gigak = c_p < (alpha/2)

print("분산 비 : " ,var_ratio)
print('기각역 경계값',c_i)
print('유의확률 : ',c_p)
print('5% 유의 수준 내 기각 가능 : ',gigak)

plt.plot(xrange,f.pdf(xrange,n_c1-1,n_c2-1))
plt.scatter(var_ratio,f.pdf(var_ratio,n_c1-1,n_c2-1),c='red',s=100)
plt.axvline(c_i[0])
plt.axvline(c_i[1])
plt.show()







#%%
