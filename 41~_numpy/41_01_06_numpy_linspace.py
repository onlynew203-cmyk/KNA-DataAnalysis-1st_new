import numpy as np

# linspace
# 개수 중신 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확히 나눕니다
# NumPy에서 시작값부터 끝값까지 일정한 간격으로 숫자를 만들어주는 함수
# np.linspace(시작값, 끝값, 개수)

# 0부터 1까지 5개로 나눠
div_five = np.linspace(0, 1, 5)
print(div_five) # [0.   0.25 0.5  0.75 1.  ]
