# else와 finally 코드

# text = "24.5" # 정상 출력됨

# 비정상 해결해보자
text = "뭠마!"
temp = 0

try :
    temp = float(text)
    print(temp * 2)
except ValueError:
    print("야야 큰일났다: 밸류에러")
except NameError:
    print("야야 큰일났다: 네임에러")
finally:
    # 오류가 있건 없건 finally의 코드를 실행하고 마무리 된다
    print(temp * 2)

# -------------------------
# 실습 1. finally로 파일 안전하게 닫기
# ① try 블록에서 파일을 열어 처리
# ② 처리 도중 오류가 날 수 있음을 가정
# ③ finally 블록에 close를 넣어 오류 여부와 상관없이 닫기
# ④ 일부러 오류를 내도 finally가 실행되는지 확인

num = input("숫자를 입력하세요 :")

try:
    num = int(num)
    print(f"{num}의 2배 = {num * 2}")
except ValueError:
    print("숫자가 아닙니다.")
except NameError:
    print("올바른 값을 입력하세요.")
finally:
    print("프로그램 종료")