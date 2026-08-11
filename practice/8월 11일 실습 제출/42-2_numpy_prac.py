# 실습 4. 이상 센서값 필터링하기
# 목표
# 조건에 맞는 이상 센서값만 불리언 인덱싱으로 선별
# 단계

import numpy as np
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
