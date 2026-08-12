# 실습 5. 경로·옵션 오류 고치기

# 경로· 철자· 확장자
# data/ 누락, 철자, .csv 누락— 세 종류의 FileNotFoundError

import pandas as pd

# 파일 이름 오류
# df_5 = pd.read_csv("PANDAS/data/잘못된_파일_이름.csv")
# print(df_5.shape) # FileNotFoundError: [Errno 2] No such file or directory: '잘못된파일.csv'

# 누락
# df_5 = pd.read_csv("PANDAS/12_metro_digital.csv") # data/ -- 누락

# .csv 누락
# df_5 = pd.read_csv("PANDAS/data/12_metro_digital")