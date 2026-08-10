# 실습 2. with open으로 파일에 쓰기
# ① with open으로 파일을 쓰기 모드 w, utf-8로 열기
# ② write로 내용을 쓰기(줄을 나눌 땐 줄바꿈 기호)
# ③ with 블록이 끝나면 파일이 자동으로 닫힘
# ④ r 모드로 다시 열어 쓴 내용을 확인

f = open("hello.txt", "w", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("Hello?\n") # hello.txt 파일에서 쓰여진 것을 확인할 수 있다
f.write("Is any by there?") # hello.txt 파일에서 쓰여진 것을 확인할 수 있다
f.close()
