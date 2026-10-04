# print_func.py
na = 10
nb = 20.2
sa = 'python'

# print(인수1, 인수2, 인수3, ...)
print()
print(na)   # 데이터가 공백으로 구분되서 나온다.
print("na변수값", na, sep=" ") # sep 값 지정해서 바꾸기
print("nb변수값", nb, sep=",") 
print("sa변수값", sa, sep=":")

print("----------")

nc=30
nd=40
print("nc=",nc,"nd=",nd)
nd = nc     # 재 할당
print("nc=", nc, "nd=", nd)