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
