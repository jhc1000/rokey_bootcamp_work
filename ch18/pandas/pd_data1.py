# pd_data1.py

import pandas as pd 

data = {
    'ID':[1, 2, 3],
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age':[30,35,25]
}

df = pd.DataFrame(data)
print(df)

print("데이터 조작----------")

print("-데이터 선택 및 필터링--------")
print('--열 선택---------------')
# 열 선택 
print(df["Name"])
# 0      Alice
# 1        Bob
# 2    Charlie
# Name: Name, dtype: str

print('--조건 필터링---------------')
# 조건 필터링
filtered = df[df["Age"] > 30]
print(df["Age"] > 30)
print(type(df["Age"] > 30))
# 0    False
# 1     True
# 2    False
# Name: Age, dtype: bool
# <class 'pandas.Series'>
print(filtered)
#    ID Name  Age
# 1   2  Bob   35

print('--행 * 열 필터링---------------')
# 행 * 열 필터링
# df.loc[행_레이블, 열_레이블] -> loc 인덱싱 접근자
filtered = df.loc[df['Age']>30, ['Name','Age']]
print(filtered)
#   Name  Age
# 1  Bob   35

print("-데이터 정렬----------")
# 데이터 정렬
# 값으로 정렬 (기준 열을 by 옵션으로 처리)

print('--오름차순---------------')
# 오름차순
sorted_df = df.sort_values(by='Age')
print(sorted_df)
#    ID     Name  Age
# 2   3  Charlie   25
# 0   1    Alice   30
# 1   2      Bob   35

print('--내림차순---------------')
# 내림차순 (ascending 옵션)
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
#    ID     Name  Age
# 1   2      Bob   35
# 0   1    Alice   30
# 2   3  Charlie   25

sorted_df = df.sort_values(by='Name', ascending=False)  # str 은 알파벳순
print(sorted_df)
#    ID     Name  Age
# 2   3  Charlie   25
# 1   2      Bob   35
# 0   1    Alice   30

print('-데이터 추가 및 삭제---------------')

print('--열 추가---------------')
# 열 추가
df['Salary'] = [50000, 60000, 70000]
print(df)
#    ID     Name  Age  Salary
# 0   1    Alice   30   50000
# 1   2      Bob   35   60000
# 2   3  Charlie   25   70000

print('--행 추가---------------')
# 행 추가
print(len(df))  # 행 번호 : 3
# df.loc[3] = [4, 'David', 40, 80000]   # 마지막 행에 추가함
df.loc[len(df)] = [4, 'David', 40, 80000]   # 마지막 행에 추가함
print(df)
#    ID     Name  Age  Salary
# 0   1    Alice   30   50000
# 1   2      Bob   35   60000
# 2   3  Charlie   25   70000
# 3   4    David   40   80000

print('--행 삭제---------------')
# 행 삭제
df = df.drop(1) # 1번 인덱스 행 삭제
print(df)
#    ID     Name  Age  Salary
# 0   1    Alice   30   50000
# 2   3  Charlie   25   70000
# 3   4    David   40   80000

# print('index 재정렬------')
# # index 재정렬
# # df1 = df.reset_index()
# df1 = df.reset_index(drop=True) # 기존 index 저장 X
# print(df1)
# # index 열 로 기존 인덱스를 저장해놈

print('-데이터 연결---------------')
print('--DataFrame 행 연결---------------')
data2 = {
    'ID': [5,6],
    'Name': ['Eve', 'Frank'],
    'Age': [28, 33]
}
df2 = pd.DataFrame(data2)
print(df2)
concated = pd.concat([df, df2])
print(concated)
#    ID     Name  Age   Salary
# 0   1    Alice   30  50000.0
# 2   3  Charlie   25  70000.0
# 3   4    David   40  80000.0
# 0   5      Eve   28      NaN
# 1   6    Frank   33      NaN

