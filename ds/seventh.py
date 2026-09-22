#data standardization
import pandas as pd
df=pd.DataFrame({
    'Date': ['2022-01-01','2022-02-01','2022-03-01','Jan 5, 2022','2025.01.01']
})
print(df)
df['Date']=pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)