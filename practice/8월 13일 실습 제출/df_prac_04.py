# 실습 4. 열 이름·자료형 점검
import pandas as pd

df_4 = pd.read_csv("PANDAS/data/12_metro_compressor.csv",
                 encoding= 'utf-8')

print(df_4.columns) 
print(df_4.columns.tolist())
print(df_4.dtypes) 

print(df_4.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 200 entries, 0 to 199 ----- # → 200행
# Data columns (total 7 columns): ------- # → 7열
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
# None
