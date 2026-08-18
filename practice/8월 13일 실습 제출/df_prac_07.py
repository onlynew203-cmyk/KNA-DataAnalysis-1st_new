# 실습 7. 통계량 문장으로 묘사
import pandas as pd
# describe 통계를 자기 말로 풀어 설명
# 설비 센서 데이터의 한 열 묘사
# 온도·진동·전류 중 하나 골라 문장으로

df_7 = pd.read_csv("PANDAS/data/12_metro_compressor.csv",
                 encoding='utf-8')

df_7.info()

# 오일온도 컬럼만 떼어내서 describe 통계 보기
print(df_7["오일온도"])
# 0      51.3
# 1      56.8
# 2      55.7
# 3       NaN
# 4      55.3
#        ... 
# 195    60.7
# 196    61.9
# 197    73.0
# 198    72.5
# 199    71.7
# Name: 오일온도, Length: 200, dtype: float64

# 오일온도 컬럼만 정보 보기
df_7["오일온도"].info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 200 entries, 0 to 199
# Series name: 오일온도
# Non-Null Count  Dtype  
# --------------  -----  
# 199 non-null    float64
# dtypes: float64(1)
# memory usage: 1.7 KB

# 오일온도 컬럼만 describe 통계보기
print(df_7["오일온도"].describe())
# count    199.000000
# mean      63.181910 (평균)
# std        6.249822 (표준편차)
# min       50.100000 (최소)
# 25%       58.100000
# 50%       62.900000 (중앙값)
# 75%       68.100000
# max       75.000000 (최대)
# Name: 오일온도, dtype: float64