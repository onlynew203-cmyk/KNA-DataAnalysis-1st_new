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