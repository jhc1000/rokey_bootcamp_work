# hard_ch01.py

a = [1, 2, 3]
b = a           # b = a 같은 리스트에 붙인 별명이 된다
b.append(4)
print(a)
# [1, 2, 3, 4]

print('---------')

a = [1, 2, 3]
b = a.copy()
b = a[:]
b.append(4)
print(a)
print(b)
# [1, 2, 3]

print('---------')
a, b = b, a
print(a)
print(b)

print('---------')

nums = [3, 1, 2]
result = nums.sort() # sort() 는 원본을 정렬하고 아무것도 반환하지 않는다.
print(result)
# None

print(nums)

nums = [3, 1, 2]
print(sorted(nums))
# [3, 1, 2]

print('---------')

temps = [78.2, 91.0, 65.3, 88.9]
print([t for t in temps if t > 85])
# [91.0, 88.9]
# 리스트 컴프리헨션의 기본 골격은 [표현식 for 변수 in 반복대상 if 조건]입니다.
# if는 거르기(필터), 앞쪽 표현식은 바꾸기(변환)를 담당합니다.

print('---------')

def add_item(item, box=[]):
    box.append(item)
    return box

print(add_item("a")) 
# [a]
print(add_item("b")) 
# [a, b]

# 기본값 리스트는 함수가 정의될 때 단 한 번 만들어져서 모든 호출이 공유합니다. 
# 가변 객체(리스트·딕셔너리)를 기본값으로 쓰면 안 되는 이유입니다.

def add_item(item, box=None):
    if box is None: box = []
    box.append(item)
    return box

print(add_item("a")) 
# [a]
print(add_item("b")) 
# [b]

print('---------')

nums = [1, 2, 2, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
# [1, 2]
# 순회 중에 리스트에서 원소를 빼면 인덱스가 앞으로 밀려서 다음 원소를 건너뜁니다.
# 순회 중인 리스트는 건드리지 말고, 컴프리헨션으로 새 리스트를 만드는 게 정석입니다
nums = [1, 2, 2, 4]
result = [n for n in nums if n % 2 != 0]
print(result)
# [1]

# Q1 : [1, 2, 3, 4] , Q2 : None, Q3 : [91.0, 88.9]