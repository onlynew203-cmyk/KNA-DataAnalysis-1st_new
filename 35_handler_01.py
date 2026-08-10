# 트레이스백으로 에러 읽기
# -----------------------------
# valueError: 글자를 숫자로 변환 요구
# temp = int("스물") # ValueError: invalid literal for int() with base 10: '스물

# 정상화
temp = int("12")

print("=" * 20)

# -----------------------------
# ZeroDivisionError
# result = 10 / 0 # ZeroDivisionError: division by zero

# 정상화
result = 10 / 3

# -----------------------------
# NameError : 그런 이름도 있었어요?라는 에러
# hello() # NameError: name 'hello' is not defined



