sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]

# -------------------------------------------------
# todo 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력

num = 0
danger = 0
warning = 0
normal = 0
    
for name, temp, vibration in sensors:
    num += 1
    if temp > 90 or vibration > 5.0:
        danger += 1
        status = "위험 🚨"
    elif temp >= 80 or vibration >= 3.0:
        warning += 1
        status = "주의 ⚠️"
    else:
        normal += 1
        status = "정상 ✅"
    print(f"{num}. {name} | {temp} | {vibration} | {status}")

# 1. 컨베이어_01 | 78 | 2.1 | 정상 ✅
# 2. 용접기_02 | 92 | 5.4 | 위험 🚨
# 3. 절단기_03 | 85 | 3.2 | 주의 ⚠️
# 4. 건조로_04 | 101 | 6.8 | 위험 🚨
# 5. 냉각탑_05 | 67 | 1.5 | 정상 ✅
# 6. 도장부스_06 | 88 | 4.1 | 주의 ⚠️
# 7. 성형기_07 | 90 | 2.9 | 주의 ⚠️


# -------------------------------------------------
# todo 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력

print("위험:",danger)
print("주의:",warning)
print("정상:",normal)


# -------------------------------------------------
# todo 3. 이상 설비(주의 + 위험) 비율 % 출력

total_Equipment = len(sensors)

not_warning = 0
warning_num = 0

for name, temp, vibration in sensors:
    if temp > 90 or vibration > 5.0:
        warning_num += 1
    elif temp >= 80 or vibration >= 3.0:
        warning_num += 1
    else:
        not_warning += 1
print(warning_num)

print("이상 설비 비율:", (round((warning_num/total_Equipment)*100,1)),"%")



# -------------------------------------------------
# todo 4. 전체 평균 온도 출력

total_temps = 0

for name, temp, vibration in sensors:
    total_temps += temp
print(total_temps)

print(round(total_temps/len(sensors),1))


# -------------------------------------------------
# todo 5. 온도 가장 높은 설비 이름 + 온도 출력

max_temp = 0

for name, temp, vibration in sensors:
    if temp > max_temp:
        max_temp = temp
print(f"최고 온도 설비: {name} ({max_temp}℃)")



# -------------------------------------------------
# todo 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력

danger_list = []

for name, temp, vibration in sensors:
    if temp > 90 or vibration > 5.0:
        danger_list.append(name)

danger_list.sort()
print(danger_list)

# -------------------------------------------------
print("=" * 45)
print("          설비 종합 모니터링 리포트          ")
print("=" * 45)
num = 0
danger = 0
warning = 0
normal = 0
    
for name, temp, vibration in sensors:
    num += 1
    if temp > 90 or vibration > 5.0:
        danger += 1
        status = "위험 🚨"
    elif temp >= 80 or vibration >= 3.0:
        warning += 1
        status = "주의 ⚠️"
    else:
        normal += 1
        status = "정상 ✅"
    print(f"{num}. {name} | {temp} | {vibration} | {status}")
print("-" * 45)
print("총 설비:",total_Equipment,"대")
# ==
total_Equipment = len(sensors)
not_warning = 0
warning_num = 0
for name, temp, vibration in sensors:
    if temp > 90 or vibration > 5.0:
        warning_num += 1
    elif temp >= 80 or vibration >= 3.0:
        warning_num += 1
    else:
        not_warning += 1
print("이상 설비 비율:", (round((warning_num/total_Equipment)*100,1)),"%")
# ==
total_temps = 0
for name, temp, vibration in sensors:
    total_temps += temp
print("평균 온도:",round(total_temps/len(sensors),1),"℃")
# ==
max_temp = 0
for name, temp, vibration in sensors:
    if temp > max_temp:
        max_temp = temp
print(f"최고 온도 설비: {name} ({max_temp}℃)")
# ==
print("위험 설비 목록:", danger_list)
# ==
print("=" * 45)

# ===============================================================================