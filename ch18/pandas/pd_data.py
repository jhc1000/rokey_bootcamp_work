# pd_data.py

import pandas as pd 

path = r"C:\rokey\py_work\ch18\pandas\data.csv"
df_csv = pd.read_csv(path)  # DataFrame 으로 반환
# df_csv = pd.read_csv(path, header=None)  # 첫행이 label이 아닐때

print(df_csv)
print(type(df_csv)) # <class 'pandas.DataFrame'>

#    ID   이름   가격
# 0   1   비누  300
# 1   2   장갑  150
# 2   3  마스크  230
# 3   4  손수건  400
# 4   5   볼펜  200
# 5   6  건전지  250

## CSV 파일
# 줄바꿈으로 행을 구분
# 첫 행은 label (안줄수도 있음)
# 열은 , 로 구분
# 필드는 "" 로 둘러싸도 됌 (ex)"1","비누","300")

print('---------')
# Excel 파일 데이터 읽기
# openpyxl 라이브러리 필요

path = r"C:\rokey\py_work\ch18\pandas\data.xlsx"
df_xl = pd.read_excel(path)
print(df_xl)

## Excel 파일 구조
# book > sheet > cell

# 기타 분석 가능 파일 등
# json 파일
# xml 파일 

print("데이터 탐색----------")
print("데이터 상위 5개 행 보기----------")
# 데이터 상위 5개 행 보기   head()
# print(df_csv.head())
print(df_csv.head(3))
#    ID   이름   가격
# 0   1   비누  300
# 1   2   장갑  150
# 2   3  마스크  230

print('데이터 하위 5개 행 보기---------')
# 데이터 하위 5개 행 보기   tail()
# print(df_csv.tail())
print(df_csv.tail(2))
#    ID   이름   가격
# 4   5   볼펜  200
# 5   6  건전지  250

print('데이터 요약 정보---------')
# 데이터 요약 정보      info()
# print(df_csv.info())    
df_csv.info()
# info() 만 해도 출력됌 반환값 None

# <class 'pandas.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   ID      6 non-null      int64
#  1   이름      6 non-null      str  
#  2   가격      6 non-null      int64
# dtypes: int64(2), str(1)
# memory usage: 276.0 bytes

print('기술 통계---------')
# 기술 통계
print(df_csv.describe())
#              ID          가격
# count  6.000000    6.000000
# mean   3.500000  255.000000
# std    1.870829   86.890736
# min    1.000000  150.000000
# 25%    2.250000  207.500000
# 50%    3.500000  240.000000
# 75%    4.750000  287.500000
# max    6.000000  400.000000

print("데이터 활용-----------")
print('개수로 랜덤 샘플링---------')
# 데이터 샘플링
# 개수로 랜덤 샘플링
print(df_csv.sample(2)) # 개수 지정
#    ID  이름   가격
# 4   5  볼펜  200
# 1   2  장갑  150
print('특정 비율로 랜덤 샘플링---------')
# 특정 비율로 랜덤 샘플링
print(df_csv.sample(frac=0.5)) # 비율로 랜덤 # 50%
#    ID   이름   가격
# 2   3  마스크  230
# 0   1   비누  300
# 3   4  손수건  400
