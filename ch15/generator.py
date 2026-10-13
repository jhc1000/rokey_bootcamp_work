# generator.py

# 제너레이터 생성 방법
# 1. yield
def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
print(type(g))
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # StpoIteration
for i in g:
    print(i)

# 제너레이터 < 이터레이터 (포함관계)
#   : 이터레이터가 더 큰 개념,
#       제러레이터는 그 구현 방업 중 하나

print('------------')
print("__iter__" in dir(g))     # True
print("__next__" in dir(g))     # True


print('------------')
def mygen():
    for i in range(1,100):
        result = i*i
        yield result

gen = mygen()
print(type(gen))
print(gen)
for item in gen:
    print(item)
# print(next(gen))
print(next(gen, "끝"))
print(next(gen, "끝"))  # StopIteration 대신 동작할 내용 추가
print('------------')

# 제너레이터 생성 방법
# 2. 제너레이터 표현식 활용: 제너레이터 컴프리핸션
gen = (i*i for i in range(1,100))
print(type(gen))
print(gen)
for item in gen:
    print(item)