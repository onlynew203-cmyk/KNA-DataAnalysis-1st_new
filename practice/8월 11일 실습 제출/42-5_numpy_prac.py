# 실습 7. 파일 데이터로 기초 통계 구하기
# 목표
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산
# 단계

import numpy as np

# · np.loadtxt로 회전수 열을 파일에서 불러오기
rpm = np.loadtxt('data/10_mct_tool.csv', delimiter=',', skiprows= 1, usecols= 4)
# delimiter= ',' -- 쉼표 구분자를 의미, 컬럼을 나누는 역할
# skiprows= 1 -- 1행을 스킵하는 기능
# usecols= 4 -- 어떤 열을 가져다 쓸지 지정해주는 역할

# · 불러온 배열의 평균과 표준편차 계산
print(round(rpm.mean(), 1)) # 4212.6
print(round(rpm.std(), 1)) # 1144.9

# · 최솟값과 최댓값으로 값의 범위 확인
min_rpm = rpm.min()
max_rpm = rpm.max()

print(min_rpm) # 58.0
print(max_rpm) # 4987.0

print(max_rpm - min_rpm) # 4929.0

# 예상 결과
# 회전수의 평균·표준편차와 최솟값·최댓값이 출력

