# list_id.py


a = [10, 11, 12, 13]
print('리스트 a:', a)
print('리스트 a id:', id(a))
print('리스트 a[0] id:', id(a[0]))
print('리스트 a[1] id:', id(a[1]))
print('리스트 a[2] id:', id(a[2]))

a[1] = 21
print('리스트 a:', a)
print('리스트 a id:', id(a))
print('리스트 a[0] id:', id(a[0]))
print('리스트 a[1] id:', id(a[1])) # a[1] id 값 바뀌니까 a[1] id 값 바뀜
print('리스트 a[2] id:', id(a[2]))
b = a
print('리스트 b:', b)
print('리스트 b id:', id(b))
print('리스트 b[0] id:', id(b[0]))
print('리스트 b[1] id:', id(b[1]))
print('리스트 b[2] id:', id(b[2]))

b = [30, 31, 32, 33]
print('리스트 b:', b)
print('리스트 b id:', id(b)) # b 재할당 하니까 b id 다 바뀜
print('리스트 b[0] id:', id(b[0]))
print('리스트 b[1] id:', id(b[1]))
print('리스트 b[2] id:', id(b[2]))
print('-----------')