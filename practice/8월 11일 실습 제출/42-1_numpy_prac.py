# 실습 3. 센서값 정규화하기
# 목표
# 회전수 배열을 0과 1 사이 값으로 정규화
# 단계

import numpy as np
# · 회전수 측정 배열 준비
rpm = np.array([1200, 1300, 1500, 1400, 1600, 1800])

# · 최솟값과 최댓값을 min, max로 확인
print(rpm.min()) # 1200
print(rpm.max()) # 1800

# · 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화 된 x = (비교 대상 - 최소값) / (최대값 - 최소값)
rpm_min = rpm.min()
rpm_max = rpm.max()

normalized = (rpm - rpm_min) / (rpm_max - rpm_min)
print(normalized) # [0.         0.16666667 0.5        0.33333333 0.66666667 1.        ]
print(np.round(normalized, 2)) # [0.   0.17 0.5  0.33 0.67 1.  ]

# 예상 결과
# 가장 작은 값이 0, 가장 큰 값이 1이 되는 정규화 배열 출력