# NaN (Not a number)
# 결측값(NA, Not Available) : 정의되지 않은 값, 누락된 값
# 값이 없는 경우, None으로 데이터 입력 가능 (데이터 없음을 입력시 None 사용)

print('-데이터 병합---------------')
print('--DataFrame 열 병합---------------')
data3 = {
    'ID': [1,2,3,4,5,6],
    'Department': ['HR', 'Engineering', 'Sales', 'R&D', 'Finance', 'Planning']
}
df3 = pd.DataFrame(data3)
print(df3)
#    ID   Department
# 0   1           HR
# 1   2  Engineering
# 2   3        Sales
# 3   4          R&D
# 4   5      Finance
# 5   6     Planning
mearged = pd.merge(concated, df3)
# mearged = pd.merge(concated, df3, on='ID')  # on 옵션: 기준이 되는 열 지정
# mearged = pd.merge(df3, concated)
print(mearged)
#    ID     Name  Age   Salary Department
# 0   1    Alice   30  50000.0         HR
# 1   3  Charlie   25  70000.0      Sales
# 2   4    David   40  80000.0        R&D
# 3   5      Eve   28      NaN    Finance
# 4   6    Frank   33      NaN   Planning
# 인덱스가 정렬 되어있다.(merge() 때문)

print('데이터 처리---------------')
print('-결측치 처리---------------')

print('--결측치 확인---------------')
print(mearged.isnull())  # NaN 인지 T/F 된 데이터프레임
print(mearged.isnull().sum())
# ID            0
# Name          0
# Age           0
# Salary        2
# Department    0
# dtype: int64

print('--결측치 채우기---------------')
# 평균으로 채우기
meanVal = mearged['Salary'].mean()
print(meanVal)
mearged['Salary'] = mearged['Salary'].fillna(meanVal)
print(mearged)
#    ID     Name  Age        Salary Department
# 0   1    Alice   30  50000.000000         HR
# 1   3  Charlie   25  70000.000000      Sales
# 2   4    David   40  80000.000000        R&D
# 3   5      Eve   28  66666.666667    Finance
# 4   6    Frank   33  66666.666667   Planning

print("통계 메서드 들----------------")
print(mearged['Salary'].count())
print(mearged['Salary'].mean())
print(mearged['Salary'].std())
print(mearged['Salary'].min())
print(mearged['Salary'].max())
print(mearged['Salary'].quantile(0.25))
print(mearged['Salary'].quantile(0.50))
print(mearged['Salary'].quantile(0.75))

print('-중복 데이터 처리---------------')
print('--중복 확인---------------')
data1 = {
    'ID': [1,3],
    'Name': ['Alice', 'Charlie'],
    'Age': [30, 25],
    'Salary': [50000, 70000],
    'Department': ['HR', 'Sales']
}
df1 = pd.DataFrame(data1)
df1 = pd.concat([mearged, df1])
print(df1)
#    ID     Name  Age        Salary Department
# 0   1    Alice   30  50000.000000         HR
# 1   3  Charlie   25  70000.000000      Sales
# 2   4    David   40  80000.000000        R&D
# 3   5      Eve   28  66666.666667    Finance
# 4   6    Frank   33  66666.666667   Planning
# 0   1    Alice   30  50000.000000         HR
# 1   3  Charlie   25  70000.000000      Sales
print(df1.duplicated())         # 중복인지 bool Series 로 반환
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 0     True
# 1     True
# dtype: bool
print(type(df1.duplicated()))   # <class 'pandas.Series'>

print('--중복 제거---------------')
df1_1 = df1.drop_duplicates()   # 중복제거 DataFrame 반환
print(df1_1)
#    ID     Name  Age        Salary Department
# 0   1    Alice   30  50000.000000         HR
# 1   3  Charlie   25  70000.000000      Sales
# 2   4    David   40  80000.000000        R&D
# 3   5      Eve   28  66666.666667    Finance
# 4   6    Frank   33  66666.666667   Planning