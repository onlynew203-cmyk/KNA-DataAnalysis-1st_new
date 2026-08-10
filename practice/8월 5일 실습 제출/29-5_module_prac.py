# 실습3. os로 폴더 목록 살펴보기
# ① os 모듈을 import
# ② getcwd로 현재 작업 폴더를 확인
# ③ listdir로 폴더 안 목록을 변수에 담기
# ④ for로 목록을 하나씩 출력하고 csv만 골라 출력

import os

current_working_directory = os.getcwd()
print(current_working_directory)

csv_files = []

file_list = os.listdir()
for file_name in file_list:
    if file_name.endswith(".csv"):
        csv_files.append(file_name)

print(csv_files)