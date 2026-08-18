# Boolean Series
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

s = df['비스킷두께'] # Series --> df에서 해당하는 열 1개만 가져옴
s.info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 비스킷두께
# Non-Null Count  Dtype  
# --------------  -----  
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 368.0 bytes

print(s.head()) # --> 잘 가져왔나 확인
print(s.tail())


# boolean serise 생성 : true or false
s_boolean = s >= 13 # 이 조건으로 true or false를 가려보자
print(s_boolean.head())
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# Name: 비스킷두께, dtype: bool


# 위에서 생성된 boolean series에서 True 값의 개수는? ------------------------
# true/false 모두 30개인 것을 확인할 수 있다
s_boolean.info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 비스킷두께
# Non-Null Count  Dtype
# --------------  -----
# 30 non-null     bool 
# dtypes: bool(1)
# memory usage: 158.0 bytes


# true == 1, false == 0
# --> 때문에, 합산으로 true인 것들의 숫자를 알 수 있음
print(s_boolean.sum()) # 6

# --> 그럼 전체 개수 30에서 트루 6을 제외하면 false는 24개임을 알 수 있다.


# ------------------------
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
df_sub = df[df['실린더압력'] >= 230]
print(len(df_sub)) # 5

# 예상 결과
# 참 개수와 추출 행 수가 같게 출력 (실린더압력 230 이상 19건)


# ------------------------
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



import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

df_sub1 = df[df['비스킷두께'] >= 13]
df_sub1.info()

df_sub2 = df[df['사이클타임'] >= 25]
df_sub2.info()

df_and = df[(df['비스킷두께'] >= 13) & (df['사이클타임'] >= 25)]
df_and.info() # 개수 :5

df_or = df[(df['비스킷두께'] >= 13) | (df['사이클타임'] >= 25)]
df_or.info() # 개수 :7


# ------->> True의 개수를 세기 위해 .sum()을 사용하는 것은 데이터가 bool 타입일 때 가능
s_1 = df['비스킷두께'] # bool 타입이 아니므로 .sum()으로 True 개수 확인 불가
s_1.info() # dtypes: float64(1)

# s_1_bool = s_1 >= 13 # bool Series → .sum()으로 True 개수 확인 가능
s_1_bool = df['비스킷두께'] >= 13 # 164 코드와 동일하게 작동

s_1_bool.info() # dtypes: bool(1)
print(s_1_bool.sum()) # 6

# --------------------------
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


# --------------------------
# 실습 4. 부정·목록·범위 조건
# 목표
# 부정·목록 매칭·범위 조건을 각각 적용
import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")
df.info() # 전체 30개
# 단계
# · 물결 기호로 고장이 아닌 설비만 뒤집어 추출

print(df.tail()) # --> 불량을 발견했다
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 25  26  218.0  1055.0   20.9   11.0  255.0   양품
# 26  27  217.0  1051.0   20.9   12.0  257.0   양품
# 27  28  265.0   595.0   33.8   19.0  355.0   주의
# 28  29  218.0  1055.0   20.7   11.0  255.0   양품
# 29  30  218.0  1054.0   21.4    2.0  253.0   불량

print(df[df['품질등급'] == '불량'].head())
#  샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 4    5  108.0   522.0  652.3   14.0  222.0   불량
# 9   10  214.0  1036.0   93.1   12.0  247.0   불량
# 14  15  215.0  1041.0   21.3    4.0  258.0   불량
# 19  20  216.0  1044.0   21.2   11.0  259.0   불량
# 24  25  219.0  1058.0   21.3    2.0  255.0   불량
print(df[df['품질등급'] == '불량'].tail())

# 갯수 세기
print("불량 갯수 : ", len(df[df['품질등급'] == '불량'])) # 불량 갯수 :  6
print("불량이 아닌 갯수 : ", len(df[~(df['품질등급'] == '불량')])) # 불량 갯수 :  24

# · isin으로 품질등급이 특정 목록에 속하는 행 추출
print(df[df['품질등급'].isin(['불량', '주의'])]) # df의 품질등급 열에서 불량과 주의 값이 들어있는, df의 행을 출력
print(len(df[df['품질등급'].isin(['불량', '주의'])])) # 12 # 위 행의 개수를 알려줘

# · between으로 실린더압력가 지정 범위에 든 행 추출 : 210~230
print(df[df['실린더압력'].between(210, 230)]) # between(210, 230) = 210 이상 ~ 230 이하
# df에서 '실린더압력'에 해당하는 열을 가져와. 그 중에서도 210이상 230이하에 해당하는 열을 df에서 가져와서 출력해
# (df['실린더압력'] >= 210) & (df['실린더압력'] <= 230) # between 풀어쓰기

print(len(df[df['실린더압력'].between(210, 230)])) # 24 출력
print(len(df[~(df['실린더압력'].between(210, 230))])) # 6 출력

# 예상 결과
# 순서대로 192건·94건·108건 출력

