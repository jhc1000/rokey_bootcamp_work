# global4.py

def scope_test():
    # global a
    a = 1   # 전역변수
    print("scope_test() 안 a:", a)
    # print("scope_test() 안 c:", c) # c 전역변수 접근
    c = 2 # UnboundLocalError 지역변수 할당 X
          # 지역변수 선언 여부에 따라 달라진다.
    print("scope_test() 안 c:", c) # c 지역변수 접근

a = 0   # 전역변수
c = 1
print("scope_test() 밖 a:", a)
print("scope_test() 밖 c:", c)

scope_test()    # 함수 호출
print("scope_test() 호출 후 밖 a:", a)
print("scope_test() 호출 후 밖 c:", c)

print('----------')

# 함수 내 전역변수에 대한 접근 가능(read)
# 함수 내 전역변수에 대한 쓰기 불가능(write) 하려면 global 키워드 사용