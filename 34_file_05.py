import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾으면 출력
if os.path.exists(csv_path):
    print("파일 있음")


with open(csv_path, "r", encoding="utf-8") as f:

    reader = csv.reader(f)

    # DictReader가 아닌 그냥 reader를 사용하면
    # 보통 csv파일의 첫줄인 헤더줄도 읽어버린다
    # reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
    # next(reader)는 한줄 건너뛰고 reader가 반응하게 된다

    header = next(reader)

print(header) # ['설비ID', '시각', '진동X', '진동Y', '전류', '상태']


# -------------------------
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