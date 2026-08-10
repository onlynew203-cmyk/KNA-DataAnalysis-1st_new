# 실습 7. 센서 데이터 표로 정리하기
# 목표
# 한 줄로 이어진 측정값을 행=시점, 열=센서 표로 정리
# 단계

import numpy as np

# · 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
data = np.array(
    [
    [12, 34], 
    [23, 56], 
    [74, 41], 
    [92, 72]
    ])


# · 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
data_reshape = data.reshape(4, 2)

# · 정리된 표 배열 출력
print(data_reshape)
# [[12 34]
#  [23 56]
#  [74 41]
#  [92 72]]
