# select_sort2.py

# 오름차순 1, 2, 3, 4, 5
# 내림차순 5, 4, 3, 2, 1

print('5--------------')
#step5
ca = [21, 10, 11, 15, 13]
print('ca:', ca)
for i in range(0, len(ca)-1, 1):
    mina = ca[i]
    minx = i
    for sb in range(i+1, len(ca), 1):
        if mina > ca[sb]:
            mina = ca[sb]
            minx = sb
        
    temp = ca[i]
    ca[i] = ca[minx]
    ca[minx] = temp
    
print('ca:', ca)

# 목표 ca: [10, 11, 13, 15, 21]


print('6--------------')
#step6
def fselsort(cb: list):
    for i in range(0, len(cb)-1, 1):
        mina = cb[i]
        minx = i
        for sb in range(i+1, len(cb), 1):
            if mina > cb[sb]:
                mina = cb[sb]
                minx = sb
                
        temp = cb[i]
        cb[i] = cb[minx]
        cb[minx] = temp
        print('cb:', cb)
    
ca = [21, 10, 11, 15, 13]
print('ca:', ca)
fselsort(ca)
print('ca:', ca)

# 목표 ca: [10, 11, 13, 15, 21]
