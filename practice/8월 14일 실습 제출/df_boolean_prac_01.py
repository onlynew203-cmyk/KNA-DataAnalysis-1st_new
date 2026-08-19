# 실습 1. 단일 조건으로 행 추출하기
# 목표
# 조건을 만들고 그 조건으로 원하는 행만 추출
# 단계
import pandas as pd
df_1 = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성
s_pre = df_1['실린더압력']
s_pre.info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 실린더압력
# Non-Null Count  Dtype  
# --------------  -----  
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 368.0 bytes

print(s_pre.head())
print(len(s_pre)) # 30

s_pre_boolean = s_pre >= 230

# · sum으로 조건을 만족하는 행 개수 확인
print(s_pre_boolean.sum()) # 5

# · 만든 조건을 데이터프레임 대괄호에 넣어 행(의 갯수) 추출
df_sub = df_1[df_1['실린더압력'] >= 230]
print(len(df_sub)) # 5

# 예상 결과
# 참 개수와 추출 행 수가 같게 출력 (실린더압력 230 이상 19건)


# ------->> True의 개수를 세기 위해 .sum()을 사용하는 것은 데이터가 bool 타입일 때 가능
s_1 = df_1['비스킷두께'] # bool 타입이 아니므로 .sum()으로 True 개수 확인 불가
s_1.info() # dtypes: float64(1)

# s_1_bool = s_1 >= 13 # bool Series → .sum()으로 True 개수 확인 가능
s_1_bool = df_1['비스킷두께'] >= 13 # 164 코드와 동일하게 작동

s_1_bool.info() # dtypes: bool(1)
print(s_1_bool.sum()) # 6