# global3.py

# def scope_test():
#     a = a + 3   # 지역변수 # UnboundLocalError
#     print("scope_test() 안 a:", a)

# a = 0   # 전역변수
# print("scope_test() 밖 a:", a)
# scope_test()    # 함수 호출
# print("scope_test() 호출 후 밖 a:", a)

print('----------')

# # 1. 함수 내 a 변수 값을 전역변수 선언
# def scope_test():
#     global a # 이 키워드 이후로는 a 는 전역변수를 나타낸다.
#     a = a + 3   # 전역변수
#     print("scope_test() 안 a:", a)

# a = 0   # 전역변수
# print("scope_test() 밖 a:", a)
# scope_test()    # 함수 호출
# print("scope_test() 호출 후 밖 a:", a)

print('----------')

# # 2. 함수 내 변수 a 값을 지역변수로 초기화
# def scope_test():
#     a = 0
#     a = a + 3   # 지역변수
#     print("scope_test() 안 a:", a)

# a = 0   # 전역변수
# print("scope_test() 밖 a:", a)
# scope_test()    # 함수 호출
# print("scope_test() 호출 후 밖 a:", a)

print('----------')

# 3. 함수 매개변수 a 값을 지역변수로 재할당
def scope_test(a):
    a = a + 3   # 지역변수
    print("scope_test() 안 a:", a)
    return a

a = 0   # 전역변수
print("scope_test() 밖 a:", a)
a = scope_test(a)    # 함수 호출
print("scope_test() 호출 후 밖 a:", a)

print('----------')