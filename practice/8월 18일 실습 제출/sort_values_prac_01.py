# 실습 5. 위험 순으로 정렬하기
# 목표
# 데이터를 위험한 순서로 정렬하고 상위만 추출
# 단계
import pandas as pd

df = pd.read_csv("PANDAS/data/13_diecasting_shot.csv",
                 encoding='utf-8')

# · sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
df_align = df.sort_values('비스킷두께', ascending=False)

# · head로 상위 다섯 개만 추출해 값 확인
print(df_align.head(5))

# · 여러 열을 리스트로 묶어 우선순위 다중 정렬
df_multi = df.sort_values(['실린더압력', '주조압력'], ascending=[True, False])
print(df_multi.head(5))
#       샷 실린더압력  주조압력   사이클타임  비스킷두께    형체력 품질등급
# 199  200  108.0  525.0  6170.0   15.0  237.0   불량
# 186  187  108.0  524.0    22.9   14.0  247.0   불량
# 180  181  108.0  522.0   652.3   14.0  222.0   불량
# 191  192  113.0  255.0    36.9   26.0  366.0   불량
# 193  194  113.0  255.0    34.4   19.0  370.0   불량

# 예상 결과
# 상위 5개 비스킷두께 값과 다중 정렬 첫 행 품질등급 출력

