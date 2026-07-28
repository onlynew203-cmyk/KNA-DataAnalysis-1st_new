# find() - 코드 예시
# 특정 글자가 처음 나오는 위치(번호)

email = 'hong@company.com' # email 변수 지정
at = email.find('@') # email에서 @를 find -> 위치 번호를 at에 넣음
print(at) # 4 출력
print(email[:at]) # hong 출력 -> email에서 at(4번)의 앞(3번)까지 출력
print(email.find("@")) # 4 출력

# 못 찾았다 -> -1을 출력
print('정상'.find('고장')) # -1 출력 -> '고장'을 '정상'에서 찾지 못함
print('123'.find('2')) # 1 출력 -> 2를 [1]번 자리에서 찾음
print("기계 작동 : 정상".find("정상")) # 8 출력 -> 공백을 포함해서 "정상"의 첫글자 "정"의 위치는 8번째

# ------------------------------------------------------------------------------------
# index() 특정 문자열의 위치(인덱스 번호)를 출력(반환)
# 앞에서부터 가장 처음 나오는 것의 인덱스만 반환
# 찾는 문자열이 없으면 error 발생

email = "hong@gmail.com"
at = email.index("@") # 4 출력
print(email[:at]) # hong 출력 (시작 번호 0 생략)
print(email[at:]) # @gmail.com 출력 (끝까지 출력하고 싶고, 뒤에 몇 글자인지 몰라서 생략)
print(email[at+1:]) # gmail.com 출력
# at+1 -> @를 포함하지 않고 출력

# ------------------------------------------------------------------------------------
print("============== count() ================")

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e, a, a"
print(str.count("a")) # 3 출력
print(str.count(",")) # 6 출력
print(str.count(", ")) # 6 출력
print(str.count(" ,")) # 0 출력 (찾는 문자열과 완전히 동일해야 카운팅)

# ------------------------------------------------------------------------------------
# SQE-00Q8 이라는 설비의 SQE만 뽑아내기 (find와 slicing 사용)
sqe = "SQE-00Q8"
sqe_index = sqe.find("-")
print(sqe_index) # 3

sqe_fin = sqe[:sqe_index]
print(sqe_fin) # SQE 출력

# SQE-00Q8 이라는 설비의 SQE만 뽑아내기 (index 사용)
sqe = "SQE-00Q8"
at = sqe.index("-")
print(sqe[:at]) # SQE 출력


# ------------------------------------------------------------------------------------
print("============== startswith() ================")

# 특정 문자열로 시작하는지 검사
# True/False (bool 타입)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP")) # True

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp)) # True
# 변수명은 따옴표 감싸기 금지 ! !

str = "월요일입니다! 여러분은 할 수 있어요!"
print(str.endswith("!")) # True
print(str.endswith(".")) # False
print(str.endswith("월요일입니다! 여러분은 할 수 있어요!")) # True
print(str.endswith("월요일입니다! 여러분은 할 수 있어요! ")) # False (완전히 같은 문자열만 True)

# 실습 startswith와 endswith
fname = "sensor_log.csv"
print(fname.startswith("sensor")) # True
print(fname.endswith(".csv")) # True

# ------------------------------------------------------------------------------------
print("============== 값은 객체다 ================")

print(type("잊어버리지 말자~!"))
# .으로 연결하는 친구들은 메서드라고 불러여
# 특정 자료형 내부의 포함된 기능들을 의미해요 -> 자료형 타입마다 달라요 (int에는 .startswith 없음)
# len()과 같은 애들은 함수에여 -> 기분 제공 함수 "내장 함수"

# 메서드, 점 문법 예시
word = "python"
print(word.upper()) # PYTHON 출력 / upper = 모두 대문자로
print(word.count("p")) # 1 출력
print(word.startswith("p")) # True 출력

word2 = "rainbow"
word2 = word2.upper() # word에 .upper를 붙여서 재할당! 
print(word2) # RAINBOW

# ------------------------------------------------------------------------------------
# 재할당 복습
str3 = "abcdefg"
print(str3) # abcdefg

str3.upper()
print(str3) # abcdefg

str3 = str3.upper() # 여기서 재할당이 들어갔기 때문에 다음 코드에서 대문자를 볼 수 있음
print(str3) # ABCDEFG

# ---------------------------
# 실습 대문자로 바꾸기
name = "ready"
name = name.upper()
print(name) # READY 출력
# ---------------------------
# 실습 소문자로 바꾸기
name2 = "ALL"
name2 = name2.lower()
print(name2) # all 출력

# ------------------------------------------------------------------------------------
user_name = "kim chul soo"

print(user_name.capitalize()) # Kim chul soo 출력 (capitalize : 첫 글자만 대문자로)
print(user_name.title()) # Kim Chul Soo 출력 (title : 띄어쓰기를 기준으로 각 단어의 첫 글자를 모두 대문자로)

