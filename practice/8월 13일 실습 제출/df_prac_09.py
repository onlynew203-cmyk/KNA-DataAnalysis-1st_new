# 실습 9. 첫 탐색 종합
# 데이터를 불러와 구조까지 스스로 파악
# 앞서 배운 불러오기와 구조 파악을 한 번에 적용

import pandas as pd

df_sample = pd.read_csv(
    "PANDAS/data/12_metro_digital.csv",
    encoding= 'utf-8'
)

print(df_sample.head())


print(df_sample.shape)

print(df_sample.columns)

print(df_sample.dtypes)


df_sample.info()

