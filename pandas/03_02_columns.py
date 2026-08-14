# 열 이름 확인

import pandas as pd

df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")
df.info()

print(df.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='object')


# -----------------------------------
# 실습 1. 데이터 불러오기와 구조 확인하기
# 목표
# 설비 센서 CSV를 불러와 크기와 열 이름 확인
# 단계

import pandas as pd

# · read_csv로 설비 센서 파일 불러오기
df_prc = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · head로 앞부분, shape로 행·열 크기 확인
print(df_prc.head())
print(df_prc.shape)

# · columns로 열 이름 목록 확인
print(df_prc.columns)

# 예상 결과
# 앞 5행, 크기 (30, 7), 열 이름 목록 출력


# -----------------------------------
# 실습 2. 열 선택하기

# 목표
# 한 열(Series)과 여러 열(DataFrame)을 선택하고 바로 계산
# 단계

import pandas as pd
df_prc = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · 대괄호 한 겹으로 단일 열을 Series로 선택
df_prc['형체력'].info()

# · 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
df_prc[['형체력', '실린더압력']].info()

# · 선택한 열에 mean으로 평균 계산
print(round(df_prc['형체력'].mean(),1))


# 예상 결과
# Series·DataFrame 형태와 형체력 평균 출력


# -----------------------------------
# 실습 3. 공정 센서 열 골라내기

# · 주조 로그 파일 불러오기
# data/13_diecasting_shot.csv 파일 열기
import pandas as pd
df_prc = pd.read_csv("PANDAS/data/13_diecasting_shot.csv")

# · 한 센서 열을 Series로 선택
# '형체력' 선택
df_prc['형체력'].info()


# · 여러 feature 열을 DataFrame으로 선택해 형태 확인
# df[['형체력', '실린더압력', '주조압력']].shape 출력
print(df_prc[['형체력', '실린더압력', '주조압력']].shape) # (200, 3)

