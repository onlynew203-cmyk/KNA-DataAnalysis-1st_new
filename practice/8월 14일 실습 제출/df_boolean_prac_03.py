# 실습 3. 두 조건 묶기
# 목표
# 두 조건을 그리고·또는로 묶어 행을 추출
import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# 단계
# · 비스킷두께 조건과 사이클타임 조건을 각각 괄호로 감싸기
# · 두 조건을 그리고 기호로 묶어 모두 만족하는 행 추출
# · 같은 두 조건을 또는 기호로 묶어 결과 수 비교

df_pre3_and = df[(df['비스킷두께'] >= 9) & (df['사이클타임'] >= 30)]
df_pre3_and.info() # 6개
# <class 'pandas.core.frame.DataFrame'>
# Index: 6 entries, 4 to 27
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   샷       6 non-null      int64  
#  1   실린더압력   6 non-null      float64
#  2   주조압력    6 non-null      float64
#  3   사이클타임   6 non-null      float64
#  4   비스킷두께   6 non-null      float64
#  5   형체력     6 non-null      float64
#  6   품질등급    6 non-null      object 
# dtypes: float64(5), int64(1), object(1)
# memory usage: 384.0+ bytes

print(len(df_pre3_and)) # 6개

df_pre3_or = df[(df['비스킷두께'] >= 9) | (df['사이클타임'] >= 30)]
df_pre3_or.info() # 26개
print(len(df_pre3_or)) # 26개


# 예상 결과
# 그리고는 12건, 또는는 94건으로 개수 차이 확인