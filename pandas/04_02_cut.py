import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')

print(df['온도'].value_counts())

# pd.cut로 범위를 설정하기
band = pd.cut(df['온도'], bins=[0, 40, 50, 200], labels=['낮음', '보통', '높음'])
# bins로 설정한 구간에 따라 라벨을 하나씩 붙인다
# 0-40 : 낮음, 40-50 : 보통, 50-200 : 높음

print(band.value_counts())
# 온도
# 낮음    41
# 보통    40
# 높음    39

# -----------------------
# 실습 1. value_counts로 빈도 세기
# 한 열을 골라 value_counts로 값별 개수 세기
# 목표
# 한 열의 값별 개수를 세어 데이터 구성 파악

import pandas as pd

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')

df.info()

# 단계
# · 설비 데이터를 불러와 앞부분과 구조 확인
# · 설비 열에 value_counts를 붙여 값별 개수 세기
print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40

# · 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print(df['운전부하'].value_counts())
# 운전부하
# 고부하    60
# 저부하    60


# 예상 결과
# 설비별·교대별 빈도표 출력 (심각 42건이 최다)  # x



# -----------------------
# 실습 2. 비율과 불균형 데이터
# qc 합격·불합격 빈도와 비율로 불균형 확인
# 목표
# 합격·불합격 빈도와 비율을 구해 불균형 데이터 확인
import pandas as pd

df_qc = pd.read_csv("PANDAS/data/14_hydraulic_qc.csv",
                 encoding='utf-8')

df_qc.info()
print(df_qc.head(3))
# 검사결과  지표01   지표02    지표03  ...  지표07    지표08  지표09  지표10
# 0   합격  44.7  0.615  159.01  ...  59.7  107.93  1.81  49.7
# 1   합격  41.9  0.611  159.55  ...  59.4  108.37  1.87  48.1
# 2   합격  40.1  0.599  159.87  ...  59.4  108.61  1.92  46.2

# 단계
# · 공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기
print(df_qc['검사결과'].value_counts())
# 검사결과
# 합격     188
# 불합격     12

# · normalize 옵션으로 각 값의 비율을 소수로 확인
print(df_qc['검사결과'].value_counts(normalize=True))
# 검사결과
# 합격     0.94
# 불합격    0.06

# · round로 비율을 소수점 셋째 자리까지 정리
print(df_qc['검사결과'].value_counts(normalize=True).round(1))

# 예상 결과
# 불합격이 전체 약 6%인 불균형 확인


# pd.cut로 지표01에 대한 범위를 설정 해보기
band_prac = pd.cut(df_qc['지표01'], bins=[0, 35, 50, 100], labels=['낮음', '보통', '높음'])
print(band_prac.value_counts())
# 지표01
# 보통    188
# 높음     12
# 낮음      0

# value == '보통'의 비율을 계산해보기
print(band_prac.value_counts(normalize=True)['보통']) # 0.94




# -----------------------
# 실습 3. 구간으로 묶어 세기
# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기
# 목표
# 수치형 센서 값을 구간으로 나눠 분포 확인
import pandas as pd
import numpy as np

df = pd.read_csv("PANDAS/data/14_hydraulic.csv",
                 encoding='utf-8')

print(df.head())

# 단계
# · 진동 열의 최솟값과 최댓값으로 값의 범위 확인
print(df['진동'].max()) # 0.779
print(df['진동'].min()) # 0.53


# · pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
band_prac_2 = pd.cut(df['진동'], bins= [0.0, 0.6, 0.7, 10.0], labels= ['약함', '보통', '강함'])

# · 묶은 구간에 value_counts로 구간별 빈도 세기
print(band_prac_2.value_counts(normalize=True).round(2))
# 진동
# 보통    0.46
# 약함    0.40
# 강함    0.14

# value == '약함'만 비율 출력
print(band_prac_2.value_counts(normalize=True)['약함']) # 0.4



# 예상 결과
# 약함·보통·강함 구간별 빈도 출력 (보통 43건 최다)