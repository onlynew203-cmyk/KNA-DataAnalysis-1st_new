# 1차원 슬라이싱

# 시작: 끝으로 구간 잘라내기 (끝 번호 제외)

import numpy as np

temp = np.array([12,13,14,15,16,17])

print(temp) # [12 13 14 15 16 17]

print(temp[0:2]) # [12 13]
print(temp[-1:]) # [17]
print(temp[:-1]) # [12 13 14 15 16]

print(temp[::2]) # [12 14 16] --> 0부터 간격 2
print(temp[2::2]) # [14 16] --> 2부터 간격 2

