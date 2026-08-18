import pandas as pd

df_3 = pd.read_csv("PANDAS/data/12_metro_digital.csv",
                 encoding= 'utf-8')

print(df_3.shape) # (120, 4)
print(df_3.columns) # Index(['측정시각', '압축기', '타워', '저압스위치'], dtype='object')
print(df_3.columns.tolist())
# ['측정시각', '압축기', '타워', '저압스위치']
# 측정시각     object
# 압축기       int64
# 타워        int64
# 저압스위치     int64
print(df_3.dtypes) # dtype: object