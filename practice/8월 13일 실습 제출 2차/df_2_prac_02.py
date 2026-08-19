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