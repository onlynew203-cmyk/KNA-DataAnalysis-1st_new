# 구분선 출력 - 코드 예시
status = '정상'
line = '=' * 20
print(line)
print('상태: ' + status)
print('횟수: ' + str(5))

# len() 문자열 길이 구하기
# len() 문자열의 글자 수를 숫자로 알려 줌
word = "rainbow"
print(len(word)) # 7 출력

# 실습
phone = "01012345678"
print(len(phone)) # 11 출력

# -----------------------------------------------
# in - 특정 문자가 문자열에 포함되어있는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# "찾을거" in "전체" - "찾을거"가 "전체"에 포함 여부를 판별 (bool 타입)

print("고장" in "설비 고장 발생") # True 출력
print("정상" in "설비 고장 발생") # False 출력

# not in
print("고장" not in "설비 고장 발생") # False 출력
print("정상" not in "설비 고장 발생") # True 출력

# -----------------------------------------------
# count() - 개수 세기
# 특정 글자, 단어가 몇 번 나오는지 셈

print("banana".count("a")) # 3 출력
print('a,b,c,d'.count(',')) # 3 출력

# ================================================