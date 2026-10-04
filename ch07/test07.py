# test07.py

#26
x = 10  # 전역변수
def fadd(num): 
    b = x + num # 전역변수 read 는 가능
    print("x:", x) 
    print("b:", b)
fadd(10)
# x 10 b 20

print('----------')

# x = 10
# def fadd(num):
#     # 해결방법
#     # 1. 지역변수 초기화
#     x = 10
#     # 2. global x 선언
#     global x
#     x = x + num       # UnboundLocalError
#     print("x:", x)
# fadd(10)
# # 전역변수 write 여서 에러발생, x 지역 변수 선언

print('----------')

x = 10
def fadd(num):
    global x
    x = x + num
    print("x:", x)
fadd(10)
# x 20

print('----------')

#27
def print_lower_price():
    price = int(input('현재 가격 입력:'))
    print("할인된 가격:", price*0.9, "원")

print_lower_price()

def print_lower_price(price):
    return 0.9 * price

price = int(input('현재 가격 입력:'))
a = print_lower_price(price)
print("할인된 가격:", a, "원")

print('----------')

#28
def func1(num):
    return num+4

a = func1(10)
b = func1(a)
c = func1(b)
print(c)
# 22