print("i'm full".title()) # I'M Full 출력
print("i'm full".capitalize()) # I'm full 출력

# ---------------------------
# 실습 대소문자 무시하고 비교하기
a = "ALL"
b = "all"
print(a == b) # False 대소문자가 달라요!
print(a.lower() == b.lower()) # True 소문자로 통일 후 비교
print(a.upper() == b.upper()) # True 대문자로 통일 후 비교

# ---------------------------
# 실습 대소문자 검사하기
print("abc".islower()) # True
print("ABC".isupper()) # True
print("Abc".isupper()) # False

# ---------------------------
# 실습 파일명 규칙 한 번에 점검하기
fname = "Sensor_LOG.CSV"
fname = fname.lower()
print(fname.startswith("sensor")) # True
print(fname.endswith(".csv")) # True

# ------------------------------------------------------------------------------------
# strip() 앞뒤 공백 제거
sensor2 = "   정상   "
print('['+ sensor2 +']')
sensor3 = sensor2.strip() # 요거는 스트립을 사용하여 양쪽 공백을 제거한 뒤 재할당 하는 코드
print('['+ sensor3 +']')

# lstrip() -- 왼쪽 공백만 제거
pre = "   왼쪽 공백 제거 연습"
print(pre.lstrip())

# rstrip() -- 오른쪽 공백만 제거
pre2 = "오른쪽 공백 제거 연습   "
print(pre2.rstrip())

# strip()으로 특정 문자 제거
str4 = "===정상==="
print(str4.strip("=")) # 정상 출력

str4 = "===정상==="
print(str4.strip("=  ")) # 정상 출력 -> 공백 상관없이 양 끝에 해당 문자열 삭제

str5 = "====정===상===="
print(str5.strip("=")) # 정===상 출력 -> 앞뒤의 특정 문자만 제거

# ---------------------------
# 실습 특정 문자 제거하기
pre_strip = "***경고***"
print(pre_strip.strip("*"))

# ------------------------------------------------------------------------------------
# strip()로 못 지우는 중간 공백
# 체이닝 == 메서드 연결해서 쓰기

raw = "   NORMAL   "
clear = raw.strip().lower()
print(clear) # normal 출력

# ---------------------------
# 실습 메서드 이어붙이기

raw2 = ' WARNING '
clear = raw2.strip().lower() # 체이닝해서 재할당
print(clear) # warning 출력

print(raw2.strip().lower()) # warning 출력 (재할당 없이)

# ---------------------------
# 실습
str = "    Warning   "
print('[' + str.lower() + ']') # [    warning   ] 출력
print('[' + str.strip().lower() + ']') # [warning] 출력

str2 = "    Warning   "
str2 = str2.strip().lower()
print(str2.capitalize())

str6 = "aabd 연습 cda"
print(str6.strip("abcd ")) # 연습 출력 (괄호 안에 있는 a,b,c,d, (공백)을 str8의 양끝에서 삭제)
print(str6.strip("c")) # aabd 연습 da 출력 (괄호 안에 있는 c는 str8의 양끝이 아닌 중간열에 있어서 삭제하지 않음)
print(str6.strip("ac ")) # bd 연습 cd 출력 (괄호 안에 있는 a,c, (공백) 중, str8의 양끝에서 삭제할 수 있는 것은 a뿐)

# ------------------------------------------------------------------------------------
# replace()로 공백, 기호 제거 - 제거도 할 수 있고 바꾸기도 할 수 있어요!

print("============== replace() ================")
# .replace("바꾸고 싶은 문자열","바꿀 문자열")

# 공백 제거
text_3 = "정 상 가 동"
print(text_3.replace(" ", "")) # 정상가동 출력

# 글자 치환
print("고장".replace("고장", "fault")) # fault 출력
print("고장".replace("고", "fault")) # fault장 출력

# replace() 체이닝
str9 = "설비 정상 가동"
print(str9.replace("정상","점검")) # str9에서 정상을 점검으로 바꿔달라는 코드 -> 설비 점검 가동 출력

num = "  010-1234-1234  "
num = num.replace(" ", "").replace("-", "") # replace 체이닝
print(num) #01012341234 출력

# ------------------------------------------------------------------------------------
# split() 공백을 기준으로 나누기

print("============== split() ================")
# 문자열 자르기
# 결과는 대괄호에 감싸진 list 자료형
# 리스트는 순서가 있기 떄문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성 됩니다

drinks = "에쏘 아아 라떼"
print(drinks.split()) # 인자를 보내지 않음. ['에쏘', '아아', '라떼'] 출력 -> 띄어쓰기를 기준으로 나뉘어진 3개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특정하고 싶은 경우
fruits = "딸기,수박,바나나,사쿠란보"
print(fruits.split(",")) # ['딸기', '수박', '바나나', '사쿠란보'] 출력 -> 문자열 ,를 기준으로 분할

