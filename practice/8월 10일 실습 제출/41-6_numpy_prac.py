# 실습 8. 배열 생성부터 정리까지
# 목표
# 배열 생성, 구조 확인, 형태 변환을 하나의 흐름으로 수행
# 단계

import numpy as np

# · 센서 측정값을 np.array로 배열 생성
data_2 = np.array([4.1, 3.6, 8.2, 4.7, 2.9, 1.1])

# · shape과 dtype으로 구조 확인
print(data_2.shape)
print(data_2.dtype) # float64

# · reshape으로 분석용 표 형태로 정리한 뒤 출력
data_2_reshape = data_2.reshape(3, 2)
print(data_2_reshape)
# [[4.1 3.6]
#  [8.2 4.7]
#  [2.9 1.1]]


# 예상 결과
# 형태와 자료형 확인 후 3행 2열 표로 정리된 배열 출력