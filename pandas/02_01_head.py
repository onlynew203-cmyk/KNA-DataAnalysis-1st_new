# 실습 1. head·tail로 디지털 신호 살펴보기
import pandas as pd


df = pd.read_csv("PANDAS/data/12_metro_digital.csv",
                 encoding= 'utf-8')

print(df.shape) # (120, 4)
print(df.head()) # 처음부터 5줄
print(df.tail()) # 끝에서 5줄

df_2 = pd.read_csv("PANDAS/data/12_metro_small.csv",
                 encoding= 'utf-8')

print(df_2.shape) # (30, 7)
print(df_2.head())
print(df_2.tail())


# 실습 2. head·tail 행 개수 조절
print(df_2.head(10))
print(df_2.tail(25))


# 실습 3. 구조 파악 3종 도구
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


# 실습 4. 열 이름·자료형 점검
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


# 실습 5. info로 데이터 건강검진
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