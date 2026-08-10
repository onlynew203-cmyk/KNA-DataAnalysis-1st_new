# 실습 3. a 모드로 기록 이어붙이기
# ① with open으로 파일을 추가 모드 a로 열기
# ② write로 새 기록 문장을 쓰기
# ③ w 모드와 달리 기존 내용이 보존됨을 확인 !!
# ④ r 모드로 열어 전체가 쌓였는지 확인

f = open("hello.txt", "a", encoding="utf-8") # hello.txt 파일이 새로 생겨난 것을 왼쪽의 파일 목록에서 확인 가능
f.write("\nhi!")
f.close()