# 실습 4. 필요한 열만 골라 불러오기

# 센서 3개만 골라 불러오기
# usecols=[...]

import pandas as pd

df_4 = pd.read_csv("PANDAS/data/12_metro_compressor.csv",
                   usecols=['측정시각','오일온도','가동상태'],
                   encoding="utf-8")
print(df_4.shape) # (200, 3)
print(df_4.head(2))