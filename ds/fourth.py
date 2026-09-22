import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Age':[25,30,np.nan,35,40],
    'Department':['HR','IT','Finance',np.nan,'HR']})
print(df)
df_drop_rows=df.dropna()
print(df_drop_rows)
df_drop_cols=df.dropna(axis=1)
print(df_drop_cols)
