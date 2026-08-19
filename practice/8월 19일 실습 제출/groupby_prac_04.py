# 실습 7. 빈도와 그룹 집계 종합
# 빈도 집계와 그룹 집계를 한 흐름으로 연결
# 목표
# 빈도 집계와 그룹 집계를 한 흐름으로 연결해 분석
import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')
# 단계
# · value_counts로 설비 구성과 정상·고장 비율 파악
# value_counts는 결측(null값) 미포함 !!
print(df['밸브상태'].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19
# Name: count, dtype: int64
# --> 각 상태별 갯수를 확인할 수 잆다

# 밸브상태별 비율 확인
print(df['밸브상태'].value_counts(normalize=True).round(2))
# 밸브상태
# 정상    0.51
# 지연    0.17
# 경미    0.17
# 심각    0.16
# Name: proportion, dtype: float64


# · 고장 행만 걸러 라인별 고장 건수 집계
print((df['result'] == '고장').value_counts())
# result
# False    67
# True     53
print(df.groupby('result').size())
# result
# 고장    53
# 정상    67

# · groupby로 설비별 온도·진동 평균까지 비교
print(df.groupby('밸브상태')[['온도', '진동']].mean().round(2))
#          온도    진동
# 밸브상태             
# 경미    44.86  0.62
# 심각    46.02  0.63
# 정상    45.11  0.61
# 지연    45.86  0.62

# 예상 결과
# 구성·비율·라인별 고장 건수·설비별 평균 출력