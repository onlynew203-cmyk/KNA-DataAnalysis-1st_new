# # tuple: 값을 묶어주는 역할
# # () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# # 그리고 마지막 값에는 꼭 ,를 붙여야 python이 tuple로 인식을 함
# # 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# sensor = ("모터 온도", 78) # 괄호 있고, 끝에 쉼표가 없어
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'tuple'>
# sensor = "모터 온도", 78 # 괄호 없고, 끝에 쉼표가 없어
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'tuple'>
# sensor = ("모터 온도", 78,) # 괄호 있고, 끝에 쉼표 있어
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'tuple'>
# sensor = 78 # 괄호 없고, 끝에 쉼표 없어
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'int'>
# sensor = (78,) # 괄호 있고, 끝에 쉼표 있어
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'tuple'>

# # 원소가 2개 이상이면 괄호의 유무, 끝에 쉼표의 유무 상관없이 모두 튜플
# # 원소가 1개일 경우, 반드시 쉼표가 있어야 튜플

# sensor = () # 빈 괄호
# print("sensor: ", sensor) 
# print("type(sensor): ", type(sensor)) # <class 'tuple'>

# # 원소가 존재하지 않을 경우, 빈 괄호()일 때 <class 'tuple'>
# # -------------------------------------------------------------------------
# # 튜플의 인덱싱
# sensor = ("모터 온도", 78)
# print(sensor[0]) # 모터 온도 출력 --> tuple에서도 인덱스 사용 가능

# # -------------------------------------------------------------------------
# # 튜플의 슬라이싱
# a = ("1", "2", "3", "4", "5", "6")
# print(a[2:5]) # ('3', '4', '5') 출력 --> 출력된 값의 타입도 튜플
# # 튜플은 슬라이싱해도 튜플을 유지한다

# # 튜플 언패킹
# # 튜플에 담긴 값을 변수로 한 번에 분리

# # 복습) 복수의 변수 한 번에 선언
# a, b, c = "a", "b", "c"
# print(a) # 문자열 a
# print(b) # 문자열 b
# print(c) # 문자열 c

# unpacking = (
#     1, # 변수 one
#     2, # 변수 two
#     3, # 변수 three
#     )

# # unpacking = one, two, three
# # one, two, three라는 알 수 없는 변수를
# # unpacking 변수에 할당하겠다는 의미
# # 동작하지 않음

# one, two, three = unpacking
# # unpacking이라는 변수에 담긴 tuple 내부의 값들을
# # 할당 연산자 왼쪽 one, two, three 변수에
# # 풀어서 담는다는 뜻
# print("one:", one)
# print("two:", two)
# print("three:", three)

# # one, two, three, four = unpacking
# # # unpacking이라는 변수에 담긴 tuple 내부의 값들을
# # # 할당 연산자 왼쪽 one, two, three 변수에
# # # 풀어서 담는다는 뜻
# # print("one:", one)
# # print("two:", two)
# # print("three:", three)
# # print("four:", four)
# # # 오류 발생
# # # 튜플의 언패킹은 변수의 개수와
# # # 튜플에 담긴 값의 개수가 동일해야 함

# # -------------------------------------------------------------------------
# # 리스트 언패킹
# one, two, three, four = [11,22,33,44]
# print("one:", one)
# print("two:", two)
# print("three:", three)
# print("four:", four)
# # 가능. 변수의 개수와 담긴 값의 개수가 동일하다면!

# # -------------------------------------------------------------------------
# tub = (
#     "nomal",
#     "nomal",
#     "warninig",
#     "nomal",
#     "warninig",
#     )

# # 튜플의 길이
# print(len(tub)) # 5 출력
# # 특정 값의 갯수 세기
# print(tub.count("warninig")) # 2 출력
# # 특정 값이 처음 나온 인덱스
# print(tub.index("warninig")) # 2 출력

# -------------------------------------------------------------------------
# 튜플 리스트
# 리스트 안에 튜플을 담음 [("1", 1), ("2", 2)]
# for문 : 리스트를 사용해서 리스트 내부의 튜플에 접근하고, 튜플에 담긴 값을 사용할 수 있다
# 언패킹을 사용해서 접근한 튜플 내부의 값을 변수에 바로 할당해서 접근

hour_13 = [
    ("모터 온도",77),
    ("모터 진동",0.2),
    ("모터 압력",91),
    ]

now = 0

for name, value in hour_13:
    now += 1
    print(now, "번째 반복")
    print("name:", name, "  value:", value)

    # 1 번째 반복
    # name: 모터 온도   value: 77
    # 2 번째 반복
    # name: 모터 진동   value: 0.2
    # 3 번째 반복
    # name: 모터 압력   value: 91

# ------------------------------------
temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]

warning = 90
for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상") # 경고 qox_003 설비 온도 이상 --> 출력

# 리스트 안의 튜플 갯수가 늘어나면 for 문에서 변수를 여러개 작성하면 됨

tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2"),
    ("삼", "three", 3, "3"),
    ]

# for문에서도 언패킹 할 때는 무조건 튜플의 값 개수와 for문의 변수 갯수 통일!
for kor_str, eng_str, num, num_str in tup_list:
    print("kor_str:",kor_str," eng_str:",eng_str," num:",num," num_str:",num_str)
    # kor_str: 일  eng_str: one  num: 1  num_str: 1
    # kor_str: 이  eng_str: two  num: 2  num_str: 2
    # kor_str: 삼  eng_str: three  num: 3  num_str: 3

# -------------------------------------------------------------------------
# 튜플 리스트 정렬
# sorted()를 사용하여 튜플의 특정 값 기준으로 리스트를 정렬

temps_13 = [
    (81, "qox_001"),
    (88, "qox_002"),
    (95, "qox_003"),
    (90,"qox_004"),
]

hot = sorted(temps_13, reverse=True) # 값이 큰 순서로 정렬
print(hot) # 원본(temps_13)을 해치지 않고, hot에 할당하고 출력
# [(95, 'qox_003'), (90, 'qox_004'), (88, 'qox_002'), (81, 'qox_001')]

# ---------------------
# 실습 센서를 튜플로 묶고 꺼내기
tuple_pre_1 = [
    ("모터온도", 78)
    ]
print(tuple_pre_1[0]) # ('모터온도', 78)
print(tuple_pre_1[0][0]) # 모터온도
print(tuple_pre_1[0][1]) # 78

for name, value in tuple_pre_1:
    print(name, value) # 모터온도 78

# ---------------------
# 실습 튜플 리스트를 반복 처리하기
tuple_pre_2 = [
    ("회전속도",99),
    ("펌프압력",98),
    ("모터속도",62),
    ("모터압력",56),
]
for name, value in tuple_pre_2:
    if value > 90:
        print(name, "경고")
        # 회전속도 경고
        # 펌프압력 경고

# ---------------------
# 실습 중첩 튜플로 센서 위치 관리하기
tuple_pre_2 = [
    ("회전속도",99,(1,2)),
    ("펌프압력",98,(3,4)),
    ("모터속도",62,(5,6)),
    ("모터압력",56,(7,8)),
]
for name,value,(x,y) in tuple_pre_2:
    if x <= 5:
        print(name,value,(x,y))
        # 회전속도 99 (1, 2)
        # 펌프압력 98 (3, 4)
        # 모터속도 62 (5, 6)