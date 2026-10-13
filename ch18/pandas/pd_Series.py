# pd_Series.py

# 1차원 배열(array), 라벨 있음
# 배열(array): 한 종류의 자료형 데이터로 구성
import pandas as pd

data = [10,20,30]
series = pd.Series(data)
print(series)

# dtype: int64      64비트 정수형 데이터
# 64비트(bits) = 8바이트(bytes)
print('------------')

data = {'a':10, 'b':20, 'c':30}
series = pd.Series(data)
print(series)
print(type(series)) # <class 'pandas.Series'>
# 딕셔너리 key 가 인덱스값으로 쓰이는 형태

# a    10
# b    20
# c    30
# dtype: int64
