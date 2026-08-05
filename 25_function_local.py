# 지금까지 배운 내용을 활용해서 함수 만들기 예제

import random

groups = ["에스파", "하투하", "리센느", "엔믹스"]

# 랜덤 뽑기
my_group = random.choice(groups)
print(my_group) # 리센느

# step. 1
group_details = [
    {
        "이름" : "에스파",
        "리더" : "카리나"
    },
    {
        "이름" : "엔믹스",
        "리더" : "해원"
    },
    {
        "이름" : "리센느",
        "리더" : "원이"
    }
]

# step. 2
def get_random_group():
    groups = [
    {
        "이름" : "에스파",
        "리더" : "카리나"
    },
    {
        "이름" : "엔믹스",
        "리더" : "해원"
    },
    {
        "이름" : "리센느",
        "리더" : "원이"
    }
    ]

    my_group = random.choice(groups)
    return my_group.get("이름"), my_group.get("리더")

group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다.")


# --------------------------
# 실습 1. 가보고싶은 여행지
# 함수를 호출하면 랜덤으로 국가 이름과 수도 가져오기
# "환영합니다! ~나라의 수도 ~입니다!" 출력


def get_random_nation():
    nations = [
    {
        "국가" : "프랑스",
        "수도" : "파리"
    },
    {
        "국가" : "일본",
        "수도" : "도쿄"
    },
    {
        "국가" : "영국",
        "수도" : "런던"
    },
    {
        "국가" : "대한민국",
        "수도" : "서울"
    },
    {
        "국가" : "스페인",
        "수도" : "마드리드"
    }
    ]

    my_nation = random.choice(nations)
    return my_nation.get("국가"), my_nation.get("수도")

nation, capital = get_random_nation()
print(f"환영합니다! {nation}의 수도는 {capital}입니다.") # 환영합니다! 영국의 수도는 런던입니다.
