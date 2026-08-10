# 실습 6. 배열 모양 바꾸기
# 목표
# 한 줄 배열을 값 개수에 맞는 표 모양으로 변환
# 단계

import numpy as np

# · 연속 정수 배열을 arange로 생성
data = np.array([12, 34, 23, 56, 74, 41, 92, 72])

# · 값 개수에 맞는 행·열을 정해 reshape로 형태 변환
converted_data = data.reshape(2, 4)

# · 바뀐 배열 출력
print(converted_data)
# [[12 34 23 56]
#  [74 41 92 72]]