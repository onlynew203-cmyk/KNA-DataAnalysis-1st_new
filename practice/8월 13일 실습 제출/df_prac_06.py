import pandas as pd

df = pd.read_csv("PANDAS/data/12_metro_compressor.csv",
                 encoding='utf-8')
print(df.shape) # (200, 7)
print(df.head())
print(df.tail())
df.info() # ----> print를 굳이 적지 않아도 됌
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   측정시각    200 non-null    object 
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    object 
# dtypes: float64(5), object(2)
# memory usage: 11.1+ KB

print(df.describe())
#              압축압력        배출압력        저장압력        오일온도        모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000