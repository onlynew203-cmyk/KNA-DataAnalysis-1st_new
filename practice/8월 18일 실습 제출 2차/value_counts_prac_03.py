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