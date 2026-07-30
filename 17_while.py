# while은 특정 조건(횟수 x)이 False가 될 때까지
# 반복해야하는 경우 사용

# # 무한루프 유의
# count = 1
# while count <= 3: # count가 3보다 크거나 작으면 아래의 코드를 실행해
#     print() # 무한으로 코드를 실행
#     # while은 조건이 거짓이 되는 플래그를 꼭 세워야 함!!
# 무한루프 강제 종료: control + c

# while문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재
# 2. 반복을 멈출 수 있는, False가 될 수 있는 종료 조건 포함
# 3. 변수가 거짓 방향으로 값이 변경되는지
# 예시)
count = 1 # 1. count 변수를 지정한다(반복 전, 시작값이 필요해요)
while count <= 3: # 2. count가 3보다 작거나 같을때 반복하라
    # count = 0 # 반복문 안에서 재할당 ->> 무한루프
    print(count) # 반복문의 조건아래에서 반복할 행동을 지정한다
    count += 1 # 3. 종료 조건을 설정하라

# ------------------
# 실습 while로 목표값 도달까지 반복하기
answer = 7 # 정답
guess = 0 # 사용자의 임시 추측값 (1.)
while guess != answer: # != 같지 않다 -> 추측과 정답이 같지 않을 동안 반복하라 (2.) (3.)
    guess = int(input("맞혀보세요.")) # 사용자에게 입력받기 (3.)
print("정답입니다!") # 반복문 종료시 출력

# ---------------------------------------------------------------------
# break로 반복 중단하기
# 반복을 그만 돌고 싶을 때 사용

for i in range(1, 11):
    if i == 5:
        break # 즉시 종료
    print(i)
# 출력: 1, 2, 3, 4

# 실습
input_sum = 0
while True: # while이 True일 때 --> 조건만 보면 무한 반복하는 코드
    user_input = int(input("값을 입력하세요. 누적값 15 초과시 종료"))
    input_sum += user_input # 값을 누적시킵니다

    if input_sum > 15: # 만약 누적값이 15를 초과하면
        print("누적 합계: ", input_sum, "입력을 종료합니다") # 종료시 출력
        break # 종료
print("break를 통해 while문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
while True:
    # 변수 x는 반복을 돌 때마다 재할당
    x = input("입력 (종료는 q입력)")
    if x == "q":
        break
    print("입력받은 값 :", x)

# ---------------------------------------------------------------------
# 반복 속 조건 분기

n = int(input("횟수 :")) # 사용자에게 횟수 값을 받아

for i in range(n):
    v = int(input("측정값: "))

    if v > 80: # 값이 80 초과시
        print("이상 발생") # 프린트
        print("가동 횟수:", n) # 프린트
        break # 정지
    else:
        print("정상 상태") # 80을 초과하지 않은 경우, 프린트


# ---------------------------
# 실습 up down 게임 만들기

answer = 8 # 미리 지정할 정답은 8 이에요
guess = 0 # 사용자에게 받을 임시 값을 0으로 둘게요

while guess != answer: # 사용자의 추측과 정답이 같지 않으면 반복해요
    guess = int(input("정답을 입력하세요: ")) # 추측 값을 입력 받아요

    if guess > answer: # 만약 추측이 정답보다 크다면
        print("down") # down 프린트
    elif guess < answer: # 추측이 정답보다 작다면
        print("up") # up 프린트
    else: # 둘 다 아니라면 (정답이라면)
        print("입력 값: ", guess, ", 정답!") # 출력
        print("게임을 종료합니다.") # 출력
        break # 정답을 맞추면 종료

# ---------------------------------------------------------------------
# 최댓값 찾기

first = 0
# 첫 번째 입력값은 임시로 지정해둡니다. (변수가 필요해서)
max_value = first # max_value에는 현 시점 최댓값(현 시점은 first 값이겠죠)
# for문 사용으로 4번 입력 받고 가장 큰 값을 출력하기
for i in range(4): # 4번을 반복할 거라고 지정했어요
    v = int(input(f"{i + 1}번째 입력: ")) # 사용자에게 값을 받으며, 지금이 몇번째 입력인지도 함꼐 안내해요
# max_value에는 현 시점 최댓값
# v에는 방금 사용자가 입력한 값
# max_value와 v값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
print("최댓값: ", max_value) # for 반복문 종료 후 최종 최댓값 출력


# ---------------------------
# 실습 조건, 반복 결합 흐름 읽기

# 사용자에게 값을 입력 받는 방법으로 짜봤어요
v = 0
v_sum = 0
for i in range(3):
    v = int(input("answer: "))
    if v > 5:
        v_sum += v
        print(f"누적 합계: {v_sum}")
    else:
        print("5 이하의 값은 누적시키기 않습니다.")
print("종료")

# ---------------------------

# 실습 플래그로 조건 만족 값 검색하기

n = int(input("값을 입력할 횟수를 입력하세요 : ")) # 횟수를 입력 받기
found = False # task가 80초과 값을 "찾는"것이기 때문에 found에 플래그(True/False)를 세워요
for i in range(n): # n에 입력받은 값 만큼 이 반복문을 반복합니다
    v = int(input("값을 입력하세요 : ")) # 이제, 값을 입력 받아요
    if v > 80: # 입력 받은 값이 80을 초과하면
        found = True # task를 이뤘으니, 플래그는 True가 됩니다
        break # 반복문 멈춤
if found: # 찾으면
    print("발견") # 프린트해요
else: # 찾지 못한 경우에
    print("없음") # 프린트해요

