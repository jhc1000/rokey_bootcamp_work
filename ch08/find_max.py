# find_max.py

print('1--------------')
# 최대값 찾기
ca = [10, 17, 13, 11]
max = ca[0]
if max < ca[1]:
    max = ca[1]
if max < ca[2]:
    max = ca[2]
if max < ca[3]:
    max = ca[3]

print('max:', max)

print('2--------------')

# for문 이용해 최대값 찾기
ca = [10, 17, 13, 11]
max = ca[0]
for i in range(1, 4, 1):
    if max < ca[i]:
        max = ca[i]
print('max:', max)

print('3--------------')

# for문 이용해 리스트값 직접 받아 최대값 찾기
ca = [10, 17, 13, 11]
max = ca[0]
for sb in ca:
    if max < sb:
        max = sb
print('max:', max)

ca = [10, 17, 13, 11]
max = float('-inf')
for num in ca:
    if max < num:
        max = num
print('max:', max)


print('---------------')


