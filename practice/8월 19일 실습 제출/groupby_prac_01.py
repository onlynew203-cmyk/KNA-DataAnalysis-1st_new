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