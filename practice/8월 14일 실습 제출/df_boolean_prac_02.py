# 실습 2. 임계값 넘는 설비 골라내기
# 목표
# 실제 제조 데이터에서 위험 임계값을 넘는 설비 추출
# 단계
import pandas as pd
df_2 = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · 비스킷두께 열에 비교 연산자로 임계값 기준 조건 생성
# · 조건을 대괄호에 넣어 임계값 초과 설비만 추출
# · 결과에서 샷와 비스킷두께 열만 골라 확인

s_2 = df_2[df_2['비스킷두께'] >= 16]
# df_2에서 ['비스킷두께']를 가져오고, 그에 조건을 달아서 가져오는데 df_2에서 가져오기 --> series

s_2.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 5 entries, 2 to 27
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   샷       5 non-null      int64  
#  1   실린더압력   5 non-null      float64
#  2   주조압력    5 non-null      float64
#  3   사이클타임   5 non-null      float64
#  4   비스킷두께   5 non-null      float64
#  5   형체력     5 non-null      float64
#  6   품질등급    5 non-null      object 
# dtypes: float64(5), int64(1), object(1)
# memory usage: 320.0+ bytes

print(s_2['샷'].head()) # 결과에서 샷 열만 골라 확인
print(s_2[['샷','비스킷두께']].head()) # 결과에서 샷와 비스킷두께 열만 골라 확인

print(len(s_2))

# 예상 결과
# 비스킷두께 16 이상 40건, 샷·비스킷두께 목록 출력