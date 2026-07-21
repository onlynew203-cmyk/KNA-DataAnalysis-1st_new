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

