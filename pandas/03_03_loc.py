# loc 행 ---------------------------------------

import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

print("-"*40)

df.loc[0].info() # Series
# <class 'pandas.core.series.Series'>
# Index: 7 entries, 샷 to 품질등급
# Series name: 0
# Non-Null Count  Dtype 
# --------------  ----- 
# 7 non-null      object
# dtypes: object(1)
# memory usage: 112.0+ bytes

print("-"*40)

df.loc[0:2].info() # DataFrame
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   샷       3 non-null      int64  
#  1   실린더압력   3 non-null      float64
#  2   주조압력    3 non-null      float64
#  3   사이클타임   3 non-null      float64
#  4   비스킷두께   3 non-null      float64
#  5   형체력     3 non-null      float64
#  6   품질등급    3 non-null      object 
# dtypes: float64(5), int64(1), object(1)
# memory usage: 296.0+ bytes

# 행 언급 서브 df 만들기 ---------------------------------------
df_sub = df.loc[0:2]
df_sub.info()
print(df_sub)
print(df_sub.head())

# 행(row)과 열(col) 언급 서브 df 만들기 ---------------------------------------
df_sub_2 = df.loc[0:2, ['품질등급', '형체력']]
df_sub_2.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   품질등급    3 non-null      object 
#  1   형체력     3 non-null      float64
# dtypes: float64(1), object(1)
# memory usage: 176.0+ bytes


# -----------------------------------
# 실습 4. loc와 iloc로 행 선택하기
# 목표
# 라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이 확인
# 단계

import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · loc로 라벨 기준 단일 행 선택
# → 행 라벨이 0인 행에서 '품질등급' 열을 가져와라.
print(df.loc[0, '품질등급']) # 양품 --> df의 0번 행에서 '품질등급' 열의 값을 가져와라
# loc → 행의 이름(라벨)을 보고 찾는다.

# · iloc로 번호 기준 단일 행 선택
# → 위에서 0번째 위치(첫 번째)에 있는 행을 가져온 다음, 그 행에서 '품질등급'을 가져와라.
print(df.iloc[0]['품질등급']) # 양품 --> df의 0번 행에서 '품질등급' 열의 값을 가져와라
# iloc → 몇 번째 위치인지 보고 찾는다.

# · 범위 선택으로 loc 끝 포함·iloc 끝 제외 차이 확인
print(len(df.loc[0:2])) # loc는 범위를 선택할 때 마지막 2를 포함
print(len(df.iloc[0:2])) # iloc는 파이썬의 일반적인 슬라이싱처럼 마지막 2를 포함하지 않음

# 예상 결과
# 품질등급 값과 범위 줄 수 3·2 출력


# -----------------------------------
# 실습 5. loc·iloc로 행·열 동시 선택하기
# 목표
# 행과 열을 동시에 지정해 원하는 부분만 추출
# 단계
# · loc로 행 범위와 열 이름을 함께 지정
result_1 = df.loc[0:4, ['실린더압력', '형체력']]

# 1. loc로 0~4번 행 + 두 개 열 선택
result_1 = df.loc[0:4, ['실린더압력', '형체력']]

print(result_1)
print(result_1.shape)  # (5, 2)

# · 다른 행 범위에서 세 열 선택
# 2. loc로 5~9번 행 + 세 개 열 선택
result_2 = df.loc[5:9, ['실린더압력', '형체력', '품질등급']]

print(result_2)
print(result_2.shape)  # (5, 3)

# · iloc 음수 인덱스로 마지막 행 선택
print(df.iloc[-3:])

# 예상 결과
# (5, 2)·(5, 3)·마지막 3행 출력





# -----------------------------------
# 실습 6. 특정 구간 추출 종합
# 목표
# 열 선택·loc·iloc를 결합해 특정 구간을 추출하는 종합
# 단계
df_shot = pd.read_csv("PANDAS/data/13_diecasting_shot.csv")

# · 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
feature = ['실린더압력','주조압력','사이클타임','비스킷두께','형체력']
print(df_shot[feature].iloc[0:10].shape) # (10, 5)

# · loc 라벨 범위로 두 열 구간 추출
print(df_shot.loc[0:10, ['실린더압력', '주조압력']].shape)  # (11, 2)

# · iloc 위치 범위로 앞쪽 열 구간 추출
print(df_shot.iloc[0:10, 0:6].shape)  # (10, 6)

# 예상 결과
# (10, 5)·(11, 2)·(10, 6) 출력
