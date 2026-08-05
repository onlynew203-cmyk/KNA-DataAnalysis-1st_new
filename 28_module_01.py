# 수학 관련 모듈을 불러옵니다
import math

# 수학 관련 모듈에서 sqrt 기능만 불러옵니다
from math import sqrt

# 해당 모듈이름.함수() 식으로 호출해야한다
result = math.sqrt(16)
print(result)

# 이젠 sqrt만 불러도 됩니다
result = sqrt(16)
print(result) # 4.0

# math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다
import math as mt # math를 이제 mt로 쓸거야 -->이제 math 쓰면 오류나요

# 별칭으로 가져온 모듈 이름을 언급해봅시다
result = mt.sqrt(16)
print(result) # 4.0

# datetime 모듈을 가져옵니다
import datetime
# datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다
now = datetime.datetime.now()
print(now) # 2026-08-05 11:20:04.444093
print(type(now)) # <class 'datetime.datetime'>