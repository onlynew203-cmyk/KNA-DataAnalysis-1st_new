# 실습 5. info로 데이터 건강검진
import pandas as pd

df_5 = pd.read_csv("PANDAS/data/12_metro_digital.csv",
                 encoding= 'utf-8')

print(df_5.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 120 entries, 0 to 119
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   측정시각    120 non-null    object
#  1   압축기     120 non-null    int64 
#  2   타워      120 non-null    int64 
#  3   저압스위치   120 non-null    int64 
# dtypes: int64(3), object(1)
# memory usage: 3.9+ KB
# None