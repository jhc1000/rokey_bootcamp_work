# test06.py

#20-1
def welcome():
    print('이상한 나라에 오신 것을 환영합니다.')

welcome()

print('-------')

#20-2
def welcome(name):
    print(name, '님 이상한 나라에 오신 것을 환영합니다.')


welcome('앨리스')
welcome('도도새')

print('-------')

#21
def draw_stars(num):
    print('*' * num) # * 문자열 반복 연산자 

draw_stars(3)
draw_stars(2)
draw_stars(1)

print('hi' * 4)
print('-------')

#22
def fadd(pa, pb):
    return pa + pb

def fsub(pa, pb):
    return pa - pb

def fmul(pa, pb):
    return pa * pb

def fdiv(pa, pb):
    return pa / pb

na = 100
nb = 3
nc = fadd(100, 3)
print(na, "+", nb, "=", nc)
nc = fsub(100, 3)
print(na, "_", nb, "=", nc)
nc = fmul(100, 3)
print(na, "*", nb, "=", nc)
nc = fdiv(100, 3)
print(na, "/", nb, "=", nc)

print('-------')

#23

# na = float(input("1번 수:"))
# nb = float(input("2번 수:"))
# nc = fadd(na, nb)
# print(na, "+", nb, "=", nc)
# nc = fsub(na, nb)
# print(na, "_", nb, "=", nc)
# nc = fmul(na, nb)
# print(na, "*", nb, "=", nc)
# nc = fdiv(na, nb)
# print(na, "/", nb, "=", nc)

print('-------')

#24
def string_length(stb):
    len = 0
    for i in stb:
        len += 1
        # print(i, len)
    return len

# pass 키워드 : 아무 작업도 하지 않고 넘어가라
# (문법상 코드가 필요하나 아직 작성하지 않았을때 넘기는 방법)

sta = "python example"
# sta = "001 0101 1010 0011010"
lena = len(sta)
print(lena)

lena = string_length(sta)
print(lena)

print('-------')

# #25
# def fdiv(pa, pb):
#     if pb == 0:
#         # print('0으로는 나눌수 없다.') # ZeroDivisionError 발생
#         return '0으로는 나눌수 없다.'
#     else:
#         pc = pa / pb
#         # print(pa, "/", pb, "=", pc)
#         return pc

# na = float(input("1번 수:"))
# nb = float(input("2번 수:"))
# nc = fdiv(na, nb)
# print(nc)

# print('-------')

#26
# num = int(input("배수의 합을 구하고자 하는 정수를 입력하세요."))
# sum = 0
# for i in range(1, 101):
#     if i % num == 0:
#         sum += i
# print(sum)

num = int(input("배수의 합을 구하고자 하는 정수를 입력하세요."))
sum = 0
for i in range(num, 101, num):
    sum += i
print(sum)

print('-------')
    
# #27
# def funca(num):
#     sum = 0
#     for i in range(1, 101):
#         if i % num == 0:
#             sum += i
#     return sum

# num = int(input("배수의 합을 구하고자 하는 정수를 입력하세요."))
# sum = funca(num)
# print(sum)