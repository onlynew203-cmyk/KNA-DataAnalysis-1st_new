# import os
# import sys
# import csv

# csv_path = os.path.join("data", "08_press.csv")

# # 위 경로의 파일을 찾으면 출력
# if os.path.exists(csv_path):
#     print("파일 찾음")


# # --------------------------
# # csv_path = os.path.join("data", "99_press.csv")

# # # 위 경로의 파일을 찾지 못하면 출력
# # if not os.path.exists(csv_path):
# #     print("파일 없음")

# # # # 위 경로의 파일을 찾지 못하면 강제 종료
# # # if not os.path.exists(csv_path):
# # #     print("파일 없음")
# # #     sys.exit(1)

# # with open(csv_path, "r", encoding="utf-8") as f:
# #     print(f.readlines())


# with open(csv_path, "r", encoding="utf-8") as f:
# # print(f.readlines()) --> csv 전문가에게 맡깁시다
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# -------------------------
# 실습 4. csv.reader로 CSV 읽기
# ① csv 모듈을 import
# ② with open으로 CSV를 읽기 모드 utf-8로 열기
# ③ csv.reader로 reader 객체를 만들기
# ④ for로 각 행(리스트)을 하나씩 꺼내 출력

import csv

# with open을 사용해서, 경로 data 폴더에 08~ 파일을, "r" 읽기, 모드 utf-8로 -> 그리고 이 열어놓은 파일을 f라는 이름으로 사용할게
with open ("data/08_press.csv", "r", encoding= "utf-8") as f:
    reader = csv.reader(f) # csv 파일을 읽기 쉽게 변환하고 reader에 넣을게
    for row in reader: # reader에 정보를 for문을 사용해 한줄씩 읽어서 row에 담기
        print(row) # row 출력 == 데이터를 한줄씩 출력


# 아래는 변수를 선언한 코드
# csv_path = os.path.join("data", "08_press.csv")

# with open(csv_path, "r", encoding="utf-8") as f:
# # print(f.readlines()) --> csv 전문가에게 맡깁시다
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)