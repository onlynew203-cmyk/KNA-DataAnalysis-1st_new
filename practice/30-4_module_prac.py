# 실습 5. datetime으로 점검 기록 남기기
# ① os와 datetime을 import
# ② listdir로 폴더 파일 수를 구하기
# ③ datetime.now로 현재 시각을 담기
# ④ f-string으로 파일 수와 시각을 한 문장으로 출력

import os
import datetime

file_list = os.listdir()
count_file_list = len(file_list)
print(count_file_list) # 35

now = datetime.datetime.now() 
print(now) # 2026-08-05 16:03:05.938497

print(f"파일 수: {count_file_list}, 현재 시각: {now}")
# 파일 수: 35, 현재 시각: 2026-08-05 16:04:54.133426
