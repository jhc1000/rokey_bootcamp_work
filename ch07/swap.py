# swap.py

# 변수간 데이터 스왑
na = 10
nb = 11
print("na:", na, "nb:", nb)

temp = na
na = nb
nb = temp
print("na:", na, "nb:", nb)


print('--------')

# 변수간 데이터 스왑2
na = 10
nb = 11
print("na:", na, "nb:", nb)

na, nb = nb, na # tuple 언패킹(unpacking)
print("na:", na, "nb:", nb)

print('--------')

# 함수로 데이터 스왑 시도
def funca(pa, pb): # 지역변수
    temp = pa # 지역변수
    pa = pb
    pb = temp

na = 10 # 전역변수
nb = 11 # 전역변수
print("na:", na, "nb:", nb)
funca(na, nb)
print("na:", na, "nb:", nb)
# print(pa) # NameError

print('--------')

# 함수로 데이터 스왑
def funca(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    return pa, pb

na = 10
nb = 11
print("na:", na, "nb:", nb)
na, nb = funca(na, nb)  # 언패킹(unpacking)
print("na:", na, "nb:", nb)

print('--------')
