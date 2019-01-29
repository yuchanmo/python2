import numpy as np
import pandas as pd

vals1 = np.array([1,None,3,4])
vals1.sum()

vals2 = np.array([1,np.nan,3,4])
vals2.sum()

np.nansum(vals2)

v = pd.Series(vals2)
v.isnull()

v[v.notnull()]

v.dropna()

df = pd.DataFrame([[1,np.nan,2],
                [2,3,5],
                [np.nan,4,6]])

df

dd = df.dropna(axis='columns')