# 실습 1. import 세방식으로모듈가져오기
# ① import 모듈명으로 통째로 가져와 모듈명.기능() 으로 사용
# ② from 모듈 import 기능 으로 일부만 가져와 모듈명 없이 사용
# ③ import 모듈 as 별명 으로 별명.기능() 으로 사용
# ④ 세 방식의 출력이 같은지 확인

# 방식 1. import 모듈명으로 통째로 가져오기
import math

result = math.sqrt(16)
print(result)

# 방식 2. from 모듈 import 기능으로 일부만 가져오기
from math import sqrt

result = sqrt(16)
print(result) # 4.0

# 방식 3. import 모듈 as 별명
import math as mt

result = mt.sqrt(16)
print(result) # 4.0