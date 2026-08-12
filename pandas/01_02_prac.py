# 실습 1. CSV 불러오기 워밍업

import pandas as pd
import os

# CSV를 DataFrame으로 — 분석의 시작
# df = pd.read_csv("data/12_metro_compressor.csv")
# df.head()

# 괄호 안에 파일 이름을 따옴표로 감싸 넣으면 Pandas가 읽어 DataFrame으로 돌려줌— 결과를 df에 담음
file_path = os.path.join("PANDAS", "data", "12_metro_small.csv")

# read_csv 결과는 반드시 변수에
# read_csv 결과를 변수에 안 담으면 읽은 데이터가 사라짐
df_small = pd.read_csv(file_path)
print(df_small.shape) # (30, 7)
print(df_small.head()) # 첫 줄부터 5줄을 불러오기

try :
    df_small = pd.read_csv(file_path)
    print(df_small.shape)

except FileNotFoundError:
    print(f"파일이 없습니다 : {df_small}")


# read_csv 옵션— encoding
# 한글 안 깨지게 인코딩 지정
df = pd.read_csv("data.csv", encoding="utf-8-sig")

