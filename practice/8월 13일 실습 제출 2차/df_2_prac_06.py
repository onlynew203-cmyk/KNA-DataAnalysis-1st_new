# 실습 6. 특정 구간 추출 종합
# 목표
# 열 선택·loc·iloc를 결합해 특정 구간을 추출하는 종합
# 단계
import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

df_shot = pd.read_csv("PANDAS/data/13_diecasting_shot.csv")

# · 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
feature = ['실린더압력','주조압력','사이클타임','비스킷두께','형체력']
print(df_shot[feature].iloc[0:10].shape) # (10, 5)

# · loc 라벨 범위로 두 열 구간 추출
print(df_shot.loc[0:10, ['실린더압력', '주조압력']].shape)  # (11, 2)

# · iloc 위치 범위로 앞쪽 열 구간 추출
print(df_shot.iloc[0:10, 0:6].shape)  # (10, 6)

# 예상 결과
# (10, 5)·(11, 2)·(10, 6) 출력