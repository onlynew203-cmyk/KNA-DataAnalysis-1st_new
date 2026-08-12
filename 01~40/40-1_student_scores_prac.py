# 학생들의 점수를 가져와서
# 각 학생별 합계와 모든 학생들의 평균 점수 내기


# -------------------------
# 실습 연습
# 위 코드 마지막에 1. 최고점 학생, 최저점 학생을 찾아서 출력
# 2. 각 과목별 평균 점수 출력


import os
import sys
import csv

# 0. 미리 전체 합산 점수를 낼 준비를 한다
students_count = 0
avg_all = 0

max_kor = 0
max_kor_name = ""

max_eng = 0
max_eng_name = ""

max_math = 0
max_math_name = ""

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

        if kor > max_kor:
            max_kor = kor
            max_kor_name = name

        if eng > max_eng:
            max_eng = eng
            max_eng_name = name

        if math > max_math:
            max_math = math
            max_math_name = name


        avg = round((kor + eng + math) / 3, 1)
        print(f"{name} | {kor} | {eng} | {math} | {avg}")


        # 3. 점수 계산 (합계, 평균)
        students_count += 1
        avg_all += avg
fin_avg = round(avg_all / students_count , 1)


# 4. 결과를 화면에 보여주기
print('-' * 30)
print(f"전체 {students_count}명의 평균 점수는 {fin_avg}점 입니다")
print('-' * 30)
print(f"국어 최고점: {max_kor_name}({max_kor}점)")
print(f"영어 최고점: {max_eng_name}({max_eng}점)")
print(f"수학 최고점: {max_math_name}({max_math}점)")
print('=' * 30)

