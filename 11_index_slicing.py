# index
word = "PYTHON"
print(word[0]) # P
print(word[2]) # T
print(word[5]) # N

# 음수 index
word = "PYTHON"
print(word[-1]) # N
print(word[-2]) # O

# 인덱스 범위를 벗어나면 - IndexError 발생

# ==================================================
# 슬라이싱 문법
# word[0:3] -> word의 인덱싱 [0]부터 [3]의 앞까지 = 0부터 2까지
word = "python"
print(word[0:2]) # py 출력

code = 'EQP-001'
print(code[1:4]) # QP- 출력
print(code[-3:-1]) # 00 출력
print(code[0:1]) # E 출력 (0부터 0까지 = 0만 출력 = E 출력)

# ----------------------------------------------------
# 실습 - 슬라이싱
word = "PYTHON"
print(word[0:3]) # PYT 출력
print(word[2:5]) # THO 출력
print(word[-4:-1]) # THO 출력

# ----------------------------------------------------
# 슬라이싱 - start 생략
# 시작을 비우면 0부터 라는 뜻
word = "PYTHON"
print(word[0:3]) # PYT 출력
print(word[:3]) # PYT 출력

# 슬라이싱 - end 생략
# 끝을 비우면 마지막 글자까지 가져온다는 뜻
word = 'PYTHON'
print(word[3:]) # HON 출력

# 슬라이싱 - 앞뒤 생략
# 전체를 모두 가져오라는 뜻
word = 'PYTHON'
print(word[:]) # PYTHON 출력

# ----------------------------------------------------
# 실습 - [:n] start 생략
word = 'temp_sensor'
print(word[:4]) # temp 출력

# 실습 - [:n] end 생략
word = 'temp_sensor'
print(word[5:]) # sensor 출력

# 실습 - [-n:] 음수 슬라이싱 (뒤 n글자)
word = 'sensor_01'
print(word[-2:]) # 01 출력

# ==================================================
#