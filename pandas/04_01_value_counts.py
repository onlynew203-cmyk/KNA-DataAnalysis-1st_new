import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')

df.info()

df_old = df[df['냉각기상태'] == '고장']
print(len(df_old)) # 40 출력

# 이 방식으로 모든 상태를 찾아 통계 내는 것은 비효율
# 모든 경우의 카테고리별 갯수 세기
# value_counts

# 냉각기 상태별 사이클 건수를 세기
print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40


# result 컬럼의 정상/고장 건수 세기
print(df['result'].value_counts())
# result
# 정상    67
# 고장    53


# 케이스마다의 비율 알아보기
# 정규화 (normalize)
print(df['result'].value_counts(normalize=True))
# result
# 정상    0.558333
# 고장    0.441667


# 정규화 비율 결과는 Round 처리할때가 많음
print(df['result'].value_counts(normalize=True).round(3))
# result
# 정상    0.558
# 고장    0.442
