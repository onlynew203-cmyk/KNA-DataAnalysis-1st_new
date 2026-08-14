# .describe() — 기초 통계 요약 ----------------------------------

# 숫자 열들의 평균·최대·최소를 한 번에 자동 계산
# 수만 줄을 안 봐도 전체 모습 파악
# 글자 열은 빼고 숫자 열만 자동 계산

# (설비 안정성 보려면 표준편차를 꼭 함께 확인)


# 첫 탐색 체크리스트— 단계별 의미 ----------------------------------

# .head() -- 실제 값 확인 : 무엇에 관한 데이터인가
# .shape -- 크기 확인 : 얼마나 큰가
# .info() -- 구조·결측 : 어디가 문제인가
# .describe() -- 통계·이상 : 값이 정상인가

# 이 네 가지 질문 순서로 기억하면 모든 데이터 첫 탐색이 익숙해짐
# 이 체크리스트를 성격이 다른 두 데이터에 적용하면 차이가 잘 보임

# ----------------------------------------
# 실습 6. describe로 이상 신호 찾기
# 평균·분위수·최대를 읽어 이상 신호 있는 열 찾기
# 12_metro_compressor.csv
# 온도·진동에 이상값 존재

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


# ----------------------------------------
# 실습 7. 통계량 문장으로 묘사
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

# ----------------------------------------
# 실습 8. 압축기와 디지털 신호 구조 비교
# 같은 체크리스트로 깔끔한 데이터와 지저분한 데이터 비교

df_metro_compressor = pd.read_csv(
    "PANDAS/data/12_metro_compressor.csv",
    encoding= 'utf-8'
)

df_metro_digital = pd.read_csv(
    "PANDAS/data/12_metro_digital.csv",
    encoding= 'utf-8'
)

df_metro_compressor.info()
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

print(df_metro_compressor.describe())
#   압축압력        배출압력        저장압력        오일온도        모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000

df_metro_digital.info()
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

print(df_metro_digital.describe())
#               압축기          타워  저압스위치
# count  120.000000  120.000000  120.0
# mean     0.908333    0.933333    0.0
# std      0.289765    0.250490    0.0
# min      0.000000    0.000000    0.0
# 25%      1.000000    1.000000    0.0
# 50%      1.000000    1.000000    0.0
# 75%      1.000000    1.000000    0.0
# max      1.000000    1.000000    0.0

# ----------------------------------------
# 실습 9. 첫 탐색 종합
# 데이터를 불러와 구조까지 스스로 파악
# 앞서 배운 불러오기와 구조 파악을 한 번에 적용

df_sample = pd.read_csv(
    "PANDAS/data/12_metro_digital.csv",
    encoding= 'utf-8'
)

print(df.head())
#                   측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
# 0  2020-02-27 06:38:47  9.30 -0.02  9.30  51.3  6.04   가동
# 1  2020-02-27 07:28:21  8.55 -0.02  8.55  56.8  0.04   정지
# 2  2020-02-27 08:17:54  8.67 -0.02  8.67  55.7  0.03   정지
# 3  2020-02-27 09:07:27  9.76 -0.02  9.76   NaN  3.81   가동
# 4  2020-02-27 09:57:01  8.49 -0.02  8.49  55.3  0.04   정지

print(df.shape)
# (200, 7)

print(df.columns)
# Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='object')

print(df.dtypes)
# 측정시각     object
# 압축압력    float64
# 배출압력    float64
# 저장압력    float64
# 오일온도    float64
# 모터전류    float64
# 가동상태     object
# dtype: object

df.info()
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


# ----------------------------------------
# 종합 실습 2 — 통계 미리보기
# describe로 통계를 뽑고 이상 신호 찾기
# describe 후 평균·표준편차·min·max로 이상 신호 찾기

df_data = pd.read_csv(
    "PANDAS/data/12_metro_compressor.csv",
    encoding= 'utf-8'
)

print(df_data.describe())
#            압축압력      배출압력      저장압력       오일온도      모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000

# --->> 1. 배출압력의 최대 값이 표준편차와 차이가 너무 크다
# --->> 2. 오일온도 count 199.0

print(df_data[df_data["배출압력"] > 0])
#                 측정시각   압축압력  배출압력   저장압력  오일온도  모터전류 가동상태
# 157  2020-03-05 04:23:55  10.18  0.60  10.17  73.1  6.18   가동
# 191  2020-03-06 09:58:38  10.22  0.22  10.22  73.4  3.85   가동
# --> 튀는 값을 찾았다

print(df_data[df_data["오일온도"].isna()])
#               측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
# 3  2020-02-27 09:07:27  9.76 -0.02  9.76   NaN  3.81   가동
# --> 오일온도 NaN을 찾았다


# ----------------------------------------
# 종합 실습 3 — 첫 탐색 리포트
# 탐색 결과를 하나의 리포트로 정리
# 6개 항목을 채워 리포트 완성
# 개요· 열 구성· 결측· 통계· 이상 신호· 종합 의견


df_report = pd.read_csv(
    "PANDAS/data/12_metro_compressor_semicolon.csv",
    sep=";",
    encoding= 'utf-8'
)

# 1. 개요
# 데이터가 몇 행, 몇 열인지 확인
print("\n1. 개요")
print("데이터 크기:", df_report.shape)
# 데이터 크기: (200, 7)

# 2. 열 구성
# 어떤 열들이 있는지 확인
print("\n2. 열 구성")
print(df_report.columns)
# Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='object')

# 3. 결측
# 각 열에 비어 있는 값이 몇 개인지 확인
print("\n3. 결측")
print(df_report.isna().sum())
# 측정시각    0
# 압축압력    0
# 배출압력    0
# 저장압력    0
# 오일온도    1
# 모터전류    0
# 가동상태    0
# dtype: int64

# 4. 통계
# 평균, 표준편차, 최소, 최대, 사분위수 등 확인
print("\n4. 통계")
print(df_report.describe())
#            압축압력      배출압력      저장압력       오일온도      모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000


# 5. 이상 신호
# describe() 결과를 보고 이상해 보이는 값의 실제 행 확인
print("\n5. 이상 신호")

print("1) 배출압력의 최대 값이 표준편차와 차이가 너무 크다")
print(df_report[df_report["배출압력"] > 0])

print("-" * 60)

print("2) 오일온도 count 199.0")
print(df_report[df_report["오일온도"].isna()])
