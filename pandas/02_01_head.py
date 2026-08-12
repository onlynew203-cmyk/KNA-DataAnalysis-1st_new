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