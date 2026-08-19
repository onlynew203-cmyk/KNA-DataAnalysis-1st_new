# groupby 기본 코드

import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')
df.info()

# '냉각기상태' 컬럼의 내용별로 그룹핑(분할)하기
print(df.groupby('냉각기상태'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x1071fd220>

print(df.groupby('냉각기상태')['온도'])
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x107126e50>

print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89
# Name: 온도, dtype: float64/

print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55
# Name: 진동, dtype: float64

# 냉각기상태에 따른 그룹별 온도 평균과 진도 평균 구하기
print(df.groupby('냉각기상태')[['온도', '진동']].mean().round(2))
# 냉각기상태             
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55


# 냉각기상태별로 먼저 나누고, 그 안에서 다시 운전부하별로 나눠서 온도 평균 구하기
print(df.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89

# -----------------------
# 실습 4. groupby로 그룹 집계
# 기준 → 열 → 함수 순으로 그룹별 통계 구하기
# 목표
# 기준 열로 그룹을 나눠 그룹별 통계 구하기
import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')
df.info()

# 단계
# · 라인으로 그룹을 나눠 압력 열의 평균 집계
# 밸브상태별 압력 평균
print(df.groupby('밸브상태')['압력'].mean().round(2))
# 밸브상태
# 경미    161.56
# 심각    163.39
# 정상    159.99
# 지연    161.27

# · 집계 함수를 바꿔 설비별 최고 온도 확인
print(df.groupby('밸브상태')['온도'].max())
# 밸브상태
# 경미    57.1
# 심각    57.6
# 정상    57.8
# 지연    57.5

# · size로 교대별 측정 건수까지 확인
# size로 갯수 세기 (결측-null값 갯수도 포함)
print(df.groupby('밸브상태').size())
# 밸브상태
# 경미    20
# 심각    19
# 정상    61
# 지연    20
# dtype: int64

# 예상 결과
# 라인별 평균 압력·설비별 최고 온도·교대별 건수 출력



# -----------------------
# 실습 5. 그룹별 평균 비교와 정렬
# 그룹별 평균을 구해 정렬로 두드러진 그룹 찾기
# 목표
# 그룹별 평균을 구하고 정렬해 두드러진 그룹 찾기
import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')
df.info()
# 단계
# · 냉각기상태별로 그룹을 나눠 진동 평균 집계
print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55

# · 집계 결과에 정렬을 이어 붙여 내림차순으로 정렬
print(df.groupby('냉각효율')['진동'].mean().round(2).sort_values(ascending=False).head(5))
# 냉각효율
# 20.8    0.78
# 19.1    0.77
# 19.3    0.76
# 19.7    0.74
# 19.0    0.74
# 왼쪽 숫자는 냉각효율, 오른쪽 숫자는 해당 냉각효율 그룹의 평균 진동값

# · 가장 진동이 큰 설비를 맨 위에서 확인
print(df.sort_values('진동', ascending=False).head(5))
# 냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 20    고장  고부하   경미  56.0  0.779  180.41  20.8     고장
# 31    고장  고부하   지연  57.2  0.774  173.32  19.1     정상
# 27    고장  고부하   경미  57.1  0.759  173.06  19.3     고장
# 19    고장  고부하   심각  54.4  0.749  173.28  20.2     고장
# 32    고장  저부하   정상  57.0  0.741  156.60  19.0     정상

# 예상 결과
# 진동 평균이 큰 설비 순 정렬 (정상 최대)
df_normal = df[df['냉각기상태'] == '정상']
print(df_normal.sort_values('진동', ascending=False).head(5))
#  냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 82    정상  고부하   정상  35.4  0.566  161.00  46.6     정상
# 85    정상  고부하   정상  35.5  0.564  161.03  46.7     정상
# 80    정상  고부하   정상  36.2  0.563  160.72  47.3     정상
# 84    정상  고부하   정상  35.5  0.562  161.01  46.7     정상
# 81    정상  고부하   정상  35.5  0.561  160.97  46.5     정상


