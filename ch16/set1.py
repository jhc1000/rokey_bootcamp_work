# set1.py

# set(세트) : 중복을 허용하지 않는 자료구조
# 집합과 비슷함

# 세트 생정 (중복 제거)
numbers = {1,2,3,3,4}
print(numbers)

# 요소 추가 및 제거 
numbers.add(5)
numbers.remove(3)

print(numbers)
print('----------')
## 집합연산 
set1 = {1,2,3}
set2 = {3,4,5}

# 교집합 : &
print(set1 & set2) # {3}

# 합집합 : |
print(set1 | set2) # {1, 2, 3, 4, 5}

# 차집합 : -
print(set1 - set2) # {1, 2}
print(set2 - set1) # {4, 5}

print('----------')
# set 활용
# 1. 중복 제거
# 2. 특정 값의 존재 빠르게 확인 (교집합으로)
# 3. 두 데이터의 공통/차이 확인

python = {"이수근", "강호동", "유재석", "하하"}
java = {"유재석", "하하", "박명수"}

# python, java 모두 수강하는 사람
print(python & java)
# python 만 수강하는 사람
print(python - java)
# java 만 수강하는 사람
print(java - python)