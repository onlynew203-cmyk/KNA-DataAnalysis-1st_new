# 실습 2. head·tail 행 개수 조절

import pandas as pd

df_2 = pd.read_csv("PANDAS/data/12_metro_small.csv",
                 encoding= 'utf-8')

print(df_2.head(10))
print(df_2.tail(25))