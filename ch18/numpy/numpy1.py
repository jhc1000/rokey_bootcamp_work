# numpy1.py

import numpy as np 

print('배열 생성 및 초기화--------')
print('-배열 생성------------')
arr = np.array([1,2,3,4,5])
print(arr)          # [1 2 3 4 5]
print(type(arr))    # <class 'numpy.ndarray'>

print('-배열 속성 확인------------')
print(arr.shape)    # (5,)  -> 배열 모양 (길이,)
print(arr.dtype)    # int64 -> 데이터 타임

print('-다양한 배열 생성 방법------------')
print('--0으로 초기화된 배열------------')
zeros = np.zeros((3,3))
print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
print(zeros.shape)  # (3, 3)  -> 배열 모양 (행, 열)
print(zeros.dtype)  # float64

print('--1로 초기화된 배열------------')
ones = np.ones((2,4))
print(ones)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

print('--특정 값으로 채운 배열------------')
full = np.full((2,2), 7)
print(full)
# [[7 7]
#  [7 7]]

print('--단위 행렬------------')
# 단위 행렬: 대각선 상의 원소가 1이고 나머지 원소는 모두 0인 행렬
identity1 = np.eye(2,3) # 단위행렬
print(identity1)
# [[1. 0. 0.]
#  [0. 1. 0.]]
identity2 = np.identity(3)  # 정사각행렬
print(identity2)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print('역행렬--------')
A = np.array([
    [1, 2],
    [3, 4]
])
A_inv = np.linalg.inv(A)
print(A_inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

print('-랜덤 배열 생성------------')
print('--난수 배열------------')
random = np.random.rand(3,3)
# 0이상 1미만 범위의 실수 난수 생성
print(random)
# [[0.05287986 0.25448275 0.90875916]
#  [0.05084148 0.55627279 0.42182412]
#  [0.99019565 0.80854707 0.75411103]]

print('--정수 난수 배열------------')
# 1 이상 10미만 범위의 정수 난수 생성
randint = np.random.randint(1,10,(3,3))
print(randint)
# [[3 3 7]
#  [6 4 7]
#  [9 2 9]]

print('배열 연산------------')
print('-기본 산술 연산------------')
arr = np.array([1,2,3,4])
print(arr + 5)
print(arr * 2)

print('-통계 함수------------')
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

print('-브로드캐스팅------------')
# 브로드캐스팅(virtual expansion)
# : 작은 배열을 큰 배열의 크기에 맞춰 확장해서 연산
print('--배열 간 연산------------')
arr1 = np.array([1,2,3])        # 행 벡터 1d(3,) -> 2d(1,3) -> 2d(3,3)
print(arr1)
print(arr1.shape)   # -> (3,)
arr2 = np.array([               # 열 벡터 (3,1) -> (3,3) 확장
    [1],
    [2],
    [3]
])
print(arr2)         
print(arr2.shape)   # -> (3,1)

result = arr1 + arr2
print(result)
print(result.shape) # -> (3, 3)
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]

# [[1 2 3]        [[1 1 1]
#  [1 2 3]    +    [2 2 2]
#  [1 2 3]]        [3 3 3]] 

result = arr1 * arr2
print(result)
print(result.shape) 
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]

# [[1 2 3]        [[1 1 1]
#  [1 2 3]    *    [2 2 2]
#  [1 2 3]]        [3 3 3]] 

result = arr1 - arr2
print(result)
print(result.shape) 
# [[ 0  1  2]
#  [-1  0  1]
#  [-2 -1  0]]

result = arr1 / arr2
print(result)
print(result.shape) 
# [[1.         2.         3.        ]
#  [0.5        1.         1.5       ]
#  [0.33333333 0.66666667 1.        ]]

# 차원 비교: 두 배열의 차원을 오른쪽 부터 비교함
# 각 차원은 다음 중 하나를 만족하면 브로드캐스팅 가능
# - 두 차원의 크기가 같다.
# - 둘 중 하나의 크기가 1이다.
# - 한쪽이 차원이 없다면 1인것처럼 취급한다.

# 선형 대수 연산
print('--행렬 곱------------')
# dot 곱
matrix1 = np.array([
    [1,2],
    [3,4]
])
matrix2 = np.array([
    [5,6],
    [7,8]
])
result = np.dot(matrix1, matrix2)
print(result)

print('배열 인덱싱 및 슬라이싱------------')
print('-기본 인덱싱------------')
print('--1차원 배열------------')
arr = np.array([10, 20, 30, 40])
print(arr[2])       # 30

print('--다차원 배열------------')
arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr[행, 열]
print(arr[1, 2])    # 6

print('-슬라이싱------------')
# arr[행 범위, 열 범위]
print('--배열 부분 선택------------')
print(arr[0,:])     # 1번째 행
print(arr[:,1])     # 2번째 열
# [1 2 3]
# [2 5]

print('고급 기능------------')
print('-조건부 연산------------')
print('--조건 필터링------------')
arr = np.array([1, 2, 3, 4, 5])
filtered = arr[arr > 3]
print(filtered) # [4 5]
print(arr > 3)  # [False False False  True  True]

print('-Numpy 와 Pandas 통합 사용------------')
print('--Pandas DataFrame으로 변환------------')
import pandas as pd 
df = pd.DataFrame(arr, columns=['Value'])
print(df)
print(type(df))

df2 = pd.DataFrame(arr.reshape(1,5), columns=['A','B','C','D','E'])
print(df2)
print(type(df2))