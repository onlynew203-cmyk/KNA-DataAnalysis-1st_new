# set
# 자동으로 중복 제거
# 순서가 없음 --> 복주머니에 요소 우당탕탕

# 빈 set 만들기
list_ = [] # 빈 리스트
tuple_ = () # 빈 튜플

empty_set = {}
print(type(empty_set)) # <class 'dict'>
# 빈 중괄호는 dictionary 라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장 함수를 사용
real_empty_set = set()
print(type(real_empty_set)) # <class 'set'>

# 값을 포함한 셋 만들기
logs = ["S01", "S02", "S03", "S01"]
# 리스트를 중괄호에 감쌀 경우
# unique = {logs} 
# TypeError: unhashable type: 'list'

# 복수의 값을 중괄호에 감싸 작성
unique = {"S01", "S02", "S03", "S01"}

# set 사용
unique = set(logs)
print(type(unique)) # <class 'set'>
print(unique) # {'S03', 'S01', 'S02'}
# unique 셋에는 기존 중복되었던 S01이 한 번만 들어감
# set에서 인덱스 사용시 에러 발생

# set에 바로 여러 값을 작성
unique = set(["S01", "S02", "S03", "S01"])
print(type(unique)) # <class 'set'>
print(unique) # {'S02', 'S01', 'S03'}

# set을 사용해서 리스트에 들어있는 값 종류의 갯수를 알 수 있음 --> 중복을 제거함으로
print(len(unique)) # 3 출력

# set에 값 추가하기
alerts = {"S01", "S02"}
print(alerts) # {'02', '01'}
alerts.add("S03")
print(alerts) # {'03', '01', '02'} --> 기존에 없던 03은 추가 함
alerts.add("S01")
print(alerts) # {'03', '01', '02'} --> 기존에 있는 것과 동일한 01의 추가는 무시함
# 기존 값과 똑같은 값을 또 넣으면 무시하고 한 개만 존재하도록 함
# 독립적인 값을 저장하기에 아주 편리함

# set에 특정 값 여부 확인

# ["S01", "S02", "S03", "S01"]
# {"S01", "S02", "S03"}
# set은 중복을 제거 -> 리스트보다 길이가 짧음
# set은 인덱스가 없음
# 순회 속도: set이 리스트보다 훨씬 빠르다

# in으로 포함 여부 확인하기
print("S01" in alerts) # True

# if문 활용
if "S01" in alerts:
    print("S01 정비 필요")

# ---------------------
# 실습 셋으로 중복 센서 제거하기
sensor_id_list = ["WQR_01","WQR_01","WQR_01","WQR_01","WQR_06","WQR_06","WQR_03","WQR_05"]
sensor_id = set(sensor_id_list) # {'WQR_05', 'WQR_03', 'WQR_06', 'WQR_01'}
sorted(sensor_id) # ['WQR_01', 'WQR_03', 'WQR_05', 'WQR_06']
print("종류 갯수: ",len(sensor_id)) # 종류 갯수:  4

# -----------------------------------------------------------------------------------------
# 집합 연산
hour_14 = {"WQR_01", "WQR_06", "WQR_07", "WQR_02"}
hour_15 = {"WQR_01", "WQR_07", "WQR_03", "WQR_09", "WQR_11"}

# ---------------------------------------------------------
# 합집합
print(hour_14.union(hour_15))
print(hour_15.union(hour_14)) # 두 코드는 동일한 작동 (합집합이라,,)

# 연산자 |를 활용해 짧게 작성 가능
print(hour_14 | hour_15)
# {'WQR_02', 'WQR_09', 'WQR_11', 'WQR_01', 'WQR_03', 'WQR_06', 'WQR_07'} --> set으로 합집합 출력
print(hour_14) # {'WQR_02', 'WQR_01', 'WQR_06', 'WQR_07'} --> 기존 값 변동 x
# .union은 원본 셋에 변화를 주지 않는다

# ---------------------------------------------------------
# 교집합
print(hour_14.intersection(hour_15)) # {'WQR_07', 'WQR_01'} 출력
print(hour_15.intersection(hour_14)) # 두 코드는 동일한 작동 (교집합이라,,)

# 연산자 & 사용
print(hour_14 & hour_15) # 위와 결과 같음

# ---------------------------------------------------------
# 차집합
print(hour_14.difference(hour_15)) # 14-15 {'WQR_06', 'WQR_02'}
print(hour_15.difference(hour_14)) # 15-14 {'WQR_11', 'WQR_03', 'WQR_09'}
# 이 둘은 다른 결과
# 순서에 따라 결과가 다른 것 유의

# 연산자 - 사용
print(hour_14 - hour_15) # 14-15 {'WQR_06', 'WQR_02'}
print(hour_15 - hour_14) # 15-14 {'WQR_11', 'WQR_03', 'WQR_09'}

# ---------------------
# 실습 두 라인의 센서 구성 비교하기
line_1 = {"s01", "s09", "s13", "s07", "s03"}
line_2 = {"s03", "s09", "s05", "s11", "s18"}

print(line_1 | line_2) # 합집합 {'s05', 's13', 's18', 's11', 's07', 's01', 's03', 's09'}
print(line_1 & line_2) # 교집합 {'s03', 's09'}
print(line_1 - line_2) # 1에만 {'s07', 's01', 's13'}
print(line_2 - line_1) # 2에만 {'s11', 's18', 's05'}

# ---------------------
# 실습 두 시점의 이벤트 센서 추적하기
yesterday = {'S02','S03','S09','S08'}
today = {'S05','S02','S03','S07','S10'}
print("신규:",(today - yesterday)) # 신규: {'S10', 'S07', 'S05'}
print("지속:",(yesterday & today)) # 지속: {'S03', 'S02'}

# ---------------------
# 실습 복습
# 셋으로 중복 센서 제거하기
pre = [1,2,3,1,2,3,4,5]
pre_set = set(pre)
print(pre_set) # {1, 2, 3, 4, 5}
print(len(pre_set)) # 5

# 두 라인의 센서 구성 비교
a = {1,2,3,4,5}
b = {2,4,6,8}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 8} 합집합
print(a.intersection(b)) # {2, 4} 교집합
print(a.difference(b)) # {1, 3, 5} a 차집합 b
print(b.difference(a)) # {8, 6} b 차집합 a

# 두 시점의 센서
old = {1,2,3,4,5}
new = {1,3,5,7}
print("new:",(new.difference(old))) # new: {7}
print("origin:",(new.intersection(old))) # origin: {1, 3, 5}