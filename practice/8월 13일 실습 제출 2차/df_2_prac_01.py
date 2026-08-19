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
