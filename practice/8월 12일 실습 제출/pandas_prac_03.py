# 실습 3. 한글·구분자 깨짐 옵션 다루기

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

df_3 = pd.read_csv("PANDAS/data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8")
print(df_3.shape) # (200, 7)
print(df_3.head(4))
