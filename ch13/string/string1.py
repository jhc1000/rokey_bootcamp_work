# string1.py

muna="python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))
try:
    muna[0]='k' # 문자열은 문자열 상수여서 변경할 수 없다
    # TypeError: 'str' object does not support item assignment
except TypeError as e:
    print(type(e), e)
    
print('---------')

munb=["python"]
print(munb[0])
print(type(munb))

print('---------')

munc=["p","y","t","h","o","n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0]='k'
print(munc)

print('---------')

for i in range(0,6,1):
    print(munc[i], end="")
print("")

print('---------')

for i in range(len((munc))):
    print(munc[i], end="")
print("")

print('---------')
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))

import locale
print(locale.getpreferredencoding())