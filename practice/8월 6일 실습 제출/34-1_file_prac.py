# 실습 6. CSV 읽어 조건 저장하기
# ① csv를 import
# ② csv.reader로 읽고 첫 줄 헤더는 건너뛰기
# ③ 값을 float로 변환해 기준(90) 초과 행만 리스트에 모으기
# ④ csv.writer로 모은 행들을 새 CSV에 저장

import csv

warning_list = []

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # 첫 줄 헤더는 건너뛰기

    for row in reader:
        pressure = float(row[1])

        if pressure > 90:
            warning_list.append(row)
        print("저장 완료")