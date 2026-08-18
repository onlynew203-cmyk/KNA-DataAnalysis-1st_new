# 실습 1. head·tail로 디지털 신호 살펴보기
import pandas as pd


df = pd.read_csv("PANDAS/data/12_metro_digital.csv",
                 encoding= 'utf-8')

print(df.shape) # (120, 4)
print(df.head()) # 처음부터 5줄
print(df.tail()) # 끝에서 5줄

df_2 = pd.read_csv("PANDAS/data/12_metro_small.csv",
                 encoding= 'utf-8')

print(df_2.shape) # (30, 7)
print(df_2.head())
print(df_2.tail())