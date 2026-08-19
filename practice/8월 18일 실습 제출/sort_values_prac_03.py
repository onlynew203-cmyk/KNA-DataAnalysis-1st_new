# 실습 7. 이상 의심 설비 리포트
# 목표
# 불러오기부터 판단 문장까지 전체 워크플로우를 두 데이터에 적용
# 단계
import pandas as pd

df = pd.read_csv("PANDAS/data/13_diecasting_shot.csv",
                 encoding='utf-8')

# · 복합 조건으로 위험 설비를 거르고 비스킷두께 내림차순 정렬
df.info()
df_warning = df[(df['실린더압력'] >= 28) | (df['주조압력'] >= 17)]
print(len(df_warning)) # 186

df_report = df_warning.sort_values('사이클타임', ascending=False)
print(df_report.head(4))

#        샷  실린더압력    주조압력   사이클타임  비스킷두께    형체력 품질등급
# 199  200  108.0   525.0  6170.0   15.0  237.0   불량
# 180  181  108.0   522.0   652.3   14.0  222.0   불량
# 146  147  263.0   592.0   125.9   19.0  372.0   주의
# 181  182  214.0  1036.0    93.1   12.0  247.0   불량

# 열을 골라내 선택할때는 대괄호 중첩이 필요!
df_fin = df_report[['샷', '품질등급', '형체력']]
print(df_fin.head(3))
#        샷 품질등급    형체력
# 199  200   불량  237.0
# 180  181   불량  222.0
# 146  147   주의  372.0

print("-" * 30)
print("가장 위험 목록")
print(df_fin.head())

df_danger = (df_fin.head(1))
print("가장 위험한 항목")
print(df_danger)

# · 필요한 주요 열만 선택하고 가장 위험한 설비로 판단 문장 작성
# · 같은 흐름을 주조 로그 불량 데이터에도 적용해 결과 비교
# 예상 결과
# 주조 로그 위험 50건·판단 문장, 주조 로그 불량 상위 목록 출력