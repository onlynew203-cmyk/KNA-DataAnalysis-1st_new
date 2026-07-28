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


