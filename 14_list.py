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

# ------------------------------------------------------------------------------------
# 인덱스로 특정 값 바꾸기
temps = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
temps[2] = 99 # [2]번 인덱스 값 변경
print(temps) # [31, 32, 99, 34, 35, 36, 37, 38, 39, 40] 출력

# in 존재 확인
machines = ["펌프", "압축기", "모터"] # string list
print("펌프" in machines) # True
print("펌프" not in machines) # False
print("프레스" in machines) # False
print("프레스" not in machines) # True

# 특정 값의 인덱스 찾기
# 리스트.index(찾고자하는 값)
i = machines.index("펌프") 
print(i) # 0 출력

# .index() 메서드는 리스트에서 가장 처음 등장하는 인덱스만 반환
machines2 = ["펌프", "압축기", "압축기", "모터"]
i2 = machines2.index("압축기")
print(i2) # 1 출력 -> 첫번째로 찾은 [1]만 출력. 뒤에 또 있는 것은 출력 안함.

# ---------------------------
# 실습 값 찾아 바꾸기
temps = [31, 32, 33, 34, 35, 36, 37, 38, 39, 240]
print(240 in temps) # True
print(temps.index(240)) # 9
temps[9] = 40
print(240 in temps) # False
print(temps) # [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# ------------------------------------------------------------------------------------
# append()로 끝에 값 추가하기
# 리스트 원본이 수정되는 거! 자동으로 재할당! -> 원본도 살려놔야 ,,, 된다는 말 .. ?
# 원본 리스트가 필요하다면 리스트를 복사해서 수정 진행
# 기존 리스트는 원본으로
temps = [37, 38, 39, 40]
new_temps = temps

# 원본.copy() 하지 않고 append -> 원본에 영향을 줍니다 !!
new_temps.append(41)
print(new_temps) # [37, 38, 39, 40, 41] 출력
print(temps) # [37, 38, 39, 40, 41] -> 원본에도 영향을 줘요

# 원본.copy() 사용 -> 원본을 유지 !!
new_temps2 = temps.copy()
new_temps2.append(100)
print("원본 :", temps) # 원본 : [37, 38, 39, 40, 41] -> 원본에 영향을 주지 않아요
print("복사본 new_temps2 :", new_temps2) # 복사본 new_temps2 : [37, 38, 39, 40, 41, 100]

# ------------------------------------------------------------------------------------
# insert()로 원하는 위치에 값 추가하기

temps = [37, 38, 39, 40]
temps.insert(2, 99) # [2]번 자리에 99가 끼어서 들어감! 원래 값이 사라지지는 않아요
print(temps) # [37, 38, 99, 39, 40] 출력 -> [2]자리에 99가 추가되었고, 원래 [2]자리에 있던 39는 뒤로 한 칸 물러남
# 한 번 더 해볼게요
temps.insert(3, 333) # 위와 같이, 원본 배열에 바로 삽입
print(temps) # [37, 38, 99, 333, 39, 40] 출력 -> 삽입되고 밀어내기 !


# ------------------------------------------------------------------------------------
# extend()로 리스트 이어붙이기

morning = [1, 2, 3]
afternoon = [11, 22, 33]
morning.extend(afternoon) # morning에 이어붙여요(afternoon)을!
print(morning) # [1, 2, 3, 11, 22, 33] 출력 -> morning 원본 자체가 바뀌었어요 !
print(afternoon) # [11, 22, 33] -> afternoon은 변하지 않았네요

# extend() 메서드는 리스트를 수정하는 역할만 ! 반환하는 역할은 하지 않아요. print할 값이 없는 것!
print(morning.extend(afternoon)) # None을 반환 !


data = [1,2,3]
new_data = [9, 19, 21]
data.extend(new_data)
print(data) # [1, 2, 3, 9, 19, 21] 출력

# ------------------------------------------------------------------------------------
# 정리
# 오늘 꼭 알아야 하는 리스트 수정 메서드와 개념
# .append(추가할 값) : 리스트의 가장 마지막에 값 추가
# .insert(삽입 위치, 삽입할 값) : 첫 번쨰 인자인 위치 인덱스에 값 삽입
# .extend(합칠 리스트) : 두 리스트를 하나의 리스트로 합체
# 위 세 가지 리스트는 원본 자체를 수정
# 리스트를 수정하는 역할을 하는 세 가지 메서드는 모두 반환값이 없어요 !

# ---------------------------
# 실습 측정값 추가하기
pre_list = []
pre_list.append(99)
pre_list.insert(0, 88)
print(pre_list) # [88, 99] 출력
pre_list.extend([0])
print(pre_list) # [88, 99, 0] 출력

plus_list = [3, 3, 3]
pre_list.extend(plus_list)
print(pre_list) # [88, 99, 0, 3, 3, 3] 출력

pre_list.extend([12, 13, 14])
print(pre_list) # [88, 99, 0, 3, 3, 3, 12, 13, 14] 출력

pre_list.insert(-1, 9999)
print(pre_list) # [88, 99, 0, 3, 3, 3, 12, 13, 9999, 14] 출력

# ------------------------------------------------------------------------------------
# .remove(값) 값 제거
# 위치는 모르고 삭제할 값만 알때 사용하는 삭제 메서드

cups = [37, 38, 39, 40]
cups.remove(40)
print(cups) # [37, 38, 39] 출력

