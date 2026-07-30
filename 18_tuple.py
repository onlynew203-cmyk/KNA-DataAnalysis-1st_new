# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 python이 tuple로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터 온도", 78) # 괄호 있고, 끝에 쉼표가 없어
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'tuple'>
sensor = "모터 온도", 78 # 괄호 없고, 끝에 쉼표가 없어
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'tuple'>
sensor = ("모터 온도", 78,) # 괄호 있고, 끝에 쉼표 있어
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'tuple'>
sensor = 78 # 괄호 없고, 끝에 쉼표 없어
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'int'>
sensor = (78,) # 괄호 있고, 끝에 쉼표 있어
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'tuple'>

# 원소가 2개 이상이면 괄호의 유무, 끝에 쉼표의 유무 상관없이 모두 튜플
# 원소가 1개일 경우, 반드시 쉼표가 있어야 튜플

sensor = () # 빈 괄호
print("sensor: ", sensor) 
print("type(sensor): ", type(sensor)) # <class 'tuple'>

# 원소가 존재하지 않을 경우, 빈 괄호()일 때 <class 'tuple'>
# ----------------------
# 튜플의 인덱싱
sensor = ("모터 온도", 78)
print(sensor[0]) # 모터 온도 출력 --> tuple에서도 인덱스 사용 가능

# 튜플의 슬라이싱
a = ("1", "2", "3", "4", "5", "6")
print(a[2:5]) # ('3', '4', '5') 출력 --> 출력된 값의 타입도 튜플
# 튜플은 슬라이싱해도 튜플을 유지한다

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
a, b, c = "a", "b", "c"
print(a) # 문자열 a
print(b) # 문자열 b
print(c) # 문자열 c

unpacking = (
    1, # 변수 one
    2, # 변수 two
    3, # 변수 three
    )

unpacking = one, two, three
# one, two, three라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작하지 않음

one, two, three = unpacking
# unpacking이라는 변수에 담긴 tuple 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는 뜻
print("one:", one)
print("two:", two)
print("three:", three)

# one, two, three, four = unpacking
# # unpacking이라는 변수에 담긴 tuple 내부의 값들을
# # 할당 연산자 왼쪽 one, two, three 변수에
# # 풀어서 담는다는 뜻
# print("one:", one)
# print("two:", two)
# print("three:", three)
# print("four:", four)
# # 오류 발생
# # 튜플의 언패킹은 변수의 개수와
# # 튜플에 담긴 값의 개수가 동일해야 함

# ----------------------
# 리스트 언패킹 가능할까?
one, two, three, four = [11,22,33,44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
# 가능하다. 변수의 개수와 담긴 값의 개수가 동일하다면!
