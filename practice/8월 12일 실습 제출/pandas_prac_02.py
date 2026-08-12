# 실습 2. 설비 센서 CSV 불러오기

# read_csv로 데이터를 불러와 head로 확인

# 12_metro_compressor.csv
# 200행 7열— 인덱스 3번 행 오일온도가 NaN

import pandas as pd

df = pd.read_csv("PANDAS/data/12_metro_compressor.csv", encoding="utf-8")
print(df.head(5))
print(df.shape) # (200, 7)