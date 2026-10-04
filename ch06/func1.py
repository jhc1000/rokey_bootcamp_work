# func1.py

# 함수 정의
# def 함수명([매개변수]):
#     코드블록
#     [return 반환값]  []: 생략가능

# 함수 호출(사용)
# 함수명(인수)

# 사용자 정의 함수
def my_func():
    print("토끼야 안녕!!")

my_func()

print('---------')

na = 10
nb = 11
nc = na + nb
print(na, "+", nb, "=", nc)

print('---------')

def funca(na,nb):
    nc = na + nb
    print(na, "+", nb, "=", nc)
    return nc

nc = funca(10,20)
print(nc)

print('---------')

def add(num1, num2):
    num3 = num1 + num2
    return num1, num2, num3

print(add(2,3))

print('---------')
