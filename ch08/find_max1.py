# find_max1.py

# 최대값 찾기
su = [ 5, 4, 7, 10, 6]

def fmax(fu: list):
    max = fu[0]
    for i in range(1, len(fu), 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su)
print('max=', max)

print('------------')

print('1-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print('max=', max)

print('2-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    if max < fu[1]:
        max = fu[1]
    if max < fu[2]:
        max = fu[2]
    if max < fu[3]:
        max = fu[3]
    if max < fu[4]:
        max = fu[4]
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print('max=', max)

print('3-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print('max=', max)

print('4-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print('max=', max)

print('5-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print('max=', max)

print('6-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su)
print('max=', max)

print('7-----------')
su = [ 5, 4, 7, 10, 6]

def fmax(fu: list):
    max = fu[0]
    for i in range(1, len(fu), 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su)
print('max=', max)