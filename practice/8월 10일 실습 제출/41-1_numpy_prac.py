# 실습 1. 센서값 배열 만들기
# 목표
# 섭씨 센서값 리스트를 배열로 만들고 화씨 단위로 한 번에 변환
# 단계
# · 섭씨 측정값 리스트를 np.array로 배열 생성
# · 배열에 곱셈과 덧셈을 묶음 연산으로 적용해 화씨로 변환
# · 변환된 배열 출력
# 예상 결과
# 섭씨 네 개 값이 화씨 네 개 값으로 한 번에 바뀐 배열 출력

# 섭씨 → 화씨
# °F = °C × 1.8 + 32
# 섭씨 → Celsius → °C
# 화씨 → Fahrenheit → °F

import numpy as np

celsius = np.array([32, 48, -9])
fahrenheit = (celsius * 1.8) + 32

print(fahrenheit) # [ 89.6 118.4  15.8]