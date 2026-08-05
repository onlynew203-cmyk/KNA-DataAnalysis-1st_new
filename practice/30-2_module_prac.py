# 실습 2. 표준 라이브러리로 센서값 만들기
# ① random 모듈을 import
# ② randint로 무작위 센서값을 만들어 출력
# ③ math 모듈로 그 값을 가공(제곱근)
# ④ 다시 실행하면 값이 달라지는지 확인

import random
import math

a = random.randint(1, 10) # 1~10 범위의 정수 랜덤 뽑기
print(a) # 4

result = math.sqrt(a)
print(round(result, 2)) # 2.0


