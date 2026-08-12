# reshape로 형태 바꾸기
# size로 확인되는 값 개수는 같아야 한다 !! 

import numpy as np

under_ten = np.arange(10)
print(under_ten) # [0 1 2 3 4 5 6 7 8 9]
print("nidm:", under_ten.ndim) # nidm: 1
print("shape:", under_ten.shape) # shape: (10,)
print("size:", under_ten.size) # size: 10

reshape_ten = under_ten.reshape(2, 5) # 값 10개짜리를 2행 5열로 바꿈. 값은 그대로고 모양만 변함.
print(reshape_ten)
# [[0 1 2 3 4]
#  [5 6 7 8 9]] 출력


# --------------------------------------------------------------------
# flatten으로 1차원 만들기
# 표 모양을 한 줄로 펴기— 위 행부터 왼쪽에서 오른쪽으로

flatten_ten = reshape_ten.flatten
print(flatten_ten)


