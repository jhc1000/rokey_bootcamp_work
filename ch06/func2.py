# func2.py

# 함수 정의
def funca(pa,pb):
    nc = pa + pb
    return nc

na = 10
nb = 11

# 함수 호출
nc = funca(na, nb) # funca(10, 11)
# pa = na
# pb = nb

print(na, "+", nb, "=", nc)

print('-------')

def fplusminus(arg):
    if arg > 0:
        return "plus", arg
    elif arg < 0:
        return "minus", arg


stra = fplusminus(0)
stra = fplusminus(7)
stra = fplusminus(-3)
print(stra[0])
print(stra[1])

print('-------')
