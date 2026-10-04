# dict_func.py

a = {1: '월', 'tue': '화', 'wed': '수'}
print(a, type(a), id(a))
x = a
print(x, type(x), id(x))
x[1] = '일'
print(x)
print(a)

print('------------')

def fch(x: dict):
    x[1] = '일'
    
a = {1: '월', 'tue': '화', 'wed': '수'}
print(a)
fch(a)
print(a)