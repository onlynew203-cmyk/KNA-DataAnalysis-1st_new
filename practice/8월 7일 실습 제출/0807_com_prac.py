# 종합실습
# 1단계 CSV 읽기

import csv

with open("data/09_ict_inspection_dirty.csv", "r", encoding="utf-8") as f:

    lines = f.readline()
    print(lines)
    print(len(lines))

    dict_data = csv.DictReader(f)

    for row in dict_data:
        # 검사ID,부품명,측정값,기준값,상한치,하한치,검사결과
        name = []
        name = row.get("검사ID")

        print(name)
        
