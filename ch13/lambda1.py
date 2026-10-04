# lambda1.py

# 일반적 함수 정의 및 호출
# def 함수명(매개변수):
#     코드블록
#     return 코드블록
# 함수명(인수)
def add(x):
    return x+x
print(add(1))
print(add(2))
print(add(3))


print('--------')

# 람다 함수 정의 및 호출
# 사용목적: 이름이 필요없는 짧은 함수를 한번 사용하기 위해서
# lambda 매개변수:표현식
add = lambda x:x+x
# print(add(1))
# print(add(2))
# print(add(3))
print((lambda x:x+x)(1))
print((lambda x:x+x)(2))
print((lambda x:x+x)(3))

print('--------')
# 표현식(expression)
# : 실행했을 때 하나의 값을 만들어 내는 코드
# 기본형태
# 1. 값
# 10+20
# x*2
# a>b
# 2. 변수
# x=10
# print(x)
# 3. 함수 호출
# len("python")
# 4. 조건 표현식
# age = 20
# result = "성인" if age >= 18 else "미성년자"

square = lambda x:x**2
print(square(3))

print('--------')