import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Age':[25,30,np.nan,35,40],
    'Department':['HR','IT','Finance',np.nan,'HR']})
df_ffill=df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)
df_bfill=df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)