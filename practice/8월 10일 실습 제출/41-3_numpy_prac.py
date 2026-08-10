# 실습 5. 자료형 확인과 변환하기
# 목표
# 배열의 자료형을 확인하고 정수형으로 변환
# 단계
# · 소수점이 있는 측정값 배열 준비
# · dtype으로 현재 자료형 확인
# · astype으로 정수형으로 변환한 새 배열 출력
# 예상 결과
# 자료형 float64 확인, 소수점이 잘린 정수 배열 출력

import numpy as np

data = np.array([1234.242, 2356.448, 7441.392])

print(data.ndim)
print(data.shape)
print(data.dtype) # float64

converted_data = data.astype(int)
print(converted_data.dtype) # int64
