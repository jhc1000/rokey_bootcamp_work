# func_call.py

def myabs(arg): # 절대값 반환 코드
    if (arg<0):
        result = arg*-1
    else:
        result = arg
    return result

print(myabs(10))

print('-------')

def funca():
    print("funca 함수 호출")

def funcb():
    funca()
    print("funcb 함수 호출")
    
def funcc():
    funcb()
    print("funcc 함수 호출")
    
funcc()

print('-------')

def fadd(pa, pb):
    return pa + pb

na = 10
nb = 20
nc = fadd(na, nb)
print(na, "+", nb, "결괏값은", nc, "이다.")