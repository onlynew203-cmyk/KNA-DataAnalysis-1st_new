import os
import sys
import csv
# CSV는 표(Table) 형태
# 리스트가 바로 한 행의 데이터를 표현하기에 가장 적합

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding= "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

# -------------------------
# 실습 5. csv.writer로 CSV 쓰기
# ① csv를 import
# ② with open으로 w·utf-8·newline 옵션으로 열기
# ③ csv.writer로 writer 객체를 만들기
# ④ writerow로 헤더와 각 데이터 행을 쓰기

# import csv

# with open("data/result.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["위치", "시각", "장비"])
#     writer.writerow(["포항시", "21:00", "냉각기"])