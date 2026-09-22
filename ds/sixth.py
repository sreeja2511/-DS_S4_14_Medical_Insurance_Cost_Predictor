#remvoing duplicates on particular column
import pandas as pd
df=pd.DataFrame({
    'ID':[1,2,3,4,5,1,2],
    'Name':['Alice','Bob','Charlie','David','Eva','Alice','Bob'],
    'Age':[25,30,35,40,45,25,30]})
print(df)
df_no_duplicates=df.drop_duplicates(subset=['ID'])
print(df_no_duplicates)