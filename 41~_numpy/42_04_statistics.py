import numpy as np

# 합계와 평균(mean)
s = np.array([70, 71, 72, 73, 74, 199])
print(s.sum()) # 559 합계
print(s.mean()) # 93.16666666666667 평균

# 중앙값(median)
print(np.median(s)) # 72.5 중앙값

# 이상치에 흔들리는 평균값과는 다르게, 중앙값은 이상치에 흔들리지 않음
# 평균과 중앙값이 크게 다르면 이상치가 있다는 신호

# 최대/최소 범위
print(s.max()) # 199 - 최대
print(s.min()) # 70 - 최소
print(s.max() - s.min()) # 129 - 범위

# 분산 -------------------------------------------------
# 값들이 평균에서 흩어진 정도를 하나의 숫자로

stable = np.array([70, 71, 72, 70, 71])
unstable = np.array([60, 80, 62, 90, 70])


print(stable.var()) # 0.559999
print(round(stable.var(), 2)) # 0.56

print(unstable.var()) # 127.04


# 표준편차 -------------------------------------------------
# 분산의 제곱근— 원래 단위로 흩어진 정도 표현

s2 = np.array([70, 71, 72, 70, 71, 99])
print(round(s.var(), 2)) # 2241.81 -- 분산 값
print(round(s.std(), 2)) # 47.35 -- 표준편차


# axis 개념 -------------------------------------------------
mat = np.array([
    [70, 2.1],
    [72, 3.5],
])

# mat.mean() → 전체 평균
print(mat.mean()) # 36.9

# axis=0 → 세로 방향 ↓ 열의 평균
print(mat.mean(axis= 0)) # [71.   2.8]
    #  ↓       ↓
    # 70      2.1
    # 72      3.5
    # ──      ───
    # 71      2.8

# axis=1 → 가로 방향 → 행의 평균
print(mat.mean(axis= 1)) # [36.05 37.75]
# [70, 2.1] → (70 + 2.1) / 2 = 36.05
# [72, 3.5] → (72 + 3.5) / 2 = 37.75


# -----------------------
# 실습 6. 센서별 기초 통계 구하기
# 목표
# 표 모양 데이터에서 센서별(열별) 통계 계산
# 단계

# · 여러 설비의 회전수·토크 이차원 배열 준비
sensor_data = np.array([
    [1200, 35.0],
    [1300, 38.0],
    [1400, 40.0],
    [1500, 42.0],
    [1600, 45.0]
])

# · axis를 열 방향으로 지정해 센서별 평균 계산
print(sensor_data.mean(axis= 0)) # [1400.   40.]

# · 센서별 표준편차 계산
print(round(sensor_data.std(), 2)) # 687.32

# 예상 결과
# 회전수·토크 각각의 평균과 표준편차가 출력

# -----------------------
# 실습 7. 파일 데이터로 기초 통계 구하기
# 목표
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산
# 단계
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


# -----------------------
# 실습 8. 필터링과 통계 결합하기
# 목표
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산
# 단계
# · 토크 배열 준비
torque = np.array([28.5, 35.0, 42.3, 31.8, 47.5, 39.2, 50.1, 33.4])

# · 불리언 인덱싱으로 기준을 넘는 값만 추출
high_t = torque > 40.0
print(high_t) # [False False  True False  True False  True False]
print(torque[torque > 40.0]) # [42.3 47.5 50.1]

# · 추출한 값들의 평균과 개수 계산
print(high_t.sum()) # 3 -- 개수
print(round(torque[high_t].mean(), 1)) # 46.6



# 예상 결과
# 기준 초과 값들의 평균과 개수가 출력


# -----------------------
# 실습 9. NumPy 기초 종합 분석
# 목표
# 데이터 불러오기, 구조 확인, 필터링, 통계를 하나의 흐름으로 수행
# 단계
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

