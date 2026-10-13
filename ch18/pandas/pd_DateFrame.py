# pd_DataFrame.py

import pandas as pd

## 중첩 리스트로 생성
data = [
    [1, 'Alice', 30],
    [2, 'Bob', 35],
    [3, 'Charlie', 25]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
print(df)
print(type(df)) # <class 'pandas.DataFrame'>
# 컬럼 명을 옵션으로 사용

#    ID     Name  Age
# 0   1    Alice   30
# 1   2      Bob   35
# 2   3  Charlie   25

print('--------------')

## 딕셔너리로 생성
data = {
    'ID':[1, 2, 3],
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age':[30,35,25]
}

df = pd.DataFrame(data)
print(df)
# key를 컬럼 명으로 사용

#    ID     Name  Age
# 0   1    Alice   30
# 1   2      Bob   35
# 2   3  Charlie   25