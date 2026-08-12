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


# ------------------------
# 실습 6. 배열 모양 바꾸기
# 목표
# 한 줄 배열을 값 개수에 맞는 표 모양으로 변환
# 단계
# · 연속 정수 배열을 arange로 생성
numbers = np.arange(6)
print(numbers) # [0 1 2 3 4 5]

# · 값 개수에 맞는 행·열을 정해 reshape로 형태 변환
converted_numbers = numbers.reshape(2, 3)
# · 바뀐 배열 출력
print(converted_numbers)
# [[0 1 2]
#  [3 4 5]]

# 예상 결과
# 여덟 개 값이 2행 4열 표 모양으로 바뀐 배열 출력


# ------------------------
# 실습 7. 센서 데이터 표로 정리하기
# 목표
# 한 줄로 이어진 측정값을 행=시점, 열=센서 표로 정리
# 단계

# · 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
data = np.arange(10)


# · 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
data_reshape = data.reshape(2, 5)

# · 정리된 표 배열 출력
print(data_reshape)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# 예상 결과
# 여섯 개 값이 3행 2열(시점 3 × 센서 2) 표로 정리된 배열 출력


# ------------------------
# 실습 8. 배열 생성부터 정리까지
# 목표
# 배열 생성, 구조 확인, 형태 변환을 하나의 흐름으로 수행
# 단계

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
