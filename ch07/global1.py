# global1.py

b = 0
print("b:", b)
b = 1
print("b:", b)

def scope_test():
    a = 1   # 지역변수
    print("scope_test() 안 a:", a)

a = 0   # 전역변수
print("scope_test() 밖 a:", a)
scope_test()    # 함수 호출
print("scope_test() 호출 후 밖 a:", a)

print('----------')

def scope_test():
    global a
    a = 1   # 전역변수
    print("scope_test() 안 a:", a)

a = 0   # 전역변수
print("scope_test() 밖 a:", a)
scope_test()    # 함수 호출
print("scope_test() 호출 후 밖 a:", a)

print('----------')