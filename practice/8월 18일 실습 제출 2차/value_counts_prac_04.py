# 선택 문제 : 첨부된 CSV 파일을 통해 다음 통계들을 내는 코드를 작성해 제출해주세요.
import pandas as pd

df = pd.read_csv("PANDAS/data/students_groupby_practice.csv")
df.info()
# class 'pandas.core.frame.DataFrame'>
# RangeIndex: 60 entries, 0 to 59
# Data columns (total 6 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   학년      60 non-null     int64 
#  1   반       60 non-null     object
#  2   이름      60 non-null     object
#  3   국어      60 non-null     int64 
#  4   영어      60 non-null     int64 
#  5   수학      60 non-null     int64 
# dtypes: int64(4), object(2)
# memory usage: 2.9+ KB
# --> 데이터가 잘 불러져 오고 있으며, 전체 통계를 확인

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
print(len(df['이름'])) # 60
# --> 60명의 학생을 확인

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)
print(df.groupby('학년')['이름'].count()) 
# 학년
# 1    20
# 2    20
# 3    20
# --> 각 학년당 20명의 학생을 확인

# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
print(df.groupby(['학년','반'])['이름'].count()) 
# 학년  반
# 1   A    5
#     B    5
#     C    5
#     D    5
# 2   A    5
#     B    5
#     C    5
#     D    5
# 3   A    5
#     B    5
#     C    5
#     D    5
# --> 각 학년별 4개의 반과 각 반에 5명의 학생이 있는 것을 확인

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df.groupby(['학년', '반'])['국어'].mean().round(2))
# 학년  반
# 1   A    76.8
#     B    78.8
#     C    66.0
#     D    59.4
# 2   A    64.6
#     B    81.4
#     C    84.6
#     D    72.0
# 3   A    68.6
#     B    81.4
#     C    73.0
#     D    69.8
# Name: 국어, dtype: float64

# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요. 
print(df.groupby(['학년'])['영어'].mean().round(2))
# 학년
# 1    64.80
# 2    73.35
# 3    69.90
# Name: 영어, dtype: float64

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print("전체 재학생의 평균 수학 점수: ", df['수학'].mean().round(2), "점")
# 전체 재학생의 평균 수학 점수:  68.95 점