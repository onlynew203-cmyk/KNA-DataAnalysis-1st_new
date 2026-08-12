import numpy as np
# 비교 연산과 불리언 배열
v = np.array([1,2,3,4,5])
print(v > 3) # [False False False  True  True] 출력

# 불리언 인덱싱
# 불리언 배열로 조건에 맞는 값만 골라내기
print(v[v > 3]) # [4 5]

# np.where 조건 처리 -------------------------------------------
# 조건에 따라 값을 둘 중 하나로 바꾸기— 조건·참·거짓 세 가지 인자

# true 일땐 1, false 일땐 0으로 보여줘 !
print(np.where(v > 3, 1, 0)) # [0 0 0 1 1]

# true 일땐 0, false 일땐 9으로 보여줘 !
print(np.where(v > 3, 0, 9)) # [9 9 9 0 0]


# 다중 조건 결합 -------------------------------------------
print(v) # [1 2 3 4 5]

v_step1 = v[v > 2] # v에서 걸러낼게, 2보다 큰 애들 걸러서 v_step1에 넣어
print(v_step1) # [3 4 5]

v_step2 = v_step1[v_step1 < 4] # v_step1에서 한번 더 걸러낼게, 4보다 작은 애들 v_step2에 넣어
print(v_step2) # [3]

v_mixed = v[(v > 2) & (v < 4)]
print(v_mixed)

# 참고, 조건 대신 true를 직접 준다면?
print(v[True]) # [[70 95 71 88 73]]


# -----------------------
# 실습 4. 이상 센서값 필터링하기
# 목표
# 조건에 맞는 이상 센서값만 불리언 인덱싱으로 선별
# 단계
# · 회전수와 토크 배열 준비
rpm = np.array([1200, 1350, 1600, 1450, 1800, 1300, 1700])
torque = np.array([35.2, 32.5, 28.0, 40.1, 25.5, 38.0, 31.0])

# · 비교 연산으로 회전수가 기준을 넘는 조건 생성
print(rpm[rpm > 1500]) # 1500 이상
print(torque[torque > 40.0])

# · 다중 조건으로 회전수 과다 또는 토크 과소 위험 시점 필터링
print((rpm > 1500) | (torque > 40.0)) # [False False  True  True  True False  True]
print((rpm > 1500) & (torque > 30.0)) # [False False False False False False  True]

# 예상 결과
# 기준 초과 회전수 값과, 위험 조건을 만족하는 위치가 출력

# -----------------------
# 실습 5. 조건별 개수와 비율 세기
# 목표
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산
# 단계
# · 토크 배열 준비
torque = np.array([35.2, 32.5, 28.0, 40.1, 25.5, 38.0, 31.0, 42.3, 41.8, 39.9, 30.7])

# · 비교 조건으로 참·거짓 불리언 배열 생성
op_high = torque > 35.0
print(op_high) # [ True False False  True False  True False  True  True  True False]

# 인덱싱 자리에 조건을 넣어야 해당하는 값을 확인할 수 있다
print(torque[torque > 35.0]) # [35.2 40.1 38.  42.3 41.8 39.9]

# · 불리언 배열의 합으로 개수, 평균으로 비율 계산
print(op_high.sum()) # 6 출력 --> 해당하는 값의 개수
print(round(op_high.mean(), 2)) # 0.55 출력


# 예상 결과
# 조건을 만족하는 값의 개수와 비율이 출력

