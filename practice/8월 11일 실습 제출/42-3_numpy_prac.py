# 실습 5. 조건별 개수와 비율 세기
# 목표
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산
# 단계

import numpy as np
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
