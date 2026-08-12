# 실습 2번 같이 풀어보기

origin = input("온도 :")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except:
    print("숫자 아니면 왜 저를 부르셨나요")

next_temp = temp + 10

print(f"10도만 더 높으면 {next_temp}")


#  ----

try:
    temp = int(origin)
except ValueError: # ValueError 상황이라면 여기로 예외처리 하라는 코드
    print("숫자 아니면 왜 저를 부르셨나요")
except TypeError: # TypeError의 경우는 이렇게
    print("타입 에러 발생")

