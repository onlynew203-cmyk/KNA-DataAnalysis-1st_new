# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 읽기로 한다
# 가져온 정보(파인 접근 열쇠/참조값)을 f에 담는다

f = open("sample.txt", "r", encoding="utf-8")
# 인코딩(utf-8)이 중요한 이유
# 인코딩은 글자를 숫자로 바꾸는 약속— 한글 깨지면 utf-8 ↔ cp949 전환

print(type(f).__name__)

# 텍스트파일 파일 한줄씩 문자열을 만들기
lines = f.readline()
print(lines)

f.close() # 열었다면 언젠가는 꼭 닫아주자

# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다

# ------------------------------------------
# with open 사용

with open("sample.txt", "r", encoding="utf-8") as f:

    # 앞으로 이렇게 들여쓰기 된 코드가 끝나면
    # 파일 접근을 닫습니다(close) # close가 필요하지 않은 이유

    lines = f.readline()
    print(lines)

# -------------------------
# 실습 1. open으로 파일 읽기
# ① open으로 파일을 읽기 모드 r, utf-8로 열기
# ② read로 전체를 한 문자열로 읽어 출력
# ③ readlines로 줄 리스트로 읽어 출력
# ④ 두 방식의 결과 차이를 비교하고 파일을 close

# readline()
f_open_01_print = open("01_print.py" , "r", encoding="utf-8")
line_f_open_01_print = f_open_01_print.readline()
print(line_f_open_01_print)
f.close()

# readlines()
f_open_01_print = open("01_print.py" , "r", encoding="utf-8")
lines_f_open_01_print = f_open_01_print.readlines()
print(lines_f_open_01_print)
f.close()

# with open ... as 변수명:
# close가 따로 필요 없어요 ~
with open("01_print.py" , "r", encoding="utf-8") as f_open_01_print:
    line_f_open_01_print = f_open_01_print.readline()
    print(line_f_open_01_print)

# ------------------------------------------
# 쓰기모드로 파일을 새롭게 만들어 보겠습니다
f = open("hello.txt", "w", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("hello?") # hello.txt 파일에서 쓰여진 것을 확인할 수 있다

# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함시킨다
f.write("hello?\n")
# 파일 쓰기에 들여쓰기를 포함하려면 \n을 포함시킨다
f.write("\thello?")
f.close()

# 이어쓰기 모드(append)
f = open("hello.txt", "a", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("\thi!")
f.close()


# -------------------------
# 실습 2. with open으로 파일에 쓰기
# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
# ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
# ③ with 블록이 끝나면 파일이 자동으로 닫힘
# ④ r 모드로 다시 열어 쓴 내용을 확인

f = open("hello.txt", "w", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("Hello?\n") # hello.txt 파일에서 쓰여진 것을 확인할 수 있다
f.write("Is any by there?") # hello.txt 파일에서 쓰여진 것을 확인할 수 있다
f.close()

# -------------------------
# 실습 3. a 모드로 기록 이어붙이기
# ① with open으로 파일을 추가 모드 a로 열기
# ② write로 새 기록 문장을 쓰기
# ③ w 모드와 달리 기존 내용이 보존됨을 확인 !!
# ④ r 모드로 열어 전체가 쌓였는지 확인

f = open("hello.txt", "a", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("\nhi!")
f.close()