# iterable.py

# 1. iterable: 반복가능한 
# 2. iterator: 반복자

# a = [1,2,3]
# next(a)     # 이터레이터로부터 값을 순차적으로 반환

# TypeError: 'list' object is not an iterator
# 리스트는 iterable 하지만, iterator 아니다.
# 리스트는 __iter__() 포함하지만, __next__() 포함하지 않는다.

# iterable -> iterator 변환
a = [1,2,3]
iter_a = iter(a)        # iterator 로 변환 
print(type(iter_a))     # <class 'list_iterator'>
# print(next(iter_a))     # 1
# print(next(iter_a))     # 2
# print(next(iter_a))     # 3
# print(next(iter_a))     # StopIteration 예외

for j in iter_a:
    print(j)
# print(next(iter_a))     # StopIteration 예외

for j in iter_a:
    print(j)
# 예외 발생 안함. for문은 데이터 없으면 반복을 안해서