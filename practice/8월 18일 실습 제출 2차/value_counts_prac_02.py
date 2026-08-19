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