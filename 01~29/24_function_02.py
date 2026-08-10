# 인삿말 출력 함수 간단 버전
def say_hello():
    print("hello")

say_hello() # hello

# ---------------------------------------------------
# 함수의 매개변수 활용
# 하나의 함수를 그릇처럼 활용해요

def say_hello(name):
    print(f"hello, {name}")

say_hello("Ned") # hello, Ned
say_hello("Tina") # hello, Tina

# 예제
# 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name} 장비의 점검을 시작합니다")

check("압축기A") # 압축기A 장비의 점검을 시작합니다


# 매개변수가 2개 이상인 예제 - 덧셈
def calc_sum(num_a, num_b):
    total = num_a + num_b
    print(f"{num_a} + {num_b} = {total}")

calc_sum(1, 2) # 1 + 2 = 3


# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
# step 1.
def report():
    print("압축기 A의 온도는 75.3도 입니다.")
report()

# step 2.
def report():
    name = "압축기 A"
    temp = 75.3
    print(f"{name}의 온도는 {temp}도 입니다.")
report()

# step 3.
def report(name, temp):
    # name = "압축기 A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도 입니다.")
report("압축기 A", 75.3)
report("펌프", 22.8)

# --------------------------
# 실습 2. 다중 매개변수로 센서값 계산하기
# ① def 괄호 안에 매개변수 두 개를 쉼표로 정의
# ② 함수 안에서 두 매개변수를 함께 활용
# ③ 인자 두 개를 순서대로 전달해 호출
# ④ 인자 순서를 바꾸면 결과가 어떻게 달라지는지 확인

def report(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")
report("모터", 78) # 모터의 온도는 78도 입니다.
report("펌프", 92) # 펌프의 온도는 92도 입니다.

# ---------------------------------------------------
# 매개변수 순서가 맞지 않으면 엉뚱하게 호출됩니다
report(22.8, "보일러") # 22.8의 온도는 보일러도 입니다.
# 첫번째 매개변수는 무조건 name, 두번째 매개변수는 temp가 되어 원하지 않는 결과가 나올 수 있다

# 매개변수 숫자가 맞지 않으면 --> TypeError 발생
# report("보일러", 22.8, "가동중") # TypeError: report() takes 2 positional arguments but 3 were given

# --> 키워드 인자를 사용해서 오류를 막아보자
# ---------------------------------------------------
# 키워드 인자 사용해 호출
# 순서가 뒤바뀌어 호출되는 문제의 근본을 차단
def report(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")
report(name="모터", temp=78) # 모터의 온도는 78도 입니다.
report(temp=78, name="모터") # 모터의 온도는 78도 입니다.

# --------------------------
# 실습 3. 키워드 인자 함수로 출력하기
# ① 매개변수 두 개를 가진 함수를 정의
# ② 호출할 때 매개변수 이름을 지정해 값을 전달
# ③ 키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
# ④ 위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인

def report(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")
report(name= "모터", temp= 78) # 모터의 온도는 78도 입니다.
report(temp= 78, name= "모터") # 모터의 온도는 78도 입니다.
report(name= "펌프", temp= 92) # 펌프의 온도는 92도 입니다.

# --------------------------
# 반환값
# step 1.
def add():
    a = 1
    b = 2
    total = a + b
    return
result = add()
print(f"1 + 2 = {result}") # 1 + 2 = None

# step 2.
def add():
    a = 1
    b = 2
    total = a + b
    return total # total을 돌려줌 ! --> add()에 값이 생김
result = add() # 그 값을 result에 할당
print(f"1 + 2 = {result}") # 1 + 2 = 3 --> result가 잘 출력됨

# step 3.
def add(a, b):
    total = a + b
    return total
print(add(1,2)) # 3

# 여러번 같은 결과를 호출해야한다면
# 변수에 담아서 사용
result = add(1, 2)
print(result + 1) # 4
print(result + 2) # 5
print(result + 3) # 6

# 평균 내는 함수 만들기
# step 1.
def calc_average(): # calc_average = 4.0
    return 4.0

avg = calc_average() # avg = 4.0
print(f"평균 온도: {avg}") # 평균 온도: 4.0

# step 2.
def calc_average(a, b):
    return (a + b) / 2

avg = calc_average(a= 75.6, b= 88.2)
print(f"평균 온도: {avg}")

# --------------------------
# 실습 4. 반환값으로 간단 계산기 만들기
# ① 값을 받아 계산하는 함수를 정의
# ② 계산 결과를 print가 아니라 return으로 돌려주기
# ③ 호출 결과를 변수에 담기
# ④ 담은 값을 다음 계산·출력에 이어 쓰기

# ---------------------------------------------------
# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값과 최대값을 동시에 return한다
def calc_min_max(values):
    minimum = min(values) # 배열 안의 최소값 minimum에 할당
    maximum = max(values) # 배열 안의 최대값 maximum에 할당
    return minimum, maximum

target_list = [1,2,3,4,5,6]
result = calc_min_max(target_list)
print(result) # (1, 5) 튜플로 출력

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에 결과 튜플의 내용을 풀어서 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)
print("최소값", str(result_min)) # 최소값 1
print("최대값", str(result_max)) # 최대값 6

# return 반환 값이 없는 함수를 호출하고 결과를 어디에 담겠다고하면, None이 담긴다
def say_hi():
    print("hi")
    return

result = say_hi()
print(result) # None

# --------------------------
# 실습 5. 센서 통계 함수 만들기
# 내장 함수 min(), max(), sum(), len() 활용

