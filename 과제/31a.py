import pandas as pd
import numpy as np

exam_data = {
    'name':['Anastasia','Catherine','Cahill','James','Emily'
    ,'Michael','Monica','Laura','Kevin','Jordan']
    ,'score' :[13,9.5,16.5,np.nan,11,20,17,np.nan,8.5,19]
    ,'attempts':[1,3,3,2,2,3,2,3,2,1]
    ,'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']

}
labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data,index=labels)

#1-1
df[['name','score']]
#1-2
df.iloc[:3]
#1-3
df[['name','score']].iloc[[0,1,4,5]]
#1-4
df[df['attempts']>2]