# 단일 컬럼 선택

import pandas as pd

df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   샷       30 non-null     int64  
#  1   실린더압력   30 non-null     float64
#  2   주조압력    30 non-null     float64
#  3   사이클타임   30 non-null     float64
#  4   비스킷두께   30 non-null     float64
#  5   형체력     30 non-null     float64
#  6   품질등급    30 non-null     object 
# dtypes: float64(5), int64(1), object(1)
# memory usage: 1.8+ KB



# 데이터 프레임(2차원)에서 컬럼 한개를 도려내보면 시리즈(1차원)가 된다
df_sub = df['형체력']
df_sub.info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 형체력
# Non-Null Count  Dtype  
# --------------  -----  
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 368.0 bytes

# 단일 컬럼을 선택하는 또 다른 방법
df['형체력'].info()

# 여러 컬럼을 선택할 때
df[['실린더압력', '형체력',]].info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   실린더압력   30 non-null     float64
#  1   형체력     30 non-null     float64
# dtypes: float64(2)
# memory usage: 608.0 bytes

