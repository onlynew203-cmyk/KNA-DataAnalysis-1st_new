# 반복문 안에서 예외처리

my_list = ["123", "456", "789"]

for text in my_list: # my_list에 담긴 값을 하나하나 꺼내서 text에 넣자
    print(text)
    # 123
    # 456
    # 789

print(type(text)) # <class 'str'>

# ---- 

my_list = ["123", "456", "789"]

for text in my_list: 
    my_num = int(text)
    print(my_num * 2)

print(type(text)) # <class 'str'>


# ---- 

my_list = ["123", "456", "이 뭐꼬", "789"]

# 문제 발생 경우를 세어봅시다
problems = 0

for text in my_list: 
    # 반복을 하는 중에 문제가 생긴 경우에만 건너뛰고
    # 계속 반복을 이어서 진행시키기
    try :
        my_num = int(text)
    except:
        print("문제 발생")
        # 문제가 생겼다면 더이상 반복문 안의 출력까지 이어가면 안되겠다
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기 ==> continue

        # 문제 상황 누적 카운트
        problems += 1

        continue # 문제 상황 뒤 처리가 올바르게 되었다

    print(my_num)
print(f"{problems}개의 문제가 있어서 건너뜀")


# -------------------------
# 실습 2. 반복문에서 불량 줄 건너뛰기
# ① 여러 측정값(일부는 숫자가 아님)을 반복
# ② try에서 float로 변환
# ③ 변환 실패(ValueError) 시 continue로 그 줄만 건너뛰기
# ④ 정상 값만 합계에 더해 출력

# 소숫점 이하의 숫자가 포함된 숫자들을 20개 정도 만들어 문자로 배열에 담아주세요
# 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시켜주세요
# 이 리스트로 문제를 풀어주세요

num_list = ["19.2", "28.3", "5️⃣5️⃣", "37.5", "46.7"] # num_list를 만들었어요

num_sum = 0 # num 합계를 만들거에요
problems_counting = 0 # 문제 상황이 몇 개 발생했는지 세어봅시다

for num in num_list: # 리스트에 담긴 값을 하나씩 꺼내어 num에 담아요
    try: # 시도해봅시다
        num = float(num) # 하나씩 담은 값을 float으로 만들어요
    except ValueError: # 밸류에러가 발생하면
        print("오류") # 오류를 출력해요

        problems_counting += 1 # 문제 상황을 카운팅 합니다
        continue # 그리고 계속 진행시킵니다

    print(num) # 결과를 봅니다

    num_sum += num # num 값을 누적시켜서 num_sum에 담아요

print(f"정상 값의 합계 : {num_sum}")
print(f"{problems_counting}개의 문제 상황 건너 뜀")



# -------------------------
# 실습 3. 여러 파일 묶어 처리하기
# ① 여러 파일 이름을 반복
# ② try에서 파일을 열어 처리
# ③ 없는 파일(FileNotFoundError) 시 continue로 건너뛰기
# ④ 처리한 파일 수를 세어 출력

# 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다



file_names = ["data/08_press.csv", "data/09_ict_inspection.csv", "data/이게뭐꼬.jpg", "data/result.csv"]

count = 0


for f_name in file_names:
    try:
        with open(f_name, "r", encoding="utf-8") as f:
            count += 1

    except FileNotFoundError:
        print(f_name, "존재하지 않는 파일")

        continue

print(f"처리한 파일 수: {count}개")



# -------------------------
# 실습 4. 함수 안에서 입력값 검증하기
# ① 입력값을 받는 함수를 정의
# ② try에서 float로 변환해 검증
# ③ 변환 실패 시 except로 안내하고 기본값 처리
# ④ 정상·비정상 입력을 각각 넣어 확인

# 