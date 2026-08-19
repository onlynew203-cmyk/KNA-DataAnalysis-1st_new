import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')

# 분산 구하기
print(df.groupby('냉각기상태')['온도'].var().round(2))
# 냉각기상태
# 고장    14.13
# 저하     2.15
# 정상     0.13
# Name: 온도, dtype: float64


# 평균 구하기
print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89
# Name: 온도, dtype: float64


# 평균과 분산 --------------
# 평균(Mean): 데이터의 중심이 어디인지 나타내는 값
# 모든 값을 더해서 데이터 개수로 나눔
# 예: [10, 20, 30] → 평균 20
# Pandas: .mean()

# 분산(Variance): 데이터가 평균에서 얼마나 퍼져 있는지 나타내는 값
# 분산이 작음 → 값들이 평균 근처에 모여 있음
# 분산이 큼 → 값들이 평균에서 넓게 퍼져 있음
# Pandas: .var()

# 한 줄로: 평균 = 중심, 분산 = 퍼진 정도



# 표준편차 구하기 --------------
print(df.groupby('냉각기상태')['온도'].std().round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36
# Name: 온도, dtype: float64

# 표준편차(Standard Deviation): 분산에 제곱근을 씌운 값
# 역시 데이터가 평균에서 얼마나 퍼져 있는지 나타냄
# 원래 데이터와 단위가 같아서 해석하기 쉬움
# Pandas: .std()



# 중앙값 구하기 --------------
print(df.groupby('냉각기상태')['온도'].median().round(2))
# 냉각기상태
# 고장    55.45
# 저하    44.90
# 정상    35.90
# Name: 온도, dtype: float64