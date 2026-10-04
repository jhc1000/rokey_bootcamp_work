# list_append.py

listc = [] # 빈 리스트


print(type(listc))
print(listc)

listc.append(23)
print(listc)

listc.append('파이썬')
print(listc)

listc.append(-12.25)
print(listc)

listc.append(True)
print(listc)

listd = ['d', 123, 45.7]
listc.append(listd)
print(listc)

listc.append(None)
print(listc)

print(listc[4][2])