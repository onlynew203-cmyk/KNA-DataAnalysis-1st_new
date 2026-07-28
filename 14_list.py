# list는 python의 자료형 중 하나
# 여려 개의 값을 [대괄호]에 담아서 순서대로 저장
# 나열된 값은 자동으로 인덱스 부여

temps = [31, 32, 33, 34, 35] # int list
print(len(temps)) # 5 담긴 값의 개수

float_temps = [33.1, 33.2, 33.3, 33.4, 33.5] # float list
machines = ["펌프", "압축기", "모터"] # string list

# 자료형이 달라도 한 리스트에 담을 수 있어여
mixed = ["펌프", 78, True, 36.5]

# 리스트에 자동으로 순서 인덱스가 붙는다
print(temps[1]) # 32 출력 -> 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소룰 뽑고 싶다면
print(temps[-1])

# 빈 리스트와 길이
empty = []
print(len(empty)) # 0 출력

# 리스트의 담긴 값의 갯수 변수에 저장
temps_length = len(temps) # 변수에 할당
print(temps_length) # 5 출력

# ---------------------------
# 실습 나만의 데이터 리스트 만들기
my_list = [25, 26, 27, 28, 29]
print(my_list) # [25, 26, 27, 28, 29] 출력
print(len(my_list)) # 5 출력

my_empty = []
print(len(my_empty)) # 0 출력

# ------------------------------------------------------------------------------------
# 리스트의 인덱스
print(temps[0], temps[-1]) # temps의 가장 첫번째 값과 가장 마지막 값을 출력
# [-1] = 가장 마지막 값이자 가장 최신의 값

# 음수 인덱스로 뒤에서 찾기
temps = [25, 26, 24, 28, 27]
#        -5  -4  -3  -2  -1
print(temps[-1]) # 27 (마지막 값)
print(temps[-2]) # 28 (뒤에서 두 번째)
# 인덱스 범위를 벗어나면 IndexError 발생

# ---------------------------
# 실습 인덱스로 값 꺼내기
my_list2 = [45, 32, 66, 12, 27]
print(my_list2[0]) # 45 출력
print(my_list2[2]) # 66 출력
print(my_list2[-1]) # 27 출력

# ---------------------------
# 실습 인덱스로 꺼낸 값 계산하기
my_list4 = [32, 66, 12, 27]
a = my_list4[0] # 32 예상
b = my_list4[-1] # 27 예상
print(a + b) # 59 출력
print((a+b)/2) # 29.5 출력
print(f"{(a + b)/2}") # 29.5 출력
print(f"{(a + b)/2:.2f}") # 29.50 출력

# ------------------------------------------------------------------------------------
print("============== list 자료형 ================")

print(type(my_list4)) # <class 'list'>
print(type(my_list4[0])) # <class 'int'>

print(f"type(my_list) : {type(my_list4)}") # type(my_list) : <class 'list'>
print(f"type(my_list) : {type(my_list4[-1])}") # type(my_list) : <class 'int'>
print(f"type(machines) : {type(machines)}") # type(machines) : <class 'list'>
print(f"type(machines) : {type(machines[0])}") # type(machines) : <class 'str'>
print(f"type(machines) : {type(float_temps)}") # type(machines) : <class 'list'>
print(f"type(machines) : {type(float_temps[0])}") # type(machines) : <class 'float'>

# ------------------------------------------------------------------------------------
# 리스트 슬라이싱
# 슬라이싱 - 구간 잘라내기
temps = [31, 32, 33, 34, 35] # int list
print(temps[1:4]) # [32, 33, 34] 출력 1,2,3 인덱싱 출력 1부터 4 앞까지
print(temps[-3:]) # 뒤에서 3개 -3, -2, -1 출력

# 슬라이싱 간격 step
# 리스트명[시작:끝:간격]
temps = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40] # int list
print(temps[0:6:2]) # [31, 33, 35]
print(temps[0:9:2]) # [31, 33, 35, 37, 39]
print(temps[::2]) # [31, 33, 35, 37, 39]
print(temps[::3]) # [31, 34, 37, 40]
# 슬라이싱은 없는 인덱스를 넣으면 []를 반환 !

# 인덱싱 vs 슬라이싱 

# 인덱싱 temps[0]은 값 하나
# 슬라이싱 temps[0:2]는 리스트

# 없는 인덱스 사용 시 에러
# 슬라이싱은 있는 만큼만 잘라주기 때문에 없으면 [] 반환, 에러 발생하지 않는다

# ---------------------------
# 실습 슬라이싱으로 구간 자르기
temps = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(temps[:3]) # [31, 32, 33]
print(temps[-3:]) # [38, 39, 40]
print(len(temps[-3:])) # 3

# ---------------------------
# 실습 데이터를 두 구간으로 나누기
a = [1,2,3,4,5,6,7,8,9,10,11,12]
first = a[:6]
print(first) # [1, 2, 3, 4, 5, 6] 출력
second = a[-6:]
print(second) # [7, 8, 9, 10, 11, 12] 출력
print(len(first), len(second)) # 6 6 출력