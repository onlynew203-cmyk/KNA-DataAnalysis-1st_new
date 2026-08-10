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

# ---------------------------
# 실습 조건에 맞는 값만 출력하기

temps = [20,21,31,23,35,25,32]
for t in temps:
    if t >= 30:
        print("고온: ",t)

# ---------------------------
# 실습 두 조건을 모두 만족하는 값 고르기

hours = [3, 14, 24, 5, 18, 9]
for h in hours:
    if h >= 5 and h <=10:
        print(h)

# ---------------------------
# 실습 조건에 맞는 값만 골라 평균 구하기
temps = [20,21,31,23,35,25,32] # 온도 리스트 변수 지정
temps_sum = 0 # 온도 합계 변수 지정
count = 0 # 개수 변수 지정
for t in temps:
    if t > 30: # 온도가 30을 초과하면
        temps_sum += t # 누적시킨다
        count += 1 # 개수도 누적시킨다(평균값을 구하기 위함)
print(f"고온 평균: , {(temps_sum / count):.2f}") # 고온 평균: , 32.67 출력

# ---------------------------------------------------------------------
# 빈 리스트에서 시작해 값 채우기
# append 사용

temps = [25, 26, 24, 28]
doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled) # [50, 52, 48, 56]

# ---------------------------
# 실습 
# 기존 배열의 모든 요소에 *3의 값을 가진 새로운 리스트 생성

temps = [20,21,31,23,35,25,32] # 온도 리스트 변수 지정
doubled = []

for t in temps:
    doubled.append(t * 3)
print(doubled)

# ---------------------------------------------------------------------
# 조건에 맞는 값으로 새 리스트 만들기
# for, if, append 사용

temps = [25, 32, 28, 35, 27]
high = []
for t in temps:
    if t > 30:
        high.append(t)
print(high) # [32, 35]

# ---------------------------
# 실습 
temps = [5, 2, 8, 3, 7]
high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    elif t > 5:
        high.append(t)

print("high: ", high)

## 추가
# 복습 sort(): 원본 배열을 오름차순으로 정렬
# 하지만 반환은 안해주니까 print로 찍으면 none 출력
print("low: ", low.sort())

# 정렬된 배열로 출력하고 싶다면 아래처럼
low.sort()
print(low)

# ---------------------------
# 실습 조건에 맞는 값으로 새 리스트 만들기

temps = [25, 32, 38, 13, 37, 22, 29]
high_temps = []

for t in temps:
    if t > 30:
        high_temps.append(t)
print("초과 값: ",high_temps)
print("개수: ",len(high_temps))

# ---------------------------
# 실습 값을 가공해 새 리스트 만들기

temps = [20, 32, 18, 16, 17, 22]
empty = []

for t in temps:
    empty.append(t * 1.8 + 32)
print(empty) # [68.0, 89.6, 64.4, 60.8, 62.6, 71.6] 출력

# ---------------------------------------------------------------------
# 리스트 안의 리스트
rows = [["펌프", 25],["모터", 32],["압축기", 28]]
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

print(rows[0]) # ["펌프", 25] 출력
print(type(rows[0])) # list 타입
print(type(rows)) # list 타입

# 중첩된 리스트 안의 값에 접근하고 싶다면
print(rows[1][1]) # 32 출력
# 1. rows[1]을 찾음
# 2. ["모터", 32]의 [1]을 찾음
# 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근한다

# 리스트 안의 리스트 온도 값만 출력하기
rows = [["펌프", 25],["모터", 32],["압축기", 28]]
for r in rows:
    print(r[0],"온도", r[1])
# rows는 리스트를 담고 있는 큰 리스트
# r는 rows 안에 있는 작은 리스트 / ex) ["펌프", 25]


# ---------------------------
# 실습 센서 데이터 종합 분석하기
temps = [20, 32, 18, 16, 17, 22] # 온도 리스트
total = 0
for t in temps: # temps 안에 있는 값을 하나씩 꺼내서 t에 넣어라
    total += t # t의 누적
    print("전체 평균: ",round(total/len(temps),2))
hot = []
for t in temps:
    if t > 30:
        hot.append(t)
hot_total = 0
for t in hot:
    hot_total += t
print("고온 평균: ", hot_total/len(hot))
print("고온 개수: ", len(hot))

# ========
# 실습 복습
# 조건에 맞는 값으로 새 리스트 만들기

temps = [1,2,3,4,5]
hots = [] # 뜨거운 걸 담을게요
for t in temps: # 온도 리스트 안에 있는 값을 하나씩 꺼내서 t에 담아라
    if t > 3: # 만약에 t가 3보다 크면
        hots.append(t) # 뜨거운 것 리스트에 담아라
print(len(hots)) # 2 출력 --> 뜨거운 것 리스트 안에 있는 것의 개수 = 리스트의 길이
print(hots) # [4, 5] 출력

# ========
# 실습 복습
# 값을 가공해 새 리스트 만들기
subs = [2,3,4,5,6]
hwas = []
for t in subs:
    hwas.append(t * 1.8 + 32) # 요소를 계산해서 hwas에 담아야하니까 t에다 곱해야해
print(hwas) # [35.6, 37.4, 39.2, 41.0, 42.8]

# ========
# 실습 복습
# 센서 데이터 종합 분석하기

temps = [11, 22, 33, 44, 55]
total = 0
hots = []
for t in temps:
    total += t
print("전체 평균: ", (total/len(temps))) # 전체 평균:  33.0
hots_total = 0
for t in temps:
    if t > 30:
        hots.append(t)
        hots_total += t
print("고온 갯수: ",len(hots)) # 고온 갯수:  3
print("고온 평균: ",hots_total/len(hots)) # 고온 평균:  44.0