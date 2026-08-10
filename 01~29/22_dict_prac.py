# # 실습 1. 딕셔너리 만들고 다루기
# # 센서명을 키, 측정값을 값으로 하는 딕셔너리를 만들고 추가·수정·안전 조회하기
# sensors = {
#     "모터압력" : 78,
#     "모터속도" : 55,
#     "모터온도" : 39
#     }
# # 1) 키들 출력
# print(sensors.keys()) # dict_keys(['모터', '압력', '속도', '온도'])
# # 2) 키로 값 꺼내기
# print(sensors.get("모터압력")) # 78 출력
# # 3) 추가, 수정
# sensors["펌프압력"] = 80
# sensors["모터압력"] = 99
# print(sensors) # {'모터압력': 99, '모터속도': 55, '모터온도': 39, '펌프압력': 80}
# print(sensors.get("면적", -1)) # -1 --> 면적 키는 존재하지 않아서 -1로 대체
# print("진동" in sensors) # False
# print("면적" in sensors) # False

# print("모터압력" in sensors) # True
# # a = "모터압력" in sensors
# # print(a) # True

# --------------------------------------
# 실습 2. update로 여러 값 한 번에 갱신하기

sensors = {"모터압력" : 78, "모터속도" : 55, "모터온도" : 39}
new_data = {"펌프압력" : 77, "펌프속도" : 83}

sensors.update(new_data)
print(sensors) # {'모터압력': 78, '모터속도': 55, '모터온도': 39, '펌프압력': 77, '펌프속도': 83}

del sensors ["모터압력"]
del sensors ["모터온도"]
del sensors ["펌프압력"]
print(len(sensors)) # 2

# --------------------------------------
# 실습 3. 딕셔너리로 통계 내기
sensors = {
    "팬온도" : 78,
    "펌프온도" : 55,
    "모터온도" : 39
    }

temps = sensors.values()
print("평균:",round(sum(temps)/len(sensors),1)) # 평균: 57.3

max_value = 0
max_sensor = ""

for key, value in sensors.items():
    if value > max_value:
        max_value = value
        max_sensor = key
print("최댓값 센서:",max_sensor, max_value) # 최댓값 센서: 팬온도 78

# --------------------------------------
# 실습 4. zip으로 센서명-값 매핑하기

names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))

for name, value in sensors.items():
    print(name, value)
#   모터온도 78
#   진동 0.5
#   압력 95


# --------------------------------------
# 실습 5. 임계값으로 경고 센서 분류하기

# 실제 데이터
values = {"설비온도" : 120, "속도" : 0.5}
# 임계치 데이터
limits = {"설비온도" : 90, "속도" : 4.5}

for name, value in values.items():
    if value > limits[name]:
        print(name, "경고") # 설비온도 경고

# --------------------------------------
# 실습 6. 중첩 딕셔너리로 설비 관리하기
equipments = {
    "컨베이어_01": {
        "온도": 78,
        "진동": 2.1,
        "상태": "정상",
    },
    "용접기_02": {
        "온도": 92,
        "진동": 5.4,
        "상태": "위험",
    },
    "절단기_03": {
        "온도": 85,
        "진동": 3.2,
        "상태": "경고",
    },
}

for name, data in equipments.items():
    for key, value in data.items():
        if key == "상태" and value == "경고":
            print(name, "점검 필요") # 절단기_03 점검 필요

# --------------------------------------
