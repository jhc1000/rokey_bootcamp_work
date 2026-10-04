# list_swap1.py

# ca = [10, 11]
# print("ca[0]:", ca[0], "ca[1]:", ca[1])
# temp = ca[0]
# ca[0] = ca[1]
# ca[1] = temp
# print("ca[0]:", ca[0], "ca[1]:", ca[1])

print('-----------')

# 함수로 swap 시도 -> 실패
# def funca(na, nb):
#     temp = na
#     na = nb
#     nb = temp
    
# ca = [10, 11]
# na = ca[0]
# nb = ca[1]
# print("ca[0]:", ca[0], "ca[1]:", ca[1])
# funca(ca[0], ca[1])
# print("ca[0]:", ca[0], "ca[1]:", ca[1])

print('-----------')

# 리스트에 새 별명 추가
ca = [10, 11]
cb = ca
print('리스트 ca 값:', ca)
print('리스트 cb 값:', cb)
print('리스트 ca 주소:', id(ca))
print('리스트 ca[0] 주소:', id(ca[0]))
print('리스트 ca[1] 주소:', id(ca[1]))
print('리스트 cb 주소:', id(cb))
print('리스트 cb[0] 주소:', id(cb[0]))
print('리스트 cb[1] 주소:', id(cb[1]))

temp = cb[0]
cb[0] = cb[1]
cb[1] = temp

print('리스트 ca 값:', ca)
print('리스트 cb 값:', cb)
print('리스트 ca 주소:', id(ca))
print('리스트 ca[0] 주소:', id(ca[0]))
print('리스트 ca[1] 주소:', id(ca[1]))
print('리스트 cb 주소:', id(cb))
print('리스트 cb[0] 주소:', id(cb[0]))
print('리스트 cb[1] 주소:', id(cb[1]))


print('-----------')

# 리스트 swap 함수
def swap_func(cb):
    temp = cb[0]
    cb[0] = cb[1]
    cb[1] = temp
    
ca = [10, 11]
print("ca[0] =", ca[0], "ca[1] =", ca[1])
swap_func(ca)
print("ca[0] =", ca[0], "ca[1] =", ca[1])

print('-----------')


def funca(na, nb):
    temp = na
    na = nb
    nb = temp
    
ca = [10]
cb = [11]
print("ca", ca)
print("cb", cb)
funca(ca, cb)
print("ca", ca)
print("cb", cb)

print('-----------')