fruits2 = "딸기, 수박, 바나나, 사쿠란보"
print(fruits2.split(",")) # ['딸기', ' 수박', ' 바나나', ' 사쿠란보'] 출력 -> 문자열 ,를 기준으로 분할. 콤마 뒤의 공백을 유지.

fruits2 = "딸기, 수박, 바나나, 사쿠란보"
print(fruits2.split(", ")) # ['딸기', '수박', '바나나', '사쿠란보'] 출력 -> 문자열 ", "기준으로 분할. 공백이 사라짐

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list) # ['딸기', '수박', '바나나', '사쿠란보'] 출력

# 거봉만 출력하기 - 인덱스 활용
print(fruits_list[1]) # 수박 출력
print(fruits_list[-1]) # 사쿠란보 출력

# split 횟수 제한 ! !
num = "010-1234-1234"
# ["010", "1234-1234"]
print(num.split("-", 1)) # split으로 "-"를 기준으로 자를건데, 1번만 잘라 !

# ---------------------------
# 실습 쉼표 기준으로 나누기
text = "a,b,c,d"
print(text.split(',')) # ['a', 'b', 'c', 'd'] 출력

# ------------------------------------------------------------------------------------
print("============== join() ================")
# 리스트를 하나의 문자열로 합침
# "구분자" .join(리스트)

fruits_list = ['딸기', '수박', '바나나', '사쿠란보']

print("-".join(fruits_list)) # 딸기-수박-바나나-사쿠란보 출력
print(",".join(fruits_list)) # 딸기,수박,바나나,사쿠란보 출력
print(", ".join(fruits_list)) # 딸기, 수박, 바나나, 사쿠란보 출력

# ---------------------------
# 실습 
pre3 = "python"
print(pre3.replace("t","T")) # pyThon 출력

# ---------------------------
# 실습 리스트 합치기
list = ["2026","07","15"]
print("-".join(list)) # 2026-07-15 출력

# ------------------------------------------------------------------------------------
# print의 sep, end로 구분자 넣기
print("============== print 함수의 sep, end ================")

print('2026','07','27') # 2026 07 27 출력
print('2026','07','27', sep='-') # 2026-07-27 출력
print('2026','07','27', sep='/') # 2026/07/27 출력
print('2026','07','27', end='!\n') # 2026 07 27! 출력

print("안녕","하세",end="요\n") # 안녕 하세요 (end 속성 사용시, 출력 마지막에 해당 문자열이 붙어서 삽입) (\n 줄바꿈)
# end 속성 뒤에 또다른 인자 넘기기 불가 ! 

# ---------------------------
# 실습 구분자 통째로 바꾸기

text = "2025/01/15"
text2 = text.split("/")
print("-".join(text2)) # 2025-01-15 출력

text = "2025/01/15"
print("-".join(text.split("/"))) # 2025-01-15 출력

# ---------------------------
# 실습 csv 한 줄에서 값 꺼내 정리하기

text = "1, NORMAL, 25.3"
label = text.split(",")
status = label[1].strip().lower()
print(status) # normal 출력

# ------------------------------------------------------------------------------------
# f-string 기본 문법
# f"{}"를 기억하자

name = '길동'
age = 25
print(f'{name}님은 {age}살입니다.') # 길동님은 25살입니다. 출력

# ---------------------------
# 실습 f-string으로 변수 끼워 출력하기
name = "PUMP_A"
temp = 87
print(f"설비 {name}, 온도 {temp}도") # 설비 PUMP_A, 온도 87도 출력

name = "홍길동"
age = 23
print(f"{name} 님은 {age}살 입니다.")
# 따옴표 밖에 f 작성하기
# 변수명은 꼭 {중괄호}에 감싸기
# ------------------------------------------------------------------------------------
# f-string 연산
hour = 8
# 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다 - 출력하기
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분 입니다")

# ---------------------------
# 실습 f-string 안에서 계산하기
one = 10
two = 41
three = 32
print(f"평균 {(one + two + three)/3}") # 평균 27.666666666666668
print(f"평균 {(one + two + three)/3:.2f}") # 평균 27.67

# ---------------------------
# 실습 소수점 자릿수 지정하기
a = 87.456
print(f"{a:.1f}") # 87.5 출력
print(f"{a:.2f}") # 87.46 출력

# ---------------------------
# 실습 센서 로그 한 줄 정리 리포트 만들기
b = "5,sensor_2,WARNING,0.78912"
b4 = b.split(",")
sensor4 = b4[1]
state4 = b4[2].lower()
rate4 = float(b4[3].strip())
print(f"[센서 {sensor4}] 상태 {state4}, 측정값{rate4:.2f}")