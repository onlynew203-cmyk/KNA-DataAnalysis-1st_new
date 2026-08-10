# 간단한 인사 함수 만들기
# ":"으로 끝나는 줄의 뜻: 이 다음 줄부터 들여쓴 내용은 한 묶음이다
def say_hello():
    print("안녕")

# 위에서 만든 함수는 이렇게 호출해야만 실행됩니다
say_hello() # 안녕 출력

# 함수 안에서 벌어지는 일들을 만들어봅시다
def show_number():
    my_number = 44
    print(my_number)

show_number() # 44 출력

# 여기서도 my_number 값을 정해봅시다
my_number = 24 # show_number() 함수 안의 my_number와 다른 존재 !
show_number() # 44 출력

# 함수 안의 my_number가 영향을 끼치는 범위 = 전문 용어로 스코프(scope)라고 함

# ---------------------------------------------------
# 함수는 호출되기 전에 만들어져야 함

# show_title() # NameError: name 'show_title' is not defined 

def show_title():
    print("함수 배우기")
show_title() # 함수 배우기 출력

# --------------------------
# 실습 1. 첫 함수 만들고 호출하기
def start_checking():
    print("점검을 시작합니다")

start_checking() # 점검을 시작합니다 출력

# ---------------------------------------------------
# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다

def show_counter():
    count = 0
    count = count + 1
    print(count)
    # 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐
show_counter()

# ---------------------------------------------------
# 각 함수는 이름에 걸맞은 역할만 해줘야 한다
def show_students(): # 학생을 부르는 역할만 합시다
    print("학생1: 짱구")
    print("학생2: 철수")
    print("학생3: 훈이")
show_students()

def show_teacher(): # 선생님을 부르는 역할만 합시다
    print("선생님: 채송화")
show_teacher()

def show_class(): # 반을 부르는 역할 수행
    show_teacher() # 학생과
    show_students() # 선생님을 불러서
show_class() # 완성

# ---------------------------------------------------
# 코드 중복과 함수화

# 중복되는 print
print("압축기A 온도 확인 중")
print("결과를 기록합니다")
print("펌프1 온도 확인 중")
print("결과를 기록합니다")

# 이렇게 함수로 코드를 정리해주세요
def start_check():
    print("점검 시작")
    print("안전 장비 확인 요망")
    print("기록을 준비하세요")
start_check()

# 함수로 설비 점검 자동화하기
# 여러 함수를 정의하고 순서대로 호출해 점검 흐름을 자동화하기

# 구분선과 점검 안내 2줄이 설비마다 반복 출력
# ① 구분선을 출력하는 함수를 정의
# ② 점검 안내 여러 줄을 출력하는 함수를 정의
# ③ 두 함수를 설비마다 순서대로 호출
# ④ 실행해 각 설비마다 같은 안내가 반복되는지 확인

def print_line():
    print("=" * 20)

def print_check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")

# 장비 1에 대한 함수 호출
print_line()
print_check()