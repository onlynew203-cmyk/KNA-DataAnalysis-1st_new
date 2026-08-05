# 표준 라이브러리의 math 모듈
import math

print(math.sqrt(9)) # 3.0 출력 --> 제곱근 값
print(math.ceil(4.2)) # 5 출력 --> 올림 값
print(2 ** 3) # 8 출력 --> 2의 2승 == 2 * 2 * 2 math와 무관한 기본 연산자

# --------
# 아래와 같이 더 많이 써요
# math에서 sqrt, ceil 두 개만 사용한다면 이렇게 써도 됩니다
# 실전에서는 코드 줄 중간에 import 안써요. 가장 위에 다 써요.
from math import sqrt, ceil
# 위에서 가져온 math 함수들 사용 예제
print(sqrt(9))
print(ceil(3.9))

print("=" * 20)
# --------------------------------------------------------
# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10)) # 1~10 범위의 정수 랜덤 뽑기
print(random.choice(["정상", "경고", "위험"])) # 셋 중 무작위

print("=" * 20)

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()

print(now) # 2026-08-05 13:18:32.615109

print("=" * 20)
# --------------------------------------------------------
# 절대경로와 상대경로
# 절대경로의 예시 | C:\Users\me\project\data\a.csv 
# 만약 어떤 폴더에 터미널을 연 상태에서 code.py 코드를 실행하고 싶다면
# python code.py --> 상대경로를 의미
# python C:\Users\me\project\data\a.csv --> 절대경로로 지정해도 됨

# --------------------------------------------------------
# 표준 라이브러리의 os 모듈 활용
import os
current_working_directory = os.getcwd()
print(current_working_directory)

# 현재 작업디렉토리의 파일 목록 가져오기
file_list = os.listdir()
for file_name in file_list:
    print(file_name)

# --------------------------------------------------------
# 파일이 존재하는지 알아봅시다
# 운영체제(윈도우/맥/리눅스)마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 경로 문자열을 만들어 주는 os의 함수를 사용합시다
path = os.path.join("data", "08_press.csv")

# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아봅시다: True/False
if os.path.exists(path):
    print(f"파일 있음:, {path}")

