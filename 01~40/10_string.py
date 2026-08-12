# 따옴표로 문자열 만들기
name = '홍길동' # name 변수 저장
status = "정상" # status 변수 저장
code = 'EQP-001' # code 변수 저장
print(name, status, code)

# 따옴표 안에 따옴표 넣기
status = "It's normal"
print(status) # It's normal 출력

# 여러 줄 문자열 - 삼중 따옴표
notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(notice) # 따옴표 세 개를 사용해, 여러 줄(줄바꿈 포함)을 그대로 담음

# 이스케이프 문자
# 역슬래시(\)로 줄바꿈,탭,따옴표를 표현
status = "안녕\n하세요" #n\ : 줄바꿈
print(status)
# 안녕
# 하세요 출력
status = "안녕\t하세요" # \t 탭(간격)
print(status) # 안녕    하세요 출력

pre = "여기는\\학교"
print(pre) # 여기는\학교 출력
pre2 = "여기는\학교"
print(pre2) # 여기는\학교 출력
## \\를 사용할 때 : 파일 경로나 URL 작성시 디렉토리 구분자로 사용

# \ 사용 : 감싸는 따옴표와 내부의 따옴표의 생김새가 같을때
pre = 'It\'s me'
print(pre) # It's me
pre2 = "He said, \"It's mine\"and blabla."
print(pre2) # He said, "It's mine"and blabla.

# --------------------------------------------------------------
# 실습 - 여러 줄, 이스케이프 다루기
# 삼중 따옴표로 3줄 점검 안내문
status = """설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(status)

# --------------------------------------------------------------
# 실습 - 설비 라벨 문자열 만들기
name = "PUMP_A"
status = "정상"
date = "2025-01-15"
print(name, "/", status, "/", date) #PUMP_A / 정상 / 2025-01-15 출력

# --------------------------------------------------------------
# 실습 - 설비 정보 출력 카드 만들기

code = "PUMP_B"
state = "정상"
hours = 1200
day = "2025-01-15"
card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hours) + "시간\n점검: " + day
# 설비 : code (줄바꿈) 상태 : state (줄바꿈) 가동 : hours를 str으로 감싸서, 시간 단위표시(줄바꿈) 점검 : day
print(card)
# 설비: PUMP_B
# 상태: 정상
# 가동: 1200시간
# 점검: 2025-01-15 출력
# --------------------------------------------------------------