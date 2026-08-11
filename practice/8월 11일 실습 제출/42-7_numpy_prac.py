# 실습 9. NumPy 기초 종합 분석
# 목표
# 데이터 불러오기, 구조 확인, 필터링, 통계를 하나의 흐름으로 수행
# 단계

import numpy as np

# · np.loadtxt로 회전수와 토크 두 열을 불러오기
data = np.loadtxt('data/10_mct_tool.csv', delimiter=',', skiprows= 1, usecols= (4, 5))

# · shape과 dtype으로 구조 확인
print(data.shape, data.dtype) # (40, 2) float64


# · 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm = data[:, 0]
low_data = rpm[rpm < 1200]
print(low_data.size, round(low_data.mean(), 1)) # 1 58.0 출력

# 예상 결과
# 데이터 구조, 이상 시점 개수, 이상 시점 평균 회전수가 출력