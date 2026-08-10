# try-except
# try에 위험한 코드, except에 대처 방법을 적습니다.
# 오류가 나면 except로 점프합니다. 프로그램은 멈추지 않습니다.

try:
    temp = int("스물")
except:
    print("해봤는데 안되네요")

# --------------------------

temp = -1

try:
    temp = int("스물")
except:
    print("해봤는데 안되네요")
    temp = 0 # 문제가 있어도 앞으로 잘 진행되도록 대안/추가 처리 필요

print(temp) # 0