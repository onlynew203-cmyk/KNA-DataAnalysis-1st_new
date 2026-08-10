# 실습 3. 구체적 예외로 입력 검증하기
# ① 입력을 int로 바꾸는 코드를 try에 넣기
# ② ValueError를 except로 잡아 안내
# ③ 여러 except로 ZeroDivisionError도 구분해 처리
# ④ 잘못된 입력을 넣어 프로그램이 멈추지 않는지 확인

total = input("전체 값을 입력하세요 :")
divisor = input("나눌 값을 입력하세요 :")
result = 0 

try:
    result = int(total) / int(divisor)
    print("결과 값:", result)
except ValueError: # ValueError 상황이라면 여기로 예외처리 하라는 코드
    print("숫자 아니면 왜 저를 부르셨나요")
except ZeroDivisionError:
    print("ZeroDivisionError 발생, 중단")