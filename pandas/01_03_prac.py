# 실습 2. 설비 센서 CSV 불러오기

# read_csv로 데이터를 불러와 head로 확인

# 12_metro_compressor.csv
# 200행 7열— 인덱스 3번 행 오일온도가 NaN

import pandas as pd

df = pd.read_csv("PANDAS/data/12_metro_compressor.csv", encoding="utf-8")
print(df.head(5))
print(df.shape) # (200, 7)

# -----------------------------------
# 실습 3. 한글·구분자 깨짐 옵션 다루기

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

df_3 = pd.read_csv("PANDAS/data/12_metro_compressor_semicolon.csv", sep=";", encoding="utf-8")
print(df_3.shape) # (200, 7)
print(df_3.head(4))


# -----------------------------------
# 실습 4. 필요한 열만 골라 불러오기

# 센서 3개만 골라 불러오기
# usecols=[...]

import pandas as pd

df_4 = pd.read_csv("PANDAS/data/12_metro_compressor.csv",
                   usecols=['측정시각','오일온도','가동상태'],
                   encoding="utf-8")
print(df_4.shape) # (200, 3)
print(df_4.head(2))


# -----------------------------------
# 실습 5. 경로·옵션 오류 고치기

# 경로· 철자· 확장자
# data/ 누락, 철자, .csv 누락— 세 종류의 FileNotFoundError

import pandas as pd

# df_5 = pd.read_csv("잘못된파일.csv")
# print(df_5.shape) # FileNotFoundError: [Errno 2] No such file or directory: '잘못된파일.csv'


# -----------------------------------
# 실습 6. read_csv 옵션 종합 연습
# G O A L 경로· 인코딩· 구분자· 열 선택을 한 번에 적용

# 세미콜론+한글 파일에서 필요한 열만
# sep + encoding + usecols → 200행 3열

# 여러 옵션을 함께 써서 shape 확인

# -------------------------------------
# 파일 : data 폴더 안의 12_metro_compressor_semicolon.csv
# sep를 잘 사용해서 여러 컬럼이 읽히도록 해주세요
# encoding도 지정해주세요
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요

import pandas as pd

df_6 = pd.read_csv("PANDAS/data/12_metro_compressor_semicolon.csv", 
                   sep= ";", 
                   encoding= "utf-8",
                   usecols= ["측정시각", "오일온도", "모터전류"])

print(df_6.head(5))
