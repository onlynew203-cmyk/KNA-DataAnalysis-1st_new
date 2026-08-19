# 실습 5. loc·iloc로 행·열 동시 선택하기
# 목표
# 행과 열을 동시에 지정해 원하는 부분만 추출
# 단계
import pandas as pd
df = pd.read_csv("PANDAS/data/13_diecasting_small.csv")

# · loc로 행 범위와 열 이름을 함께 지정
result_1 = df.loc[0:4, ['실린더압력', '형체력']]

# 1. loc로 0~4번 행 + 두 개 열 선택
result_1 = df.loc[0:4, ['실린더압력', '형체력']]

print(result_1)
print(result_1.shape)  # (5, 2)

# · 다른 행 범위에서 세 열 선택
# 2. loc로 5~9번 행 + 세 개 열 선택
result_2 = df.loc[5:9, ['실린더압력', '형체력', '품질등급']]

print(result_2)
print(result_2.shape)  # (5, 3)

# · iloc 음수 인덱스로 마지막 행 선택
print(df.iloc[-3:])

# 예상 결과
# (5, 2)·(5, 3)·마지막 3행 출력