# == 같다
print(5 == 5) # 5는 5와 같다(==) -> 비교연산자, bool 타입 = True, False

# and : 둘 다 True 여야 True 출력
print(5 == 5 and 7 == 7) # True
print(5 == 5 and 7 != 7) # False

# or : 하나라도 True라면 True 출력
print(5 == 5 or 7 == 7) # True
print(5 == 5 or 7 != 7) # True (하나라도 True)

# not : 값을 반대로 뒤집음
print(not True) # False 출력
print(not False) # True 출력
print(not 5 == 5) # False 출력 (5 == 5 -> True, not을 붙여서 False 출력)
print(not 5 != 7) # False 출력 (5 != 7 -> True, not을 붙여서 False 출력)
print(not 5 == 7) # True 출력 ( 5 == 7 -> False, not을 붙여서 True 출력)

# -------------------------------------------------------------------

temp = 85
temp_status = temp >= 50 and temp <= 90
print(temp_status)

pressure = 5
pressure_status = pressure >= 3 and pressure <= 7
print(pressure_status)

print(temp_status and pressure_status)

# -------------------------------------------------------------------
# 설비 지표 계산

# 불량률 구하기
total = 500 # 전체 수량 500개
defect = 23 # 불량품 23개
print((defect/total) * 100, "%") # 불량/전체 * 100 -> 불량률 구하기

# 가동률 구하기
run_h = 21 # 가동 시간
all_h = 24 # 전체 시간
print((run_h / all_h) * 100, "%") # 가동시간/전체시간 * 100 -> 가동률 구하기

# 시간 변환
# ① 500분 → 시간=//60, 분=%60 → ② 부품 47, 상자당 6 → ③ 남김없이 = (부품+상자-1)//상자
minutes = 500 # 전체 500분을 시간 변환
print(500 // 60, ":", 500 % 60) # 500을 60으로 나누었을때 몫과 나머지

# 상자 포장
# 전체 부품 47개, 상자 1개당 필요한 부품 6
bolt = 47
print(47 // 6, "개 포장,", "남은 볼트",47 % 6)

# -------------------------------------------------------------------
