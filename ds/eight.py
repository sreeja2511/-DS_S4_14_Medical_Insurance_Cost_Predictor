#case normalization
import pandas as pd

df=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David','Eva'],
})
print(df)
df['Name_lower']=df['Name'].str.lower()
print(df)
df['Name_upper']=df['Name'].str.upper()
print(df)