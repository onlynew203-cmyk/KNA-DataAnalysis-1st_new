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


