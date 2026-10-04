# list_insert.py

# 특정 위치에 값 추가하기
# 리스트명.insert(인덱스, 추가할_값)

clovers = ['클로버1', '클로버2', '클로버3']
clovers.insert(0, '클로버0')
print(clovers)

clovers.insert(1, '하트1')
print(clovers)

print('---------')

# 여러 값 추가하기
# 리스트.extend([값1, 값2, 값3, ...])

new_list = ['하트3', '클로버4']
clovers.extend(new_list)
print(clovers)
