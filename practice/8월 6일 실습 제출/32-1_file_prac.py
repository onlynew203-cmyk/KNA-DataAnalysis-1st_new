# 실습 5. csv.writer로 CSV 쓰기
# ① csv를 import
# ② with open으로 w·utf-8·newline 옵션으로 열기
# ③ csv.writer로 writer 객체를 만들기
# ④ writerow로 헤더와 각 데이터 행을 쓰기

import csv

with open("data/result.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["위치", "시각", "장비"])
    writer.writerow(["포항시", "21:00", "냉각기"])