import numpy as np

# 형변환(astype)
# 예를 들어 아래의 float들로 가득한 배열이 있다면
convertable = np.array([3.14, 2.12, 5.26])
print(convertable.dtype) # float64

# int 배열로 형변환
converted = convertable.astype(int)
print(converted) # [3 2 5] --> "버림"을 적용 !
print(converted.dtype) # int64

# ---------------------------------------------
# 실습 4. 배열 구조 확인하기

# 목표
# 표 모양 배열의 차원·형태·개수를 속성으로 확인
# 단계
# · 설비별 측정값을 담은 이차원 배열 준비
# · ndim으로 차원, shape으로 형태, size로 전체 개수 확인
# · 세 속성값 출력
# 예상 결과
# 차원 2, 형태 (2, 3), 개수 6 출력

prac_list = [
    [3, 6, 9],
    [4, 8, 12],
    [9, 6, 1]
]

prac_array = np.array(prac_list)

# ndim 차원
print(prac_array.ndim) # 2
# shape 형태
print(prac_array.shape) # (3, 3)
# size 전체 개수
print(prac_array.size) # 9