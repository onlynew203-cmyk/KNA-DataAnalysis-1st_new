# 실습 8. 필터링과 통계 결합하기
# 목표
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산
# 단계

import numpy as np

# · 토크 배열 준비
torque = np.array([28.5, 35.0, 42.3, 31.8, 47.5, 39.2, 50.1, 33.4])

# · 불리언 인덱싱으로 기준을 넘는 값만 추출
high_t = torque > 40.0
print(high_t) # [False False  True False  True False  True False]
print(torque[torque > 40.0]) # [42.3 47.5 50.1]

# · 추출한 값들의 평균과 개수 계산
print(high_t.sum()) # 3 -- 개수
print(round(torque[high_t].mean(), 1)) # 46.6
