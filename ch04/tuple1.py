# tuple1.py

# tuple 생성 방법
# 튜플변수명 = (요소1, 요소2, 요소3, ...)
# clovers = ('클로버1', '하트2', '클로버3')

# # 데이터 변경 불가능

# # 값 가져오기
# # 튜플변수명[인덱스]
# print(clovers[0])
# print(clovers[1])
# print(clovers[2])
# print(clovers)
# print(type(clovers))

# print('----------')

# my_tuple1 = () # 빈 튜플 가능
# print(my_tuple1)
# print(type(my_tuple1))

# print('----------')

# my_tuple1 = ('클로버1') # str
# print(my_tuple1)
# print(type(my_tuple1))

# print('----------')

# my_tuple1 = ('클로버1',) # tuple
# print(my_tuple1)
# print(type(my_tuple1))

# print('----------')

# my_tuple2 = (1, -2, 3.14, [2, 3], (2, 3))
# print(my_tuple2)

# print('----------')

# my_tuple3 = '앨리스', 10, 1.0, 1.2 # 괄호 생략이 가능
# print(my_tuple3)
# print(type(my_tuple3))

print('----------')

a = (1, 2, 3)
# a[0] = 7
print(a, type(a))

b = list(a)
print(b, type(b))

b[0] = 7
print(b, type(b))

c = tuple(b)
print(c, type(c))