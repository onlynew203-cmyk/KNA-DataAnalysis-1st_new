# 학생들의 점수를 가져와서
# 각 학생별 합계와 모든 학생들의 평균 점수 내기

import os
import sys
import csv

# 0. 미리 전체 합산 점수를 낼 준비를 한다
students_count = 0
total_all = 0

# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path): # 파일이 없으면
    print("파일을 찾지 못했습니다")
    sys.exit(1) # 시스템 종료

with open(file_path, "r", encoding="utf-8") as f:
    # 2. 파일 내용으로부터 리스트 데이터 얻기  
    reader = csv.DictReader(f) # 전문가야 읽어줘 ~ 그리고 그거 reader에 담아

    for row in reader: # 담은거 한줄한줄 row에 담아

        name = row.get("\ufeff이름", "(이름없음)") # 이름 부분 가져와서 name에 담아. 없으면 이름없음으로 대체해

        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        total = round((kor + eng + math) / 3, 1)
        print(f"{name} | {kor} | {eng} | {math} | {total}")


        # 3. 점수 계산 (합계, 평균)
        students_count += 1
        total_all += total

# 4. 결과를 화면에 보여주기
avg_all = round(total_all / students_count , 1)
print(f"전체 {students_count}명의 평균 점수는 {avg_all}점 입니다")