list1 = [1,2,3,4,5,6]
list1.remove(5)
print(list1) # [1, 2, 3, 4, 6] 출력


# ------------------------------------------------------------------------------------
# .pop(인덱스) 위치로 꺼내며 값 제거
# 해당 위치 값을 꺼내 돌려주며 제거
# 없는 인덱스로 값 삭제 시도 했을때 -> IndexError 발생

cups = [37, 38, 39, 40]
removed = cups.pop(1)
print(removed) # 38 출력

list2 = ["딸기", "사과", "포도", "배", "감", "망고"]
print(list2.pop(0)) # 딸기 출력
print(list2) # ['사과', '포도', '배', '감', '망고'] 출력

# ------------------------------------------------------------------------------------
# del 인덱스로 삭제

list2 = ["딸기", "사과", "포도", "배", "감", "망고"]
del list2[1:4] # 인덱스, 슬라이싱 가능
print(list2) # ['딸기', '감', '망고'] 출력

list2 = ["딸기", "사과", "포도", "배", "감", "망고"]
del list2[::2]
print(list2) # ['사과', '배', '망고'] 출력

list2 = ["딸기", "사과", "포도", "배", "감", "망고"]
del list2[::3]
print(list2) # ['사과', '포도', '감', '망고'] 출력

del list2[:] # 전체 삭제
print(list2) # [] 출력

# ---------------------------
# 실습 잘못된 값 제거하기

list3 = [25,26,24,28,26,999]
list3.remove(999)
list3.pop(1)
del list3[0]
print(list3) # [24, 28, 26] 출력

# ------------------------------------------------------------------------------------
# 복습하기

# find() 괄호 안에 것을 찾아, 위치를 반환해줘요
email = "onyu1221@gmail.com" # email 이란 변수에 str 값 지정
at = email.find("@") # at 이란 변수에 email에서 "@"의 위치 값을 지정
print(at) # 8 출력 -> 지정된 값
print(email.find("@")) # 8 출력 -> "@"의 위치 값

print("기기가 정상으로 작동합니다.".find("정상")) # 4 출력
# "기기가 정상으로 작동합니다."에서 "정상"을 찾아

# ---------------------------
# index()
email = "onyu1221@gmail.com" # email 이란 변수에 str 값 지정
at = email.index("@")
print(at) # 8 출력
print(email[:at]) # @ 앞까지 출력 -> onyu1221
print(email[at:]) # @ 부터 출력 -> @gmail.com
print(email[at+1:]) # at+1의 인덱싱 위치 값부터 출력 -> gmail.com

# ---------------------------
# count() 개수 세기
num = [1,2,3,4,5,6,6,6]
print(num.count(6)) # 3 출력

# ---------------------------
# 인덱스 기준으로 잘라내기
name = "ABC-007"
name_index = name.index("-")
print(name_index) # 3 출력
print(name[3+1:]) # 4부터 끝까지 출력 -> 007
print(name[:3]) # 3 앞까지 출력 -> ABC
# startswith와 endswith로 검사하기
print(name.startswith("ABC")) # True
print(name.endswith("7")) # True

# ---------------------------
# 모두 소문자로 - lower()
name_first = name[:3]
print(name_first.lower()) # abc 출력
# 모두 대문자로 - upper()
city = "seoul" 
print(city.upper()) # SEOUL
# 앞글자만 대문자로 - capitalize()
print(city.capitalize()) # Seoul
# 모든 단어의 앞글자를 대문자로 - title()
status = "we are here"
print(status.title())

# ---------------------------
# strip() 앞 뒤 가장자리에서 괄호에 든 것을 제거 -> 중앙에 들어와 있으면 제거 안됩니다
status = "   we are here.  "
print(status.strip()) # we are here. 출력
print(status.strip(".")) #    we are here.  출력 -> .이 중간에 있기 때문에 아무것도 제거 되지 않음

status = "we are here."
print(status.strip(".")) # we are here 출력

# ---------------------------
# replace(왼쪽,오른쪽) - 왼쪽을 오른쪽으로 바꿔
a = "밥 먹었다?"
print(a.replace("?","!")) # 밥 먹었다! 출력

status = "설비 오류"
print(status.replace("오류","정상")) # 설비 정상 출력

# ---------------------------
# split() 괄호에 든 것 기준으로 나누기
status = "a b c"
print(status.split()) # ['a', 'b', 'c'] 출력

# ---------------------------
# join() 리스트를 하나의 문자열로 합침
join = ["하나", "둘", "셋", "넷", "다섯"]
print("-".join(join)) # 하나-둘-셋-넷-다섯

# ---------------------------
# 구분자 통째로 바꾸기
date = "2026/07/26" # 원래 데이터의 구분자 /를 바꿔보자
date2 = date.split("/") # /를 기준으로 나눠서
print("-".join(date2)) # "-" 구분자로 join -> 2026-07-26 출력

# ---------------------------
# f-str
# 중간 괄호를 활용해서 따옴표 안에서도 변수를 고대로 활용
name = "홍길동"
age = 99
print(f"{name}님의 나이는 {age}살 입니다") # 홍길동님의 나이는 99살 입니다 출력

# f-str 연산
a = 34
b = 52
c = 81
# 소숫점 1째 자리까지
# round(연산자, 소숫점 자리) 사용
print(round((a + b + c)/3,1)) # 55.7 출력
# f-str 연산 사용
print(f"{(a + b + c)/3:.1f}") # 55.7 출력

# ---------------------------

